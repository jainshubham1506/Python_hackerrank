a=[int(x) for x in input().split()]
for i in range(0,len(a)-1):
    mini=i
    for j in range(i+1,len(a)):
        if a[j]<a[mini]:
            mini=j
    a[mini],a[i]=a[i],a[mini]
print (a)