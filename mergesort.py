def merge(a,b):
    (c,m,n) = ([],len(a),len(b))
    (i,j) = (0,0) # initial indices of a and b
    while i+j < m+n:
        if i == m:
            c.append(b[j])
            j += 1
        elif j == n:
            c.append(a[i])
            i += 1
        elif a[i] <= b[j]:
            c.append(a[i])
            i += 1
        elif a[i] > b[j]:
            c.append(b[j])
            j += 1
    return c
def mergesort(a,l,r):
    if r-l <= 1:
        return a[l:r]
    elif r-l > 1:
        mid = (r+l)//2
        left = mergesort(a,l,mid)
        right = mergesort(a,mid,r)
    return merge(left,right)
size = int(input("How many numbers"))
print("Enter the numbers to be sorted")
n = list(map(int,input().split()))
print("Sorted list is {} ".format(mergesort(n,0,size)))
