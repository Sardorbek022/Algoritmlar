a=int(input("A kesmani kiriting A => "))
b=int(input("B kesmani kiriting B => "))
l=0
if a>b:
    while (a>b):
        a=a-b
        l=l+1
    print(l)
else:
    print("A > B shartiga e'tibor bering!")