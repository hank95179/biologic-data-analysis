import math
import turtle
import random
import time
def Olympic(t, r):
    t.pensize(0.15*r)
    t.pu()
    t.goto(0,r)
    t.pd()
    t.circle(r)
    t.pu()
    t.pencolor('blue')
    t.goto(-2.4*r,r)
    t.pd()
    t.circle(r)
    t.pu()
    t.pencolor('yellow')
    t.goto(-1.2*r,0)
    t.pd()
    t.circle(r)
    t.pu()
    t.pencolor('green')
    t.goto(1.2*r,0)
    t.pd()
    t.circle(r)
    t.pu()
    t.pencolor('red')
    t.goto(2.4*r,r)
    t.pd()
    t.circle(r)
def PalindromeQ(s):
    original = 'ATCGatcg'
    transform = 'TAGCtagc'
    table = s.maketrans(original,transform)
    tmp = s.translate(table)
    tmp = tmp[::-1]
    if s == tmp:
        return "True"
    return "False"
def SubjectMean(fi, fo):
    fin = open(fi, 'r')
    fout = open(fo, 'w')
    line = fin.readline()
    fout.write(line[0:len(line)-1]+"\n")   
    line = fin.readline()
    Cn =0
    En=0
    Bl=0
    Mt=0
    while(line):
        Cn += float(line[8:10])  
        En += float(line[12:14])  
        Bl += float(line[16:18])  
        Mt += float(line[20:22])  
        line = line[0:len(line)]
        fout.write(line[0:22]+ "\n")     
        line = fin.readline()
    fout.write("mean\t {0:.2f}\t{1:.2f}\t{2:.2f}\t{0:.2f}".format(Cn/4,En/4,Bl/4,Mt/4))
    fin.close()
    fout.close()
def ShowMatrix(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j],end = '\t')
        print("")
def Transpose(m):
    re = []
    for i in range(len(m[0])):
        tmp = []
        for j in range(len(m)):
            tmp.append(m[j][i])
        re.append(tmp)
    return re
def FastaLength(fi):
    fin = open(fi, 'r')
    line = fin.readline()
    id = line.rstrip().split()[1]
    line = fin.readline()
    sl = 0
    ans_list = []
    # print(line)
    while(line):
        if line[0] == '>':
            ans_list.append(sl)
            id = line.rstrip().split()[1]
            sl = 0
        else: 
            sl += len(line)
        line = fin.readline().rstrip()
    ans_list.append(sl)
    return ans_list
def N50(ans_list):
    size = sum(ans_list)
    ans = 0
    ans_list.sort(reverse=True)
    for i in(ans_list):
        ans += i
        if ans >= size/2: 
            return i

#第一題
t1 = turtle.Turtle()
Olympic(t1,50)
turtle.exitonclick()
#第二題
s = 'CGCG'
print(PalindromeQ(s))
#第三題
SubjectMean("grades.txt","outpu.txt")
#第四題
a = FastaLength("ASM78801v1.fna")
n50 = N50(a)
print(n50)
#第五六題
m = [[11, 12], [21, 22], [31, 32]]
tm = Transpose(m)
ShowMatrix(tm)