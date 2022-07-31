## Bismillahir rohmanir rohim!

# # 1-masala:
# n = int(input("n = "))
# x = []
# for i in range(n):
#     b = i + 1
#     a = int(input(f"{b}-raqam: "))
#     if a % 2 != 0:
#         x.append(a)
# for j in range(len(x)):
#     print(x[j],end=" ")

# # 2-masala:
# n = int(input("n = "))
# x = []
# for i in range(n):
#     a = pow(2,i)
#     x.append(a)
# for j in range(len(x)):
#     print(x[j],end=" ")

# # 3-masala:
# n = int(input("n = "))
# a = int(input("a = "))
# d = int(input("d = "))
# x = [a]
# for i in range(n-1):
#     a += d
#     x.append(a)
# print(x)

# # 4-masala:
# n = int(input("n = "))
# a = int(input("a = "))
# d = int(input("d = "))
# x = [a]
# for i in range(1,n):
#     a *= d
#     x.append(a)
# print(x)

# # 5-masala:
# n = int(input("n = "))
# x = []
# f0 = 1
# x.append(f0)
# f1 = 1
# x.append(f1)
# for i in range(2,n):
#     f2 = f1 + f0
#     x.append(f2)
#     f0 = f1
#     f1 = f2
# print(x)

# 6-masala:

# # 7-masala:
# n = int(input("n = "))
# x = []
# for i in range(n):
#     s = i + 1
#     a = int(input(f"{s}-raqam: "))
#     x.append(a)
# for j in range(1,len(x)+1):
#     print(x[-j],end=" ")

# # 8-masala:
# n = int(input("n = "))
# x = []
# count = 0
# for i in range(n):
#     s = i + 1
#     a = int(input(f"{s}-raqam: "))
#     if a % 2 != 0:
#         x.append(a)
#         count += 1
# print(count)

# # 9-masala:
# n = int(input("n = "))
# x = []
# count = 0
# for i in range(n):
#     s = i + 1
#     a = int(input(f"{s}-raqam: "))
#     if a % 2 == 0: 
#         x.append(a)
#         count += 1
# print(count)

# 10-masala:
# n = int(input("n = "))
# x = []
# count1 = 0
# count2 = 0
# for i in range(n):
#     s = i + 1
#     a = int(input(f"{s}-raqam: "))
#     if a % 2 == 0:
#         x.append(a)
#         count1 += 1
#     elif a % 2 != 0:
#         x.append(a)
#         count2 += 1
# print(f"massivda {count1} ta juft, {count2} ta toq element mavjud")

# n = int(input("n = "))
# x = []
# y = []
# for i in range(n):
#     s = i + 1
#     a = int(input(f"{s}-raqam: "))
#     if a % 2 == 0:
#         x.append(a)
#     elif a % 2 != 0:
#         y.append(a)
# for j in range(len(x)):
#     print(x[j],end=" ")
# for k in range(1,len(y)+1):
#     print(y[-k],end=" ")

# 11-masala:
# n = int(input("n = "))
# k = int(input("k = "))
# x = []
# for i in range(n):
#     s = i + 1
#     a = int(input(f"{s}-raqam: "))
#     if a % k == 0:
#         x.append(a)
# print(x)

# # 12-masala:
# n = int(input("n = "))
# x = []
# for i in range(n):
#     s = i + 1
#     a = int(input(f"{s}-raqam: "))
#     x.append(a)
# for j in range(len(x)):
#     if j % 2 == 0:
#         print(x[j],end=" ")
    
# # 13-masala:
# n = int(input("n = "))
# x = []
# for i in range(n):
#     s = i + 1
#     a = int(input(f"{s}-raqam: "))
#     x.append(a)
# for j in range(2,len(x)+1):
#     print(x[-j],end=" ")

# # 14-masala:
# n = int(input("n = "))
# x = []
# for i in range(n):
#     s = i + 1
#     a = int(input(f"{s}-raqam: "))
#     x.append(a)
# for j in range(len(x)):
#     if j % 2 == 0:
#         print(x[j],end=" ")
# for k in range(len(x)):
#     if k % 2 != 0:
#         print(x[k],end=" ")

# # 15-masala:
# n = int(input("n = "))
# x = []
# for i in range(n):
#     s = i + 1
#     a = int(input(f"{s}-raqam: "))
#     x.append(a)
# for j in range(len(x)):
#     if j % 2 != 0:
#         print(x[j],end=" ")
# for k in range(1,len(x)+1):
#     if k % 2 == 0:
#         print(x[-k],end=" ")

# # 16-masala:
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,13,14,15]
# k = len(a) // 2
# n = len(a)
# for i in range(k):
#     print(a[i],end=" ")
#     print(a[n - i - 1],end=" ")
# for j in range(n - k * 2):
#     print(a[k], end=" ")

# # 17-masala:
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,13,14,15]
# k = len(a) // 4
# n = len(a)
# for i in range(k):
#     print(a[2 * i], end=" ")
#     print(a[2 * i + 1], end=" ")
#     print(a[n - 2 * i - 1], end=" ")
#     print(a[n - 2 * i - 2], end=" ")
# for i in range(n - k * 4):
#     print(a[k * 2 + i], end=" ")

# # 18-masala:
# n = int(input("n = "))
# x = []
# for i in range(n):
#     s = i + 1
#     a = int(input(f"{s}-raqam: "))
#     x.append(a)
# for j in range(len(x)):
#     if x[j] < x[-1]:
#         print(x[j])
#         break

# # 19-masala:
# n = int(input("n = "))
# x = []
# count = 0
# for i in range(n):
#     s = i + 1
#     a = int(input(f"{s}-raqam: "))
#     x.append(a)
# for j in range(len(x)):
#     if x[0] < x[j] and x[-1] > x[j]:
#         b = x[j]
# print(b)

# # 20-masala:
# n = int(input("n = "))
# k = int(input("k = "))
# l = int(input("l = "))
# x = []
# sum = 0
# for i in range(n):
#     s = i + 1
#     a = int(input(f"{s}-raqam: "))
#     x.append(a)
# for j in range(len(x)):
#     if x[j] >= x[k] and x[j] <= x[l]:
#         sum += x[j]
# print(sum)

# # 21-masala:
# n = int(input("n = "))
# k = int(input("k = "))
# l = int(input("l = "))
# x = []
# sum = 0
# for i in range(n):
#     s = i + 1
#     a = int(input(f"{s}-raqam: "))
#     x.append(a)
# for j in range(len(x)):
#     if x[j] >= x[k] and x[j] <= x[l]:
#         sum += x[j]
# print(sum/(abs(k-l)+1))

# # 22-masala:
# n = int(input("n = "))
# k = int(input("k = "))
# l = int(input("l = "))
# x = []
# sum = 0
# for i in range(n):
#     s = i + 1
#     a = int(input(f"{s}-raqam: "))
#     x.append(a)
# for j in range(len(x)):
#     if x[j] < x[k] and x[j] < x[l]:
#         sum += x[j]
# print(sum)

# # 23-masala:
# n = int(input("n = "))
# k = int(input("k = "))
# l = int(input("l = "))
# x = []
# sum = 0
# for i in range(n):
#     s = i + 1
#     a = int(input(f"{s}-raqam: "))
#     x.append(a)
# for j in range(len(x)):
#     if x[j] < x[k] and x[j] < x[l]:
#         sum += x[j]
# print(sum/(n - (abs(k-l)+1)))

# # 24-masala:
# d = 3
# a1 = 4
# a = [4, 7, 10, 13, 16, 19]
# bool = True
# k = a[1] - a[0]
# for i in range(1,len(a)):
#     if a[i] - a[i - 1] != k:
#         bool == False
# if bool:
#     print(k)
# else:
#     print(0)

# 25-masala:


# # 28-masala:
# n = int(input("n = "))
# x = []
# y = []
# for i in range(n):
#     s = i + 1
#     a = int(input(f"{s}-raqam: "))
#     x.append(a)
# for j in range(len(x)):
#     if j % 2 == 0:
#         y.append(x[j])
# for k in range(len(y)):
#     min = y[0]
#     if min > y[k]:
#         min = y[k]
# print(min)

# # 29-masala:
# n = int(input("n = "))
# x = []
# y = []
# for i in range(n):
#     s = i + 1
#     a = int(input(f"{s}-raqam: "))
#     x.append(a)
# for j in range(len(x)):
#     if j % 2 != 0:
#         y.append(x[j])
# for k in range(len(y)):
#     max = y[0]
#     if max < y[k]:
#         max = y[k]
# print(max)

## 30-masala:
# n = [1,2,4,3,5,7,6,8,9,12,11]
# count = 0
# for i in range(len(n)):
#     if i + 1 < len(n):
#         if n[i] > n[i+1]:
#             count = i
#             print(count)

# # 31-masala:
# n = [1,2,4,3,5,7,6,8,9,12,11]
# x = []
# count = 0
# for i in range(len(n)):
#     if i + 1 < len(n):
#         if n[i] < n[i+1]:
#             count = i
#             x.append(count)
# for j in range(1,len(x)+1):
#     print(x[-j],end=" ")

# 32-masala:
# x = [1,4,6,7,3,5,6]
# count = 0
# for i in range(1,len(x)+1):
#     if i + 1 < len(x) + 1:
#         if x[i] < x[i-1] and x[i] < x[i+1]:
#             count = i
#             print(count)
#             break

# # 33-masala:
# x = [8,4,3,7,3,4,2]
# count = 0
# for i in range(1,len(x)+1):
#     if i + 1 < len(x) + 1:
#         if x[i] > x[i-1] and x[i] > x[i+1]:
#             count = i
#print(count)

# # 34-masala:
# x = [1,4,6,7,3,5,6,4,5,9,7,8]
# y = []
# for i in range(1,len(x)+1):
#     if i + 1 < len(x) + 1:
#         if x[i] < x[i-1] and x[i] < x[i+1]:
#             y.append(x[i])
# for j in range(len(y)):
#     max = y[0]
#     if max < y[j]:
#         max = y[j]
# print(max)

# # 35-masala:
# x = [1,4,6,7,3,5,6,4,5,9,7,8]
# y = []
# for i in range(1,len(x)+1):
#     if i + 1 < len(x) + 1:
#         if x[i] < x[i-1] and x[i] < x[i+1]:
#             y.append(x[i])
# for j in range(len(y)):
#     min = y[0]
#     if min > y[j]:
#         min = y[j]
# print(min)

# # 36-masala:
# x = [1,4,6,7,3,5,6,4,5,9,7,8]
# for i in range(1,len(x)+1):
#     if i+1 < len(x):
#         if x[i] < x[i-1] and x[i] < x[i+1]:
#             x.pop(i)
# print(x)


# # 37-masala: chala:
# x = [9,4,1,2,3,5,7]
# for i in range(len(x)):
#     if i + 1 < len(x):
#         if x[i] < x[i+1]:
#             print(x[i])

# # 38-masala: chala:
# x = [9,4,1,2,3,5,7]
# for i in range(len(x)):
#     if i + 1 < len(x):
#         if x[i] > x[i+1]:
#             print(x[i])


# # 39-masala: chala:
# x = [9,4,1,2,3,5,7]
# a = 0
# for i in range(len(x)):
#     if i + 1 < len(x):c
#         if x[i] < x[i+1]:
#             a += 1
#         elif x[i] > x[i+1]:
#             a += 1
# print(a)

# # 40-masala:chala:
# n = int(input("n = "))
# r = int(input("r = "))
# x = []
# y = []
# z = []
# for i in range(n):
#     s = i + 1
#     a = int(input(f"{s}-raqam: "))
#     x.append(a)
# for j in range(len(x)):
#     if x[j] < r:
#         y.append(x[j])
# for k in range(len(x)):
#     if x[j] > r:
#         z.append(x[j])
# a = max(y)
# b = min(z)
# print(f"o'ng tomondan eng yaqini {a}, chap tomondan esa {b}")  

# # 41-masala: 
# x = [1,3,2,8,3,7,4,6,5]
# y = []
# n = len(x)
# sum = 0
# for i in range(1,n+1):
#     if i+1 < n:
#         sum = x[i-1] + x[i+1]
#         y.append(sum)
# max = y[0]
# for j in range(1,len(y)):
#     if max < y[j]:
#         max = y[j]
# for k in range(1,n+1):
#     if k + 1 < n:
#         if x[k-1] + x[k+1] == max:
#             print(x[k-1])
#             print(x[k+1])

# # 42-masala:
# x = [1,3,2,8,3,7,4,6,5]
    
# # 43-masala:
# n = int(input("n = "))
# x = []
# y = []
# for i in range(n):
#     s = i + 1
#     a = int(input(f"{s}-element: "))
#     x.append(a)
# for j in range(len(x)):
#     if x[j] not in y:
#         y.append(x[j])
# print(f"massiv: {y}, elementlar soni {len(y)}")

# # 44-masala:
# x = [1,2,3,4,5,6,3,7]
# index = 0
# index1 = 0
# for i in range(len(x)):
#     for j in range(len(x)):
#         if x[i] == x[j] and i != j :
#             index = j
#             index1 = i
# print(index)
# print(index1)

# 45-masala:


# # 47-masala:
# n = int(input("n = "))
# x = []
# y = []
# for i in range(n):
#     s = i + 1
#     a = int(input(f"{s}-element: "))
#     x.append(a)
# for j in range(len(x)):
#     if x[j] not in y:
#         y.append(x[j])
#     else:
#         print(x[j])

# # 51-masala:
# n = 7
# a = [1,3,5,7,9,11,13]
# b = [2,4,6,8,10,12,14]
# x = []
# y = []
# for i in range(len(a)):
#     x.append(a[i])
# for j in range(len(b)):
#     y.append(b[j])
# a = y
# b = x
# print(a)
# print(b)

# # 54-masala:
# n = int(input("n = "))
# a = []
# b = []
# count = 0
# for i in range(n):
#     s = i + 1
#     x = int(input(f"{s}-element: "))
#     a.append(x)
# for j in range(len(a)):
#     if a[j] % 2 == 0:
#         b.append(a[j])
#         count += 1
# print(f"b massivda {len(b)} ta element mavjuf ular {b}")

# # 55-masala:
# n = int(input("n = "))
# a = []
# b = []
# for i in range(n):
#     s = i 
#     x = int(input(f"{s}- indexdagi element: "))
#     a.append(x)
# for j in  range(1,len(a),2):
#     b.append(a[j])
# print(f"b massiv elementlar soni {len(b)} ta ular {b}")

# # 56-masala:
# n = int(input("n = "))
# a = []
# b = []
# for i in range(n):
#     s = i 
#     x = int(input(f"{s}- indexdagi element: "))
#     a.append(x)
# for j in  range(1,len(a)):
#     if j % 3 == 0:
#         b.append(a[j])
# print(f"b massiv elementlar soni {len(b)} ta ular {b}")

# # 57-masala:
# n = int(input("n = "))
# a = []
# b = []
# for i in range(n):
#     s = i 
#     x = int(input(f"{s}- indexdagi element: "))
#     a.append(x)
# for j in  range(len(a)):
#     if j % 2 == 0:
#         b.append(a[j])
# for k in range(len(a)):
#     if k % 2 != 0:
#         b.append(a[k])
# print(f"b massiv elementlar soni {len(b)} ta ular {b}")

# 58-masala:

# # 65-masala:
# n = int(input("n = "))
# k = int(input("k = "))
# a = []
# for i in range(n):
#     s = i + 1
#     x = int(input(f"{s}-element: "))
#     a.append(x)
# for j in range(len(a)):
#     if j == k:
#         b = a[j]
# for k in range(len(a)):
#     print(a[k]+b,end=" ")

# # 66-masala:
# n = int(input("n = "))
# a = []
# for i in range(n):
#     s = i + 1
#     x = int(input(f"{s}-element: "))
#     a.append(x)
# for j in range(len(a)):
#     if a[j] % 2 == 0:
#         b = a[j]
#         break
# for k in range(len(a)):
#     if a[k] % 2 == 0:
#         print(a[k] + b,end=" ")

# # 67-masala:
# n = int(input("n = "))
# a = []
# b = []
# for i in range(n):
#     s = i + 1
#     x = int(input(f"{s}-element: "))
#     a.append(x)
# for j in range(len(a)):
#     if a[j] % 2 != 0:
#         b.append(a[j])
# for k in range(len(b)):
#     print(b[k]+b[-1],end=" ")

# # 68-masala: chala:
# n = int(input("n = "))
# x = []
# y = []
# for i in range(n):
#     s = i + 1
#     a = int(input(f"{s}-element: "))
#     x.append(a)
# max = x[0]
# min = x[0]
# for j in range(len(x)):
#     if max < x[j]:
#         max = x[j]
#     elif min > x[j]:
#         min = x[j]
# print(f"max: {max}, min: {min}")

# # 69-masala: xato:
# n = int(input("n = "))
# a = []
# b = []
# c = []
# d = []
# for i in range(n):
#     s = i + 1
#     x = int(input(f"{s}-element: "))
#     a.append(x)
    
# for j in range(len(a)):
#     if j % 2 == 0:
#         b.append(a[j])
# for k in range(len(a)):
#     if k % 2 != 0:
#         c.append(a[k])
# for l in range(len(a)):
#     d.append(c[l])
#     d.append(b[l])
# print(d)

# # 71-masala:
# import random
# n = int(input("n = "))
# x = []
# y = []
# for i in range(n):
#     a = random.randint(0,n)
#     x.append(a)
# print(f"x massiv: {x}")
# for j in range(1,len(x)+1):
#     y.append(x[-j])
# x = y
# print(f"y massiv: {x}")

# # 72-masala:
# import random
# n = int(input("n = "))
# k = int(input("k = "))
# h = int(input("h = "))
# a = []
# b = []
# for i in range(n):
#     x = random.randint(1,n)
#     a.append(x)
# print(a)
# for j in range(len(a)):
#     if j >= k and h >= j:
#         b.append(a[j])
# for d in range(1,len(b)+1):
#     print(b[-d],end=" ")

# # 73-masala:
# import random
# n = int(input("n = "))
# k = int(input("k = "))
# h = int(input("h = "))
# a = []
# b = []
# for i in range(n):
#     x = random.randint(1,n)
#     a.append(x)
# print(a)
# for j in range(len(a)):
#     if j > k and h > j:
#         b.append(a[j])
# for d in range(1,len(b)+1):
#     print(b[-d],end=" ")

# # 74-masala: chala:
# import random
# n = int(input("n = "))
# a = []
# b = []
# for i in range(n):
#     x = random.randint(1,n)
#     a.append(x)
# print(a)
# l = max(a)
# f = min(a)
# for k in range(len(a)):
#     if a[k] > f and a[k] < l:
#         print(a[k])

# # 76-masala: chala:
# n = int(input("n = "))
# a = []
# b = []
# for i in range(n):
#     s = i + 1
#     x = int(input("a = "))
#     a.append(x)
# for j in range(len(a)):
#     if j+2 < len(a):
#         if a[j] > a[j+1] and a[j] > a[j-1]:
#             aj = a[j]
# for k in range(len(a)):
#     if a[k] == aj:
#         b.append(0)
#         continue
#     b.append(a[k])
# print(b)

# # 90-masala:
# n = int(input("n = "))
# k = int(input("k = "))
# x = []
# y = []
# for i in range(n):
#     a = int(input(f"{i}-ixdexdagi element: "))
#     x.append(a)
# for j in range(len(x)):
#     if j == k:
#         continue
#     y.append(x[j])
# print(y)

# # 92-masala:
# n = int(input("n = "))
# x = []
# y = []
# for i in range(n):
#     a = int(input(f"{i}-indexdagi element: "))
#     x.append(a)
# for j in range(len(x)):
#     if x[j] % 2 != 0:
#         continue
#     y.append(x[j])
# print(f"hosil bo'lgan massiv: {y}, elementlar soni:{len(y)}")

# # 93-masala:
# n = int(input("n = "))
# x = []
# y = []
# for i in range(n):
#     a = int(input(f"{i}-indexdagi element: "))
#     x.append(a)
# for j in range(len(x)):
#     if j % 2 == 0:
#         continue
#     y.append(x[j])
# print(f"massiv: {y}, indexlar soni: {len(y)}")

# # 94-masala:
# n = int(input("n = "))
# x = []
# y = []
# for i in range(n):
#     a = int(input(f"{i}-indexdagi element: "))
#     x.append(a)
# for j in range(len(x)):
#     if j % 2 != 0:
#         continue
#     y.append(x[j])
# print(f"massiv: {y}, elementlar soni: {len(y)}")

# # 95-masala: chala:
# x = [1,2,3,6,3,7,1,4]
# y = []
# for i in x:
#     if i not in y:
#         y.append(i)
# print(y)

# # 106-masala:
# n = int(input("n = "))
# x = []
# sum = 0
# for i in range(n):
#     s = i + 1
#     a = int(input(f"{s}-element: "))
#     x.append(a)
# for j in range(0,len(x),2):
#     sum += x[j]
# print(sum)

# # 107-masala:
# n = int(input("n = "))
# x = []
# sum = 0
# for i in range(n):
#     s = i + 1
#     a = int(input(f"{s}-element: "))
#     x.append(a)
# for j in range(1,len(x),2):
#     sum += x[j]
# print(sum * 2)

# # 108-masala: chala:
# x = [1,3,5,8,9,4,6]
# y = []
# z = []
# a = []
# n = len(x)
# for i in range(len(x)):
#     if x[i] % 2 == 0:
#         y.append(x[i])
#     else:
#         z.append(x[i])
# for j in range(n//2):
#     a.append(z[j])
#     a.append(0)
#     a.append(y[j])
# print(a)

# # 110-masala:
# x = [1,2,3,4,5,6,7,8,9]
# n = len(x)
# sum = 0
# for i in range(n):
#     if x[i] % 2 == 0:
#         sum += x[i]
# print(sum)

# # 110-masala:
# x = [1,2,3,4,5,6,7,8,9]
# n = len(x)
# sum = 0
# for i in range(n):
#     if x[i] % 2 != 0:
#         sum += x[i]
# print(sum*2)

# # 112-masala: chala:
# x = [1, 9, 2, 8, 3, 7, 4, 6, 5]
# n = len(x)
# for i in range(n-1):
#     for j in range(n - 1):
#         if x[j] > x[j + 1]:
#             x[j],x[j+1] == x[j+1],x[j]
# print(x)

# # for 40
# a = int(input("a = "))
# b = int(input("b = "))
# count = 1
# if a < b:
#     for i in range(a, b + 1):
#         for j in range(count):
#             print(i, end=" ")
#         count += 1
# else:
#     print("yuq")
# # array 17
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,13,14,15]
# k = len(a) // 4
# n = len(a)
# for i in range(k):
#     print(a[2 * i], end=" ")
#     print(a[2 * i + 1], end=" ")
#     print(a[n - 2 * i - 1], end=" ")
#     print(a[n - 2 * i - 2], end=" ")
# for i in range(n - k * 4):
#     print(a[k * 2 + i], end=" ")
# # array 24
# d = 3
# a1 = 4
# x = [4, 7, 10, 13, 16, 19]
# bool = True
# k = a[1] - a[0]
# for i in range(1,len(x)):
#     if a[i]-a[i-1]!=k:
#         bool=False
# if bool:
#     print(k)
# else:
#     print(0)
# # array 27
# x = [-4, 7, -10, -13, 16, 19]
# index = 0
# for i in range(1, len(x)):
#     if x[i] > 0 != x[i - 1] > 0:
#         index = i
#         break
# if index:
#     print(index)
# else:
#     print(0)
# array 48
# a = [-4, 7, -10, -13, 16, 19]
# count = 0
# s = 0
# for i in range(len(a)):
#     count = 0
#     for j in range(len(a)):
#         if a[i] == a[j] and i != j:
#             count += 1
#     if count > s:
#         s = count


# # array 50
# a = [1, 2, 3, 4, 5, 2, 13, 57, 42, 1]
# count = 0
# for i in range(1, len(a)):
#     if a[i - 1] > a[i]:
#         print("i = ", i) 
#         count += 1
# print("soni  = ",count)

# array 58
# a = [1, 2, 3, 4, 5, 2, 13, 57, 42, 1]
# b = []
# summ = 0
# for i in range(1, len(a)):
#     for j in range(i):
#         summ += a[j]
#     b.append(summ)
#     summ = 0
# print(b)
# array 64
# a = [1, 2, 3, 4, 5]
# b = [2, 13, 57, 42]
# c = [3, 4, 5, 2, 13]
# k = a + b + c
# print(k)
# for i in range(len(k)-1):
#     for j in range(len(k) - 1):
#         if k[j] > k[j + 1]:
#             k[j], k[j + 1] = k[j + 1], k[j]
#
# print(k)
# array 69
# a = [1, 2, 3, 4, 5, 13, 42, 57]
# for i in range(1, len(a), 2):
#     a[i], a[i - 1] = a[i - 1], a[i]
# print(a)
# array 82
# a = [1, 2, 3, 4, 5, 13, 42, 57]
# k = int(input(" k= "))
# n = len(a)-1
# if 1 < k < len(a):
#     for i in range(len(a) - k):
#         a[n - i], a[n - i - k] = 0, a[n - i]
# print(a)
# array 95
# a = [1, 2, 1, 3, 1, 1, 1, 1, 4, 2, 5, 5, 4, 13, 13, 42, 57]
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)
# array 98
# a = [1, 2, 1, 3, 1, 1, 1, 1, 4, 2, 5, 2, 5, 4, 5, 13, 13, 13, 42, 57]
# j = 0
# count = 0
# while j < len(a):
#     x = a[j]
#     for i in a:
#         if i == a[j]:
#             count += 1
#     if count < 3:
#         while x in a:
#             a.remove(x)
#     j += 1
#     count = 0
# print(a)
# chala
# array 108
# a = [1, 2, -3, -4, 5, 13, -42, 57]
# b = []
# for i in a:
#     if i > 0:
#         b.append(i)
#         b.append(0)
#
#     else:
#         b.append(i)
# print(b)
# a = [1, 2, -3, -4, 5, 13, -42, 57]
# print(len(a))
# 1-xolat
# for i in a:
#     print(i,end=" ")
# 2- xolat
# for i in range(len(a)):
#     print(a[i])


# 90-masala:
# x = [1,2,3,4,5,6,7]
# y = []
# n = len(x)
# k = int(input("k = "))
# for i in range(n):
#     if i == k:
#         continue
#     y.append(x[i])
# print(y)

# x = [1,2,3,4,5,6,7]
# k = int(input("k = "))
# x.pop(k)
# print(x)

# # 91-masala:
# x = [1,2,3,4,5,6,7,8,9]
# y = []
# k = int(input("k = "))
# m = int(input("m = "))
# for i in range(len(x)):
#     if i < k:
#         y.append(x[i])
#     elif i > m:
#         y.append(x[i])
# print(y) 

# # 92-masala:
# x = [1,9,2,8,3,7,4,6,5]
# y = []
# for i in range(len(x)):
#     if x[i] % 2 == 0:
#         y.append(x[i])
# print(y)

# # 93-masala:
# x = [1,2,3,4,5,6,7,8,9]
# y = []
# for i in range(1,len(x),2):
#     y.append(x[i])
# print(y)    

# # 94-masala:
# x = [1,2,3,4,5,6,7,8,9]
# y = []
# for i in range(0,len(x),2):
#     y.append(x[i])
# print(y) 

# # 95-masala:
# x = [1,2,3,3,4,5,6,6,7]
# y = []
# for i in x:
#     if i not in y:
#         y.append(i)
# print(y)

# # 96-masala:
# x = [1,2,3,3,4,5,6,6,7]
# y = []
# for i in x:
#     if i not in y:
#         y.append(i)
# print(y)

# # 97-masala:
# a = [1, 2, 1, 3, 1, 1, 1, 1, 4, 2, 5, 2, 5, 4, 5, 13, 13, 13, 42, 57]
# j = 0
# count = 0
# while j < len(a):
#     x = a[j]
#     for i in a:
#         if i == a[j]:
#             count += 1
#     if count < 3:
#         while x in a:
#             a.remove(x)
#     j += 1
#     count = 0
# print(a)


# x = [1,9,2,1,8,3,3,7,4,6,5,5]
# y = []
# for i in range(1,len(x)):
#     for j in range(i):
#         if x[i] == x[j]:
#             y.append(x[i])
# print(y)
    
# # 112-masala:
# x = [1,9,2,8,3,7,4,6,5]
# for i in range(len(x)):
#     for j in range(0,len(x)-i-1):
#         if x[j] > x[j+1]:
#             x[j],x[j+1] = x[j+1],x[j]
# print(x)
            
# # array 116
# a = [1, 1, 1, 78, 78, 78, 6, 6, 6, 6, 65, 5, 5, 5, 5]
# b = []
# c = []
# b.append(a[0])
# c.append(1)
# j = 0
# for i in range(1, len(a)):
#     if a[i] == a[i - 1]:
#         c[j] += 1
#     else:
#         b.append(a[i])
#         c.append(1)
#         j += 1
# print(b)
# print(c)

# # array 117
# a = [1, 1, 1, 78, 78, 78, 6, 6, 6, 6, 65, 5, 5, 5, 5]
# b = []
# c = []
# b.append(a[0])
# c.append(1)
# j = 0
# for i in range(1, len(a)):
#     if a[i] == a[i - 1]:
#         c[j] += 1
#     else:
#         b.append(a[i])
#         c.append(1)
#         j += 1
# print(b)
# print(c)
# x = []
# for i in range(len(b)):
#     x.append(0)
#     for j in range(c[i]):
#         x.append(b[i])
# print(x)

# # 118-masala:
# a = [9,9,1,2,8,8,3,3,4,7,7,7,7,5,6,6]
# b = []
# c = []
# b.append(a[0])
# c.append(1)
# nolcha = 0
# for i in range(1,len(a)):
#     if a[i] == a[i-1]:
#         c[nolcha] += 1
#     else:
#         b.append(a[i])
#         c.append(1)
#         nolcha += 1
# print(b)
# print(c)
# x = []
# for i in range(len(b)):
#     for j in range(c[i]):
#         x.append(b[i])
#     x.append(0)
# print(x)

# # 119-masala: 
# a = [9,9,1,2,8,8,3,3,4,7,7,7,7,5,6,6]
# d = int(input("element kiriting: "))
# b = []
# c = []
# b.append(a[0])
# c.append(1)
# nolcha = 0
# for i in range(1,len(a)):
#     if a[i] == a[i-1]:
#         c[nolcha] += 1
#     else:
#         b.append(a[i])
#         c.append(1)
#         nolcha += 1
# print(b)
# print(c)
# x = []
# for i in range(len(b)):
#     for j in range(c[i]):
#         x.append(b[i]+d)
# print(x)

# # 120-masala:
# a = [9,9,1,2,8,8,3,3,4,7,7,7,7,5,6,6]
# d = int(input("element kiriting: "))
# b = []
# c = []
# b.append(a[0])
# c.append(1)
# nolcha = 0
# for i in range(1,len(a)):
#     if a[i] == a[i-1]:
#         c[nolcha] += 1
#     else:
#         b.append(a[i])
#         c.append(1)
#         nolcha += 1
# print(b)
# print(c)
# x = []
# for i in range(len(b)):
#     for j in range(c[i]):
#         x.append(b[i]-d)
# print(x)

# # 121-masala:
# a = [9,9,1,2,8,8,3,3,4,7,7,7,7,5,6,6]
# k = int(input("k = "))
# b = []
# c = []
# b.append(a[0])
# c.append(1)
# nolcha = 0
# for i in range(1,len(a)):
#     if a[i] == a[i-1]:
#         c[nolcha] += 1
#     else:
#         b.append(a[i])
#         c.append(1)
#         nolcha += 1
# print(b)
# print(c)

# # 122-masala:
# k = int(input("k = "))
# a = [1,2,3,4,4,4,5,6,6,7,8,9,9,9,9]
# n = len(a)
# b = []
# c = []
# b.append(a[0])
# c.append(1)
# j = 0
# for i in range(1,len(a)):
#     if a[i] == a[i-1]:
#         c[j] += 1
#     else:
#         b.append(a[i])
#         c.append(1)
#         j += 1
# print(b)
# print(c)

# n = int(input("n = "))
# x = []
# count = 0
# for i in range(n):
#     a = int(input("a = "))
#     x.append(a)
# for j in range(1,len(x)):
#     if a[j] == a[j-1]:
#         count += 1
# print(count)

# import numpy
# a = numpy.zeros((4,4))
# n = len(a)
# count = 0
# for i in range(n):
#     for j in range(n):
#         count += 1
#         a[i][j] = count
# for i in range(n):
#     if i % 2 == 0:
#         print(a[i])
#     else:
#         print(a[i][::-1])

