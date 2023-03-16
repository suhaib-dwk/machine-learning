
# name = "please enter your name :"
# name2 = "       please enter your name :"

# print(name.capitalize())
# print(name.count('e'))
# print(name.find("please"))
# print(name.upper())
# print(name.lower())
# print(len(name))
# print(name.rfind("e"))
# print(name.replace("e", "#"))
# print(name2.strip())
# print("suh"*3)
# print(name.split('e', 5))


"""
Write a program in Python that checks whether a given string is palindrome or not. 

name3 = input("please enter ")

if name3 == name3[::-1]:
    print("true")
else:
    print("false")

"""

"""
Write a Python program that prompts for and inputs three values,
and uses if statements to determine the minimum value, then displays it on screen.

num1 = int(input("Please Enter Number1 : "))
num2 = int(input("Please Enter Number2 : "))
num3 = int(input("Please Enter Number3 : "))

if num1 < num2 and num1 < num3:
    print(f'Number one is smallest => {num1}')
if num2 < num1 and num2 < num3:
    print(f'Number 2 is smallest => {num2}')
else:
    print(f'Number 3 is smallest => {num3}')
    
"""

# name = ["suhaib", "dweekat"]

# print(type(name))

# name1 = ("suhaib", "dweekat",)

# print(type(name1))


# import random
# for x in range(10):
#     print(random.randrange(1, 10))

# txt = "The best things in life are free!"
# print("expensive" not in txt)

# b = "Hello, World!"
# print(b[::-1])


# x = input("please name: ")
# if x == x[::-1]:
#     print("pol")
# else:
#     print("again")

# b = "Hello, World!"
# print(b.split())


# txt = "we are the so-called \"Vikings\" from the north."
# print(txt.split())

# txt = " Hello my name is suhaib  World "
# if "suhaib" in txt:
#     print("True")

# note the double round-brackets

# w = int(input())

# if w % 2 == 0 and w != 2:
#     print("Yes")
# else:
#     print("no")


# Way Too Long Words
# name = ["4", "word", "localization", "internationalization",
#         "pneumonoultramicroscopicsilicovolcanoconiosis"]

# i = 1
# d = len(name)

# for i in range(d):
#     c = len(name[i])
#     if c > 4:
#         a = name[i][0]
#         n = len(name[i])-2
#         f = name[i][-1]
#         print(f'{a}{n}{f} ')
#     elif c == 4:
#         print(name[1])

# n = int(input())
# for i in range(n):
#     st = input()
#     l = len(st)
#     if l <= 10:
#         print(st)
#     else:
#         print(st[0], l - 2, st[l - 1], sep="")


# string1 = str(input())
# print(string1[0].upper()+string1[1:])

# name = "geeks FOR geeks"

# print(name.capitalize())


# listName = list(input())

# r = len(listName)

# for i in range(r):
#     z = listName[i]
#     w = len(z)
#     if w % 2 == 0:
#         print(listName[i], "CHAT WITH HER!")
#     else:
#         print(listName[i], "IGNORE HIM!")


# def result(listName):
#     result = list(set(listName))

#     even = "CHAT WITH HER!"
#     odd = "IGNORE HIM!"

#     if len(result) % 2 == 0:
#         print("CHAT WITH HER!")
#     else:
#         print("IGNORE HIM!")


# listName = list(input())

# result(listName)

# x = int(input())

# i = 1

# for i in range(x):
#     w = i*2
#     if x-w == 0:
#         print(i)

# n = int(input())
# if n == 1 or n == 2 or n == 3 or n == 4 or n == 5:
#     print(1)
# elif n % 5 == 0:
#     print(n//5)
# else:
#     print((n//5)+1)


# std = ("Ahmad majdi", "nadeR jaFar", "Sami oDeh")
# for i in range(1, len(std)):
#     print("i=%d" % i, "|", str(std[i]).title())

# p = [4, 5, 1j]
# x = p.sort()
# print(x)

# x, y = z = 6+2, "python is good"
# print("x = %d" % x, "\n y=", y, "\n z="+z)

# a = ({"name": "apple", "color": "green", "marks": [90, 89, 99]}, [])
# print(type(a))
# print(a[0])
# print(a[0]["color"])
# print(a[0]['marks'][2])


# x = int(input("please value 1 : "))
# y = int(input('please value 2: '))
# z = int(input("please value 3 : "))

# if x > y and x > z:
#     print("value 1", x)
# elif x < y and y > z:
#     print("value 2 : ", y)
# else:
#     print("value 3: ", z)

# x = int(input("please enter the number iteration:"))
# tup = ()
# for i in range(x):
#     name = input("please enter the name :")
#     tup += (name,)
# print(tup)

# for index, value in enumerate(tup):
#     print(index, ',', "*" * len(value))


# from functools import reduce
# def new_tup(x):
#     tup = ()
#     a = x
#     for i in range(a):
#         name = input("please enter the name :")
#         tup += ((name, i),)
#     return tup


# name = input("please : ")
# tup = tuple(enumerate(name))
# print(tup)


# print(new_tup(x))

# num = int(input("please enter number  : "))

# if num % 2 == 0:
#     print("even")
# else:
#     print("odd")


# code = "secret"
# tries = 1
# inp = input("Enter the same text :")

# while inp != code:
#     print("You are tries ,", tries, "you have the three times")
#     inp = input("Enter the same text :")
#     tries += 1
#     if tries > 2:
#         print("Game over please agian the play ")
#         break
# if tries < 5 and inp == code:
#     print("you got it after ", tries, "tries")

# words = ("word", "hello")

# text = tuple(input("please enter text :").split())

# for i in text:
#     if i in words:
#         print("yes")
#     else:
#         print("no")

# num = int(input("please enter you have a marks :"))
# tup = ()
# for i in range(num):
#     marks = int(input("please enter the marks : "))
#     tup += (marks,)

# sum = 0
# for i in tup:
#     sum += i
# print(sum / num)


# tup = tuple(input("please value ").split())


# def numbers(tup):
#     for index, value in enumerate(tup):
#         return (value, ":", value[::-1])

# first = numbers(tup)
# print(first)

# import random as ra
# def dice():
#     dic1 = ra.randint(1, 7)
#     dic2 = ra.randint(1, 10)
#     return (dic1, dic2)


# dice()
# t1, t2 = dice()
# print(t1)
# print(t2)


# n = int(input("please enter"))
# def fact(n):
#     if n <= 1:
#         return 1
#     else:
#         return n*fact(n-1)


# print(fact(n))

# tup = ({"name": "suhaib", "age": 21},[])
# print(type(tup))


# name = [10, 320, 50, 500, 562]

# res = reduce(lambda x, y: x if x > y else y, name)
# print(res)


# lis = [1, 5, 2, 9, 3, 7, 2, 3, 45, 6, 8, 5, 4]
# names = ["helo", "suhaib", "dweekat", "jeahid"]

# new = [[], [], []]

# new[0] = names
# new[1] = lis
# new[2] = 'suhaib', 212, 222, "jasd"
# print(new)

# text = input("please enter the same text : ").split()
# text.sort(reverse=True)
# print(text)

# text = input("please enter the same text : ").split()
# doc = {}
# for i in text:
#     name = text.count(i)
#     doc[i] = name

# son = list(doc.values())
# print(son)
# print(doc)
# print(doc.keys())
# print(doc.values())

# n = [19, 5, 25, 20, 15]
# arr = n
# n.sort()
# n.extend(arr)
# print(n)
# p = {22, 11, 5, 20}
# j = (10, 20)

# p = list(p)
# j = list(j)
# n.sort()
# p.sort()
# j.sort()
# print(n)
# print(p)
# print(j)

# n[1] = 30
# print(n)

# x = []
# n.extend(p)
# x = n
# print(x)

# u = 0
# for i in n:
#     u += i
# print(u)

# for i in p:
#     if i in j:
#         print(i)

# class#########################3
# class Member:
#     id = 0
#     not_used_name = ["Hell", "Shit", "Fuck"]

#     def __init__(self, f_name, m_name, l_name, gender):
#         self.fname = f_name
#         self.mname = m_name
#         self.lname = l_name
#         self.gender = gender
#         Member.id += 1

#     def full_name(self):
#         if self.fname in Member.not_used_name:
#             raise ValueError("This is not use word")
#         else:
#             return f'name => {self.fname} {self.mname} {self.lname}'

#     def get_gender(self):
#         if self.gender == "male":
#             return f'Hello Mr {self.fname}'
#         elif self.gender == "female":
#             return f'Hello Mrs {self.fname}'
#         else:
#             return f'Hello {self.fname}'

#     def get_all(self):
#         return f"{self.get_gender()}   , {self.full_name()}"


# one = Member("Hell", "jehaid", "dweekat", "male")
# sec = Member("mohammed", "jehaid", "dweekat", "male")
# three = Member("sara", "jehaid", "dweekat", "female")
# four = Member("suzan", "jehaid", "dweekat", "female")


# print(sec.get_all())


# class skills:
#     def __init__(self) -> None:
#         self.skill = ["Html", "Css"]

#     def __str__(self) -> str:
#         return f"This is My Skills =>  {self.skill}"


# profile = skills()
# print(profile)

#### Inheritanc #####
# class Food:
#     def __init__(self, name, price) -> None:
#         self.name = name
#         self.price = price

#     def eat(self):
#         print("eat is amazing")


# class Apple(Food):
#     def __init__(self, name, price) -> None:
#         super().__init__(name, price)

#     def __repr__(self) -> str:
#         return f'NAME => {self.name} price => {self.price}'


# pro = Apple("apple", 150)
# print(pro)


# class person:
#     def __init__(self, name="ahmed") -> None:
#         self.name = name

#     def set_name(self, name):
#         self.name = name

#     def get_name(self):
#         return self.name


# pro = person()
# pro.set_name("suhaib")
# print(pro.get_name())

# class car:
#     def __init__(self, d) -> None:
#         self.d = d

#     def printTokens(self):
#         for t in self.d.keys():
#             print(t)

#     def printValues(self):
#         for t in self.d.values():
#             print(t)

#     def invert(self):
#         return {v: k for (k, v) in self.d.items()}


# if __name__ == "_main_":
#     print("is Direct")
#     d = {1: "car", 2: "mar", 3: "jeep"}

#     dd = car(d)
#     dd.printTokens()
#     dd.printValues()
#     print(dd.invert())


# class doc:
#     def __init__(self, title, price) -> None:
#         self.price = price
#         self.title = title

#     def get_price(self):
#         return self.price


# class book(doc):
#     def __init__(self, title, price) -> None:
#         super().__init__(title, price)


# b1 = book()


# num = list(range(5))
# print(num)


# def opr(n):
#     def re(i):
#         return i.remove(i)
#     for i in n:
#         if i % 2 == 1:
#             re(i)
#         else:
#             return n * 2


# n = opr(num)
# print(n)

# a, b, *c = range(10)
# num = {a: a for a in [1, 2, 3]}
# print(num)
# res = list(map(lambda x: x**2, num.keys()))
# print(res)

x = (10, 10)
y = ((10, 100),)
z = x+y
print(x+y)
