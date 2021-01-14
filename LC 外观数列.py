# -*- coding: utf-8 -*-
"""
@author: Mengxuan Chen
@description:
    外观数列
@revise log:
    2021.01.14 创建程序
                解题思路：https://leetcode-cn.com/problems/count-and-say/solution/jian-dan-12wai-guan-shu-lie-de-tui-dao-di-gui-yi-c/
"""


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
            # 使用递归来一层一层往前推
        previous = self.countAndSay(n - 1)
        result = ""
        count = 1
        for i in range(len(previous)):
            # 注意这里和c++不同，C++字符串其实是以'\0' 结尾。
            if i < len(previous) - 1 and previous[i] == previous[i + 1]:
                count += 1
            else:  # 当previous[i] ！= previous[i + 1] 或者i=len(previous)-1时，count肯定也是为1的
                result += str(count) + previous[i]
                count = 1

        return result


solution = Solution()
result = solution.countAndSay(n=4)
print(result)