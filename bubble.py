def bubble(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j+1]<arr[j]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=[23,1,1,56,2,5,6,69]
bubble(arr)
print(arr)