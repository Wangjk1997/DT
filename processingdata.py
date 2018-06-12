fh = open('iris_data.txt')
fw = open('pdata.txt','w')
for line in fh:
#    for letter in line:
#        if (letter >= '0' and letter<='9' or letter == '.' or letter == ','):
#            fw.write(letter)
#    fw.write('\n')
    tmp = line.split(',')
    for word in tmp:
        if word == 'Iris-setosa\n':
            word = '1'
        if word == 'Iris-versicolor\n':
            word = '2'
        if word == 'Iris-virginica\n':
            word = '3'
        fw.write(' ')
        fw.write(word)
    fw.write(';')
fw.close();
fh.close();