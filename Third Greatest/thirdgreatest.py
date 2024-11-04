# Have the function ThirdGreatest(strArr) take the array of strings stored in strArr and return the third largest word within it. 
# So for example: if strArr is ["hello", "world", "before", "all"] your output should be world because "before" is 6 letters long,
# and "hello" and "world" are both 5, but the output should be world because it appeared as the last 5 letter word in the array. 
# If strArr was ["hello", "world", "after", "all"] the output should be after because the first three words are all 5 letters long,
# so return the last one. The array will have at least three strings and each string will only contain letters.
def ThirdGreatest(strArr):
    
    
    sorted_words = sorted(strArr, key=lambda word: (-len(word), strArr.index(word)))
    # print(sorted_words[2])
    
    return sorted_words[2]
    
  

# keep this function call here 
# print(ThirdGreatest(input()))
        
        
# def ThirdGreatest(strArr):

#   uniquestrings = list(set(strArr))
#   # print(uniquestrings)

#   uniquestrings.sort(key = len, reverse = True)

#   if len(uniquestrings) < 3:
#     return None

#   return uniquestrings[2]
   
    
    
    
    
    
print(ThirdGreatest(["hello", "world", "before", "all"]))
print(ThirdGreatest(["hello","world","world"]))