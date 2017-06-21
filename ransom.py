def ransom_note(magazine, ransom):
    lmag = list(map(str(), magazine))
    lran = list(map(str(), ransom))
    print (lmag)
    print (lran)
    count = 0
    for each in lran:
        if each in lmag:
            count += 1
        else:
            continue
    if count == len(lmag):
        return True
    else:
        return False


m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if (answer):
    print("Yes")
else:
    print("No")