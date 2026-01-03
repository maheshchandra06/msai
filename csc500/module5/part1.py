# Part 1:
# Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years.
# The program should first ask for the number of years. The outer loop will iterate once for each year.
# The inner loop will iterate twelve times, once for each month.
# Each iteration of the inner loop will ask the user for the inches of rainfall for that month.
# After all iterations, the program should display the number of months, the total inches of rainfall,
# and the average rainfall per month for the entire period.
import calendar
from datetime import datetime

if __name__ == '__main__':
    years = int(input("Enter the number of years for rainfall average: "))

    if years < 0 :
        years = -1 * years

    total_rainfall = 0.0
    total_months = 0
    for year in range(1, years+1):
        for month in range (1,13):
            recorded_rainfall = float(
                input(f"Enter the rainfall in inches for {datetime.now().year +1 - year} {calendar.month_name[month]} : "))
            total_rainfall += recorded_rainfall
            total_months += 1

    average_rainfall = total_rainfall / total_months

    print(f"\nTotal number of months: {total_months}")
    print(f"Total inches of rainfall: {total_rainfall:.2f}")
    print(f"Average rainfall per month: {average_rainfall:.2f}")
