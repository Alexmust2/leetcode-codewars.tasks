
from typing import *


class Solution:
    def isPalindrome(self, x: int) -> bool:
        b = ""
        for i in x:
            b = i + b
        print(b)
        if x == b:
            return True
        else:
            return False
            


s = Solution()
print(s.isPalindrome("121"))