# Simple age script

# Type your age
age = int(input("Enter your age: "))

if age <= 12:
	print("It's great to be a kid!")
elif age in range(13, 20):
	print("You're a teenager!")
else:
	print("Time to grow up!")

