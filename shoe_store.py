if __name__ == '__main__':
    l = int(input())
    lst = [int(x) for x in input().split()]
    lst=sorted(lst, reverse=True)
    print(lst)
    mz = max(lst)
    for i in lst:
        if i < mz:
            print(i)
            break
