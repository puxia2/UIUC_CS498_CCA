import happybase as hb

connection = hb.Connection()
# before first use
connection.open()

# Delete prior created tables
tables = connection.tables()
for tab in tables:
    connection.delete_table(tab, disable=True)

connection.create_table(
    'powers',
    {'personal': dict(),
     'professional': dict(),
     'custom': dict(),
    }
)

connection.create_table(
    'food',
    {'nutrition': dict(),
     'taste': dict(),
    }
)
