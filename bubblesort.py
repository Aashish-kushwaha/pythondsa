def bubblesort(a,n):

    for i in range(n-1):
        for j in range(n-i-1):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp


if __name__=="__main__":
    print("enter number")
    n=int(input())
    arr=[]
    print("enter element")
    for i in range(n):
        ele=int(input())
        arr.append(ele)

    print(arr)
    bubblesort(arr,n)
    print(arr)