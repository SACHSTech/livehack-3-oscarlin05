"""
------------------------------------------------------------------------------
Name:   problem2.py
Purpose:  a program that calculates the amount of days travelled to pass 100km and the average km per day.
 
Author: Lin.O
 
Created: 03/03/2021
------------------------------------------------------------------------------
"""
#title 
print("***** Welcome to the DoorDash Distance Tracker ******")

#variables 
total = 0
number = 0 

#looping calculation and number of days taken to surpass 100 km
while total <= 100:
  distance = int(input("Enter the distance travelled for the day: "))
  total += distance 
  number += 1
print("It took", number, "days to surpass 100km driven.")

#average km per day 
average = round(total / number)
print("The average distance driven per day is", average, "km.")