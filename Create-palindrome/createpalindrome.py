# Write a function solution that, given a string S of length N, returns any palindrome which can be obtained by replacing all of
# the question marks in S by lowercase letters ('a'−'z'). If no palindrome can be obtained, the function should return the string "NO".
# A palindrome is a string that reads the same both forwards and backwards. Some examples of palindromes are: "kayak", "radar", "mom".
# Examples:
# 1. Given S = "?ab??a", the function should return "aabbaa".
# 2. Given S = "bab??a", the function should return "NO".
# 3. Given S = "?a?", the function may return "aaa". It may also return "zaz", among other possible answers. 
# The function is supposed to return only one of the possible answers.
# Assume that:
# N is an integer within the range [1..1,000];
# string S consists only of lowercases letters ('a' − 'z') or '?'.
# In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.
import re
def solution(S):
    N = len(S)
    if N not in range(1, 1001):
        return f"{N} must be on the range of 1-1000"
    valid = r'^[a-z?]+$'
    if not re.match(valid, S):
        return f"{S} must only contain lowercase letters and a question mark only"
    for i in S:
        print(i)
        if i == '?':
            pass
            
        
        
        
print(solution("?ab??a"))