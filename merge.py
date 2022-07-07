import csv
from dataclasses import field

data = []
with open("archive_dataset.csv", "r") as ds2:
    csv_reader = csv.reader(ds2)
    for row in csv_reader:
        data.append(row)

headers = data[0]
planet_data = data[1:]
for data in planet_data:
    data[2] = data[2].lower()
planet_data.sort(key=lambda planet_data:planet_data[2])

with open("sorted.csv", "a+")as s:
    csvWriter =csv.writer(s)
    csvWriter.writerow(headers)
    csvWriter.writerows(planet_data)

with open("merged.csv")as input, open("completed.csv", "w", newline="") as f:
    writer = csv.writer(f)
    for row in csv.reader(input):
        if any(field.strip() for field in row):
            writer.writerow(row)