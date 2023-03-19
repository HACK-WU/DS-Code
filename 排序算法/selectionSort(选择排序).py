# _*_ coding : utf-8 _*_
# @Time : 2023/3/19 20:35
# @Author : HackWu
# @File : selectionSort(选择排序)
# @Project : DS-Code


def selectionSort(arr):
    for i in range(len(arr)):
        minIndex=i                      #暂时定义最小值的索引为minIndex
        for j in range(i+1,len(arr)):   #循环查找最小值
            if arr[j]<arr[minIndex]:        #如果后面的某一个值，比arr[minIndex]的值还小，就更新minIndex,也就是重新定义最小值
                minIndex=j

        arr[i],arr[minIndex]=arr[minIndex],arr[i]       #将最小值与已排序末尾的值互换

arr=[64, 25, 12, 22, 11]
selectionSort(arr)
print(arr)

