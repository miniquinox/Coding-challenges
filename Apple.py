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
# ['', 'aaa', 'bbb', 'ccc', 'ddd', 'e', 'f', 'g'] 
# ['aaa', 'bbb','ccc','ddd', 'e', 'f', 'g', 'aaa'] 
