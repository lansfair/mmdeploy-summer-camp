## 1. 首先安装opencv等依赖库
`sudo apt install build-essential git cmake libprotobuf-dev protobuf-compiler libvulkan-dev vulkan-utils libopencv-dev`
## 2. 安装vulkan sdk
类似于cuda，用于框架调用gpu？
```
wget https://sdk.lunarg.com/sdk/download/1.2.189.0/linux/vulkansdk-linux-x86_64-1.2.189.0.tar.gz?Human=true -O vulkansdk-linux-x86_64-1.2.189.0.tar.gz
tar -xf vulkansdk-linux-x86_64-1.2.189.0.tar.gz
export VULKAN_SDK=$(pwd)/1.2.189.0/x86_64
sudo apt install mesa-vulkan-drivers
```
## 3. 克隆ncnn
不是很清楚submodule是干嘛的
```
git clone https://github.com/Tencent/ncnn.git
cd ncnn
git submodule update --init
```
## 4. 编译ncnn
```
cd ncnn
mkdir -p build
cd build
cmake -DCMAKE_BUILD_TYPE=Release -DNCNN_VULKAN=ON -DNCNN_BUILD_EXAMPLES=ON ..
make -j$(nproc)
```
## 5. 测试
有个小坑：现版本的ncnn加载模型成功返回0，失败返回1，与之前相反，需要修改一下测试代码里的判断模型是否加载成功的if语句
```
cd ../examples
../build/examples/squeezenet ../images/256-ncnn.png
[0 llvmpipe (LLVM 12.0.0, 256 bits)]  queueC=0[1]  queueG=0[1]  queueT=0[1]
[0 llvmpipe (LLVM 12.0.0, 256 bits)]  bugsbn1=0  bugbilz=0  bugcopc=0  bugihfa=0
[0 llvmpipe (LLVM 12.0.0, 256 bits)]  fp16-p/s/a=1/1/0  int8-p/s/a=1/1/0
[0 llvmpipe (LLVM 12.0.0, 256 bits)]  subgroup=8  basic=1  vote=1  ballot=1  shuffle=0
WARNING: lavapipe is not a conformant vulkan implementation, testing use only.
load_param return  0
532 = 0.163940
920 = 0.093445
716 = 0.061310
```
