import sqlite3

conn = sqlite3.connect("test.db")
print("Opened database successfully")

conn.execute("INSERT INTO EMPLOYEES VALUES(11, 'FAITH',23,13400.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (12,'ENOX',56,41300.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES(13,'MUSYOKA',24,12000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES(14,'ALICE',37,44000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES(15,'KANINI',40,45000.00)")


conn.commit()
print("Records inserted successfully")
conn.close()