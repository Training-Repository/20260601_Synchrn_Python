# Features for collections:
#   1. Mutable/Immutable
#   2. Homogeneous
#   3. object / keys / key-value-pairs
# 
# Collections
#   (Lists, Str, Sets, Tuples, FrozenSets, NamedTuples, Dictionaries) 
#   Set/FrozenSets accept only 'keys' (hashable) elements
#   hash()


#region 1
# s1 = "Test"
# print(s1)

# print(s1[0])
# # s1[0] = "B"

# s1 = "Best"
# print(id(s1))

# s1 += "est"
# print(id(s1))

# print(s1)

# ls = [1, 2, 3, 4]
# print(id(ls))

# ls.append(5)
# print(id(ls))

# ls.remove(3)
# print(id(ls))

# print(ls)


# tp = (1, 2, 3, 4)
# tp = ('a', 'b', 'c')
# # tp.append(5)
# # tp.remove(3)
# print(tp)
#endregion

#region 2
# def Func1(data):
#     print("Data is --> ", end="")
#     for val in data:
#         print(val, end=" - ")
#     print(type(data))
#     data.remove(3)
#     data.append(11)

# lst1 = [1, 2 ,3 ,4, 5]
# Func1(lst1)
# print("Original lst1 -->", lst1)

# lst2 = [10, 20 ,3 ,40, 50]
# Func1(lst2[:])
# print("Original lst2 -->", lst2)

# tup1 = (1, 2 ,3 ,4, 5)
# Func1(tup1)
# print("Original -->", tup1)
#endregion


#region 3
# from collections import namedtuple

# points = [[1, 2], [5, 3], [7, 1]]

# Point = namedtuple("Point_data", "x y")
# p1 = Point(1, 2)
# p2 = Point(5, 3)
# p3 = Point(7, 1)

# points_2 = [p1, p2, p3]

# print(points)
# print(points_2)

# print(type(p1))

# print(p1[0], p1[1])
# print(p1.x, p1.y)
#endregion


tp1 = (3,)
print(f"{type(tp1) = }, {tp1 = }")
print(tp1[0])

