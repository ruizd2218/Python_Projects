import sqlite3 as sql
#Managing Databases in Python Practice

conn = sql.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_persons(\
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_email TEXT )")
    conn.commit()
conn.close()

conn = sql.connect('test.db')
with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) values (?,?,?)", \
                ('Bob', 'Smith', 'bsmith@gmail.com') )
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) values (?,?,?)", \
                ('Sarah', 'May', 'smay@gmail.com') )
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) values (?,?,?)", \
                ('Sally', 'Jones', 'sarahjones@gmail.com') )
    conn.commit()
conn.close()

conn = sql.connect('test.db')
with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_fname, col_lname, col_email FROM tbl_persons WHERE col_fname = 'Sarah' ")
    varPerson = cur.fetchall()
    for item in varPerson:
            msg = "First Name: {}\nLast Name: {}\nEmail: {}".format(item[0], item[1], item[2])
    print(msg)
    conn.commit()
conn.close()
