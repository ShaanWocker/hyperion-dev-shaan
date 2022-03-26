class Solution:
    def groupAnagrams(self, strs): # indented properly
      result = {}
      for i in strs:
         x = "".join(sorted(i)) # passing i to sorted func
         if x in result:
            result[x].append(i)
         else:
            result[x] = [i]
      return list(result.values())
ob1 = Solution()
print(ob1.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
