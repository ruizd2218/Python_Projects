import sqlite3 as sql

specimen = (('Jean-Baptiste Zorg', 'Human', 122), ('Korben Dallas', 'Meat Popsicle', 100), ('Ak\'not', 'Mangalore', -5) )

with sql.connect(r"C:\Users\Diego\Documents\GitHub\Python_Projects\SQLITE\pro1\pydb1.db") as connection:
    c = connection.cursor()
    c.execute("CREATE TABLE tbl(FirstName TEXT, Species TEXT, IQ INT)")
    c.executemany("INSERT INTO tbl VALUES (?,?,?)", specimen)

with sql.connect('pydb1.db'):
    c = connection.cursor()
    c.execute("UPDATE tbl SET species = 'Human' WHERE 'Meat Popsicle' ")
    
