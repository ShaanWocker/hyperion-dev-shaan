# Solution with user validation and error handling using conditionals.

class Solution:
    def groupAnagrams(self, strs):
      result = {}
      for i in strs:
         x = "".join(sorted(i))
         if x in result:
            result[x].append(i)
         else:
            result[x] = [i]
      return list(result.values())
   
ob1 = Solution()

# While loop to keep the script running / continue
while True :
    
    #  An input is used to set the strs variable
    strs = input("Enter a few words for your anagram list : ")
    
    # A conditional incase nothing is entered
    if not strs : print("You did not enter anything, try again.")
    
    # A conditional displaying your groups of anagrams
    else : print("Your group of anagrams : ", ob1.groupAnagrams(strs.split()))
    
    continue