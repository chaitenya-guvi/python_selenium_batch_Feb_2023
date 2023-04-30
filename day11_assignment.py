from csv import reader
filename = "data/time.csv"
with open(filename) as fileobj:
    csv_reader = reader(fileobj)
    print(csv_reader)
    with open("data/time1.txt", "a") as time:
        for row in csv_reader:
            time.write(f'The 12 hour format is - {row[0]} and the 24 hour format is - {row[1]}\n')
