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
# def add(a: int, b: int = 0, c: int = 0)->int:
#     print(f"{a = }, {b = }, {c = }")
#     sum  = a + b + c
#     return sum

# print(add(1, 2))
# print(add(1, 2, 3))
#endregion


#region PositionalArgs
# def add(a, b, c)->int:
#     print(f"{a = }, {b = }, {c = }")
#     sum  = a + b + c
#     return sum

# print(add(1, 2, 3))
# print(add(3, 2, 1))
#endregion


#region NamedArgs/KeywordedArgs
# def add(a, b, c=0)->int:
#     print(f"{a = }, {b = }, {c = }")
#     sum  = a + b + c
#     return sum

# print(add(a=1, b=2, c=3))
# print(add(c=3, b=2, a=1))

## open("Test.txt", closefd=False, encoding="UTC-16")
#endregion


#region (un)packing
# def add(a, b, c=0)->int:
#     print(f"{a = }, {b = }, {c = }")
#     sum  = a + b + c
#     return sum

# # a = 10
# # b = 20
# # c = 30
# a, b, c = 10, 20, 30
# print(add(a, b, c))

# data = [100, 200, 300]
# print(add(data[0], data[1], data[2]))

# data = [100, 200, 300]
# # p, q, r = data
# # print(add(p, q, r))
# print(add(*data))     # <-- Unpacks in the call (point where the data starts the journey; before actual call operation)


# ## Packing

# data = [1, 2, 3, 4, 5]
# # a, b, *rest = data
# # print(f"{a = }, {b = }, {rest = }")

# a, b, *_ = data
# print(f"{a = }, {b = }")

# a, *_, b = data
# print(f"{a = }, {b = }")

# a, *_, b, _ = data
# print(f"{a = }, {b = }")

# a, _, b, *_ = data
# print(f"{a = }, {b = }")

#endregion


#region VariableArgs
# def add(a, b, *others)->int:
#     print(f"{type(a) = }, {type(b) = }, {type(others) = }")
#     print(f"{a = }, {b = }, {others = }")
#     sum  = a + b
#     for val in others:
#         sum += val
#     return sum

# print(add(1, 2))
# print(add(1, 2, 3))
# print(add(1, 2, 3, 4))
# print(add(1, 2, 3, 4, 5))
#endregion


#region Variable Keyworded arguments
# def PrintEmp(ceo, cto, cfo, **others):
#     print(f"{ceo = }")
#     print(f"{cto = }")
#     print(f"{cfo = }")

#     # print(f"{type(others) = }, {others = }")
#     for title, name in others.items():
#         print(f"{title} = {name}")

# PrintEmp("Amit", "Nilesh", "Tanveer", cxo="Naveen", Director="Gaurav")
#endregion


#region VarAgrs-Application

def PrintEmp(ceo, cto, cfo, **others):
    print(f"{ceo = }")
    print(f"{cto = }")
    print(f"{cfo = }")

    # print(f"{type(others) = }, {others = }")
    for title, name in others.items():
        print(f"{title} = {name}")

def PrintWithBorders(*vArgs, **kwArgs):     # Packing the data
    print("\n\n###############################\n")
    PrintEmp(*vArgs, **kwArgs)              # Unpacking the data
    print("\n###############################\n\n")

PrintEmp("Amit", "Nilesh", "Tanveer", cxo="Naveen", Director="Gaurav")
print("\n\n\n------------------------------------------------------------\n\n\n")
PrintWithBorders("Amit", "Nilesh", "Tanveer", cxo="Naveen", Director="Gaurav")
#endregion