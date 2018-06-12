from function import boundarySet
from function import boundary
from function import judge_next
from function import judge_next_precision

precision_boundary = 0.00;
pos_class = 4

fh = open('iris_data.txt')
origin_dataset = list()
origin_path = [(0,0)]
for line in fh:
    tmp = line.split(',')
    dotpos = tmp[4].find('\n')
    tmp[4] = tmp[4][0:dotpos]
    origin_dataset.append(tmp);
fh.close()                      #添加数据

tmp_dataset = {'path':origin_path, 'condition':True, 'data':origin_dataset}             #openset为一直要处理的数据集为list，每个元素为dict，处理结束的标志为condition全部都是FALSE
openset = list()
openset.append(tmp_dataset)
print(openset)
print(tmp_dataset['path'])

while 1:
    break_flag = 1
    tmp_openset = list()
    for every_dataset in openset:
        if every_dataset['condition'] == True:
            # tmp_path = every_dataset['path']
            # print('tmp_path',tmp_path)
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
                print(i,gain)
                if gain > max_gain:
                    max_gain = gain
                    max_feature = i
                    max_feature_boundary = feature_boundary
                i += 1
            print(max_feature)
            print(max_feature_boundary)
            print(max_gain)
            dataset_1 = list()
            dataset_2 = list()
            for tmp in every_dataset['data']:
                if float(tmp[max_feature]) < max_feature_boundary:
                    dataset_1.append(tmp)
                else:
                    dataset_2.append(tmp)
            print('dataset_1',dataset_1)
            print('dataset_2',dataset_2)
            print(len(dataset_1))
            print(len(dataset_2))
            print(judge_next_precision(dataset_1,precision_boundary))
            print(judge_next_precision(dataset_2,precision_boundary))
            tmp_openset.append({'path':every_dataset['path'] + [(max_feature,max_feature_boundary,1)],'condition':judge_next_precision(dataset_1,precision_boundary), 'data':dataset_1})
            tmp_openset.append({'path':every_dataset['path'] + [(max_feature,max_feature_boundary,2)],'condition':judge_next_precision(dataset_2,precision_boundary), 'data':dataset_2})
        else:
            tmp_openset.append(every_dataset)

    print('tmp_openset',tmp_openset)
    openset = tmp_openset
    if break_flag == 1:#1:
        break

print(len(openset))
for result in openset:
    print(result['path'])
    # for tmp in result['data']:
    #     print(tmp[len(tmp) - 1])
    print(len(result['data']))
