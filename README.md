# SQLite3-Python-Database-Project
SQLite with Python Database

The script allows commands to be run to search and add enterys to the database.

Commands:

The search command gets info about a game:

Example - |search Minecraft

It also allows for specific info by puting the attribute after:

Example - |search price Minecraft

There is also a listall command that dumps the databse text:

Example - |listall

In order to add a new item to the database there is a new game command
that will query the user for all the relevent attributes:

Example - |new game

Name: 
...

To update an attribute you the user types update and will then be prompted
to input data about what they want to update

Example - |update

Name:...

Column:...

Change To:...

And there is also a delete items feature by typing delete which will prompt the user

Example - |delete

Name:...
