# -*- coding: utf-8 -*-
"""
@author: Mengxuan Chen
@description:
    验证回文串
@revise log:
    2021.01.13 创建程序
"""
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ##########################################################
        # 本地运行没有问题，但是平台运行不对
        # s_ = s.lower()
        # s__ = s_.replace(" ", "")
        # s = re.sub(r'[{}]+'.format('!,;:?"\'、，；'),' ',s__)
        # s = s.replace(" ", "")
        # slow = 0
        # count = 0
        # fast = len(s) - 1
        # while slow < fast:
        #     if s[fast] == s[slow]:
        #         count += 1
        #     slow += 1
        #     fast -= 1
        # if (count == len(s) / 2) or (count == (len(s) - 1) / 2):
        #     x = 1
        # else:
        #     x = 0
        # return bool(x)
        ##########################################################
        sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        return sgood == sgood[::-1]


solution = Solution()
result = solution.isPalindrome(#s = "A man, a plan, a canal: Panama")
"race a car")
print(result)
