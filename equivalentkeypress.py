# Equivalent Keypresses

# Have the function EquivalentKeypresses(strArr) read the array of strings stored in strArr which will contain 2 strings representing
# two comma separated lists of keypresses. Your goal is to return the string true if the keypresses produce the same printable string 
# and the string false if they do not. A keypress can be either a printable character or a backspace represented by -B. You can produce
# a printable string from such a string of keypresses by having backspaces erase one preceding character.

# Examples

# Input: new String[] {"a,b,c,d", "a,b,c,d,-B,d"}
# Output: true

# Input: new String[] {"c,a,r,d", "c,a,-B,r,d"}
# Output: false

def EquivalentKeypresses(strArr):
    first = strArr[0].split(',')
    second = strArr[1].split(',')
    # print(first)
    # print(second)
    result_first = []
    for key in first:
        if key == '-B':
            if result_first:
                result_first.pop()
        else:
            result_first.append(key)
    print(result_first)
    
    result_second = []
    for key in second:
        print(key)
        if key == '-B':
            if result_second:
                result_second.pop()
        else:
            result_second.append(key)
    print(result_second)
    
    if result_second == result_first:
        return "true"
    else:
        return "false"
    
    
    
    
    
    
    
    
print(EquivalentKeypresses(["a,b,c,d", "a,b,c,d,-B,d"]))
print(EquivalentKeypresses(["c,a,r,d", "c,a,-B,r,d"]))



def equivalentKeypresses(strArr):
    # print(strArr[0])
    # print(strArr[1])
    result_first = []
    second = strArr[1].split(',')
    first = strArr[0].split(',')
    for key in first:
        # print(key)
        if key == '-B':
            if result_first:
                result_first.pop()
        else:
            result_first.append(key)
            
    # print(result_first)
    result_second = []
    for key in second:
        # print(key)
        if key == '-B':
            if result_second:
                result_second.pop()
        else:
            result_second.append(key)
    print(result_second)
    if result_first == result_second:
        return "true"
    return "false"
                  
    
print(equivalentKeypresses(["a,b,c,d", "a,b,c,d,-B,d"]))
print(equivalentKeypresses(["c,a,r,d", "c,a,-B,r,d"]))