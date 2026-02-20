# [LEETCODE 215] Problem: Given an integer array nums and an integer k, return the kth largest element in the array.

import heapq

def kth_largest(nums,k):
    min_heap=[]

    for num in nums: 
        heapq.heappush(min_heap,num)
        if len(min_heap)>k: 
            heapq.heappop(min_heap)

    return min_heap[0]

if __name__ == "__main__":
    nums = [3,2,1,5,6,4]
    k = 2
    print(kth_largest(nums,k)) # Output: 5

    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    print(kth_largest(nums,k)) # Output: 4
