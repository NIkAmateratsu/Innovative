import calendar
import time

year = int(input("Input the year : "))
month = int(input("Input the month : "))
cal = calendar.month(year, month)
print ("Here is the calendar:")
print (cal)
print("Today's time is:\n")
print (time.asctime())