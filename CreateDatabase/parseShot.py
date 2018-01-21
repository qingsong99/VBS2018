import pickle

dict = pickle.load(open('name2index.pickle', 'rb'))
list = dict.items()
filePath = 'msb/%smsb'
fileSave = 'shot/%s.txt'

for item in list:
    input = open(filePath % item[0][:-3], 'r')
    output = open(fileSave % item[1], 'w')
    i = 0
    for line in input:
        i = i + 1
        if (i <= 2):
            continue
        [start, end] = line.split()
        string = 'shot%s_%s#%s#%s\n' % (item[1], str(i - 2), start, end)
        output.write(string)

