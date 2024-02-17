# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# name = "Amgad"
# age = 1950
#
#
# print(f"{name} {age}")

# courseCode = 499
# courseCode1 = "SE"
#
# cursen = 202
# cousen2 = "SE"
# # courseCode = eval(input("Put: "))
#
#
# if courseCode == 499 and courseCode1 == "SE":
#     print(courseCode, courseCode1)
#
# if cursen == 202 and cousen2 == "SE":
#     print(cousen2, cursen)
#
# age = eval(input("PUT: "))
#
# if age > 60:
#     print("senior")
# elif age > 18:
#     print("adult")
# else:
#     print("minor")

# print(type(3+2))
# X, V = eval(input("PUT: "))
#
# oper = input("Choose a math operation (+, -, *): ")
# # print(type(C))
#
# print(X ,oper, V)
#
# for i in oper:
#     print(X  i V)
# for i in range(1, 11):
#     print(operator_dict[oper](float(num), i))

# import operator
#
# operator_dict = {
#     '+': operator.add,
#     '-': operator.sub,
#     '*': operator.mul,
# }
# num = int(input("Enter a number : "))
#
# oper = input("Choose a math operation (+, -, *): ")
#
# print(operator_dict[oper](float(num)))

# v = input("PUT: ")
#
# print(type(v),len(v))

# for i in range(100,90, ): print(i)

# num = eval(input("Put the NUM: "))
#
# if num % 2 == 0:
#     print("even")
# else:
#     print("odd")

# num = eval(input("Put the NUM: "))
#
# if num < 10:
#     print(num * 2)
# elif 10 < num < 20:
#     print(num / 2)
# else:
#     print(num)

# for num in range(0, 30):
#     if num < 10:
#         print(num * 2)
#     elif 10 < num < 20:
#         print(num / 2)
#     else:
#         print(num)
# my = "hello"
# for i in my:
    # p = 1
    # print(len(i[my]))
#
# my = "hello world this is python"
#
# for i in range(len(my)):
#
#     if i % 2 == 0:
#         print(i, ':', my[i].upper())
#     else:
#         print(i, ':', my[i])

#
# a = input("the first name ")
# b = input("the seconed name ")
#
# print(f"|   {a}    |    {b}    |")
# print("------------------------")
# print(f"|   {a}    |    {b}    |")
# age = 15
# gender = "male"
# if age == 15:
#     if gender == "male":
#         print("get in")
# else:
#     print("Sorry you can't get in")

# mynum = 11
#
# if mynum > 1:
#    for i in range(2, mynum):
#        print(i)
#        if (mynum % i) == 0:
#            print(mynum, " number X is NOT PRIME")
#            break
#    else:
#        print(mynum, "x is a prime number")
# else:
#    print(mynum, "number X IS NOT ALLOWED")

# x = eval(input("Enter number: "))
# for i in range(x):
#     if i % 2 == 0:
#
#         print(i)
# x = 4
# for i in range(1,11):
#     print(f"{x} * {i} = {i * x}

# my = 81
#
# for i in range(2,my):
#     if my % i == 0:
#         print("not prime")
#         break
#
#     else:
#         print("prime")

import string

thislist = []

x = " "
while x != "exit":

    thislist.append(x)
    for i in thislist:
        for f in i:
            s = 0
            for char in string.ascii_lowercase:
                s += 1
                if char == f:
                    print(f, s)

    x = input("ENTER what you want to append: ")


