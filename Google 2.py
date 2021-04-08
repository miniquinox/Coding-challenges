# Write a function that takes in a list of integers and returns the biggest multiplication between them
#     Example 1: [3, 5, -4] returns 15
#     Example 2: [3, -2, 5, -1] returns 30

def solution(xs):
    # Your code here
    total = []
    negatives = []
    
    for i in xs:
        if i > 0:
            total.append(i)
        elif i < 0: 
            negatives.append(i)
        else:
            continue
    negatives.sort()
    if len(negatives) % 2 == 1 and len(negatives) != 1:
        negatives.pop(-1)
         
    for i in negatives:
        total.append(i)    

    if (((len(total) == 0)) and (0 in xs)) or ((len(total) == 1) and (0 in xs) and (total[0] < 0)):
        result = 0

    elif len(total) == 0:
        result = []
    else:
        result = 1
        for j in total:
            result = result * j
    
    return str(result)

print(solution([-1, 0]))
