def merge(arr,l,m,r):
    n1=m-l+1
    n2=r-m
    lr=[]
    rr=[]

    for i in range(n1):
        lr.append(arr[l+i])
    
    for j in range(n2):
        rr.append(arr[m+1+j])

    

def mergesort(arr,l,r):
    if r>l:
        m=(l+r)/2
        mergesort(arr,l,m)
        mergesort(arr,m,r)
        merge(arr,l,m,r)



if __name__=="__main__":
    n=int(input())
    arr=[]
    for i in range(n):
        ele=int(input())
        arr.append(ele)
    l=0
    r=n
    print(arr)
    mergesort(arr,l,r)
    print(arr)