# _*_ coding : utf-8 _*_
# @Time : 2023/3/19 16:58
# @Author : HackWu
# @File : bubbleSort(冒泡排序)
# @Project : DS-Code


def bubbleSort(arr):
    n=len(arr)
    #遍历所有的数组元素
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

arr = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(arr)
print(arr)

