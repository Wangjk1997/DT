from d_function import find_max_gain
from d_function import find_feature_set
from d_function import judge_next

fh = open('data.txt',encoding='utf8')
origin_dataset = list()
for line in fh:
    tmp = line.split(',')
    dotpos = tmp[9].find('\n')
    tmp[9] = tmp[9][0:dotpos]
    result = tmp[9]
    tmp = tmp[1:7]
    tmp.append(result)
    origin_dataset.append(tmp);
fh.close()
print(origin_dataset)
fh = open('title.txt',encoding='utf8').read()
word = fh.split(',')
title_list = word[1:7]
# title_list.append(word[9])
# print(title_list)

feature_set = find_feature_set(origin_dataset)
# print('feature_set',feature_set)

origin_path = [(0,0)]
tmp_dataset = {'path':origin_path, 'condition':True, 'data':origin_dataset}
openset = list()
openset.append(tmp_dataset)
print(openset)
while 1:
    break_flag = 1
    tmp_openset = list()
    for every_dataset in openset:
        print('everydata',every_dataset)
        if every_dataset['condition'] == True:
            break_flag = 0
            (max_gain, max_feature) = find_max_gain(every_dataset['data'])
            print(max_gain)
            print('max_feature',max_feature)
            feature_set = find_feature_set(every_dataset['data'])
            print('len(feature_Set)',len(feature_set))
            for diff_feature in feature_set[max_feature]:
                print(diff_feature)
                tmp_data = list()
                for tmp in every_dataset['data']:
                    if tmp[max_feature] == diff_feature:
                        tmp_data.append(tmp[0:max_feature] + tmp[max_feature+1:len(tmp)])
                print(tmp_data)
                print(len(tmp_data))
                if len(tmp_data) == 0:
                    continue
                tmp_openset.append({'path':every_dataset['path'] + [('?',diff_feature)],'condition':judge_next(tmp_data), 'data':tmp_data})
            print('tmp_openset',tmp_openset)
        else:
            tmp_openset.append(every_dataset)
    print('tmp_openset', tmp_openset)
    openset = tmp_openset
    if break_flag == 1:#1:
        break
print(openset)
for result in openset:
    print(result['path'])