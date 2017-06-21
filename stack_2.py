import sys
dict={')':'(','}':'{',']':'['}
t = int(input().strip())
for _ in range(int(input())):
    stack = []
    for x in input():
        if stack and dict.get(x) == stack[-1]:
            stack.pop()
        else:
            stack.append(x)
        print("NO" if stack else "YES")