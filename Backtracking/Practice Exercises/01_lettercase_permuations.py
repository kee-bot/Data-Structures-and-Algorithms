# [LEETCODE 784] Letter Case Permutations
# Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string. Return a list of all possible strings we could create. You can return the output in any order.

def letterCasePermutation(s):
        res=[]

        def backtrack(i,path): 
            if i==len(s): 
                res.append(path)
                return 

            if s[i].isalpha():
                # lowercase branch
                backtrack(i + 1, path + s[i].lower())
                # uppercase branch
                backtrack(i + 1, path + s[i].upper())
            else:
                # digit branch
                backtrack(i + 1, path + s[i])

        backtrack(0,'')

        return res

if __name__ == "__main__":
    s = "a1b2"
    print(letterCasePermutation(s))  # Output: ["a1b2","a1B2","A1b2","A1B2"]