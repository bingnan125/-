# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 16:45:20 2018

@author: Bona
"""

#插入排序
#待比较的元素前面的元素是排好序的，后面是乱序的，将它之其前面的元素比较，如
#如果比他大，将他们往后移动
def insert_sort(data):
    for i in range(1,len(data)):
        current_value = data[i]
        index = i
        
        while index>0 and data[index-1]>current_value:
            data[index]=data[index-1]
            index -= 1
        data[index]=current_value
    return data
insert_sort(data)


#希尔排序
def shell_sort(data):
    step = len(data)//2 #增量
    while step>0:
        for i in range(step,len(data)):
            #类似插入排序，当前值与指定步长之前的值比较，符合条件则交换位置
            while i>=step and data[i-step]>data[i]:
                data[i-step],data[i]=data[i],data[i-step]
                i-=step
        step = step//2
    return data
data = [12,89,8979,23214,214,3443,245,234]
shell_sort(data)

#冒泡排序
def bubble_sort(data):
    for i in range(len(data)-1):
        for j in range(len(data)-i-1):
            if data[j]>data[j+1]:
                data[j],data[j+1]=data[j+1],data[j]
    return data
data = [23,4,1,33,565,7,9,89,-2]
bubble_sort(data)

#改进的冒泡排序，加入一个校验，如果某次循环发现没有发生数值交换，直接跳出循环
def modi_bubble_sort(data):
    exchange = True
    passnum=len(data)-1
    while passnum>=1 and exchange:
        exchange = False
        for i in range(passnum):
            if data[i]>data[i+1]:
                data[i],data[i+1]=data[i+1],data[i]
                exchange = True
        passnum-=1
    return data



#快速排序
def quick_sort(data,low,high):
    if low<high:
        splitPoint=partition(data,low,high)
        quick_sort(data,low,splitPoint-1)
        quick_sort(data,splitPoint+1,high)
    return data

def partition(data,low,high):
    base = data[low]
    left = low
    right = high
    while left < right:
        while left<right and data[right]>=base:
            right -= 1
        data[left] = data[right]
        while left < right and data[left] <= base:
            left += 1
        data[right]=data[left]
        data[left]=base
    return left

data= [2,5,1,2,35,7,54,-8,8]
quick_sort(data,0,len(data)-1)


#归并排序
def merge(data1,data2):
    ans = []
    i = j = 0
    while i<len(data1) and j < len(data2):
        if data1[i] < data2[j]:
            ans.append(data1[i])
            i += 1
        else:
            ans.append(data2[j])
            j += 1
    ans += data1[i:]
    ans += data2[j:]
    return ans
def merge_sort(data):
    if len(data)<=1:
        return data
    mid = len(data)//2
    data1 = data[:mid]
    data2 = data[mid:]
    return merge(mergeSort(data1),mergeSort(data2))
         
a =[1,34,2,4,90,322,89]            
merge_sort(a)


#基数排序分为最低位优先法和最高位优先法
def radix_sort(data):
    if len(data)==0:
        return
    if len(data)==1:
        return data
    d = len(str(max(data)))
    for k in range(d):
        s = [[] for i in range(10)]
        for i in data:
            s[i//(10**k)%10].append(i)
        data=[j for i in s for j in i]
    return data
data = [12,89,8979,23214,214,3443,245,234]
radix_sort(data)

        
#选择排序
def selection_sort(data):
    for i in range(len(data)-1):
        min_index = i #暂时设定最小值为无序区间第一个元素
        #用当前最小的index的值分别与后面的值进行比较，以便获得最小的index
        for j in range(i+1,len(data)):
            if data[j]>data[min_index]: 
                min_index = j
            data[min_index],data[j]=data[j],data[min_index]
    return data
data = [12,89,8979,23214,214,-2,-6,3443,245,234]
selection_sort(data)

#堆排序

#在堆中做结构调整使得父节点的值大于子节点的值
def max_heapify(heap,heap_size,root):
    left = 2*root+1
    right = left + 1
    x = heap[root]
    while left < heap_size:
        if right < heap_size and heap[right] < heap[left]:#找到结点root子节点的最小值
            left += 1
        if heap[left]>=x:   #若两个子节点均不小于该结点，则不需调整
            break
        heap[root],heap[left]=heap[left],heap[root]
        root = left
        left = root*2 +1
#构建一个堆，将堆中所有数据重新排序
def Build_MAX_Heap(heap):
    heap_size = len(heap)
    for i in range((len(heap)-2)//2,-1,-1):#对非叶子节点的子节点进行调节，构建堆
        max_heapify(heap,heap_size,i)
        
#将根节点取出与最后一位做对调，对前面len-1个节点继续进行对调过程
def heap_sort(heap):
    Build_MAX_Heap(heap)   #构建最小堆
    for i in range(len(heap)-1,0,-1):   #对堆中元素逆向遍历
        heap[0],heap[i]=heap[i],heap[0]   #将堆中元素与堆中最后一个元素对调
        max_heapify(heap,i,0)   #重新调整剩下的元素使之满足最小堆的性质
    return heap
heap = [0,12,89,8979,23214,214,-2,-6,3443,245,234]
heap_sort(heap)










            