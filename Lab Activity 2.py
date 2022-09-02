month = input("Which month would you like to know the length of? ")
if month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month == "December":
    print("There are 31 days in",month + ".")
elif month == "April" or month == "June" or month == "September" or month == "November":
    print("There are 30 days in",month + ".")
elif month == "February":
    print("There are 28 days in February, or 29 days on a leap year.")
