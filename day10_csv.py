filename = 'data/storypicker.csv'

with open(filename) as file:
    # print(file.read())
    # filecontent = file.read()
    filecontentlinewise = file.readlines()
#
# print(filecontent)
# print(type(filecontent))

print(filecontentlinewise)
print(type(filecontentlinewise))