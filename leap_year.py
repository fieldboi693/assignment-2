# 2000
# 2008199
# 2004
# 2100 or 1900 not a leap

# year div 400 leap
# year div 4 but not by 100

year= int(input("enter the year:"))
if (year % 400 == 0):
    print(year,"Is leap year")
elif (year % 4 == 0 and year % 100 != 0):
    print(year,"Is leap year")
else:
    print(year,"Is not leap year")