def cal_precision_before(every_dataset, validation_set):
    right_set = list()
    for tmp_dataset in validation_set:
        right_flag = 0
        for path in every_dataset['path']:
            if path[2] == 1:
                if float(tmp_dataset[path[0]]) < path[1]:
                    continue
                else:
                    right_flag = 1
            if path[2] == 2:
                if float(tmp_dataset[path[0]]) > path [1]:
                    continue
                else:
                    right_flag = 1
        if right_flag == 0:
            right_set.append(tmp_dataset)
    cls = list()
    for tmp in right_set:   #提取类别
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
    print('max_num_class',max_num_class,'max_class',max_class)
    print('lenght_right_set',len(right_set))
    if len(right_set) != 0:
        print('precision',max_num_class/len(right_set))
        return max_num_class/len(right_set),right_set
    else:
        return None,right_set

def cal_precision_after(right_set_1, right_set_2, validation_set):
    cls = list()
    for tmp in right_set_1:   #提取类别1
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
    right_1 = max_num_class

    cls = list()
    for tmp in right_set_2:   #提取类别2
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
    right_2 = max_num_class
    if (len(right_set_1) + len(right_set_2)) == 0:
        return None
    else:
        precision = (right_1 + right_2)/(len(right_set_1) + len(right_set_2))
        print('precision_after',precision)
        return precision