import sqlite3 as s
from tkinter import *

window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('350x200')

lbl = Label(window, text="Hello")

lbl.grid(column=0, row=0)

def clicked():

    lbl.configure(text="Button was clicked !!")

btn = Button(window, text="Click Me", command=clicked)

btn.grid(column=1, row=0)

window.mainloop()

print("Welcome to the Games database.")
print("We have twenty different games, with infomation such as \nName, Discription, Developer, Price, Release Date and Star Rating.\n")
print("To search for a game please type 'search ' followed by the \nname of the game.\n")


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
          t = db_action("SELECT (name, discription, developer, price, release_date, star_rating) FROM Games")
          print("All Data In Table:\n")
          print(t)

      elif x[0:8] == "new game":
          insertGame(input("Name: "), input("Discription: "), input("developer: "), input("Price: "), input("Release Date: "), input("Star Rating: "))
          
      else:
          print("Unrecognized, Command")


      print("-----------------------------\n")
      
      main()
    except:
      print("RIP")
      main()
        
    
if __name__ == "__main__":
    main()

window.mainloop()

