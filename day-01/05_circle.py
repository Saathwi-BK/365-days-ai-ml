#Find the area and circumference of a circle from its radius
radius = float(input("Enter the radius of circle: "))

PI = 3.14
area = PI * radius ** 2
circumference = 2 * PI * radius

print(f"Area of circle: {area:.2f} \nCircumference of circle: {circumference:.2f}")