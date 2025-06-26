# Create an empty dictionary to store subject attendance
attendance = {}

# Loop to collect attendance data for 3 subjects
for i in range(3):
    subject = input(f"Enter Subject {i+1}: ")

    while True:
        try:
            attended_classes = int(input(f"Enter attendance for {subject} (1–10): "))
            if 1 <= attended_classes <= 10:
                break
            else:
                print("Attendance must be between 1 and 10.")
        except ValueError:
            print("The value must be a number!")

    # Store the valid attendance in the dictionary
    attendance[subject] = attended_classes

# Total attendance points across all subjects
total = sum(attendance.values())

# Calculate the average attendance as a percentage
average = (total / (len(attendance) * 10)) * 100

# Find the subjects with highest and lowest attendance
highest_attendance = max(attendance, key=attendance.get)
lowest_attendance = min(attendance, key=attendance.get)

# Output results
print(f"\nAverage attendance: {average:.2f}%")
print(f"Highest Attendance: {highest_attendance} ({attendance[highest_attendance]}/10)")
print(f"Lowest Attendance: {lowest_attendance} ({attendance[lowest_attendance]}/10)")

# Feedback based on average attendance
if average >= 80:
    print("Nice work!")
elif 40 <= average < 80:
    print("You can do better, keep it up!")
else:
    print("Horrible job!")
