import random
# Math Library
def Bar(dividend, divisor):
    print("Bar Start")
    # if divisor == 0:
    #     print("Division by zero not possible")
    #     return (0, 999)
    if random.randint(0, 1):
        raise BrokenPipeError("Broken Pipe Exception occurred")
    if random.randint(0, 1):
        raise UnboundLocalError("Unbound Local Exception occurred")
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
# data = [7, 0]
# data = [2999, 1000]
try:
    # Acquire critical section
    _, r = Main(*data)
    print(f"{r = }")
    
except (FloatingPointError, OverflowError, ZeroDivisionError, LookupError) as e:
    print("Calculation exception occured:", repr(e))
except UnboundLocalError as e:
    print(f"Unbound exception occured: {e!r}")
# except Exception as e:
#     # print("Some exception occured:", repr(e))
#     print(f"Some exception occured: {e!r}")
finally:
    # Release critical section
    print("Executing Finally block")

# except ZeroDivisionError as e:
#     print("ZeroDivError Occurred:", e.__repr__())
# except ArithmeticError as e:
#     print("Some Arithmetic exception occured:", repr(e))
# except UnboundLocalError as e:
#     print(f"Unbound exception occured: {e!r}")
# except Exception as e:
#     # print("Some exception occured:", repr(e))
#     print(f"Some exception occured: {e!r}")

# if r == 999:
#     print("Division by Zero not allowed")
# else:
#     print(f"{r = }")

print("Bye")
