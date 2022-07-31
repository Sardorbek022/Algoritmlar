#  Bismillahir rohmanir rohim

# # 1-masala:
# k =int(input("k = "))
# n =int(input("n = "))
# for i in range(n):
#     print(k)

# # 2-masala:
# a = int(input("a = "))
# b = int(input("b = "))
# for i in range(a,b+1):
#     print(i)

# # 3-masala:
# a = int(input("a = "))
# b = int(input("b = "))
# for i in range(b-1,a,-1):
#     print(i)

# # 4-masala:
# x = int(input("narx: "))
# for i in range(1,11):
#     print(x * i)

# # 5-masala:
# x = int(input("narx: "))
# for i in range(1,11):
#     print(x * (i/10))

# # 6-masala:
# x = int(input("narx: "))
# for i in range(12,21,2):
#     print(x * (i / 10))

# # 7-masala:
# a = int(input("a = "))
# b = int(input("b = "))
# sum = 0
# for i in range(a,b):
#     sum += i
# print(sum)

# # 8-masala:
# a = int(input("a = "))
# b = int(input("b = "))
# k = 1
# for i in range(a,b):
#     k *= i
# print(k)

# # 9-masala:
# a = int(input("a = "))
# b = int(input("b = "))
# sum = 0
# for i in range(a,b):
#     sum += i ** 2
# print(sum)

# # 10-masala:
# n = int(input("n = "))
# sum = 0
# for i in range(1,n+1):
#     sum += 1 / i
# print(sum)

# # 11-masala:
# n = int(input("n = "))
# sum = 0
# for i in range(n+1):
#     sum += (n + i) ** 2
# print(sum)

# # 12-masala:
# n = int(input("n = "))
# k = 1
# for i in range(1,n+1):
#     k *= 1 + i/10
# print(k)

# # 13-masala:
# n = int(input("n = "))
# sum = 0
# a = 2 * n
# for i in range(1,a+1):
#     sum += (-1 * (1 + (i + 1)/10)) + (1 + i/10)
# print(sum/2)

# # 14-masala:
# n = int(input("n = "))
# sum = 0
# a = 2*n - 1
# for i in range(1,a+1,2):
#     sum += i
# print(sum)

# # 15-masala:
# n = int(input("n = "))
# a = int(input("a = "))
# k = 1
# for i in range(1,n+1):
#     k *= a
# print(k)

# # 16-masala:
# n = int(input("n = "))
# a = int(input("a = "))
# k = 1
# for i in range(1,n+1):
#     k = pow(a,i)
#     print(k)

# a = int(input("a = "))
# n = int(input("b = "))
# p = 1
# for i in range(1,n + 1):
#     p *= a
#     print(p,end='\n')


# # 17-masala:
# n = int(input("n = "))
# a = int(input("a = "))
# sum = 0
# for i in range(n+1):
#     sum += pow(a,i)
# print(sum)

# # 18-masala:
# n = int(input("n = "))
# a = int(input("a = "))
# sum = 0
# for i in range(n+1):
#     sum += pow(-1,i) * pow(a,n)
# print(sum/-2)

# # 19-masala:
# n = int(input("n = "))
# k = 1
# for i in range(1,n+1):
#     k *= i
# print(k)

# # 20-masala:
# n = int(input("n = "))
# k = 1
# sum = 0
# for i in range(1,n+1):
#     k *= i
#     sum += k
# print(sum)

# # 21-masala:
# n = int(input("n = "))
# k = 1
# sum = 0
# for i in range(1,n+1):
#     k *= i
#     sum += 1/k
# print(sum+1)

# # 22-masala:
# n = int(input("n = "))
# x = int(input("x = "))
# k = 1
# sum = 0
# for i in range(1,n+1):
#     k *= i
#     sum += pow(x,i)/k
# print(sum+1)

### # 23-masala:
# n = int(input("n = "))
# x = int(input("x = "))
# k = 1
# d = 1
# sum = 0
# for i in range(1,n+1):
#     if i > 2 and i % 2 != 0:
#         k *= i
#         d *= i+1
#         sum += (-1 * pow(x,i+2)/d) + (pow(x,i)/k)
# print(sum/-2)

# # 29-masala:
# n = int(input("n = "))
# a = int(input("a = "))
# b = int(input("b = "))
# k = abs(a-b)/n
# for i in range(n):
#     a += k
#     print(a)

# # 30-masala:
# from math import sin
# n = int(input("n = "))
# a = int(input("a = "))
# b = int(input("b = "))
# k = abs(a-b)/n
# for i in range(n):
#     a += k
#     print(1 - sin(a))

# # 36-masala:
# n =int(input("n = "))
# k =int(input("k = "))
# sum = 0
# s = 1
# for i in range(1,n+1):
#     s *= k
#     sum += s
# print(sum)

# # 37-masala:
# n = int(input("n = "))
# s = 1
# sum = 0
# for i in range(1,n+1):
#     s = i ** i
#     sum += s
# print(sum)

# # 38-masala:
# n = int(input("n = "))
# x = []
# sum = 0
# for i in range(1,n+1):
#     x.append(i)
# for j in range(1,n+1):
#     sum += pow(j,x[-j])
# print(sum)
    
    
# # 39-masala:
# a = int(input("a = "))
# b = int(input("b = "))
# for i in range(a,b+1):
#     for j in range(i):
#         print(i,end=" ")

# # 40-masala:
# a = int(input("a = "))
# b = int(input("b = "))
# count = 1
# if a < b:
#     for i in range(a, b + 1):
#         for j in range(count):
#             print(i, end=" ")
#         count += 1