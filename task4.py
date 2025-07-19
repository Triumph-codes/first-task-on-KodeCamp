print(" --- Number Analyzer --- \n")
MAX_ENTRIES = 5
even_count = 0
odd_count = 0
negative_count = 0
positive_count = 0
zero_count = 0
entries = 0

while entries < MAX_ENTRIES:
    while True:
        try:
            number = int(input(f"\nEnter number {entries + 1} of {MAX_ENTRIES}: "))
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.") 

    if number % 2 == 0:
        print(f"{number} is EVEN.")
        even_count += 1
    else:
        print(f"{number} is ODD.")
        odd_count += 1

    if number > 0:
        print(f"{number} is POSITIVE.")
        positive_count += 1

    elif number < 0:
        print(f"{number} is NEGATIVE.")
        negative_count += 1
    else:
        print(f"{number} is ZERO.")
        zero_count += 1

    entries += 1

# --- Final Summary ---
print("\n--- Analysis Summary ---")
print(f"Total Even Numbers: {even_count}")
print(f"Total Odd Numbers: {odd_count}")
print(f"Total Negative Numbers: {negative_count}")
print(f"Total Positive Numbers: {positive_count}")
print(f"Total Zeros: {zero_count}")
print("--- Analysis Complete ---")            