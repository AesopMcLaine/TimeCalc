import datetime
from datetime import timedelta

# intro
print("Welcome to TimeCalc")
print("-------------------")

print("Calculating Durations")
print("-------------------")

clear = 0
while clear == 0:
    # first input
    firstNumber = 0
    while firstNumber == 0:
        time_1 = input("Please enter a time (hh:mm:ss) including 0s): ")
        if len(time_1) > 0 and len(time_1) >= 8 and time_1[-6] == ":" and time_1[-3] == ":" and int(time_1[-5:-3]) < 60 and int(time_1[-2:]) < 60:
            hours_1 = time_1[:-6]
            minutes_1 = time_1[-5:-3]
            seconds_1 = time_1[-2:]
            hours_1 = int(hours_1)
            minutes_1 = int(minutes_1)
            seconds_1 = int(seconds_1)
            print("You entered: " + time_1)
            print(str(hours_1) + " hours, " + str(minutes_1) + " minutes, and " + str(seconds_1) + " seconds.")
            firstNumber += 1
        else:
            print("Invalid Syntax")
            print("-------------------")

    print("-------------------")
    cont = 0
    while cont == 0:
        # seconds input
        secondNumber = 0
        while secondNumber == 0:
            time_2 = input("Please enter a time to add (hh:mm:ss) including zeroes: ")
            if len(time_2) > 0 and len(time_2) >= 8 and time_2[-6] == ":" and time_2[-3] == ":" and int(time_2[-5:-3]) < 60 and int(time_2[-2:]) < 60:
                hours_2 = time_2[:-6]
                minutes_2 = time_2[-5:-3]
                seconds_2 = time_2[-2:]
                hours_2 = int(hours_2)
                minutes_2 = int(minutes_2)
                seconds_2 = int(seconds_2)
                print("You entered: " + time_2)
                print(str(hours_2) + " hours, " + str(minutes_2) + " minutes, and " + str(seconds_2) + " seconds.")
                secondNumber += 1
            else:
                print("Invalid Syntax")
                print("-------------------")

        time_1 = datetime.timedelta(hours = hours_1, minutes = minutes_1, seconds = seconds_1)
        time_2 = datetime.timedelta(hours = hours_2, minutes = minutes_2, seconds = seconds_2)

        print("-------------------")
        total = time_1 + time_2
        print("The total duration is: " + str(total))

        # continue, clear, or exit
        choice = input("Continue: Y | Clear: N | Exit: X: ")
        if choice == "Y" or choice == "y":
            time_1 = total
            cont = 0
        elif choice == "N" or choice == "n":
            clear = 0
            cont = 1
        elif choice == "X" or choice == "x":
            quit()
