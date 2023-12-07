#!/usr/bin/env python
import sys
import csv

try:
    fname = sys.argv[1]
except IndexError:
    print('Run as ./actionkit-parser [name_of_input_file.csv] [optional_name_of_output_file.csv]', file=sys.stderr)
    sys.exit(1)

try:
    filename = sys.argv[2]
except IndexError:
    filename = 'output.csv'


# todo: if need be, add something to catch international numbers or malformed numbers
def parse_phone(num):
    if len(num) == 10:
        return num
    elif len(num) > 10:
        return num[:10]


header = ['firstname', 'lastname', 'cell']
with open(fname, 'r') as infile, open(filename, 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    next(reader)  # skip the header
    writer.writerow(header)  # add our header
    for row in reader:
        if row[5] == 'TRUE':  # skip anyone who is p2ptext_optout
            continue
        first = row[0]
        last = row[2]
        if row[7]:  # if they filled in the mobile number field, use that
            cell = row[7]
        else:
            cell = row[6]  # otherwise, use the "best_phone" field
        cell = parse_phone(cell)
        if cell:
            writer.writerow([first, last, cell])


