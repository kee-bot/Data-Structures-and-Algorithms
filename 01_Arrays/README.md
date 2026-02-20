# Arrays

Problems using arrays usually involve the below:

1. Hashmaps

Mainly used to keep track of frequency.

Problem: Given an integer array nums and an integer target, return the indices of the two numbers that add up to target. 

```python
def two_sum(nums, target):
    seen = {}  # value -> index
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return (seen[need], i)
        seen[x] = i
    return None
```

Note:
Another method to store frequency for strings is to use a list of size 26 and store the frequency at the index. This is more efficient than using a hashmap but it can be memory intensive.
Use ord(<char>) - ord('a') to get the index for a character.

2. Sliding Window

Taking a part of the array and moving through the array, can be fixed sized or variable according to the problem. 

Problem: Given an array arr and integer k, find the maximum sum of any contiguous subarray of length k.

```python
def max_subarray_sum_k(arr, k):
    if k > len(arr): 
        return None
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        if window_sum > max_sum:
            max_sum = window_sum
    return max_sum
```

3. Two pointers

Using two variables to store two indexs to traverse through the array. 

Problem: Given a sorted array arr (ascending) and a target, return True if any two numbers sum to target, else False. 

```python
def pair_exists_sorted(arr, target):
    i, j = 0, len(arr) - 1
    while i < j:
        s = arr[i] + arr[j]
        if s == target:
            return True
        if s < target:
            i += 1
        else:
            j -= 1
    return False
```

4. Prefix Sum

Prefix Sums/Products are techniques that store cumulative sums or products up to each index, allowing for quick subarray range queries.

Problem: Find the product of array except self.

```python
def product_except_self(nums):
    n = len(nums)
    left = [1] * n
    right = [1] * n
    for i in range(1, n):
        left[i] = left[i - 1] * nums[i - 1]
    for i in range(n - 2, -1, -1):
        right[i] = right[i + 1] * nums[i + 1]
    return [left[i] * right[i] for i in range(n)]
``` 



         






