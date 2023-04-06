import math

# Setting the variables outside of the loop as I was getting undefined variables
# error when I only had them inside the loop, even though the code still ran the
# yellow underlinings were off putting so I spent time figuring it out.

investment_amount = 0
interest_rate = 0
year_amount = 0
month_amount = 0
interest_type = ""

# Explaining the options to the user
print("Investment - to calculate the amount of interest you'll earn on your investment")
print("Bond - to calculate the amount you'll have to pay on a home loan")
print("\n")

# Ask user to choose investment or bond
while True:
    choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

    # Calculate bond repayment amount if user chose bond
    if choice.lower() == "bond":
        print("You have chosen bond")

        # Ask user to input bond details
        house_value = float(input("Please enter the current value of your house"
                                  + " (in numbers): "))
        interest_rate = float(input("Please enter the interest rate percent"
                                  + " (in numbers): "))
        month_amount = float(input("Please enter how many months you plan to "
                                  + "take to repay the bond (in numbers): "))
        
        # Asks the user to input the numbers again if they input negative numbers
        if house_value <= 0 or interest_rate <= 0 or month_amount <= 0:
            print("Invalid input. Please enter positive numbers for house value, "
                   "interest rate and months.")
            continue

        # Calculate monthly bond repayment
        monthly_interest_rate = (interest_rate / 12) / 100
        monthly_repayment = (monthly_interest_rate * house_value) \
        (1 - math.pow(1 + monthly_interest_rate, + -month_amount))

        # Print monthly bond repayment plan and exit loop
        print(f"The monthly repayment for your bond will be ${round(monthly_repayment, 2)}")
        break

    # Ask user to input the investment details if they select investment.
    elif choice.lower() == "investment":
        print("You have chosen investment")

        # Ask user to input investment details
        investment_amount = float(input("Please enter the amount of money you're "
                                    "depositing (in numbers): "))
        interest_rate = float(input("Please enter your percent of interest rate"
                                    " (in numbers): "))
        year_amount = float(input("Please enter the amount of years you'll invest"
                                  " for (in numbers): "))
        interest_type = input("Please enter if you'd like simple or compound interest: ")

        # Calculates the investment returns for simple interest rate.
        if interest_type.lower() == "simple":
            investment_returns = investment_amount * (interest_rate/100) * year_amount

            # Prints the investment calculation for simple interest.
            print("Your investment will be worth $" + str(round(investment_amount + investment_returns, 2)) 
            + " after " + str(year_amount) + " years of simple interest.")

            # Exits the loop after the investment calculation for simple interest is done.
            break

        # Calculate the investment returns for compound interest rate.
        elif interest_type.lower() == "compound":
             investment_returns = investment_amount * ((1 + (interest_rate/100)) ** year_amount)

             # Prints the investment calculation for compound interest.
             print("Your investment will be worth $" + str(round(investment_returns, 2)) +
                  " after " + str(year_amount) + " years of compound interest.")
             
             # Exits the loop after the investment calculation for compound interest is done.
             break
        
    else:
        # Tells the user to input again as they've typed an invalid input
        print("Invalid input, please input either 'investment' or 'bond' to proceed")
        continue

# Kind message to the user (and whoever's marking this!)
print("Thank you for using Jim's finance calculator today, we hope your "
      "experience was pleasant.")

# I spent a lot of time formatting this code to make it more readable, as I felt
# it was all too cluttered together, please let me know if there is more I can do
# to format it better, thanks. 

# Also wrapping my head around the maths was harder than I expected, even though
# we had the formula it still took me a good while to get it to what I think is
# correct.




