def mtd(num):
    lst2=[];
    lst2=list(str(num));
    #print (lst2);
    count=0;
    for each in lst2:
        if each!='2':
            count=count+1;

        else:

            if count<len(lst2) and count+1<=len(lst2):
                    print (count);
                    if lst2[count]=='1':
                    #print("the streak is broken!");
                        return 0;
                    
                    else:
                        continue;
            else:
                return 1;
                
               
while 1:        
    b=mtd(int(input()))
    if b==0:
        print("the streak is broken!");
    else:
        print("the streak stays in our hearts!");
    
