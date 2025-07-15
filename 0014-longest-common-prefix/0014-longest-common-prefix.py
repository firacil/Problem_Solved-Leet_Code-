class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """find the longest common prefix string"""
        if not strs:
            return ""
        

        strs.sort()
        first_str = strs[0]
        last_str = strs[-1]
        common_strs = ""

        for s in range(min(len(first_str), len(last_str))):
            if first_str[s] == last_str[s]:
                common_strs += first_str[s]
            else:
                break
        return common_strs