val = 17

if val < 10:
    print("Lesser")
elif val > 10:
    print("Greater")
else:
    print("Equal")


# void PrintName(char* name){printf("%s is the name!", name)}

# void PrintName(char* name)
# {
#     printf("%s is the name!", name)
# }

# void PrintName(char* name)
#                                     {
# printf("%s is the name!", name)
#             }

# void PrintName(char* name){
#     printf("%s is the name!", name)
# }

##########################################################

val = 5

match val:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Not supported")