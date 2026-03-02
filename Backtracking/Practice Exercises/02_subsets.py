# [LEETCODE 78] Subsets
# Given an integer array nums of unique elements, return all possible subsets (the power set). The solution set must not contain duplicate subsets. The subsets can be returned in any order.

def subsets(nums):
        res=[]

        def subs(i,path):
            if i == len(nums):
                res.append(path.copy())
                return
            
            path.append(nums[i])
            subs(i+1,path)

            path.pop()
            subs(i+1,path)

        subs(0,[])

        return res

if __name__ == "__main__":
    nums = [1,2,3]
    print(subsets(nums))  # Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]  