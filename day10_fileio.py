# Reading Files
# You can read a file with the open function
# open returns a file object to you
# # You can read a file object with the read method
# To read only part of a file, pass a number of characters into read, or use readline
# To get a list of all lines, use readlines

filename = 'data/story.txt'



# ###########closing
# You can close a file with the close method
# Once closed, a file can't be read again
# Always close files - it frees up system resources!

# Option 1 - \
# file = open(filename,'r')
# print(type(file))
# print(f"First time : "+ file.read())
# print(f"second  time : "+ file.read())
# file.close()
#
# print(file.closed)
#



#
# print(file.closed)   # True

# # Option 2 - \
# Context manager
with open(filename,'r') as file2:
    print(file2.read())

print(file2.closed)


