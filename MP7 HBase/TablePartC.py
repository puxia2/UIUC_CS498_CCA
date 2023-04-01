import happybase as hb
import csv

connection = hb.Connection()
connection.open()
table = connection.table('powers')

with open('input.csv') as f:
    rows = list(csv.reader(f, delimiter=' ')) # list of lists, each list is a line
    for row in rows:
        row = row[0].split(',') # ['row1', 'yes', 'fly', 'batman', '100', 'black']
        table.put(row[0], {b'personal:hero': row[1],
                           b'personal:power': row[2],
                           b'professional:name': row[3],
                           b'professional:xp': row[4],
                           b'custom:color': row[5]})
                           
connection.close()