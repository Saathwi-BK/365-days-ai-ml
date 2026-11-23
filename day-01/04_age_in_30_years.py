#Take a name and age, then print "Hi X, you will be 30 in Y years"
user_name = input("Enter your name: ").strip().title()
age = int(input("Enter your age: "))

years_left = 30 - age

print(f"Hi {user_name}, you will be 30 in {years_left} years")