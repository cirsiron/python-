

# def f(x, y):
#     return x + y

# sun = reduce(f, [1, 2, 3], 100) # 100是初始值

# print(sun)
###################################
# def mul(x, y):
#     return x * y

# m = reduce(mul, [1,2,3,4], 100)
# print(m)

###################################

# def pingfang(x):
#     return math.sqrt(x) % 1 == 0

# a = list(filter(pingfang, range(1, 101)))

# print(a)

############################
# print( sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower) )

###############################

# def cacl_prod():
#     def prod(x, y):
#         return x * y

#     def mul(lis):
#         return reduce(prod, lis)
#     return mul

# a = cacl_prod()

# print(a([1,2,3]))

################

# def closelur():
#     ls = []
#     for i in range(1,4):
#         def f(j):
#             def g():
#                 print(j)
#             return g
#         ls.append(f(i))
#     return ls

# for key in closelur():
#     key()

#################

#装饰器

# def f1(n):
#     return reduce(lambda x,y: x*y, range(1, n+1))


# class Fn(object):
#     hobby = "play"
#     def __init__(self, name, age, weight):
#         self.name = name
#         self.age = age
#         self.__weight = weight
    
#     @property
#     def get_weight(self):
#         return self.__weight
#     @classmethod
#     def clsmethod(clss):
#         return clss.hobby

#     def self_ins(self):
#         print("my name is %s" % (self.name))

# class BackEnd(Fn):
#     def __init__(self, name, age, weight, lg):
#         super(BackEnd, self).__init__(name, age, weight)
#         self.lg = lg
#     def self_ins(self):
#         print("my name is %s" %(self.name))

# def introduce(pa):
#     if isinstance(pa, Fn):
#         pa.self_ins()
# if __name__ == '__main__':
#     ff = Fn("rose", 17, "11")
#     f = BackEnd("jack", 18, "22", "eg")

#     introduce(f)
#     introduce(ff)
    # print(dir(f))
    # print(f.__dict__)
    # print(Fn.clsmethod())
    # print(type(f))
    # print(f.get_weight)
    # print(isinstance(f, BackEnd))
    # f.self_ins()

#
# 
# #
#     def __new__(cls, *args, **kwargs):
#         return super(Fn, cls).__new__(cls, *args, **kwargs)
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def get_age(self):
#         print(self.age)

# if __name__ == "__main__":
#     f = Fn("jack", 100)
#     print(f.__dict__)

# class Pro(object):
#     def __init__(self, age):
#         self.age = age

#     def __eq__(self, other):
#         if isinstance(other, Pro):
#             if self.age == other.age:
#                 return True
#             else:
#                 return False
#         else:
#             raise Exception("the type of object must be Pro")
#     def __add__(self, other):
#         if isinstance(other, Pro):
#             return other.age + self.age
#         else:
#             raise Exception("the type of object must be Pro")


# if __name__ == "__main__":
#     p1 = Pro(12)
#     p2 = Pro(13)

#     print(p1 == p2)
#     print(p1 + p2)

# class Pro(object):
#     def __init__(self, age):
#         self.age = age
#     def getattribute(self, age):
#         return super(Pro, self).__getattribute__(age)
#     def setattr(self, age, value):
#         self.__dict__[age] = value

# if __name__ == "__main__":
#     p = Pro(23)
#     print(p.age)

class Person(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_grade(self):
        if self.__score > 90:
            return "A"
        elif self.__score > 80:
            return "B"
        else:
            return "C"

p1 = Person('Bob', 90)
p2 = Person('Alice', 65)
p3 = Person('Tim', 48)

print (p1.get_grade())
print (p2.get_grade())
print (p3.get_grade())
