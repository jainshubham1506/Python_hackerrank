lst=[]
stu=[]
pr=0;
no=[]
has={}
ip=input()
lst=ip.strip().split()
lst=[int(y) for y in lst]
lo=input();
stu=lo.strip().split();
stu=[int(x) for x in stu]
for each in range(0,lst[2]):
    has[each+1]=lst[2]
for xy in stu:
    if has.get(xy)>0:
        has[xy]=has[xy]-1;
        pr=pr+1;
    else:
        pr=pr+1;
        no.append(pr)
#print (has);
print (len(no));