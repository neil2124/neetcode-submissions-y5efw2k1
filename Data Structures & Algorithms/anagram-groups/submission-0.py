class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapp = defaultdict(list)
        
        for s in strs:
            newMapp = [0 for i in range(26)]
            for c in s:
                newMapp[ord(c) - ord('a')] +=1
            mapp[tuple(newMapp)].append(s)
        return list(mapp.values())