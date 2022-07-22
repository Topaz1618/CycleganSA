import numpy as np


def normalization(data):
    _range = np.max(data) - np.min(data)
    return (data - np.min(data))/_range # 结果 0, 1


def standardization(data):
    # data - mean
    mu = np.mean(data, axis=0)
    sum1 = data - mu

    sigma = np.std(data, axis=0) #  data - mean 平方再开平方 只有正值

    return sum1 / sigma # 结果 1, -1


def func1(data):
    # 样本方差
    avg = np.mean(data)
    sum_val = np.sum((data - avg) ** 2)
    res = sum_val / len(data - 1)
    # by numpy
    res = np.var(a3, ddof=1)

    # 总体方差
    avg = np.mean(data)
    sum_val = np.sum((data - avg) ** 2)
    res = sum_val / len(data)

    # by numpy
    res = np.var(data)

    # 样本标准差


    res = np.std(a3, ddof=1)

    # 总体标准差
    res = np.std(a3)


if __name__ == "__main__":
    input_data = np.random.randint(0, 10, size=[2, 3])
    # input_data = np.random.random(20)
    input_data = np.random.randint(1, 20, [2, 3])
    print(input_data)
    normalization(input_data)