meters = float(input("Input distance (meters): "))
hr = float(input("Input time (hours): "))
min = float(input("Input time (minutes): "))
sec = float(input("Input time (seconds): "))
hr_total = hr + (min / 60) + ((sec / 60) / 60)
sec_total = ((hr * 60) * 60) + (min * 60) + sec
kms = meters / 1000
miles = meters / 1609.344
print("Your speed in meters/sec is:", meters / sec_total)
print("Your speed in km/h is: ", kms / hr_total)
print("Your speed in miles/h is: ", miles / hr_total)
