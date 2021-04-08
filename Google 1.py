# Given a number of square feet, return a string with the size 
# of the biggest SQUARES you can make, optimizing space
#    Example 1: area = 12 returns [9, 1, 1, 1]
#    Example 2: area = 16 returns [16]
#    Example 3: area = 13 returns [9, 4]

def solution(area):
    total = []
    
    while area != 0:
        limit = area + 1
        answer = 0
        while (answer+1)**2 < limit:
            answer += 1
        root = answer**2
        total.append(root)
        area = area - root
    return total
area = 29 
print(solution(area))
