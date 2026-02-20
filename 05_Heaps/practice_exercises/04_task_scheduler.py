# [LEETCODE 621] You are given a char array tasks where tasks[i] is the type of the ith task you need to complete. You are also given an integer n that represents the cooldown period between two same tasks. Return the least number of units of times that the CPU will take to finish all the given tasks.

import heapq
from collections import Counter, deque     


def leastInterval(tasks, n):
    count=Counter(tasks)
    max_heap=[-freq for freq in count.values()]
    heapq.heapify(max_heap)

    q=deque()
    ct=0

    while max_heap  or q: 
        ct+=1
        
        if max_heap: 
            val = 1 + heapq.heappop(max_heap)
            if val: 
                q.append((val,ct+n))

        if q and q[0][1] == ct:
            heapq.heappush(max_heap,q.popleft()[0])

    return ct

if __name__ == "__main__":
    tasks = ["A","A","A","B","B","B"]
    n = 2
    print(leastInterval(tasks,n)) # Output: 8

    tasks = ["A","A","A","B","B","B"]
    n = 0
    print(leastInterval(tasks,n)) # Output: 6

    tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
    n = 2
    print(leastInterval(tasks,n)) # Output: 16





        