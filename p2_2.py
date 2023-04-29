import datetime
# input date of birth
born = input("Enter your date of birth in YYYY/MM/DD format: ").split("/")
born = [int(i) for i in born]

# check if input is valid
if born[0] < 2023 and born[0] > 1900 and born[1] < 13 and born[1] > 0 and born[2] > 0 and born[2] < 32:
    x = datetime.date(born[0], born[1], born[2])
    y = datetime.date.today()
    z = y - x
    z= int(z.days // 365.25)
    print("Your age is", z ,"years.")
else:
    print("Invalid input. Please enter a valid date of birth between 1900 and 2023.")
