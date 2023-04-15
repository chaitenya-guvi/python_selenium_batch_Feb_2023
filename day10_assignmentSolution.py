filename  = 'data/names.txt'

with open(filename) as fileobj :
    filecontent = fileobj.read()

print(filecontent)