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
                    dataset_1.append(tmp[0:max_feature] + tmp[max_feature+1:len(tmp)])
                else:
                    dataset_2.append(tmp[0:max_feature] + tmp[max_feature + 1:len(tmp)])
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
# feature0 = boundarySet(dataset,0)
# feature1 = boundarySet(dataset,1)
# feature2 = boundarySet(dataset,2)
# feature3 = boundarySet(dataset,3)
# print(feature0)
# print(feature1)
# print(feature2)
# print(feature3)
# print(boundary(feature0,dataset,0,4))
# print(boundary(feature1,dataset,1,4))
# print(boundary(feature2,dataset,2,4))
# print(boundary(feature3,dataset,3,4))
# print(judge_next_precision(dataset,precision_boundary))
#
# dataset1_1 = list()
# dataset1_2 = list()
# for tmp in dataset:
#     if float(tmp[2])<2.45:
#         dataset1_1.append(tmp[0:2]+tmp[3:len(tmp)])
#     else:
#         dataset1_2.append(tmp[0:2]+tmp[3:len(tmp)])
# print('dataset1_1',dataset1_1)
# print('dataset1_2',dataset1_2)
# print(len(dataset1_1))
# print(len(dataset1_2))
# print(judge_next(dataset1_1))
# print(judge_next(dataset1_2))
# print(judge_next_precision(dataset1_1,precision_boundary))
# print(judge_next_precision(dataset1_2,precision_boundary))
# feature1_0 = boundarySet(dataset1_2,0)
# feature1_1 = boundarySet(dataset1_2,1)
# feature1_2 = boundarySet(dataset1_2,2)
# print(feature1_0)
# print(feature1_1)
# print(feature1_2)
# print(boundary(feature1_0,dataset1_2,0,3))
# print(boundary(feature1_1,dataset1_2,1,3))
# print(boundary(feature1_2,dataset1_2,2,3))
#
# # dataset2_1 = list()
# dataset2_2 = list()
# for tmp in dataset1_2:
#     if float(tmp[2])<1.75:
#         dataset2_1.append(tmp[0:2]+tmp[3:len(tmp)])
#     else:
#         dataset2_2.append(tmp[0:2]+tmp[3:len(tmp)])
# print('dataset2_1',dataset2_1)
# print('dataset2_2',dataset2_2)
# print(len(dataset2_1))
# print(len(dataset2_2))
# print(judge_next(dataset2_1))
# print(judge_next(dataset2_2))
