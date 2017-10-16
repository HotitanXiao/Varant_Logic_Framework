# coding:utf-8
heap_size = 0
LEFT = lambda i: 2*i+1
RIGHT = lambda i: 2*i+2 
# 维护最大堆
def HEAPIFY(A, i):
    l, r = LEFT(i), RIGHT(i)
    largest = l if l < heap_size and A[l] > A[i] else i # 最小堆则改为 A[l] < A[i]
    largest = r if r < heap_size and A[r] > A[largest] else largest # 最小堆则改为A[r] < A[largest]
    if i != largest:
        A[i], A[largest] = A[largest], A[i]
        HEAPIFY(A,largest)
# 构建最大堆
def BUILD_MAX_HEAP(A):
    global heap_size
    heap_size = len(A)
    for i in range(len(A)//2-1,-1,-1):
        HEAPIFY(A,i)
# 堆排序
def HEAPSORT(A):
    global heap_size
    BUILD_MAX_HEAP(A)
    for i in range(len(A)-1,-1,-1):
        A[i], A[0] = A[0], A[i]
        heap_size -= 1
        HEAPIFY(A,0)


def main():
    a = [1,2,3,435,324,55,6,1,3,4]
    HEAPSORT(a)
    print a

if __name__ == '__main__':
    main()