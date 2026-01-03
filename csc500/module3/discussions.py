# This is a sample Python script.
# It asks user to enter year and month and displays calendar for that month along with holidays
import calendar

if __name__ == '__main__':

    daysOfWeek = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    fixedDateFederalHolidays = {
        "01-01" : "New Year",
        "06-19" : "Juneteenth National Independence Day",
        "07-04" : "Independence Day",
        "12-25" : "Christmas Day"
    }

    #Get year and month
    year = int(input("Enter the year in yyyy format: "))
    month = int(input("Enter the month in digits mm format: "))

    firstDayOfMonth, noOfDaysInMonth = calendar.monthrange(year, month)

    leapYear = ''
    if year % 4 == 0 : leapYear = ' leap'
    print ("\n{} is the First Day of the{} year {} and month {}".format(daysOfWeek[firstDayOfMonth],leapYear,year, calendar.month_name[month]))

    #Print Calendar - White Spaces
    for j in range(0, firstDayOfMonth):
        print("{1:>2} \t {0:<10}".format('',''),end='\t')
    j = firstDayOfMonth

    #Print Calendar
    for i in range(0, noOfDaysInMonth):
        if j>6:
            j=0
            print()
        string1 = str(month).zfill(2)+'-'+str(i+1).zfill(2)
        isHoliday = bool(fixedDateFederalHolidays.get(string1))
        if isHoliday:
            print("\033[91m{1:>2} \t {0:<10}\033[0m".format(daysOfWeek[j], i + 1), end='\t')
        else:
            print("{1:>2} \t {0:<10}".format(daysOfWeek[j], i + 1), end='\t')
        j+=1
