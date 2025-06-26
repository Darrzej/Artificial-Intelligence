grades = {}

#range means how many subjects you want to add ()
for i in range(2):
    subject = input(f"Enter subject {i+1}: ")
    
    # Validate grade input
    while True:
        try:
            grade = int(input(f"Enter grade for {subject} (1–5): "))
            if 1 <= grade <= 5:
                break  # input is valid
            else:
                print("Grade must be between 1 and 5.")
        except ValueError:
            print("Please enter a valid number.")

    grades[subject] = grade

# Calculations (same as before)
total = sum(grades.values())
average = total / len(grades) 

highest_subject = max(grades, key=grades.get) 
lowest_subject = min(grades, key=grades.get) 

print(f"\nAverage Grade: {average:.2f}")
print(f"Highest Grade: {highest_subject} ({grades[highest_subject]})")
print(f"Lowest Grade: {lowest_subject} ({grades[lowest_subject]})")

# Adjusted feedback logic for 1–5 scale
if average >= 4.5:
    print("Result: Excellent!")
elif average >= 3.5:
    print("Result: Good")
else:
    print("Result: Needs Improvement")
