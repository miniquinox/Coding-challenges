def permutationn(string1, string2):
    result = ""
    if len(string1) != len(string2):
        print("Different size")

    else:
        for letter in string1:
            if letter in string2:
                string2 = string2.replace(letter, "", 1)
            else:
                result = "These are not permutations"
                print("Character ", letter, " from string 1 not found in string 2")
                break
        if result == "":
            print("These are permutations of eachother")
        else:
            print(result)

string1 = "Halo"
string2 = "Halo"
permutationn(string1, string2)
