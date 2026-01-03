# Many people keep time using a 24-hour clock (11 is 11am and 23 is 11pm, 0 is midnight).
# If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm).
# Write a Python program to solve the general version of the above problem.
# Ask the user for the time now (in hours) and then ask for the number of hours to wait for the alarm.
# Your program should output what the time will be on a 24-hour clock when the alarm goes off.

if __name__ == '__main__':

    # Ask the user for the current time (in hours)
    currentTime = int(input("Enter the current time in hours in 24 hour format (0-23): "))

    if not (0 < currentTime < 24): raise ValueError("Invalid current time: " + str(currentTime))

    # Ask the user for the number of hours to wait for the alarm
    waitHours = int(input("Enter the number of hours to wait for the alarm: "))

    if not (waitHours > 0): raise ValueError("Invalid wait time: " + str(waitHours))

    # Calculate the alarm time
    alarmTime = (currentTime + waitHours) % 24

    print("Alarm Time :", alarmTime)
