# [LEETCODE 347] Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

import heapq
from typing import Counter


def topKFrequent(nums, k):
    count=Counter(nums)
    hp=[]
    for n,ct in count.items():
        if len(hp)==k:
            heapq.heappushpop(hp,(ct,n))
        else:
            heapq.heappush(hp,(ct,n))

    return [n for ct,n in hp]

if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    k = 2
    print(topKFrequent(nums,k)) # Output: [2,1]

    nums = [1]
    k = 1
    print(topKFrequent(nums,k)) # Output: [1]