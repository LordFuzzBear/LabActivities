temp = input("Enter '1' to convert Celsius to Fahrenheit\nEnter '2' to convert Fahrenheit to Celsius\nEnter '3' to quit: ")
if "1" in temp:
    celsius = float(input("Enter the temperature in Celsius: "))
    fahrenheit = celsius*1.8+32
    print(str(celsius) + "° celsius is equivalent to " + str(fahrenheit) + "° fahrenheit")
elif "2" in temp:
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    celsius = ((fahrenheit - 32) *5 / 9)
    print(str(fahrenheit) + "° Fahrenheit is equivalent to", str(celsius) + "° Celsius")
