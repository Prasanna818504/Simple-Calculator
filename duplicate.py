def duplicate(arr):
    count=0
    
    res=arr-list(set(arr))
    return res
        

    
if __name__=='__main__':
    arr=list(map(int,input().split()))
    print(duplicate(arr))