# reader - lets you iterate over rows of the CSV as lists
# DictReader - lets you iterate over rows of the CSV as OrderedDicts
# Keys are determined by the header row
from csv import DictReader,reader
# import csv

filename = 'data/storypicker.csv'
# #
# with open(filename) as file:
#     csv_reader = reader(file)
#     for row in csv_reader:
#         # each row is a list!
#         print(row)
#
#
# print(csv_reader)
# print(type(csv_reader))





with open(filename) as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        # each row is an OrderedDict!
        print(row)



############# Delimeter ####################

# from csv import reader
# with open(filename) as file:
#     csv_reader = reader(file, delimiter="|")
#     for row in csv_reader:
#         # each row is a list!
#         print(row)


############# Writing to csv file  ####################
#
# writer - creates a writer object for writing to CSV
# writerow - method on a writer to write a row to the CSV
