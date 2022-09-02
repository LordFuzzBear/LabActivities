Sum = 0
print("Please enter 10 numbers\n")
for i in range (1,11):
    num = int(input("Number %d = " %i))
    Sum = Sum + num

avg = Sum / 10

print("The sum of these numbers equals:", Sum)
print("The average of these numbers equals:", avg)
