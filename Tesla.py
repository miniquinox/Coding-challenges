# Given a list of letters, traverse it and return another 
# list with the letter count and their correspondent letter 
# consecutively.
#     Example: "abbcaaaabeeeeeee" returns 1a2b1c4a1b7e

def function(list):
    prev = list[0]
    word = ""
    total = []
    result = ""
    for letter in list:
        if letter == prev:
            word += letter
        else:
            length = str(len(word))
            result += length
            result += word[0]
            total.append(result)
            word = letter
            result = ""
        prev = letter
        
    length = str(len(word))
    result += length
    result += word[0]
    total.append(result)
    return total

list = "abbcaaaabeeeeeeeeeeee"
done = function(list)
listToStr = ''.join(map(str, done))
print(listToStr)
