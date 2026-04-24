# a=10
# b=0
# try:
#     c=a/b
# except:
#     c=0
#     print(c)


# try:
#     a=int(input("Enter number1:"))
#     b=int(input("Enter number2:"))
#     c=a/b
#     print(c)
# except ZeroDivisionError:
#     print("Zero not possible for division")
# except TypeError:
#     print("String not allowed")
# except ValueError:
#     print("avoid string data")
# except:
#     print("error")
# else:
#     print("try block working")
# finally:
#     print("working")
    
# output
# Enter number1:12
# Enter number2:40
# 0.3
# try block working
# working

# age=int(input("Enter your age:"))
# if age <0 or age > 100:
#     raise Exception("This age is not valid")
# print("age:",age)

# class AgeError1(Exception):
#     pass
# try:
#     age=int(input("Enter your age:"))
#     if age <0 or age >100:
#         raise AgeError1("age not valid")
# except AgeError1:
#     print("age between 1 to 100 only allowed")
# except ValueError:
#     print("string not allowed")


# x=True
# while x:
#     choice=input("Enter your choice:")
#     match choice:
#         case'add':
#             a=in

