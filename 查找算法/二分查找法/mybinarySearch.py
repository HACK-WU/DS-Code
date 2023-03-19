# _*_ coding : utf-8 _*_
# @Time : 2023/3/19 15:38
# @Author : HackWu
# @File : mybinarySearch
# @Project : DS-Code

'''
    封装二分查找算法：
原理就是将数据处理的过程分装到fun函数中。这样这需要关注fun的逻辑处理即可，不用在考虑二分查找的主要结构。
    fun函数的返回值是一个元组，(res,mid)
    res        #是一个字符串，只能限定为：
    True    #表示查询成功，不用再继续查询
    bigger    #表示mid 太大了，需要减小end的值，比如 end=mid-1
    smaller   #表示mid 太小了，选哟增大start的值，比如start=start+1
    mid    #返回的就是一个已经经过处理的mid值（可能增大，也可能减小），直接使用就行了。
    所以处理过程就为：
    res,mid=fun(arr,dic)        #arr 是需要查询的数组，dic 中封装了fun 处理数据过程需要的各种数据。比如参数。
'''

# 查询某个数开根号的值

def binarySearch(arr,start,end,dic):      #dic 为一个字典，里面分装了需要使用的函数对象fun,以及fun 需要的各种参数。arr 就是被查找的对象。
    if start<=end:
        mid=(start+(end-start)//2)
        fun=dic.get("fun")
        res,mid=fun(arr,mid,dic)

        if res=="True":
            return mid
        elif res=="bigger":
            return binarySearch(arr,start,mid,dic)
        else:
            return binarySearch(arr,mid,end,dic)
    else:
        return -1   #不存在返回-1


def fun(arr,mid,dic=None):
    target=dic.get("target")      #目标
    res=mid*mid
    num=target-res
    post=int(dic.get("post"))
    current=int(dic.get("current"))
    step=1/(10**current)
    mid=float(f"%.{post}f" % mid)

    if num==0:
        return "True",mid
    elif num>0:
        newmid=mid+step
        if newmid**2>target and current==post:    #current
            return "True",mid
        elif newmid**2>target:
            current+=1
            dic["current"]=current
            step=1/(10**current)
        return  "smaller",mid+step

    else:
        return "bigger",mid-step


dic={
    "fun":fun,
    #函数对象，需要自己定义
    "target":99,    #要开根号的数字
    "post":5,       #定义最终的精度值，5表示的就是1/(10**5) ,也就是0.00001 保留5位小数

    "current":0,    #定义当前的精度，同理0，就是，1/(10**0),,也就是1，一位小数都没有保留。
}


arr=[]
res=binarySearch(arr,1,dic.get("target"),dic)    #如果没有要被查询的列表，传入一个空列表即可。
print("res",res)

'''
    运行结果：
        res 9.94987
'''