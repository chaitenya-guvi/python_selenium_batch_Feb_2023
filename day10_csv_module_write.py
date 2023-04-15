# writer - creates a writer object for writing to CSV
# writerow - method on a writer to write a row to the CSV



from csv import writer
with open("fighters.csv", "w") as file:
    csv_writer = writer(file)
    csv_writer.writerow(["Character", "Move"])
    csv_writer.writerow(["Ryu", "Hadouken"])