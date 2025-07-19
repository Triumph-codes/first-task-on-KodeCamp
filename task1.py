print("--- Student Grade Evaluator ---")

while True:
    try:
        num_students = int(input("How many students do you want to process? "))
        if num_students <= 0:
            print("Please enter a positive number of students.")
            continue # Ask again if the number is not positive
        break # Exit loop
    except ValueError:
        print("Invalid input. Please enter a whole number for the number of students.")

pass_count = 0
fail_count = 0
excellent_count = 0


current_student = 1
while current_student <= num_students:
    print(f"\n--- Processing Student {current_student} ---")
    student_name = input("Enter student name: ")

    # Score 1
    while True: # Loop until a valid score for Subject 1 is entered
        try:
            score1 = float(input("Enter score for Subject 1: "))
            if (score1 < 0 or score1 > 100): # Add range validation for scores
                print("Score must be between 0 and 100.")
                continue
            break # Exit inner loop
        except ValueError:
            print("Invalid score. Please enter a numerical value for Subject 1.")

    # Score 2
    while True:
        try:
            score2 = float(input("Enter score for Subject 2: "))
            if (score2 < 0 or score2 > 100):
                print("Score must be between 0 and 100.")
                continue
            break
        except ValueError:
            print("Invalid score. Please enter a numerical value for Subject 2.")

    # Score 3
    while True:
        try:
            score3 = float(input("Enter score for Subject 3: "))
            if (score3 < 0 or score3 > 100):
                print("Score must be between 0 and 100.")
                continue
            break 
        except ValueError:
            print("Invalid score. Please enter a numerical value for Subject 3.")

    # --- Calculate Average ---
    average_score = (score1 + score2 + score3) / 3

    # --- Determine Grade ---
    result_message = ""
    if average_score < 50:
        result_message = "Fail!"
        fail_count += 1
    elif average_score >= 50 and average_score <= 79: # Using 'and' explicitly
        result_message = "Pass!"
        pass_count += 1
    else: # average_score >= 80
        result_message = "Excellent!"
        excellent_count += 1

    # Print individual student result
    print(f"{student_name} - Average: {average_score:.2f} - Result: {result_message}")

    current_student += 1

# --- 4. Display Final Summary ---
print("\n--- Summary ---")
print(f"Total Students Processed: {num_students}")
print(f"Passed: {pass_count}")
print(f"Failed: {fail_count}")
print(f"Excellent: {excellent_count}")
print("--- Evaluation Complete ---")

