import sqlite3

class Database:
    
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("Create Table If Not Exists book (id Integer Primary Key, title Text, author Text, year Integer, isbn Integer)")
        self.conn.commit()

    def insert(self,title,author,year,isbn):
        self.cur.execute("Insert Into book Values(Null,?,?,?,?)", (title,author,year,isbn))
        self.conn.commit()

    def view(self):
        self.cur.execute("Select * From book")
        rows=self.cur.fetchall()
        return rows

    #pass an empty string into the function
    def search(self,title="",author="",year="",isbn=""):
        self.cur.execute("Select * From book Where title=? Or author=? Or year=? Or isbn=?", (title,author,year,isbn))
        rows=self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("Delete From book Where id=?",(id,))
        self.conn.commit()

    def update(self,id,title,author,year,isbn):
        self.cur.execute("Update book Set title=?, author=?, year=?, isbn=? Where id=?", (title,author,year,isbn,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

#connect()
#insert("The earth", "John Tablet", 1990, 9103419203432)
#delete(2)
#update(1,"The moon", "John Simth", 1971, 9193819203444)
#print(view())
#print(search(author="John Tablet"))