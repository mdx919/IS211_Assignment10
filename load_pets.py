import sqlite3 as lite
import sys

con = None

try:
    con = lite.connect('pets.db')
    cur = con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS person (id integer PRIMARY KEY, first_name TEST, last_name TEXT, age INTEGER)")
    cur.execute("CREATE TABLE IF NOT EXISTS pet (id INTEGER PRIMARY KEY, name TEXT, breed TEXT, age INTEGER, dead INTEGER)")
    cur.execute("CREATE TABLE IF NOT EXISTS person_pet (person_id integer, pet_id INTEGER)")

    cur.execute("INSERT INTO person VALUES(1,'James','Smith',41)")
    cur.execute("INSERT INTO person VALUES(2,'Diana','Greene',23)")
    cur.execute("INSERT INTO person VALUES(3, 'Sara','White',27)")
    cur.execute("INSERT INTO person VALUES(4,'William','Gibson',23)")

    cur.execute("INSERT INTO pet VALUES(1,'Rusty','Dalmation',4,1)")
    cur.execute("INSERT INTO pet VALUES(2,'Bella','AlaskanMalamute',3,0)")
    cur.execute("INSERT INTO pet VALUES(3,'Max','CockerSpaniel',1,0)")
    cur.execute("INSERT INTO pet VALUES(4,'Rocky','Beagle',7,0)")
    cur.execute("INSERT INTO pet VALUES(5,'Rufus','CockerSpaniel',1,0)")
    cur.execute("INSERT INTO pet VALUES(6,'Spot','Bloodhound',2,1)")

    cur.execute("INSERT INTO person_pet VALUES(1,1)")
    cur.execute("INSERT INTO person_pet VALUES(1,2)")
    cur.execute("INSERT INTO person_pet VALUES(2,3)")
    cur.execute("INSERT INTO person_pet VALUES(2,4)")
    cur.execute("INSERT INTO person_pet VALUES(3,5)")
    cur.execute("INSERT INTO person_pet VALUES(4,6)")

    con.commit()

except lite.Error as e:
    print("Error {}:".format(e.args[0]))
    sys.exit(1)

finally:
    if con:
        con.close()

