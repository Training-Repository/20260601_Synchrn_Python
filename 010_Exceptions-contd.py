## Assertion Error ################################################

# age = -5

# assert age > 0, f"age must be non-negative, got '{age}'!"

# print("Exiting now...")
####################################################################
# def divide(a, b):
#     assert b != 0, "Divisor 'b' must be non-zero"
#     return a/b

# try:
#     print(divide(10, 2))
#     print(divide(10, 0))
# except AssertionError as e:
#     print(f"Caught: {e!r}")

## try-except-else #####################################################

# def read_config(filename):
#     try:
#         f = open(filename)
#         data = f.read()
#     except FileNotFoundError as e:
#         print(f"ERROR: {e!r}")
#     else:
#         print("Read OK: {data!r}")
#         f.close()

## User-define Exceptions ###################################################

class InvalidAgeError(ValueError):
    def __init__(self, age):
        self.age = age
        super().__init__(f"Age {age} is not valid (must be 0-120)")

def setAge(age):
    if not (0 <= age <=120):
        raise InvalidAgeError(age)
    return f"Age set to {age}"

try:
    result = setAge(125)
    print(result)
except ValueError as e:
    print(f"ERROR: {e!r}")
    print(f"Age passed in is {e.age}")
