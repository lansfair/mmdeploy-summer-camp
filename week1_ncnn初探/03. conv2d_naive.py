import cv2
import numpy as np



def corr2d(X, K, padding=True):
    """计算二维互相关运算"""
    h, w = K.shape
    if padding:
        image_padded = np.zeros((X.shape[0] + h - 1, X.shape[1] + w - 1))
        image_padded[h//2:-(h//2), w//2:-(w//2)] = X
        Y = np.zeros(X.shape) # 定义运算后的特征图大小
    else:
        image_padded = X
        Y = np.zeros((X.shape[0] - h + 1, X.shape[1] - w + 1))  # 定义运算后的特征图大小
    for i in range(Y.shape[0]):
        for j in range(Y.shape[1]):
            Y[i, j] = (image_padded[i:i + h, j:j + w] * K).sum()  # 对应位置相乘并求和
    return Y


if __name__ == '__main__':
    # 以边缘检测为例，验证上述图像卷积函数的正确性
    # 以灰度图读取图像
    img = cv2.imread("./screenshot.png", 0)
    # 构造一个prewitt算子用于边缘检测
    # 水平方向
    K1 = np.array([1, 1, 1, 0, 0, 0, -1, -1, -1]).reshape(-1, 3)
    # 垂直方向
    K2 = np.array([-1, 0, 1, -1, 0, 1, -1, 0, 1]).reshape(-1, 3)
    Y1 = corr2d(img, K1)
    Y2 = corr2d(img, K2)
    Y = np.where(Y1 > Y2, Y1, Y2)
    cv2.imwrite("results.png", Y)