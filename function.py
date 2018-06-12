from math import  log2
#对第i个特征找到其连续的分界界线
def boundarySet(dataset,i):
    TsetList = list();
    setList = list();
    for tmp in dataset:
        if not tmp[i] in TsetList:
            TsetList.append(tmp[i])
    TsetList.sort()
    num = len(TsetList)
    for i in range(1,num):
        setList.append((float(TsetList[i]) + float(TsetList[i - 1]))/2)
    return setList

#在连续分界中找到最大信息增益所对应的分界
def boundary(b_set,dataset,i,pos_class):
    cls = list()
    entropy = 0;
    length_dateset = len(dataset)
    for tmp in dataset:
        if not tmp[pos_class] in cls:
            cls.append(tmp[pos_class])
    for diff_cls in cls:
        num_diff_cls = 0
        for tmp in dataset:
            if tmp[pos_class] == diff_cls:
                num_diff_cls += 1
        pi = num_diff_cls/length_dateset
        entropy += -pi*log2(pi)#计算信息熵
    max_gain = -1;
    max_boundary = 0;
    for tmp_bound in b_set :
        class1 = list()
        class2 = list()
        entropy1 = 0;
        entropy2 = 0;
        for tmp in dataset:         #分数据
            if float(tmp[i])<tmp_bound:
                class1.append(tmp)
            else:
                class2.append(tmp)
        for diff_cls in cls:
            num_diff_cls_1 = 0;
            num_diff_cls_2 = 0;
            for tmp in class1:
                if tmp[pos_class] == diff_cls:
                    num_diff_cls_1 += 1
            pi = num_diff_cls_1 / len(class1)
            if pi != 0:
                entropy1 += -pi*log2(pi)
            for tmp in class2:
                if tmp[pos_class] ==diff_cls:
                    num_diff_cls_2 += 1
            pi = num_diff_cls_2 / len(class2)
            if pi != 0:
                entropy2 += -pi*log2(pi)
        gain = entropy - (len(class1)/length_dateset*entropy1 + len(class2)/length_dateset*entropy2)
        #print('gain',gain)
        if gain > max_gain:
            max_gain = gain
            max_boundary = tmp_bound
    return max_boundary,max_gain

#判断是否还需进行下一步决策
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

#根据精准度进行判断是否要下一步决策
def judge_next_precision(dataset, preicision_boundary):
    if len(dataset[0]) == 1:
        return False
    cls = list();
    for tmp in dataset:   #提取类别
        cls.append(tmp[len(tmp)-1])
    diff_cls = list();
    for tmp in cls:
        if not tmp in diff_cls:
            diff_cls.append(tmp)
    max_num_class = 0
    max_class = None
    for tmp in diff_cls:
        num_cls = 0
        for index in cls:
            if index == tmp:
                num_cls +=1
        if num_cls > max_num_class:
            max_num_class = num_cls
            max_class = tmp
    if (max_num_class/len(cls) >= (1-preicision_boundary)):
        return False
    else:
        return True

