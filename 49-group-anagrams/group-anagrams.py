from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram=defaultdict(list)
        answer=[]
        
        for i in strs:
            sort_s=tuple(sorted(i))
            anagram[sort_s].append(i)
        for value in anagram.values():
            answer.append(value)
        return answer

        