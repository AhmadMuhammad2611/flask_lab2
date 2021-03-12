import time


def mydecorator(func):
    def newfunc(*args, **kwargs):
        print("====arguments======")
        print(args)
        print(kwargs)
        result = func(*args, **kwargs)
        print("*****Return*****")
        print(result)
        return result

    return newfunc


@mydecorator
def mysum(a, b):
    return a + b


@mydecorator
def mysub(a, b):
    return a - b


@mydecorator
def myprod(a, b):
    return a * b


# myprod(1, 3)
# print('-----------------')
# mysub(10, 6)
# print('-----------------')
# mysum(5, 1)

# def avg():
#     total = 0
#     sum_ = 0

#     def add(num):
#         nonlocal total
#         nonlocal sum_

#         total += 1
#         sum_ += num
#         return sum_ / total

#     return add

# add = avg()

# print(add(1))  #total = 1, sum = 1
# print(add(2))  #total = 2, sum = 3
# print(add(5))  #total = 2, sum = 3

# add2 = avg()
# print(add2(2))  #total = 2, sum = 3

# total = 1

# def add():
#     total = 3

#     def inner():
#         nonlocal total

#         total += 1
#         print(total)

#     return inner

# a = add()
# a()
# a()
# a()

# class Hamda():
#     def __init__(self, name):
#         self.name = name

#     def __add__(self, other):
#         print("hamdas addition")
#         return Hamda(self.name + other.name)

#     def __mul__(self, other):
#         print("hamdas multiplication")
#         return Hamda(self.name + other.name + self.name + other.name)

#     def __call__(self, *args):
#         print(args)

#     def __str__(self):
#         return "Hamda({})".format(self.name)

#     def __repr__(self):
#         return "Hamda[{}]".format(self.name)

# h1 = Hamda("h1")
# h2 = Hamda("h2")

# print(h1)
# h3 = h1 + h2  # ==> h1.__add__(h2)
# h4 = h1 * h2  # ==> h1.__mul__(h2)

# print(h3.name)
# print(h4.name)
# h1(1, "hello", True)  # ==> h1.__call__(1, "hello", True)