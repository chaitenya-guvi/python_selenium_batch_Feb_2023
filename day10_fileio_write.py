# You can also use open to write to a file
# Need to specify the "w" flag as the second argument
# r - Read a file (no writing) - this is the default
# w - Write to a file (previous contents removed)
# a - Append to a file (previous contents not removed)


filename = 'data/haiku.txt'


with open(filename, "x") as file:
    file.write("Writing files is great\n")
    file.write("Here's another line of text\n")
    file.write("Closing now, goodbye!!222222@@@@@@@!")