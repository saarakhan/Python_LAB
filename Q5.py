# To find given year is leap year or not
def checkLeapYear(year):
    if(year % 4 == 0 and year % 100 != 0 or (year % 400 == 0)):
        print(year, "is a Leap Year!")
    else:
        print(year, "is not a leap year")

year = int(input("Enter year to check if its leap year : "))
checkLeapYear(year)