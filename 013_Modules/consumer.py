# # from greetings import greet, greetName
# from greetings import *
# # from greetings import greetName

# # print(f"Consumer --> {__name__ = }")

# if __name__ == "__main__":
#     greet()
#     greetInteractive()
#     greetName("Abhijeet")
#     # print(prepGreeting("Hi", "Joe"))


###################################################

from greetings import *

def Test1():
    greetings.greet()
    print(greetings.prepGreeting("A", "B"))



def Test2():
    # from greetings import greet, greetName
    # from greetings import *
    greet()
    greetName("Vijay")

if __name__ == "__main__":
    Test2()