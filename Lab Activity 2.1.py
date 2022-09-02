month_31 =['January','March', 'May', 'July', 'August', 'October', 'December']
month_28_29 =['February']
month_30 =['April', 'June', 'September', 'November']
birth_month= input("Which month would you like to know the length of? ")
if birth_month in month_31:
    print("There are 31 days in",birth_month + ".")
elif birth_month in month_30:
    print("There are 30 days in",birth_month + ".")
elif birth_month in month_28_29:
    print("There are 28 days in February, or 29 days on a leap year.")
