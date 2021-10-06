"""
    The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1
"""

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        else:
            return self.fib(n-1) + self.fib(n-2)

"""
    1. 재귀 구조 브루트 포스
    
    2. 메모이제이션 
    import collections
    dp = collections.defaultdict(int)
    def fib(n):

        if n <= 1:
            return n
        if self.df[n]:
            return self.dp[n]
        self.dp[n] = self.fib(n-1) + self.fib(n-2)
        return self.dp[n]
    
    3. 타뷸레이션 
    import collections
    dp = collections.defaultdict(int)
    def fib(n):
        self.dp[1] = 1

        for i in range(2, n+1)
            self.dp[i] = self.dp[i-1] + self.dp[i-2]
        return self.dp[n]
    
    4. 두 변수만 이용해 공간 절약
    def fib(n):
        x, y = 0 , 1
        for i in range(0, n):
            x, y = y, x+y
        return x

"""
