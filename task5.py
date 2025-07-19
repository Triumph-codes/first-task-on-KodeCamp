print(" --- Simple ATM Simulator --- \n")
account_balance = 1000

while True :
    try :
        user_input = int(input("Enter 1 to Show current balance: \nEnter 2 to Deposit: \nEnter 3 to Withdraw: \nEnter 4 to Exit: \n What would you like to do: "))
        if user_input < 1 or user_input > 4:
            print("Invalid input. Please enter a number between 1 and 4.\n")
            continue

        if user_input == 1:
            print(f"\nYour current balance is {account_balance:.2f}$\n")

        elif user_input == 2:
            deposit_amount = float(input("How much would you like to deposit? $"))
            if deposit_amount <= 0:
                print("Deposit must be a positive amount.\n")
            else:
                account_balance += deposit_amount
                print(f"Deposited {deposit_amount:.2f}$. New balance is {account_balance:.2f}$\n")

        elif user_input == 3:
            withdraw_amount = float(input("How much would you like to withdraw? $"))
            if withdraw_amount <= 0:
                print("Withdrawal amount must be positive.\n")
            elif withdraw_amount > account_balance:
                print(f"Insufficient funds. You only have {account_balance:.2f}$ in your account.\n")
            else:
                account_balance -= withdraw_amount
                print(f"Withdrew {withdraw_amount:.2f}$. New balance is {account_balance:.2f}$\n")

        elif user_input == 4:
            print(f"\nYour final balance is {account_balance:.2f}$")
            print("Thank you. Have a great day!\n")
            break

    except ValueError:
        print("\nInvalid input. Please enter a valid number.\n")    

        
  
  
  
  
  
  
  
