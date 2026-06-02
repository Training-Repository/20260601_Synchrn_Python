#region 1
# def Factorial(num):
#     if num <= 1:
#         return 1
    
#     return num * Factorial(num - 1)

# x = 5
# res = Factorial(x)
# print("Result -->", res)

# print(type(Factorial))


# def Double(val):
#     return val * 2

# def Square(val):
#     return val ** 2


# funcs = [Factorial, Double, Square]

# print(funcs[1](10))
#endregion

#region 2
# def add(a: int, b: int)->int:
#     sum  = a + b
#     return sum

# print(add(1, 2))
# print(add(1.1, 2.2))
# print(add("1", "2"))

#endregion

#region DefaultArgs
def add(a: int, b: int = 0, c: int = 0)->int:
    print(f"{a = }, {b = }, {c = }")
    sum  = a + b + c
    return sum

print(add(1, 2))
print(add(1, 2, 3))
#endregion

