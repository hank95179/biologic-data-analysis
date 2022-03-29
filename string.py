def FindAll(s, ss):
   for i in range(0,len(s) - len(ss)+1):
       if s[i:i+len(ss)] == ss :
           print(i)
def ShowFile(fi,n):
    file = open(fi, 'r')
    line = file.readline()
    for i in range(n):
        print('{0:d}: '.format(i+1),line,end = '')
        line = file.readline()
    file.close()
# def Print(n):
#     for i in range(len(n)):
#         str = ''
#         str += n[i]
#         str += '\t'
#         if  i == 0 and len(n[i]) < 8:
#             str += '\t'
#     str += '\n'
#     return str
def ExtractDEG(fi, fo):
    fin = open(fi, 'r')
    fout = open(fo, 'w')
    line = fin.readline()
    while(line):
        if line[0] == '\n':
            line = fin.readline()
            a = line.rstrip().split(' ')
            fout.write(a[1]+'\n')
        else:
            line = fin.readline()
    fin.close()
    fout.close()
def SelectAAByCharge(fi, fo, c):
    fin = open(fi, 'r')
    fout = open(fo, 'w')
    line = fin.readline()
    fout.write(line)
    while(line):
        a = line.rstrip().split('\t')
        if a[3] == c: fout.write(line)    
        line = fin.readline()
    fin.close()
    fout.close()
def FastaLengthen(fi):
    fin = open(fi, 'r')
    line = fin.readline()
    while(line):
        if line[0] == '>':
            id = line.rstrip()[1:]
            sl = 0
        elif (line != '\n'):
            sl += len(line)
        else: print(f'{id}\t{sl}')
        line = fin.readline()
    fin.close()
def SimplifyFasta(fin,fput):
    fin = open(fin, 'r')
    fout = open(fput,'w+')
    line = fin.readline()
    id = line.rstrip()[1:]
    # print('>',id)
    sl = ''
    while(line):
        if line[0] == '>':
            if sl != '':
                fout.write('>'+id+'\n'+sl+'\n')
            id = line.rstrip()[1:]
            sl = ''
        else: sl += line.rstrip()
        line = fin.readline()
    fout.write('>'+id+'\n'+sl)
    fin.close()
    fout.close()
def RCFasta(fi, fo) :
    original = 'ATCGatcg'
    transform = 'TAGCtagc'
    
    fin = open(fi, 'r')
    fout = open(fo,'w+')    
    line = fin.readline()
    id = line.rstrip()[1:]
    sl = ''
    while(line):
        if line[0] == '>':
            if sl != '':
                sl = sl[::-1]
                fout.write('>'+id+'\n'+sl+'\n')
            id = line.rstrip()[1:]
            sl = ''
        else: 
            table = line[0:len(line)-1].maketrans(original,transform)
            tmp = line.translate(table)
            # tmp = tmp[::-1]
            sl += tmp[0:len(tmp)-1]
        line = fin.readline()
    
    sl = sl[::-1]
    fout.write('>'+id+'\n'+sl+'\n')
    fin.close()
    fout.close()
def ShowFile1(fin):
    
    fin = open(fin, 'r')    
    line = fin.readline()
    while(line):
        line = line.strip()
        print (line)
        line = fin.readline()
    fin.close()
def ShowFile(fin,row):
    fin = open(fin, 'r')
    for i in range(row):
        line = fin.readline()
        print(line)
    fin.close()

# FindAll('banana','na')
# ShowFile('text.txt',20)
# ExtractDEG('GDS4938_deg.txt','output.txt')
# SelectAAByCharge('text.txt','output.txt','-')
# FastaLengthen('p53.faa')
SimplifyFasta('p53_1.faa','output.txt')
# RCFasta('tdf.fa','output.txt')
ShowFile1('output.txt')