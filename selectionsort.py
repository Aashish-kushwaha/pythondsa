def slectionsort(a,n):
    for i in range(n):
        min_idx=i
        for  j in range(i+1,n):
            if a[j]<a[min_idx]:
                min_idx=j 
        if min_idx!=i:
            temp=a[i]
            a[i]=a[min_idx]
            a[min_idx]=temp

if __name__=="__main__":
    n=int(input())

    arr=[]
    for i in range(n):
        ele=int(input())
        arr.append(ele)
    
    print(arr)
    slectionsort(arr,n)
    print(arr)

