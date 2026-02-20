# Dynamic Programming

Dynamic programming is mainly about optimising recursive solutions to problems. 

## Algorithm 

Take the climbing stair problem as an example. 

Problem: You are given an integer n representing the number of steps to reach the top of a staircase. You can climb with either 1 or 2 steps at a time.
Return the number of distinct ways to climb to the top of the staircase.

Recursively we would calculate at each point how many ways exist to the top if we take 1 step and 2 steps from the point. 

```python
def climbStairs(n):

        def dfs(i):
            if i >= n:
                return i == n
            return dfs(i + 1) + dfs(i + 2)

        return dfs(0)
```

We are doing multiple repeated calculations above as we are calculating steps to reach the top from a given point multiplt times. We can cache this value. 

```python
def climbStairs(n):

        cache = [-1] * n

        def dfs(i):
            if i==n:
                return 1
            if i>n: 
                return 0
            if cache[i] != -1: 
                return cache[i]
            cache[i]=dfs(i+1) + dfs(i+2)
            return cache[i]

        return dfs(0) 
```

This is called memoization. 

We can also do this in a bottom up manner using tabulation. 

```python
def climbStairs(n): 
    if n <= 2: 
        return n
    dp = [0] * (n+1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
```
## When do we use Dynamic Programming? 

Overlapping Subproblems: The same subproblems are encountered and solved repeatedly when using a naive recursive approach. By storing the results of these subproblems, we can avoid redundant work and significantly reduce the time complexity.

Optimal Substructure: The optimal solution to the entire problem can be constructed from the optimal solutions of its smaller subproblems.

Heuristically, dynamic programming should be considered when a problem involves:

Optimization: Finding the maximum, minimum, shortest, or longest value (e.g., maximum profit, minimum cost, shortest path, longest common subsequence).
Counting: Finding the number of possible ways to achieve a certain outcome under given conditions (e.g., number of paths in a grid, number of ways to make change).
Sequential Dependencies: Problems where the solution for the current step depends on the results of previous steps in a sequence or grid structure.

## Example Problems

TODO: Add exercises

## References

TODO: Add references used for exercises. 