# CSV
import csv

with open('data.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row[0], row[1], row[2], sep="| ")
