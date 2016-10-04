# import libraries
import csv

# open csv
with open('Devices.csv', newline='') as csvfile:
    devices = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in devices:
        print(', '.join(row))
