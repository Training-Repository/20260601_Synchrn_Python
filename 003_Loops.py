ls = [1, 2, 3, 4, "Python", "Synechron"]

val = ls[1]
print(val, type(val), id(val))

for val in ls:
    print(val, end=" - ")
print()


srch = 13

print(srch in ls)


## For ###########################################
for val in ls:
    if val == srch:
        print(f"Found the value - {srch}")
        break
else:
    print(f"'{srch}' not found!")



for _ in range(5):
    print("Hi")


## While ##########################################
idx = 0

while idx < len(ls):
    val = ls[idx]
    if val == srch:
        print(f"[While] Found the value - {srch}")
        break
    idx += 1
else:
    print(f"'{srch}' not found!")
