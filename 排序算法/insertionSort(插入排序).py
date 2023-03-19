# _*_ coding : utf-8 _*_
# @Time : 2023/3/19 20:22
# @Author : HackWu
# @File : insertionSort(插入排序)
# @Project : DS-Code


def insertionSort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:  #把大的数字向后移动
            arr[j+1]=arr[j]         #把前面的一个数向后移动
            j-=1                    #然后j减去1，在比较前面的一个数，如果前面的一个数依然大于key,那么再把它向后移动，直到前面的数，不再大于key.
        arr[j+1]=key        #这个才是真正的插入操作。

arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print(arr)




