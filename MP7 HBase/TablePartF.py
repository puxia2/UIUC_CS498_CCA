import happybase as hb

# DON'T CHANGE THE PRINT FORMAT, WHICH IS THE OUTPUT
# OR YOU WON'T RECEIVE POINTS FROM THE GRADER
connection = hb.Connection()
connection.open()
table = connection.table('powers')

for key, row in table.scan():
    color = row[b'custom:color']
    name = row[b'professional:name']
    power = row[b'personal:power']
    for key, row1 in table.scan():
        color1 = row1[b'custom:color']
        name1 = row1[b'professional:name']
        power1 = row1[b'personal:power']
        if color == color1 and name != name1:
            print('{}, {}, {}, {}, {}'.format(name, power, name1, power1, color))

connection.close()
