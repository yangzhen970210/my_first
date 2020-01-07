# 1.2 二分查找 其输入一个有序的列表
def binary_search(lists, item):
    low = 0
    high = len(lists) - 1
    while low < high:
        mid = int((low + high)/2)
        guess = lists[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return 'not found'

lit = list(range(100000))
binary_search(lit, 666)
binary_search(lit, 666666)

# 查找对数时间      and 常量时间和线性时间
#2.2 数组和链表
import pandas as pd 
df = pd.DataFrame({'数组':['O(1)', 'O(N)', 'O(N)'],'链表':['O(N)', 'O(1)', 'O(1)']}, index = ['读取', '插入', '删除'])
df
	数组	链表
读取	O(1)	O(N)
插入	O(N)	O(1)
删除	O(N)	O(1)

# 2.3 选择排序  O(n*n)
def choice_sort(arr):
    newarr = []
    
    while len(arr) >= 1:
        lit = arr[0]
        litindex = 0
        for x in range(1,len(arr)):
            if arr[x] < lit:
                lit = arr[x]
                litindex = x
        newarr.append(arr.pop(litindex))
    return newarr
choice_sort([1,3,-5,2,22,11,6,32,77,12])

def findsmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionsort(arr):
    newarr = []
    for x in range(len(arr)):
        smallest = findsmallest(arr)
        newarr.append(arr.pop(smallest))
    return newarr
selectionsort([1,3,-5,2,22,11,6,32,77,12])

"""
❑ 计算机内存犹如一大堆抽屉。
❑ 需要存储多个元素时，可使用数组或链表。
❑ 数组的元素都在一起。
❑ 链表的元素是分开的，其中每个元素都存储了下一个元素的地址。
❑ 数组的读取速度很快。❑ 链表的插入和删除速度很快。
❑ 在同一个数组中，所有元素的类型都必须相同（都为int、double等）。
"""
# 第三章 递归
# 自己调用自己
# 基线条件和递归条件

"""
我怀着激动的心情编写本章，因为它介绍的是递归——一种优雅的问题解决方法。
递归是我最喜欢的主题之一，它将人分成三个截然不同的阵营：恨它的、爱它的以及恨了几年后又爱上它的。
"""

# 3.3 栈  后进先出   递归栈
"""
❑ 递归指的是调用自己的函数。
❑ 每个递归函数都有两个条件：基线条件和递归条件。
❑ 栈有两种操作：压入和弹出。
❑ 所有函数调用都进入调用栈。
❑ 调用栈可能很长，这将占用大量的内存。"""

"""
使用栈虽然很方便，但是也要付出代价：存储详尽的信息可能占用大量的内存。
每个函数调用都要占用一定的内存，如果栈很高，就意味着计算机存储了大量函数调用的信息。
在这种情况下，你有两种选择。
❑ 重新编写代码，转而使用循环。
❑ 使用尾递归。这是一个高级递归主题，不在本书的讨论范围内。另外，并非所有的语言都支持尾递归。"""

# 第四章 快速排序
def digui(arr):
    if len(arr) > 1:
        arr0 = arr[0]
        arr1 = []
        site = 0
        for x in range(1, len(arr)):
            if arr[x] < arr0:
                site = x
        arr1.append(arr.pop(site))
        return arr1 + (digui(arr))
    else:
        return arr     
digui([1,3,-5,2,22,11,6,32,77,12])        
