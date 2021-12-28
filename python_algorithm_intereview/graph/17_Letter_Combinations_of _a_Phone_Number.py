"""
Given a string containing digits from 2-9 inclusive, 
return all possible letter combinations that the number could represent.
Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Input: digits = ""
Output: []

Input: digits = "2"
Output: ["a","b","c"]
"""
# 32ms, 14.4MB
def letterCombinations(digits: str) -> list[str]:
    def dfs(index, path):
        print(index, path)
        if len(path) == len(digits):
            result.append(path)
            return
        
        for i in range(index, len(digits)):
            for j in dic[digits[i]]:
                dfs(i+1, path + j)
    
    if not digits:
        return []
    
    dic = { "2": "abc", "3":"def", "4":"ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    
    result = []
    dfs(0, "")
    
    return result

    # Sample 20ms:
    # from itertools import product
    # def letterCombinations(self, digits: str) -> List[str]:
    #     d={'2':['a','b','c'],
    #        '3':['d','e','f'],
    #        '4':['g','h','i'],
    #        '5':['j','k','l'],
    #        '6':['m','n','o'],
    #        '7':['p','q','r','s'],
    #        '8':['t','u','v'],
    #        '9':['w','x','y','z']}
    #     if digits=="":
    #         return []
    #     else:
    #         res=[i for i in digits]
    #         a=[d[i] for i in res]
    #         return ["".join(i) for i in product(*a)]

if __name__ == "__main__":
    print(letterCombinations("23"))