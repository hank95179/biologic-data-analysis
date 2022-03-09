# def intro(name,age,hobby):
#     print(f'Hello, I am {name}.')
#     print(f'I am {age} years old.')
#     print(f'I like {hobby}.')
#     print('I am bery happy to join this class.')
# def printN(s,n):
#     for i in range(n):
#         print(s)
def Grid(col,row,space):
    Line(' +',' -',row,space)
    for i in range(col):
        for i in range(space):
            Line(' |','  ',row,space)  
        Line(' +',' -',row,space)
def Line(node,edge,row,space):
        print(((node+edge*space)*row)+node)
def HoneyCube(row,col):
    print(' __   '*col)
    for i in range(row):
        print("/  \\__" * (col-1)+'/  \\')
        print('\\__/  '*col)
def BigX(n):
    for i in range(2*n+1):
        # print(i)
        for j in range(2*n+1):
            if i == j or ((2*n)-i) == j:
                print('x ', end = '')
            else:
                print('  ', end = '')
        print('')
def NineByNine(s,e):
    for i in range(s):
        for j in range(e):
            print(f'{j+1}x{i+1}={(i+1)*(j+1)}',end = '\t')
        print('')
def Sum(n):
    for i in range(n+1):
        if i == 0:
            continue
        for j in range(i):
            if(j == i-1):
                print(j+1,end = '=')
                # print()
            else:
                print(j+1,end = '+')
        print(count(i))
def count(n):
    tem = 0
    for i in range(n+1):
        tem += i
    return tem
Grid(2,6,2)
HoneyCube(3,7)
# # printN('Hi',5)
BigX(10)
NineByNine(15,7)
Sum(25)