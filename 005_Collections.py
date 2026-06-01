# Features for collections:
#   1. Mutable/Immutable
#   2. Homogeneous
#   3. object / keys / key-value-pairs
# 
# Collections
#   (Lists, Str, Sets, Tuples, FrozenSets, NamedTuples, Dictionaries) 
#   Set/FrozenSets accept only 'keys' (hashable) elements
#   hash()

s1 = "Test"
print(s1)

print(s1[0])
# s1[0] = "B"

s1 = "Best"
print(id(s1))

s1 += "est"
print(id(s1))

print(s1)

ls = [1, 2, 3, 4]
print(id(ls))

ls.append(5)
print(id(ls))

ls.remove(3)
print(id(ls))

print(ls)


tp = (1, 2, 3, 4)
tp = ('a', 'b', 'c')
# tp.append(5)
# tp.remove(3)
print(tp)
