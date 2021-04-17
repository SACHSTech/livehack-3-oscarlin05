"""
------------------------------------------------------------------------------
Name:   problem1.py
Purpose:  a program that calculates wins and losses for your team to find the group you are in. 
 
Author: Lin.O
 
Created: 03/03/2021
------------------------------------------------------------------------------
"""
print("******  Tournament Tracker ******")

#variables 
w = ""
total = 0 

#ask for user input 
for i in range(6):
  games = input("Enter the wins and losses for your team: ").upper()
  if games == "W":
    w += games

#output the group that the user is in 
if len(w) == 5 or len(w) == 6:
  print("Your team is in Group 1")
elif len(w) == 3 or len(w) == 4:
  print("Your team is in Group 2")
elif len(w) == 1 or len(w) == 2:
  print("Your team is in Group 3")
else:
  print("Your team is ELIMINATED!")