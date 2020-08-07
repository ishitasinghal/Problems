arr = [1,3,-4,3,0,-5,5,2,-7]
l = len(arr)
list1=[]
for i in range(l):
    s=0
    for j in range(i,l):
        s = s+arr[j]
        if(s==0):
            list1.append(list(range(i,j+1)))
for i in list1:
    for j in i:
        print(arr[j], end=' ')
    print()
