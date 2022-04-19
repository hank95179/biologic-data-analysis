import math 
def  Fibonacci(n):
    Flist = []
    for i in range(n):
        if i<2:
            Flist.append(1)
        else:Flist.append(Flist[i-1]+Flist[i-2])
    print(Flist)


def LIS(a):
    ans = []
    for i in range(len(list_a)):
        tmp = []
        for j in range(i,len(list_a)):
            if j == i: tmp.append(list_a[j])
            elif list_a[j] > tmp[len(tmp)-1]: tmp.append(list_a[j])
        if len(tmp) > len(ans):
            ans = tmp
    print(ans)
def MeanGrade(fi,fo):
    fin = open(fi, 'r')
    fout = open(fo, 'w')
    line = fin.readline()
    fout.write(line[0:len(line)-1] + "\tmean\n")   
    line = fin.readline()
    while(line):
        avg = 0
        avg += float(line[8:10])  
        avg += float(line[12:14])  
        avg += float(line[16:18])  
        avg += float(line[20:22])  
        line = line[0:len(line)]
        fout.write(line[0:22] + "  {0:.2f}\n".format(avg/4))     
        line = fin.readline()
    fin.close()
    fout.close()
def BWT(s):
    input = '$' + s
    ans = ''   
    list_bwt = []
    list_bwt.append(input)
    for i in range(len(s)):
        input = input[1:] + input[0]
        list_bwt.append(input)
    list_bwt.sort()
    for i in range(len(list_bwt)):
        ans += list_bwt[i][len(input) - 1]
    return ans
list_a = [9,2,5,1,6,4]
s = 'ATCCGATCGAGC'
print(BWT(s))
LIS(list_a)
MeanGrade("grade.txt","outpu.txt")
Fibonacci(10)