import csv
import itertools

with open('list.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line for line in stripped if line)
    grouped = itertools.izip(*[lines] * 8)
    with open('extracted.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('name', 'title', 'bank', 'address', 'city', 'phone', 'fax', 'email'))
        writer.writerows(grouped)