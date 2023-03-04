# ex 2 :  function to multiply three numbers

a = 1
b = 2
c = 3

def function1():
    """
    does not have any parameters
    :return:
    """
    return a * b * c

print(f"The output of function 1 is  :   {function1()} ")  # calling the function 1 i.e

def function2(number1, number2, number3):
    """

    :param number1:
    :param number2:
    :param number3:
    :return: multiply 3 numbers
    """
    return number1 * number2 * number3

print(f"The output of function 2 with arguments is  :   {function2(1, 2, 3)}")  # calling the function 1 i.e
# calling the function 2 with keyword arguments
print(f"The output of function 2 with arguments is  :   {function2(number1=1, number2=2, number3=3)}")

multiply_3 = lambda x, y, z: x * y * z

print(f"the output of lambda is : {multiply_3(a, b, c)}")
# excercise 4 :
# Sample List : [1,2,6,6,3,3,3,3,4,5]
# Unique List : [1, 2, 6, 3, 4, 5]


