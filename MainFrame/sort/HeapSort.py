# coding:utf-8
import numpy as np


PARENT = lambda i:i/2
LEFT = lambda i:2*i+1
RIGHT = lambda i:2*i+2




class VLHeapSort(object):
    """
        针对找矩阵中最大的那几个的队排序
    """

    def __init__(self, matrix):
        self.nums_array = []
        self.matrix = matrix
        self.flatten()
        self.heap_size = 0
        self.sorted = False

    def flatten(self):
        """
        参数: 无
        输出: 一位数组，但是记录了这个值原本在数组里的位置，x，y
        描述: 一个for循环，满满遍历寻找
        """
        y_len = len(self.matrix)
        for y in xrange(0, y_len):
            for x in xrange(0, len(self.matrix[y])):
                self.nums_array.append({"value":self.matrix[y][x], "x":x, "y":y})

    def heapfy(self,nums_array,i):
        """
        参数: 
        输出: 
        描述: 调整堆，调整为大顶堆或者小顶堆
        """
        l, r = LEFT(i), RIGHT(i)
        largest = l if l < self.heap_size and nums_array[l]["value"] < nums_array[i]["value"] else i  # 最小堆则改为 A[l] < A[i]
        largest = r if r < self.heap_size and nums_array[r]["value"] < nums_array[largest]["value"] else largest # 最小堆则改为A[r] < A[largest]

        if i!=largest:
            nums_array[i], nums_array[largest] = nums_array[largest], nums_array[i]
            self.heapfy(nums_array, largest)

    def build_max_heap(self,nums_array):
        """
        参数: 
        输出: 建立大顶堆
        描述: 从倒数第二层开始向上创建大顶堆
        """
        self.heap_size = len(self.nums_array)
        for i in range(len(nums_array)//2-1, -1, -1):
            self.heapfy(nums_array, i)

    def sort(self):
        self.sorted = True
        self.build_max_heap(self.nums_array)
        nums_array = self.nums_array
        for i in range(len(nums_array)-1, -1, -1):
            nums_array[i], nums_array[0] = nums_array[0], nums_array[i]
            self.heap_size -= 1
            self.heapfy(nums_array, 0)
    
    def top(self,num):
        """
        参数: 
        输出: 
        描述: 返回前n个
        """
        if not self.sorted:
            self.sort()
        return self.nums_array[0:num]

    def __str__(self):
        pass

def main():
    a = np.array([[1,2,3],[2,3,4],[5,6,7]])
    heapq = VLHeapSort(a)
    heapq.sort()

if __name__ == '__main__':
    main()
