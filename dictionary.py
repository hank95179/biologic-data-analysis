import re
from collections import defaultdict
def Unique(n):
    ans = []
    for i in n:
        # unique = True
        # if len(ans) == 0: ans.append(i);unique = False
        # else:
        #     for j in ans:
        #         if i == j:unique = False
        # if unique:ans.append(i)
        if i not in ans: ans.append(i)
    return ans
def WordCount(f):
    mark_set = "\"\',.?!*[]#:"
    fin = open(f, 'r',encoding="utf-8")
    ec = {}
    all = []
    a = 0
    line = fin.readline()
    while line:
        for iterator in mark_set:
                line = line.replace(iterator,'')
                line = line.replace('\n','') #replace space
                line = line.lower()
        str = line.rstrip()
        str = re.split(' |-',str)
        # print(str)
        all+=str
        a += len(str)
        line = fin.readline()
    for e in all: 
        ec[e] = ec.get(e,0) + 1
    # print(len(all))
    # for e in all: 
    #     if e == 'of':
    #         print("Y")
    sorted_count = sorted(ec.items(),key = lambda d:d[1],reverse = True)
    data_dict = {}
    for x in sorted_count:
        data_dict.setdefault(x[0],[]).append(x[1])
    print(data_dict)
    return data_dict
#####
eng2sp = {'one':'uno','two':'dps'}
# for eng in eng2sp:
#     print(f'{eng}:{eng2sp[eng]}')
def LoadDict(f):
    d = {}
    fi = open(f,'r')
    line = fi.readline()
    while line:
        a = line.rstrip().split()
        line = fi.readline()
        d[a[0]] = a[1]
    return d
def ShowDict(d):
    for k,v in d.items():
        print(f'{k} : {v}')
def Histogram(n):
    ec = {}
    for e in n:
        ec[e] = ec.get(e,0) + 1
    return ec
# ShowDict(LoadDict("dict.txt"))
#####
def  MicrornaTarget(fi, fo):
    d = {}
    fin = open(fi,'r')
    fout = open(fo,'w')
    line = fin.readline()
    line = fin.readline()
    answer = defaultdict(list)
    # for i in range(58510):
    #     line = fin.readline()
    while line:
    # for i in range(58510,58520):
        a = line.rstrip()
        str = re.split(' |//|\t',a)
        # print(str)
        for i in str:
            if i == 'Luciferase':
                if str[4] not in answer[str[1]]:
                    answer[str[1]].append(str[4])
                # print(answer)
        line = fin.readline()
    for k,v in answer.items():
        fout.write(k+"  ")
        for i in range(len(v)):
            if i == 0:
                fout.write(v[i])
            else: 
                fout.write(","+v[i])
        fout.write("\n")
    
a = [2,7,5,7,5,7,5]
ec = Histogram(a)
# ShowDict(ec)
ua = Unique(a)
WordCount("nature_short.txt")
MicrornaTarget('hsa_MTI.txt', 'output.txt')
print(ua)