class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        count = 0
        new_count = 0
        my_set = set()
        
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        
        while left <= len(s) - 2:
            right = left + 1
            if s[left] != s[right]:
                while right < len(s):
                    if s[right] not in my_set:
                        if s[left] not in my_set:
                            my_set.add(s[left])
                            count += 1
                        my_set.add(s[right])
                        count += 1
                        right += 1
                    else:
                        break
            else:
                my_set.add(s[left])
                count += 1
            
            if count > new_count:
                new_count = count
                count = 0
            count = 0
            my_set = set()
            left += 1
        return new_count
        
                 

    
            
            
                
            