def gf(n):
    for i in range(1,n+1):
        for j in range(i):
            print("*", end='')
        for k in range((2*(n-1))-(2*j)):
            print("#", end='')
        for l in range(i):
            print("*",end='')
        print()
    
testcases = int(input())
for _ in range(testcases):
    num = int(input())
    gf(num)
    print()
