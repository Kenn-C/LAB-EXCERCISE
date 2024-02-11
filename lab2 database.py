import sqlite3


con = sqlite3.connect("ACCOUNTS.db")

c = con.cursor()
#c.execute("CREATE TABLE Accounts(id INTEGER PRIMARY KEY , name text, age text, birthday text, religion text, course text, gender text, address text)")
c.execute("SELECT * FROM Accounts")

for i in c.fetchall():
    print(i)
con.commit()
con.close()
