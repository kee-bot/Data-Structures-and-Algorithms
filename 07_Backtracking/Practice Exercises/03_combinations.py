# [LEETCODE 77] Combinations
# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n]. You may return the answer in any order.

def combine(n, k):
        res=[]

        def comb(idx,path):
            if len(path) == k: 
                res.append(path.copy())
                return 

            for i in range(idx,n+1):
                path.append(i)
                comb(i+1,path)
                path.pop()

        comb(1,[])

        return res

if __name__ == "__main__":
    n = 4
    k = 2
    print(combine(n, k))  # Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

    