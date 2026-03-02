# [LEETCODE 973] Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0)

import heapq

def k_closest(nums,k): 
    min_heap=[]

    for x,y in nums: 
        dist=-((x*x)+(y*y))
        heapq.heappush(min_heap,(dist,x,y))
        if len(min_heap)>k: 
            heapq.heappop(min_heap)

    return [(x,y) for (dist,x,y) in min_heap]

if __name__ == "__main__":
    points = [[1,3],[-2,2]]
    k = 1
    print(k_closest(points,k)) # Output: [[-2,2]]

    points = [[3,3],[5,-1],[-2,4]]
    k = 2
    print(k_closest(points,k)) # Output: [[3,3],[-2,4]]
