
a = int(input())
b = []
dat = []
mx = (0,[])
for i in range(a):
    q,w = map(int,input().split())
    b.append((q,i+1,1))
    b.append((w,i+1,-1))
    dat.append((q,w))
b.sort(key = lambda k:k[2],reverse=True)
b.sort(key=lambda k:k[0])
cur = 0
for i in b:
    if i[2] == 1:
        cur+=1
    else:
        if cur > mx[0]:
            mx = (cur,i[0])
        cur-=1
print(mx[0])
lis = []
for i in range(a):
    if dat[i][0] <= mx[1] <= dat[i][1]:
        lis.append(1+i)
print(*lis)
        