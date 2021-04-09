# Given the following string, write a function to solve the following problem:
#    - Separate letters that are the same consecutively from different letters.
#    - The output should look like this:
#      ['aaa', 'bbb','ccc','ddd', 'e', 'f', 'g', 'aaa']

string = "aaabbbcccdddefgaaa"

def separate(string):
    prev = ""
    output = []
    temp = ''
    for c in string:
        
        if prev == c:
            temp+=c
        else: 
            if temp != '':
                output.append(temp)
            temp = c
        prev = c
    output.append(temp)
    return output 

print(separate(string))
