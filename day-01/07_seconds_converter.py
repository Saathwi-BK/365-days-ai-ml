#Take seconds as input and convert them to hours, minutes, and seconds (hint: // and %)
total_seconds = int(input("Enter the time in seconds: "))

hours = total_seconds // 3600
remaining = total_seconds % 3600
minutes = remaining // 60
seconds = remaining % 60

print(f"{hours} hours, {minutes} minutes, {seconds} seconds")