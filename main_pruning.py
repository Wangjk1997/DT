from function import boundarySet
from function import boundary
from function import judge_next
from function import judge_next_precision
from function_pruning import cal_precision_before
from function_pruning import cal_precision_after

precision_boundary = 0.00;
pos_class = 4

fh = open('iris_data.txt')
origin_dataset = list()
origin_path = list()
for line in fh:
    tmp = line.split(',')
    dotpos = tmp[4].find('\n')
    tmp[4] = tmp[4][0:dotpos]
    origin_dataset.append(tmp);
fh.close()                      #添加数据
i = 0
training_set = list()
validation_set = list()
for dataset in origin_dataset:
    if i%5 == 0:
        validation_set.append(dataset)
    else:
        training_set.append(dataset)
    i = i + 1
print(len(validation_set))
print(len(training_set))

tmp_dataset = {'path':origin_path, 'condition':True, 'data':training_set, 'title':[0,1,2,3]}             #openset为一直要处理的数据集为list，每个元素为dict，处理结束的标志为condition全部都是FALSE
openset = list()
openset.append(tmp_dataset)
print(openset)
print(tmp_dataset['path'])

while 1:
    break_flag = 1
    tmp_openset = list()
    for every_dataset in openset:
        print('processing_dataset',every_dataset)
        if every_dataset['condition'] == True:
            # tmp_path = every_dataset['path']
            # print('tmp_path',tmp_path)
            (precision_before, right_set) = cal_precision_before(every_dataset,validation_set)
            print(right_set)
            break_flag = 0
            feature_set = list()
            for i in range(0,len(every_dataset['data'][0]) - 1):
                feature_set.append(boundarySet(every_dataset['data'], i))
            feature_boundary_set = list()
            for i in range(0,len(feature_set)):
                feature_boundary_set.append(boundary(feature_set[i],every_dataset['data'],i,len(feature_set)))
            max_gain = 0
            max_feature = None
            max_feature_boundary = None
            i = 0
            for feature_boundary,gain in feature_boundary_set:
                print('feature_boundary',feature_boundary)
                print('gain',gain)
                if gain > max_gain:
                    max_gain = gain
                    max_feature = i
                    max_feature_boundary = feature_boundary
                i += 1
            print(max_feature)
            print(max_feature_boundary)
            print(max_gain)
###########
            right_set_1 = list()
            right_set_2 = list()
            for tmp in right_set:
                if float(tmp[every_dataset['title'][max_feature]]) < max_feature_boundary:
                    right_set_1.append(tmp)
                else:
                    right_set_2.append(tmp)
            print('feature',every_dataset['title'][max_feature])
            print('right_set_1',right_set_1)
            print('right_set_2',right_set_2)
            precision_after = cal_precision_after(right_set_1,right_set_2,validation_set)

###########此处添加剪枝准确度判断
            if (precision_after == None) or (precision_after <= precision_before):
                every_dataset['condition'] = False
                tmp_openset.append(every_dataset)
                continue
            dataset_1 = list()
            dataset_2 = list()
            for tmp in every_dataset['data']:
                if float(tmp[max_feature]) < max_feature_boundary:
                    dataset_1.append(tmp[0:max_feature] + tmp[max_feature+1:len(tmp)])
                else:
                    dataset_2.append(tmp[0:max_feature] + tmp[max_feature + 1:len(tmp)])
            print('dataset_1',dataset_1)
            print('dataset_2',dataset_2)
            print(len(dataset_1))
            print(len(dataset_2))
            print(judge_next_precision(dataset_1,precision_boundary))
            print(judge_next_precision(dataset_2,precision_boundary))
            tmp_openset.append({'path':every_dataset['path'] + [(every_dataset['title'][max_feature],max_feature_boundary,1)],'condition':judge_next_precision(dataset_1,precision_boundary), 'data':dataset_1, 'title':every_dataset['title'][0:max_feature] + every_dataset['title'][max_feature + 1:len(every_dataset['title'])]})
            tmp_openset.append({'path':every_dataset['path'] + [(every_dataset['title'][max_feature],max_feature_boundary,2)],'condition':judge_next_precision(dataset_2,precision_boundary), 'data':dataset_2, 'title':every_dataset['title'][0:max_feature] + every_dataset['title'][max_feature + 1:len(every_dataset['title'])]})
        else:
            tmp_openset.append(every_dataset)

    # print('tmp_openset',tmp_openset)
    openset = tmp_openset
    if break_flag == 1:#1:
        break

print(len(openset))
for result in openset:
    print(result['path'])
    # for tmp in result['data']:
    #     print(tmp[len(tmp) - 1])
    print(len(result['data']))
    print(result['data'])