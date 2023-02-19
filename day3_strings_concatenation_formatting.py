# # concatenation  -  using the + operator
# # formatting -
# # indexes
# # assignment operator - += . -= , *=
# # type casting -  string to int , float to int , int to float
#
string1 = "hello"
firstname = "alameen"
secondname = "good morning"
#
greeting_name = string1 +' ' +  firstname + "," + secondname # added three strings here
# greeting_name = f"line 11 :  {string1} {name}"
# greeting_name2 = "line 12 : {} {}".format(string1,name)
# greeting_name3 = "line 13 : {1} {0}".format(string1,name)


print(string1 , firstname, secondname)
print(greeting_name)
# print(greeting_name2)
# print(greeting_name3)
#
# first = "ice"
# second = " cream"
# print("The original vaue  : " + first , "The second value is : " + second )  # string concatenation
#
#
# first += second  #assignment operator ,just add second to the first variabel on the left
# first = first + second   # same syntax as above
# print("The updated  value is  : " + first)
#
# third = 3  # integer variable
# print("I have had " + third + first)   # TypeError: can only concatenate str (not "int") to str
# print("I have had " + str(third) + first)  # No error , integer variable is type casted to a string variable

# Formatting :
age = 22.5
firstname = "chaitenya"
lastname = "kumar"


print("Hello My name is " + firstname + " " + lastname + " and my age is : " + str(age) ) # string concatenation + type casting

print(f"Hello My name is {firstname} {lastname} and my age is : {age} ") # f strings

print("Hello My name is {} {} and my age is : {} ".format(firstname,lastname,age)) # format method



# indexes  :

string1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"   # 26 characters
# starts at 0
# Last position is -1

print(string1[0])
print(string1[-1])

string2 = "123456789"
print(string2[0])
print(string2[-2])



