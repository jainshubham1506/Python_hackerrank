a=input()
odd=[]
even=[]
sub=[];
for each in range(a,0,-1):
    if each%2==0:
        even.append(each);
    else:
        odd.append(each);
    o=len(even)
    e=len(odd);
    odd.sort();
    even.sort();
    if len(even)>0 and len(odd)>0:
        if odd[o-1]>even[e-1]:
            lar=odd[o-1];
        else:
            lar=even[e-1];
