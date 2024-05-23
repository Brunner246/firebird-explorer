import fdb

con = fdb.connect(
    host='cw-firebird-db', 
    database='/firebird/data/CONTENT_3D.FDB',
    user='sysdba',
    password='masterkey'
)

cur = con.cursor()

cur.execute("SELECT RDB$RELATION_NAME FROM RDB$RELATIONS WHERE RDB$RELATION_TYPE = 0 AND RDB$SYSTEM_FLAG = 0")

tables = cur.fetchall()
for table in tables:
    print(table[0].strip())

# Schließe die Verbindung
con.close()



# import fdb
#
# con = fdb.connect(
#     dsn='localhost/3050:/firebird/data/test.fdb',
#     user='SYSDBA',
#     password='dein_passwort'
# )
#
# cur = con.cursor()
# cur.execute("SELECT * FROM my_table")
# for row in cur.fetchall():
#     print(row)
#
# con.close()
