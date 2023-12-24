from functools import lru_cache
@lru_cache
def climbStairs(self, n: int) -> int:
    if n == 1 or n == 2:
        return n
    return climbStairs(n - 1) + climbStairs(n - 2)
        
