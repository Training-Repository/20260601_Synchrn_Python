# Comprehension - Creates a new collection from an existing collection, based 
# on our custom conditions and transformations

fruits = ["Apple", "Banana", "Cheeku", "Dragonfruit", "Elderberry", "Grapes", "Muskmelon"]

bowl = []
for fr in fruits:
    if 'a' not in fr.lower():
        bowl.append(fr)

print(bowl)

bowl_2 = [fr.upper()           for fr in fruits           if 'a' not in fr.lower()]
print(bowl_2)

print("\n\n-------------------\n\n")
lst = [fr.upper()           for fr in fruits           if 'a' not in fr.lower()] ; print(lst, type(lst))
st  = {fr.upper()           for fr in fruits           if 'a' not in fr.lower()} ; print(st , type(st))
dt  = {fr.upper():len(fr)   for fr in fruits           if 'a' not in fr.lower()} ; print(dt , type(dt))
tup = tuple(fr.upper()           for fr in fruits           if 'a' not in fr.lower()) ; print(tup, type(tup))



even_numbers = [n   for n in range(101)    if n%2 == 0]
print(even_numbers)
