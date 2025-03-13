import fdb

def print_table_names():
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

    con.close()

def print_cw_attributes():
    con = fdb.connect(
        host='cw-firebird-db',
        database='/firebird/data/CONTENT_3D.FDB',
        user='sysdba',
        password='masterkey'
    )

    cur = con.cursor()

    cur.execute("SELECT * FROM CW_EXTERNAL_PROJECT_DATA")

    attributes = cur.fetchall()
    if len(attributes) == 0:
        print("No external project data found")
        return
    for attribute in attributes:
        print(attribute)

    con.close()

if __name__ == '__main__':
    print_table_names()
    print_cw_attributes()
