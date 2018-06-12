from math import log2

def find_max_gain(dataset):
    #对每个特征找到其分类的类别
    num_feature = len(dataset[0]) - 1
    feature_set = list()
    for i in range(0,num_feature):
        tmp_feature = list()
        for tmp in dataset:
            if not tmp[i] in tmp_feature:
                tmp_feature.append(tmp[i])
        feature_set.append(tmp_feature)
    print('feature_func',feature_set)
    #计算信息熵
    cls = list()
    entropy = 0
    for tmp in dataset:
        if not tmp[len(dataset[0]) - 1] in cls:
            cls.append(tmp[len(dataset[0]) - 1])
    for diff_cls in cls:
        num_diff_cls = 0
        for tmp in dataset:
            if tmp[len(dataset[0]) - 1] == diff_cls:
                num_diff_cls += 1
        pi = num_diff_cls/len(dataset)
        entropy += -pi*log2(pi)#计算信息熵
    print('entropy',entropy)
    #然后计算每个类别的信息增益
    max_gain = 0
    max_feature = None
    for i in range(0,num_feature):
        feature_class_num = list()
        for j in range(0,len(feature_set[i])):
            tmp_num = list()
            for diff_cls in cls:
                tmp_num.append(0)
            # print(tmp_num)
            for tmp in dataset:
                if tmp[i] == feature_set[i][j]:
                    for k in range(0,len(cls)):
                        if tmp[len(tmp) - 1] == cls[k]:
                            tmp_num[k] += 1
            feature_class_num.append(tmp_num)
        # print(feature_class_num)
        total = 0
        for tmp in feature_class_num:
            ed = 0
            for element in tmp:
                if element ==0:
                    continue
                ed -= element/sum(tmp) * log2(element/sum(tmp))
            total += sum(tmp)/len(dataset) * ed
        gain = entropy - total
        if max_gain < gain:
            max_gain = gain
            max_feature = i
        # print(gain)
    return max_gain,max_feature

def find_feature_set(dataset):
    #对每个特征找到其分类的类别
    num_feature = len(dataset[0]) - 1
    feature_set = list()
    for i in range(0,num_feature):
        tmp_feature = list()
        for tmp in dataset:
            if not tmp[i] in tmp_feature:
                tmp_feature.append(tmp[i])
        feature_set.append(tmp_feature)
    return feature_set

def judge_next(dataset):
    if len(dataset[0]) == 1:
        return False
    flag = None
    for tmp in dataset:
        if flag ==None:
            flag = tmp[len(tmp) - 1]
        if flag != tmp[len(tmp) - 1]:
            return True
    return False