price1=float(input("Enter the price of product one: "))
price2=float(input("Enter the price of product two: "))

total_bill = price1 + price2

tip_percentage = float(input("Enter tip percentage: "))

tip = total_bill * ( tip_percentage / 100)
final_bill = total_bill + tip

print(f"Bill: {total_bill}\nTip: {tip:.2f}\nTotal amount is {final_bill:.2f}")