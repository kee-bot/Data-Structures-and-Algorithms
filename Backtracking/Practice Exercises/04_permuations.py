# [LEETCODE 46] Permutations
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

def permute(nums):
        res=[]

        def perm(path):
            if len(path)==len(nums):
                res.append(path.copy())
                return 
            
            for i in nums:
                if i not in path:
                    path.append(i)
                    perm(path)
                    path.pop()
   
        perm([])

        return res

if __name__ == "__main__":
    nums = [1,2,3]
    print(permute(nums))  # Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]