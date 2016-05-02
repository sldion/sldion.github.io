import numpy as np
import csv as csv


with open('Matches .csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        print ', '.join(row)
