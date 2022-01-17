import sqlite3 as sql

#file list, we will need to append these to our database
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

#creating our database
conn = sql.connect('db222')
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_name TEXT )")
    conn.commit()
conn.close()
        
#here I am connecting to the database and inserting the values of fileList into col_name
conn = sql.connect('db222')
with conn:
    cur=conn.cursor()
    for item in fileList:
       if item.endswith('.txt'): 
          cur.execute("INSERT INTO tbl_files(col_name) VALUES (?)", \
                      (item,) )
          print(item)
    conn.commit()
conn.close()

