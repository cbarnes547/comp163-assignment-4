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

# test case 3
study_options = ["Programming", "Math", "English", "History"]

print("Available study options:")
print(study_options)

studying = input("Choose a study option: ")

if studying in study_options:
    if current_gpa >= 3.5 and social_points > 40:
        print(f"{studying}: You are ready for an advanced workload.")
    elif current_gpa < 3.0 or social_points < 20:
        print(f"{studying}: Consider focusing on fewer courses.")
    else:
        print(f"{studying}: Moderate workload recommended.")
else:
    print("Invalid choice.")
print("")

if studying not in study_options:
    print(f"{studying} is not an available option.")

print("")

# test case 4
low_social = 20
high_social = 60

has_low_social = social_points < low_social
has_high_social = social_points > high_social

if has_high_social is True:
    print("You are highly social! Great networking opportunities ahead.")
elif has_low_social is True:
    print("Low social engagement maybe join a club or activity.")
elif has_high_social is not True and has_low_social is not True:
    print("Moderate social life you are balanced between school and friends.")
else:
    print("Stats unclear recheck your inputs.")

print("\nFinal Stats:")
print(f"Student Name: {student_name}")
print(f"GPA: {current_gpa}")
print(f"Study Hours: {study_hours}")
print(f"Social Points: {social_points}")
print(f"Stress Level: {stress_level}")
