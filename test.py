# coding:utf-8
from core.Gorilla import gorilla
from decimal import Decimal
import math
A = [2,4,6,7,8,9,1,4,56,7]
heap_size = 0
PARENT = lambda i: i/2
LEFT = lambda i: 2*i+1
RIGHT = lambda i: 2*i+2
# 维护最大堆
def heapfy(A,i):
    l,r = LEFT(i),RIGHT(i)
    largest = l if l < heap_size and A[l] > A[i] else i
    largest = r if r < heap_size and A[r] > A[largest] else largest
    if i != largest:
        A[i], A[largest] = A[largest], A[i]
        heapfy(A,largest)

def build_heap(A):
    # 自底向上进行调整
    # xrange(start,stop,step)
    global heap_size
    heap_size = len(A)
    for start in xrange(len(A)//2,-1,-1):
        heapfy(A,start)

def HEAPSORT(A):
    global heap_size
    build_heap(A)
    for i in xrange(len(A)-1,-1,-1):
        A[i], A[0] = A[0], A[i]
        heap_size -= 1
        heapfy(A,0)


def main():
    # HEAPSORT(A)
    # print A
    a = gorilla.GorilaBasis()
    n=8
    p=7
    q=3
    # print Decimal(str(a.redundants(n,p,q))) / Decimal(str(2**n))
    print a.getTriangle_SingleRow(n)
    for q in xrange(0,9):
        print a.getCview(n,q)
if __name__ == '__main__':
    main()
    # a = gorilla.GorilaBasis()
    # print a.chose(6,1)