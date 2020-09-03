import sqlite3 as s

print("Welcome to the Games database.")
print("We have twenty different games, with information such as \nName, Description, Developer, Price, Release Date and Star Rating.\n")
print("Type help if you are stuck.....")

def db_action(sql, data=None):
  conn = s.connect("GameDatabase.db")
  c = conn.cursor()
  if data == None:
    c.execute(sql)
  else:
    c.execute(sql, data)
  result = c.fetchall()
  conn.commit()
  conn.close()
  return result

def insertGame(name, dis, dev, price, reldate, stars):
    return db_action("""INSERT INTO Games
(name, discription,developer, price,release_date, star_rating)

VALUES

(?, ?, ?, ?, ?, ?)
""", (name, dis, dev, price, reldate, stars))

def update(change, column, change_to):
    db_action("UPDATE Games SET {} = {} WHERE name = {}".format(column, change_to, change))

def delete(x):
    q = input("Are you sure you want to delete "+x+"? (y/n)")
    if q == "y":
      db_action("DELETE FROM Games WHERE name = ?", (x,))
      print("-----------------------------\n")
      main()
    if q == "n":
      print("-----------------------------\n")
      main()
    else:
      delete(x)


def getinfo(query, attributes):
    l = []
    for attribute in attributes:
      
      l.append(db_action("SELECT "+attribute+" FROM Games WHERE name = (?)", (query,)))
    
    return l

def main():
    try:
      x = input("Please Enter Command: ")

      if x[0:7] == "search " and x[7:12] == "name ":
          print("Price: \n"+str(getinfo(x[12:], ["name"])[0][0][0])+"\n")

      elif x[0:7] == "search " and x[7:19] == "discription ":
          print("Discription: \n"+str(getinfo(x[19:], ["discription"])[0][0][0])+"\n")

      elif x[0:7] == "search " and x[7:17] == "developer ":
          print("Developer: \n"+str(getinfo(x[17:], ["developer"])[0][0][0])+"\n")
          
      elif x[0:7] == "search " and x[7:20] == "release date ":
          print("Release Date: \n"+str(getinfo(x[20:], ["release_date"])[0][0][0])+"\n")

      elif x[0:7] == "search " and x[7:13] == "price ":
          print("Price: \n"+str(getinfo(x[13:], ["price"])[0][0][0])+"\n")
          
      elif x[0:7] == "search " and x[7:13] == "stars ":
          print("Price: \n"+str(getinfo(x[13:], ["star_rating"])[0][0][0])+"\n")
      
      elif x[0:7] == "search ":
          q = getinfo(x[7:], ["name", "discription", "developer", "price", "release_date", "star_rating"])
          print("\nName: "+q[0][0][0]+"\n")
          print("Discription: \n"+q[1][0][0]+"\n")
          print("Developer: \n"+q[2][0][0]+"\n")
          print("Price: \n"+str(q[3][0][0])+"\n")
          print("Release Date: \n"+q[4][0][0]+"\n")
          print("Star Rating: \n"+str(q[5][0][0])+"\n")
          
      elif x[0:7] == "listall":
          t = db_action("SELECT * FROM Games")
          print("All Data In Table:\n")
          print(t)

      elif x[0:9] == "new game":
          insertGame(input("Name: "), input("Discription: "), input("developer: "), input("Price: "), input("Release Date: "), input("Star Rating: "))

      elif x[0:7] == "update":
          n = input("Name: ")
          c = input("Column: ")
          ct = input("Change Column To: ")
          
          db_action("UPDATE Games SET " + c + " = ? WHERE name = ?", (ct, n))

      elif x[0:7] == "delete":
          a = input("Name Of Game To Delete: ")
          delete(a)

      elif x[0:5] == "help":
          print("""SQLite with Python Database

The script allows commands to be run to search and add enterys to the database.

Commands:

The search command gets info about a game:

Example - |search Minecraft

It also allows for specific info by puting the attribute after:

Example - |search price Minecraft

There is also a listall command that dumps the databse text:

Example - |listall

In order to add a new item to the database there is a new game command that will query the user for all the relevent attributes:

Example - |new game

Name: ...

To update an attribute you the user types update and will then be prompted to input data about what they want to update

Example - |update

Name:...

Column:...

Change To:...

And there is also a delete items feature by typing delete which will prompt the user

Example - |delete

Name:...""")
          
      else:
          print("Unrecognized, Command")
    except:
      print("Unrecognized, Command")


    print("-----------------------------\n")
    
    main()
        
    
if __name__ == "__main__":
    main()
