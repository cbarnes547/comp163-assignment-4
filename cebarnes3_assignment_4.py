# test case 1
student_name = "Chloe Barnes"
current_gpa = 3.0
study_hours = 30
social_points = 50
stress_level = 80

# test case 2
print("Choose your course load:")
print("A) Light (12 credits)")
print("B) Standard (15 credits)")
print("C) Heavy (18 credits)")
print("")
choice = input("Your choice: ")

if choice == "A":
    if current_gpa >= 3.8:
        study_hours += 24
        stress_level += 33
        print("Light course load chosen")
elif choice == "B":
    study_hours += 30
    stress_level += 67
    print("Standard course load chosen")
elif choice == "C":
    if current_gpa >= 3.5:
        study_hours += 36
        stress_level += 100
        print("Heavy course load chosen")
    else:
        study_hours += 34
        stress_level += 80
        print("Heavy course load chosen, You have a low GPA maybe choose a different course load")
else:
    print("Invalid input.")
print("")
