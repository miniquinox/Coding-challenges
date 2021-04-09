# Given two strings of characters, write a function that returns 
# wether or not two strings are permutations of eahother
#     Example 1: "Hello" and "eHlol" returns "These are permutations of eachother"
#     Example 2: "Hello" and "eHlal" returns "These are not permutations"

def permutationn(string1, string2):
    result = ""
    if len(string1) != len(string2):
        print("Different size")

    else:
        for letter in string1:
            if letter in string2:
                string2 = string2.replace(letter, "", 1)
                continue
            else:
                result = "These are not permutations"
                print("Character ", letter, " from string 1 not found in string 2")
                break
        if result == "":
            print("These are permutations of eachother")
        else:
            print(result)

string1 = "Holo"
string2 = "Halo"
permutationn(string1, string2)
