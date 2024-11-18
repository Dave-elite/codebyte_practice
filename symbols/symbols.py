'''
Have the function SimpleSymbols(str) take the str parameter being passed and determine if it is an
acceptable sequence by either returning the string true or false. the str paramenter will be composed 
of + and = symbols with several charcters between them (ie. ++d+===+c++==a) and for the string
to be true each letter must be surrounded by a + symbol. So the string to the left
would be false. The string will not be empty and will have atleast one letter

examples
Input: "+d+=3=+s+"
Output: true
Input: "f++d+"
Output: false
'''
import string
def SimpleSymbols(str):
    for i, char in enumerate(str):
        if char.isalpha():
            #first ensure that the letter is not the first charcater of the string
            #str[i-1] == '+' This checks if the character before the letter is a + symbol
            # i < len(str) - 1 this esnure that this letter is not the last charcater in the string
            # check if the charcter after the letter is a + symbol
            if not (i > 0 and str[i - 1] == '+' and i < len(str) - 1 and str[i + 1] == '+'):
                return "false"
    return "true"
                
        
    

    
    
    
print(SimpleSymbols("f++d+"))