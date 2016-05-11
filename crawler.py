# Filename : crawler.py
# -*- coding: utf-8 -*- 
# authour 

import numpy as np

file_object = open('Question15.dat')
try:
     all_the_text = file_object.read( )
finally:
     file_object.close( )

print(all_the_text)
input("Prease <enter>")

# 经典 PLA
def naive_pla(datas):
    w = datas[0][0]
    iteration = 0
    while True:
        iteration += 1
        false_data = 0

        for data in datas:
            t = dot(w, data[0])
            if sign(data[1]) != sign(t):   #if error arises
                error = data[1]  
                false_data += 1
                w += error * data[0]	   #correct error
        print 'iter%d (%d / %d)' % (iteration, false_data, len(datas))
        if not false_data:
            break
    return w

# classic PLA
def trainPLA_Naive(X, Y, w, eta, updates):
    iterations = 0  # Record actual iteration times
    num = len(X)    # Quality of training data
    flag = True
    for i in range(updates):
        flag = True
        for j in range(num):
            if sign(X[j], w) != Y[j, 0]:
                flag = False
                w += eta * Y[j, 0] * np.matrix(X[j]).T
                break
            else:
                continue
        if flag == True:
            iterations = i
            break
    return flag, iterations, w


# Pocket PLA
def pocket_pla(datas, limit):
    ###############
    def _calc_false(vec):
        res = 0
        for data in datas:
            t = np.dot(vec, data[0])
            if np.sign(data[1]) != np.sign(t):
                res += 1
        return res
    ###############
    w = np.random.rand(5)
    least_false = _calc_false(w)
    res = w

    for i in xrange(limit):
        data = random.choice(datas)
        t = np.dot(w, data[0])
        if np.sign(data[1]) != np.sign(t):
            t = w + data[1] * data[0]
            t_false = _calc_false(t)

            w = t

            if t_false <= least_false:
                least_false = t_false
                res = t
    return res, least_false

# 从本地文件读取训练数据或测试数据，保存X,y两个变量中
def getDataSet(filename):
    dataSet = open(filename, 'r')
    dataSet = dataSet.readlines()   # 将训练数据读出，存入dataSet变量中
    num = len(dataSet)  # 训练数据的组数
    # 提取X, Y
    X = np.zeros((num, 5))
    Y = np.zeros((num, 1))
    for i in range(num):
        data = dataSet[i].strip().split()
        X[i, 0] = 1.0
        X[i, 1] = np.float(data[0])
        X[i, 2] = np.float(data[1])
        X[i, 3] = np.float(data[2])
        X[i, 4] = np.float(data[3])
        Y[i, 0] = np.int(data[4])
    return X, Y

# 将数据从网上down下来，存储到当前工作目录下
# 针对此exercise，最终可能保存在当前工作目录下的文件可能有三个：MLFex1_15_train.dat、MLFex1_18_train.dat、MLFex1_18_test.dat
def getRawDataSet(url):
    dataSet = urllib2.urlopen(url)
    filename = 'MLFex1_' + url.split('_')[1] + '_' + url.split('_')[2]
    with open(filename, 'w') as fr:
        fr.write(dataSet.read())
    return filename

# sigmoid函数，返回函数值
def sign(x, w):
    if np.dot(x, w)[0] >= 0:
        return 1
    else:
        return -1


# 使用此函数可直接解答15题
def question15():
    url = 'https://d396qusza40orc.cloudfront.net/ntumlone%2Fhw1%2Fhw1_15_train.dat'
    filename = getRawDataSet(url)
    X, y = getDataSet(filename)
    w0 = np.zeros((5, 1))
    eta = 1
    updates = 80
    flag, iterations, w = trainPLA_Naive(X, y, w0, eta, updates)
    print flag
    print iterations
    print w