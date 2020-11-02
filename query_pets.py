import sqlite3 as lite
import sys

con = None

try:
    con = lite.connect('pets.db')
    cur = con.cursor()

    if con:
        while True:
            user_id = input("Type in the user id or -1 to exit:  ")

            if user_id == -1:
                sys.exit()
            else:
                if not user_id.isdigit():
                    print('Please type an Integer! or -1 to exit')
                else:
                    cur.execute("SELECT * FROM person")
                    persons = cur.fetchall()
                    for person in persons:
                        if person[0] == int(user_id):
                            print('{} {}, {} years old'.format(person[1], person[2], person[3]))
                            pets_id = []
                            cur.execute("SELECT * FROM person_pet")
                            person_pets = cur.fetchall()
                            for person_pet in person_pets:
                                if person_pet[0] == int(user_id):
                                    pets_id.append(person_pet[1])
                            cur.execute("SELECT * FROM pet")
                            pets = cur.fetchall()
                            for pet in pets:
                                if pet[0] in pets_id:
                                    print('{} {} owned {}, a {}, that was {} years old.'.format(person[1], person[2], pet[1], pet[2], pet[3]))
                            break
                        if person[0] == len(persons):
                            print('No user with that id exists')

except lite.Error as e:
    print("Error {}:".format(e.args[0]))
    sys.exit(1)

finally:
    if con:
        con.close()
