

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

portion_down_payment = 0.25
down_payment_total = total_cost * portion_down_payment # total amount of down payment cost
current_savings = 0
monthly_salary = annual_salary / 12 # monthly salary calculation
r = .04 # annual rate of return on investment
monthly_savings = monthly_salary * portion_saved # monthly savings using the portion saved
total_months = 0 # total number of months to pay off down payment

while current_savings < down_payment_total:
    current_savings += monthly_savings
    current_savings += current_savings * r/12
    total_months += 1
print("Number of months:",total_months)
