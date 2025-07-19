BURGER_PRICE = 5.00
FRIES_PRICE = 2.00
DRINK_PRICE = 1.50
DISCOUNT_THRESHOLD = 20.00
DISCOUNT_PERCENTAGE = 0.10

customer_count = 0
print("--- XYZ Fast Food ---")
print("Welcome to XYZ Fast Food")


while True:
    customer_name = input("\nPlease Enter your name to order (or type 'exit' to finish): ")
    if customer_name.lower() == 'exit':
        print("Exiting order system.")
        break
   
    print("Welcome, " + customer_name)
    current_customer_total = 0.0
    discount_amount = 0.0

    while True:
        try :
            num_burger = int(input("How many BURGERS would you like to order: "))
            if num_burger < 0:
                print("Quantity cannot be negative. Please enter a whole number")
                continue
            current_customer_total += num_burger * BURGER_PRICE
            break
        except ValueError:
            print("Invalid input. Please enter a whole number")
        
    while True:
        try :
            num_fries = int(input("How many FRIES would you like to order: "))
            if num_fries < 0:
                print("Quantity cannot be negative. Please enter a whole number")
                continue
            current_customer_total += num_fries * FRIES_PRICE
            break
        except ValueError:
            print("Invalid input. Please enter a whole number")
        
    while True:
        try :
            num_drink = int(input("How many DRINKS would you like to order: "))
            if num_drink < 0 :
                print("Quantity cannot be negative. Please enter a whole number")
                continue
            current_customer_total += num_drink * DRINK_PRICE
            break
        except ValueError:
            print("Invalid input. Please enter a whole number")
        

    if current_customer_total > DISCOUNT_THRESHOLD:
        discount_amount = current_customer_total * DISCOUNT_PERCENTAGE
        final_bill = current_customer_total - discount_amount
        print(f"\nA discount of {discount_amount:.2f}$ has been applied")
        
    else:
        final_bill = current_customer_total
        print("\nNo discount applied (total must be over $20.00).")

    print(f"\n --- {customer_name}'s Bill ---")
    print("Items Ordered:")
    print(f"  Burgers ({num_burger}) x {BURGER_PRICE:.2f}$ = {num_burger * BURGER_PRICE:.2f}$")
    print(f"  Fries   ({num_fries}) x {FRIES_PRICE:.2f}$ = {num_fries * FRIES_PRICE:.2f}$")
    print(f"  Drinks  ({num_drink}) x {DRINK_PRICE:.2f}$ = {num_drink * DRINK_PRICE:.2f}$")
    print(f"Original Total: {current_customer_total:.2f}$")
    if discount_amount > 0 :
        print(f"Discount Applied: -{discount_amount:.2f}$")
    print(f"Final Bill: {final_bill:.2f}$")
    print("\nThank you for your order, " + customer_name + "! We hope to serve you again soon.")

    customer_count += 1
print("\n--- Order System Summary ---")
print(f"Total customers served: {customer_count}")
print("Thank you for using the system!")
