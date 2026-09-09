class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for wrd in strs:
            key = "".join(sorted(wrd))
            groups[key].append(wrd)
        return list(groups.values())