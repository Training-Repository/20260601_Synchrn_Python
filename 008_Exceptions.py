import random
# Math Library
def Bar(dividend, divisor):
    print("Bar Start")
    # if divisor == 0:
    #     print("Division by zero not possible")
    #     return (0, 999)
    if random.randint(0, 1):
        raise FloatingPointError("Floating Point Exception occurred")
    quotient = dividend/divisor
    remainder = dividend%divisor
    print("Bar End")
    return quotient, remainder

def Foo(*vArgs, **kwArgs):
    print("Foo Start")

    ret = Bar(*vArgs, **kwArgs)
    # try:
    #     ret = Bar(*vArgs, **kwArgs)
    # except:
    #     print("Some exception occured")
    #     ret = (-1, -1)
    print("Foo End")
    return ret

def Main(*vArgs, **kwArgs):
    print("Main Start")
    ret = Foo(*vArgs, **kwArgs)
    print("Main End")
    return ret



# Library Consumer
data = [7, 3]
data = [7, 0]
# data = [2999, 1000]
try:
    _, r = Main(*data)
    print(f"{r = }")
except ZeroDivisionError as e:
    print("ZeroDivError Occurred:", e)
except ArithmeticError as e:
    print("Some Arithmetic exception occured:", e)
except Exception as e:
    print("Some exception occured")

# if r == 999:
#     print("Division by Zero not allowed")
# else:
#     print(f"{r = }")

print("Bye")
