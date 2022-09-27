# # for1
# k = int(input("k = "))
# n = int(input("n = "))
# for i in range(n):
#     print(k)

# # for2
# a = int(input("a = "))
# b = int(input("b = "))
# for i in range(a,b+1):
#     print(i)

# # for3
# a = int(input("a = "))
# b = int(input("b = "))
# for i in range(b-1,a,-1):
#     print(i)

# # for4
# x = int(input("x = "))
# for i in range(1,11):
#     print(i * x)

# # for5
# x = int(input("x = "))
# for i in range(1,11):
#     print((i / 10) * x)

# # for6
# x = int(input("x = "))
# for i in range(12,21,2):
#     print((i / 10) * x)

# # for7
# a = int(input("a = "))
# b = int(input("b = "))
# s = 0
# for i in range(a,b):
#     s += i
# print(s)

# # for8
# a = int(input("a = "))
# b = int(input("b = "))
# k = 1
# for i in range(a,b):
#     k *= i
# print(k)

# # for9
# a = int(input("a = "))
# b = int(input("b = "))
# s = 0
# for i in range(a,b):
#     s += i ** 2
# print(s)

# # for10
# n = int(input("n = "))
# s = 0
# for i in range(1,n+1):
#     s += 1 / i
# print(s)

# # for11
# n = int(input("n = "))
# s = 0
# for i in range(0,n+1):
#     s += (n + i) ** 2
# print(s)

# # for12
# n = int(input("n = "))
# k = 1
# for i in range(1,n+1):
#     k *= 1 + (i / 10)
# print(k)

# # for13
# n = int(input("n = "))
# s = 0
# for i in range(1,n/2):
#     s += (1 + (i / 10)) * (-1) ** (i + 1)
# print(s)

# # for14
# n = int(input("n = "))
# s = 0
# for i in range(1,n+1):
#     s += 2 * i - 1
#     print(s)

# # for15
# n = int(input("n = "))
# a = int(input("a = "))
# k = 1
# for i in range(1,n+1):
#     k *= a
# print(k)

# # for16
# n = int(input("n = "))
# a = int(input("a = "))
# k = 1
# for i in range(1,n+1):
#     k *= a
#     print(k)

# # for17
# n = int(input("n = "))
# a = int(input("a = "))
# k = 1
# s = 0
# for i in range(n+1):
#     s += a ** i
# print(s)

# # for18
# n = int(input("n = "))
# a = int(input("a = "))
# s = 0
# for i in range(n+1):
#     s += (a ** i) * ((-1) ** i)
# print(s)

# # for19
# n = int(input("n = "))
# k = 1
# for i in range(1,n+1):
#     k *= i
# print(k)

# # for20
# n = int(input("n = "))
# k = 1
# s = 0
# for i in range(1,n+1):
#     k *= i
#     s += k
# print(s)

# # for21
# n = int(input("n = "))
# k = 1
# s = 0
# for i in range(1,n+1):
#     k *= i
#     s += 1 / k
# print(s+1)

# # for22
# n = int(input("n = "))
# x = int(input("x = "))
# k = 1
# s = 0
# for i in range(1,n+1):
#     k *= i
#     s += (x ** i) / k
# print(s+1)

# # for29
# n = int(input("n = "))
# a = int(input("a = "))
# b = int(input("b = "))
# x = abs(a - b) / n
# for i in range(n):
#     a += x
#     print(a)

# # for30
# from math import sin
# n = int(input("n = "))
# a = int(input("a = "))
# b = int(input("b = "))
# x = abs(a - b) / n
# for i in range(n):
#     a += x
#     print(1 - sin(a))

# # for31
# n = int(input("n = "))
# a0 = 2
# print(a0)
# for i in range(1,n+1):
#     a1 = 2 + 1 / a0
#     a0 = a1
#     print(a1)

# # for32
# n = int(input("n = "))
# a0 = 1
# print(a0)
# for i in range(1,n+1):
#     a1 = (a0 + 1) / i
#     a0 = a1
#     print(a0)

# # for33
# n = int(input("n = "))
# f1 = 1
# f2 = 1
# print(f1)
# print(f2)
# for i in range(n+1):
#     f3 = f1 + f2
#     f1 = f2
#     f2 = f3
#     print(f3)

# # for34
# n = int(input("n = "))
# a1 = 1
# a2 = 2
# print(a1)
# print(a2)
# for i in range(n+1):
#     a3 = (a1 + 2 * a2) / 3
#     a1 = a2
#     a2 = a3
#     print(a3)

# # for35
# n = int(input("n = "))
# a1 = 1
# a2 = 2
# a3 = 3
# print(a1)
# print(a2)
# print(a3)
# for i in range(n+1):
#     a4 = a3 + a2 - 2 * a1
#     a1 = a2
#     a2 = a3
#     a3 = a4
#     print(a4)

# # for36
# n = int(input("n = "))
# k = int(input("k = "))
# s = 0
# for i in range(1,n+1):
#     s += pow(i,k)
# print(s)

# # for37
# n = int(input("n = "))
# s = 0
# for i in range(1,n+1):
#     s += i ** i
# print(s)

# # for38
# n = int(input("n = "))
# s = 0
# for i in range(1,n+1):
#     k = 1
#     for j in range(n+1-i):
#         k *= i
#     s += k
#     print(k)
# print("s = ",s)

# # for39
# a = int(input("a = "))
# b = int(input("b = "))
# for i in range(a,b+1):
#     for j in range(i):
#         print(i)

# for40
a = int(input("a = "))
b = int(input("b = "))
count = 1
for i in range(a,b+1):
    for j in range(count):
        print(i)
    count += 1
