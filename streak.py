a=int(input());


def mtd(num):
    lst2 = [];
    lst2 = list(str(num));
    # print (lst2);
    count = 0;
    for each in lst2:
        if each != '2':
            count = count + 1;

        else:

            if count < len(lst2) and count + 1 < len(lst2):
                #print(count);
                if lst2[count+1] == '1':
                    # print("the streak is broken!");
                    return 0;

                else:
                    continue;
            else:
                return 1;

    del count,lst2,num;
    

for _ in range(a,0,-1):
    number=input()
    b=0;
    c=0;
    x=sum(map(int, str(number)))
    if x%3==0:
        b=0
    else:b=1;
    y=str(number)
    lst=[]
    lst=y.split()
    j=len(lst)
    f=lst[j-1]
    if 2*int(f)%7==0:
        c=0;
    else:
        c=1;
    if b==0 and c==0:
        print("The streak is broken!")
        
    else:
        #print (number);
        b=mtd(number);
        if b==0:
            print("The streak is broken!")
            
        else:
           print("The streak lives still in our heart!")
           
    del number;
    del b,x,y,lst,j,f;
    
