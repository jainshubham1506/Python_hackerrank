def super_sum(x):
    print (x)
    x=[int(y) for y in str(x)]
    if len(x)!=1:
         #print (x)
         super_sum(sum(x))
    else:
        return x
x=input()
m,n=x.split(' ')
#print (m)
n=int(n)
#print (n)
lst=[int(y) for y in list(m)]
mst=[]
for _ in range(0,n):
    for e in lst:
         mst.append(e)
        # print (type(mst))
#print (mst)
t=super_sum(mst)
print (t)