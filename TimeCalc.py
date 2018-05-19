import datetime
from datetime import timedelta

# intro
print("Welcome to TimeCalc"
      "Calculating Durations")

clear = True
while clear == True:
    # first input
    firstNumber = True
    while firstNumber == True:
        time_1 = input("Please enter a time [hh:mm:ss] including 0s: ")
        if len(time_1) >= 8 and time_1[-6] == ":" and time_1[-3] == ":" and int(time_1[-5:-3]) < 60 and int(time_1[-2:]) < 60:
            hours_1 = time_1[:-6]
            minutes_1 = time_1[-5:-3]
            seconds_1 = time_1[-2:]
            hours_1 = int(hours_1)
            minutes_1 = int(minutes_1)
            seconds_1 = int(seconds_1)
            firstNumber = False
        else:
            print("Invalid Syntax")
    time_1 = datetime.timedelta(hours=hours_1, minutes=minutes_1, seconds=seconds_1)

    cont = True
    while cont == True:
        # second input
        secondNumber = True
        while secondNumber == True:
            time_2 = input("Please enter a time to add [hh:mm:ss] including 0s: ")
            if len(time_2) >= 8 and time_2[-6] == ":" and time_2[-3] == ":" and int(time_2[-5:-3]) < 60 and int(time_2[-2:]) < 60:
                hours_2 = time_2[:-6]
                minutes_2 = time_2[-5:-3]
                seconds_2 = time_2[-2:]
                hours_2 = int(hours_2)
                minutes_2 = int(minutes_2)
                seconds_2 = int(seconds_2)
                secondNumber = False
            else:
                print("Invalid Syntax")
        time_2 = datetime.timedelta(hours = hours_2, minutes = minutes_2, seconds = seconds_2)

        total = time_1 + time_2
        print("The total duration is: " + str(total))

        # continue, clear, or exit
        options = True
        while options == True:
            choice = input("Continue: Y | Clear: N | Exit: X: ")
            if choice == "Y" or choice == "y":
                time_1 = total
                options = False
            elif choice == "N" or choice == "n":
                cont = False
                options = False
            elif choice == "X" or choice == "x":
                quit()
            else:
                print("Invalid Syntax")