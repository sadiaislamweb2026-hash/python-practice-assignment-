name = input("Enter student name: ")

math = float(input("Enter Math marks: "))
english = float(input("Enter English marks: "))
python = float(input("Enter Python marks: "))

# Check valid marks
if (math < 0 or math > 100 or
    english < 0 or english > 100 or
    python < 0 or python > 100):

    print("Invalid marks! Marks must be between 0 and 100.")

else:
    # Calculate average
    average = (math + english + python) / 3

    # Determine grade
    if average >= 80:
        grade = "A+"
    elif average >= 70:
        grade = "A"
    elif average >= 60:
        grade = "A-"
    elif average >= 50:
        grade = "B"
    elif average >= 40:
        grade = "C"
    else:
        grade = "F"

    # Display result
    print("\nStudent Name:", name)
    print(f"Average Marks: {average:.2f}")
    print(f"Final Grade: {grade}")
