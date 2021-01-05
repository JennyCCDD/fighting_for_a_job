class Solution(object):
    def largeGroupPositions(self, s):
        ans = []
        fast, slow = 0, 0
        while fast < len(s):
            # 起始位置相同，慢指针保持不变、快指针移动到连续区间末尾
            while fast < len(s) and s[slow] == s[fast]:
                fast += 1
            # 判断是否符合“较大分组”
            if fast - slow >= 3:
                ans.append([slow, fast-1])
            # 从新的区间开始，更新慢指针与快指针
            slow = fast
            fast += 1
        return ans
solution = Solution()#[[3,5],[6,9],[12,14]]
result = solution.largeGroupPositions("abcdddeeeeaabbbcd")#"abbxxxxzzy")
print(result)