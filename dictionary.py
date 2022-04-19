def Unique(n):
    ans = []
    for i in n:
        unique = True
        if len(ans) == 0: ans.append(i);unique = False
        else:
            for j in ans:
                if i == j:unique = False
        if unique:ans.append(i)
    return ans
#####
eng2sp = {'one':'uno','two':'dps'}
# for eng in eng2sp:
#     print(f'{eng}:{eng2sp[eng]}')
def ShowDict(d):
    for k,v in d.items():
        print(f'{k} : {v}')
ShowDict(eng2sp)
#####
a = [2,7,5,7,5,7,5]
ua = Unique(a)
# print(ua)