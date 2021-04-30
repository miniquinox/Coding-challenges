# Given an array and a scalar K, find the BIGGEST sum, by only adding K numbers 
# from the corners and removing them after every addition.
#     Example: array = [5, 2, 3, 4, 5, 2, 7, 8]     K = 3
#             Result = 5 + 8 + 7 = 20

def solution(array, k):
    array1 = array[0:k] # array of first k
    size = len(array)-k 
    array2 = array[size:] # array of last k
    final = []
    for i in range(k): 
        sum1 = sum(array1)
        sum2 = sum(array2)
        if sum1 >= sum2:
            final.append(array1[0])
            array1.pop(0)
            array2.pop(0)
        else:
            final.append(array2[-1])
            array2.pop()
            array1.pop()
    print(final)
    print(sum(final))

k = 5
array = [8, 2, 10, 1, 5, 6, 1, 1, 9, 10, 11, 12, 3, 4, 13, 4]

solution(array,k)
