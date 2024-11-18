'''
palindrome

have the function Palindrome(str) take the str parameter being passed and return the string true
if the parameter is a palindrome(the string is the same fowards as it is backward) otherwise
return the string false. for example "racecar" is also "racecar backwards. punctuation and numbers
will not be part of the string

examples
input: "never odd or even
output: "true"

input: "eye"
output: "true
'''
import string

def palindrome(str):
    
   
    str = str.lower().replace(" ", "")

   
    str = ''.join(word for word in str if word not in string.punctuation)
    print(str)
    
    backwards = str[::-1]
    print(backwards)
    if backwards == str:
        return "true"
    else:
        return "false"
    
    
    
print(palindrome("A man, a plan, a canal: Panama"))