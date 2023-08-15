

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semiannual raise, as a decimal: "))

portion_down_payment = float(0.25*total_cost)                                        # the total down payment
current_savings = 0
monthly_savings = float(portion_saved*annual_salary/12)                              # monthly savings using the portion saved

r = .04                                                                              # annual rate of return on investment
total_months = 0                                                                     # total number of months to pay off down payment

while current_savings < portion_down_payment:
    if total_months % 6 == 0 and total_months != 0:                                  # checking for every 6 months to add the semi annual raise to the annual salary
        annual_salary += (annual_salary * semi_annual_raise)                                                             
    current_savings += (annual_salary * portion_saved/12) + (current_savings * r/12) # adding the monthly portion saved and the return on investment every month
    total_months += 1                                                                # adding a month for each iteration of the while loop
print("Number of months:",total_months)