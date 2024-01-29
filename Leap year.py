year = int(input("Enter a year u wanna check:  "))
def check_leap_year(year):
    return year % 400 == 0 or year % 4 == 0 and year % 100 != 0

if check_leap_year(year) == True:
    print ("its a leap year")
else:
    print ("its a not leap year")

