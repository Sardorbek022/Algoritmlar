# If 23 masalasi

x1 = int(input(" x1 nuqtani kiriting = "))
y1 = int(input(" y1 nuqtani kiriting = "))
x2 = int(input(" x2 nuqtani kiriting = "))
y2 = int(input(" y2 nuqtani kiriting = "))
x3 = int(input(" x3 nuqtani kiriting = "))
y3 = int(input(" y3 nuqtani kiriting = "))

x4=0
y4=0

# X4  nuqtani  topamiz
if x1 == x2:
    x4 = x3
elif x1 == x3:
    x4 = x2
elif x2 == x3:
    x4 = x1

# Y4  nuqtani  topamiz
if y1 == y2:
    y4 = y3
elif y1 == y3:
    y4 = y2
elif y2 == y3:
    y4 = y1

print(f" x4 = {x4} \n y4 = {y4}")