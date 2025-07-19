print(" --- Ticket Price Checker --- ")
PRICE_5_17 = 5.00
PRICE_18_59 = 10.00
PRICE_60_PLUS = 7.00
COUPON_DISCOUNT_PERCENTAGE = 0.20
while True:
    visitor_name =input("Enter visitor name (or type 'done' to finish): ")
    if visitor_name.lower() == 'done':
        print("Exiting entry checker.")
        break
    while True:
        try:
            visitor_age = int(input(f"Enter age for {visitor_name}: "))
            if visitor_age < 0: 
                print("Age cannot be negative.")
            break
        except ValueError:
            print("Invalid input. Please enter a whole number for age.")

    base_price = 0.0
    discount_amount = 0.0 
    final_price = 0.0     


    if visitor_age < 5:
        base_price = 0.0
        final_price = base_price
        print(f"\n{visitor_name} (Age: {visitor_age}): Base Price: {base_price:.2f}$ (Free)")
    elif visitor_age >= 5 and visitor_age <= 17:
        base_price = PRICE_5_17
        print(f"\n{visitor_name} (Age: {visitor_age}): Base Price: {base_price:.2f}$")
    elif visitor_age >= 18 and visitor_age <= 59:
        base_price = PRICE_18_59
        print(f"\n{visitor_name} (Age: {visitor_age}): Base Price: {base_price:.2f}$")
    else: 
        base_price = PRICE_60_PLUS
        print(f"\n{visitor_name} (Age: {visitor_age}): Base Price: {base_price:.2f}$")

   
    if visitor_age >= 5: # Only ask for coupon if the base price is not free
        has_coupon_input = input("Do they have a coupon? (Yes/No): ").lower()

        final_price = base_price 

        if has_coupon_input == 'yes':
            discount_amount = base_price * COUPON_DISCOUNT_PERCENTAGE
            final_price = base_price - discount_amount
            print(f"20.0% coupon discount applied: -{discount_amount:.2f}$")
        else:
            print("No coupon applied.")
    else: 
        pass 
        
    print("Name: ", visitor_name)
    print("Age: ", visitor_age)
    print(f"Base Ticket Price (before discount):  {base_price:.2f}$")

    if discount_amount > 0:
        print(f"Discount Applied: -${discount_amount:.2f}")
    else:
        print("No coupon discount applied.")

    print(f"Discount Applied: {discount_amount:.2f}$")
    print(f"Final Ticket Price: {final_price:.2f}$")
