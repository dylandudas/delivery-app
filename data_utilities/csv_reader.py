import csv

from data_utilities.hash_table import HashTable
from objects.package import Package

# Read package data from CSV file, create, and insert in HASH Table
def csv_reader_packages(csv_file):
    rows = []
    with open(csv_file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            rows.append(row)

    packages = HashTable()

    for row in rows:
        id = int(row[0])
        address = row[1]
        city = row[2]
        state = row[3]
        zip_code = int(row[4])
        deadline = row[5]
        weight = int(row[6])

        new_package = Package(id, address, city, state, zip_code, deadline, weight)
        packages.insert(new_package.id, new_package)

    return packages

# Read distance data from CSV and create a matrix
def csv_reader_distances(csv_file):
    rows = []
    with open(csv_file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            rows.append(row)

    distances = [[0 for _ in range(len(rows))] for _ in range(len(rows))]

    j = 0
    for row in rows:
        for i in range(len(row) - 1):
            distances[j][i] = row[i]
        j += 1

    return distances
