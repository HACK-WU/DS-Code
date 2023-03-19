# _*_ coding : utf-8 _*_
# @Time : 2023/3/19 15:33
# @Author : HackWu
# @File : binarySearch
# @Project : DS-Code

def binarySearch(arr,start,end,target):
    while start<=end:                        #必须是start<=end,如果是start<end 会有死循环的风险，
        mid=(start+(end-start)//2)            #mid=(start+end)//2   ,这种写法，如果start或者end,数据过大，可能会造成溢出的风险，
        if arr[mid]==target:
            return mid                      #查到就返回索引
        elif arr[mid]<target:
            start=mid+1
        else:
            end=mid-1
    return -1


arr = [ 2, 3, 4, 10, 40 ]

res=binarySearch(arr,0,len(arr)-1,10)
print(res)


