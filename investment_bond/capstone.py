import math

# Ask user to choose between Investment or Bond

print("Investment = To calculate amount of interest you will earn on investment.")
print("Bond = To calculte the amount you will have to pay on a home loan")

while True:
    user_choice = input("Please enter either 'investment' or 'bond' from the menu above to proceed:").lower()
    if user_choice in ("investment","bond"):
        break

# Investment- Ask questions to user and based on answers use(simple or compound interest) formula to print answer.

if user_choice == "investment":

    deposit_amount = float(input("How much money are you depositing?:"))
    percentage_preference = float(input("Please enter interest rate?:"))
    years_of_investment = float(input("How many years, are you planning to invest for?:"))
    interest = input("What interest options are you looking for, select either 'compound interest' or 'simple interest':").lower()
    total_amount_once_interest_is_applied = 0

    P = deposit_amount
    r = percentage_preference/100
    t = years_of_investment
    A = total_amount_once_interest_is_applied

    if interest == "simple interest":
         
        A = P*(1+r*t)
        print("Your simple interest is {:.2f}.".format(A))

    elif interest == "compound interest":
        
        A = P*(math.pow((1+r),t))
        print("Your compound interest is {:.2f}.".format(A))

# Bond- Ask questions to user and based on answers, calculate repayment and print payment for each month.

elif user_choice == "bond":

    house_value = int(input("What is the present value of the house?:"))
    prefer_interest_rate = int(input("Please enter interest rate?:"))
    duration_of_repay_bond = int(input("How many months are you planning to repay the bond?:"))

    P = house_value
    i = (prefer_interest_rate/100)/12
    n = duration_of_repay_bond

    repayment = (i*P)/(1-(1+i)**(-n))

    print("Your payment for each month is {:.2f}.".format(repayment))
    