import csv
from email import header

data_set1 = []
data_set2 = []

with open("final.csv", "r") as ds1:
    csv_reader = csv.reader(ds1)
    for row in csv_reader:
        data_set1.append(row)

with open("sorted1.csv", "r") as ds2:
    csv_reader = csv.reader(ds2)
    for row in csv_reader:
        data_set2.append(row)
headers = data_set1[0]
planet_data1 = data_set1[1:]
headers1 = data_set2[0]
planet_data2 = data_set2[1:]

ff = headers + headers1
dataData = []
for idx,  data in enumerate(planet_data1):
    dataData.append(planet_data1[idx]+planet_data2[idx])

with open("merged.csv", "a+") as final:
    csvWriter = csv.writer(final)
    csvWriter.writerow(ff)
    csvWriter.writerows(dataData)

with open("sorted1.csv")as input, open("sorted1.csv", "w", newline="") as f:
    writer = csv.writer(f)
    for row in csv.reader(input):
        if any(field.strip() for field in row):
            writer.writerow(row)