# input method  - always string
# conditions - if elif else ,multiple elif , nested if , continue pass
# false  - 0 , empty strings , None

# name = input("Please share your name : ")
# age = input("Please share your age : ")
#
# print("You had input your name as " + name + " and age as : {}".format(age))
# print(type(age))
# age = int(age)
# print(type(age))


# flow control , conditional
"""
if some condition is True :
    execute the python code
elif some other condition is True :
    execute the python code
# else :
#     execute the python code
# """
# #
# # age = input("Please share your age : ")
# age = 92 # assignment operator
# if age > 18:
#     print("You are an adult . ")
# #     print("thsnk you for attending .")
# elif age < 18 :
#     print("You are not an adult yet . ")
# elif age == 18 :
#     print("congratulations you are 18 year old . ")
#
# print("\nyou are at end of program .") # outside of condition block


"""
if
age is 
0-2 : no entry is allowed
3 - 18  : ticket price is rs 50 
18-65 : ticket price is rs 100
65 : free ticket for you 

"""
zoo_age = input("please input your age : ")
zoo_age = int(zoo_age)

if (zoo_age>= 0) and (zoo_age <=2) :
    print("You are not allowed entry in the zoo . ")
elif (zoo_age >= 3) and  (zoo_age <= 18) :
    print("the ticket price is rs 50 for you .")
elif (zoo_age > 18) and  (zoo_age <= 65) :
    print("the ticket price is rs 100 for you .")
elif (zoo_age > 65) :
    print("You are allowed free entry in the Zoo!!!!!")

#

#Excercise  check wheteher a number is even or odd and print the number and whether it is even or odd