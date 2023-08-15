salary = int(input("Enter the starting salary: "))
total_cost = 1000000
semi_annual_raise = 0.07

portion_down_payment = 0.25 * total_cost
current_savings = 0

number_of_guesses = 0
low = 0
high = 10000

guess = int((low + high) / 2)
guessed_savings_rate = guess / 10000



def savings (current_savings, salary, semi_annual_raise, guessed_savings_rate):
    for number_of_months in range(0, 36):
        if number_of_months % 6 == 0 and number_of_months != 0:
            salary += salary * semi_annual_raise
        current_savings += guessed_savings_rate * salary / 12 + current_savings * 0.04 / 12
    return current_savings

current_savings = savings (0, salary, semi_annual_raise, high/10000)

if current_savings < portion_down_payment:
    print("Unfortunately, it is not possible to pay for the down payment in 36 months.")
else: 
    current_savings = savings (0, salary, semi_annual_raise, guessed_savings_rate)
    number_of_guesses += 1

    while abs(portion_down_payment - current_savings) >= 100:
        if  portion_down_payment > current_savings:
            low = guess
        else:
            high = guess
        guess = int((low + high) / 2)
        guessed_savings_rate = guess / 10000

        current_savings = int(savings (0, salary, semi_annual_raise, guessed_savings_rate))
        number_of_guesses += 1
    print("Best savings rate: " , guessed_savings_rate)
    print("Steps in bisecton search: " , number_of_guesses)

