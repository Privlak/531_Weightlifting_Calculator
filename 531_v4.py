# Module for writing the output
import os

# Username prompt
while True:
    username = input("Enter your name: ")
    
    if not isinstance(username, str) or not username.strip() or not username.isalpha():
        print("Input must be a string!")
        continue
    else:
        username_capitalized = username.capitalize()
        break

# Creating a list of exercises
print("---------------------------------------------------------------------------------------------------------------")
print("Enter the exercises you want to calculate your training max for, one per line!" + "\n")
print('Enter "back" (without the quotes) to go back and rewrite the exercise.' + "\n")
print('Enter "done" (without the quotes) to end the list.')
print("---------------------------------------------------------------------------------------------------------------")

exercises = []
current_index = 0 

while True:
    e = input(f"Exercise {current_index + 1}: ")
    
    if e.lower() == "done":
        break
        
    elif e.lower() == "back":
        if current_index > 0:
            current_index -= 1
            del exercises[current_index]
            print(f"Returning to Exercise {current_index + 1}")
            continue
        else:
            print("You need to enter an exercise!")
            continue
            
    elif e == "":
        print("You need to enter an exercise!")
        continue
        
    elif not e.isalpha():
        print("Input must be a string!")
        continue
        
    exercises.append(e)
    current_index += 1

# Capitalize the exercises 
for c in range(len(exercises)):
    exercises[c] = exercises[c].title()

print()
print(exercises)

# Creating a list of training max values
print("---------------------------------------------------------------------------------------------------------------")
print("Enter your training maxes in the same order as your exercises (check list above), one per line!" + "\n")
print('If you dont know your training max, enter "tm" (without the quotes).' + "\n")
print('Enter "back" (without the quotes) to go back and rewrite the training max.' + "\n")
print('Enter "done" (without the quotes) to end the list.')
print("---------------------------------------------------------------------------------------------------------------")

training_max = []
current_index = 0

while True:
    tm = input(f"Training max {current_index + 1}: ")

    if tm.lower() == "done":
        break

    elif tm.lower() == "back":
        if current_index > 0:
            current_index -= 1
            del training_max[current_index]
            print(f"Returning to training max for exercise {current_index + 1}")
            continue
        else:
            print("You need to enter a training max!")
            continue

    if tm == "tm":
        while True:
            weight_lifted = input(f'What is the highest weight you successfully lifted for {exercises[current_index]}? (Type "back" to go back): ')

            if weight_lifted == "":
                print("You need to enter a training max!")
                continue

            elif weight_lifted.lower() == "back":
                break

            elif not weight_lifted.isdigit():
                print("Input must be an integer!")
                continue

            while True:
                n_reps = input('How many times did you lift it in a single set? (Type "back" to go back): ')

                if n_reps == "":
                    print("You need to enter a number of repetitions!")
                    continue

                elif n_reps.lower() == "back":
                    break

                elif not n_reps.isdigit():
                    print("Input must be an integer!")
                    continue

                weight_lifted = int(weight_lifted)
                n_reps = int(n_reps)

                tm = float(round((n_reps * weight_lifted * 0.0333 + weight_lifted) * 0.9)) # Currently using 90%
                training_max.append(tm)
                print(f"Calculated training max added to exercise {exercises[current_index]}!")
                current_index += 1

                break 
            break
        continue

    elif tm == "":
        print(f'You need to enter a training max! If you do not know your training max, enter "tm" (without the quotes).')
        continue

    elif not tm.isnumeric():
        print("Input must be an integer!")
        continue

    training_max.append(tm)
    current_index += 1


# Create a directory and write the monthly program to "{username_capitalized}_531.txt"
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
gym_path = os.path.join(desktop_path, "Gym")

if not os.path.exists(gym_path):
    os.mkdir(gym_path)
    
file_path = os.path.join(gym_path, f"{username_capitalized}_531.txt")
    
with open(file_path, "w") as f:
    f.write("Training maxes: " + "\n")
    
    for e, tm in zip(exercises, training_max):
        f.write(e + "-" + str(tm) + "kg" + "\n")
    f.write("\n")
    
    for e, tm in zip(exercises, training_max):
        f.write(e + "\n")
        f.write("Week 1 -" + " " + str(round(0.65 * float(tm), 2)) + "x5, " + str(round(0.75 * float(tm), 2)) + "x5, " + str(round(0.85 * float(tm), 2)) + "x5+" + "\n")
        f.write("Week 2 -" + " " + str(round(0.70 * float(tm), 2)) + "x3, " + str(round(0.80 * float(tm), 2)) + "x3, " + str(round(0.90 * float(tm), 2)) + "x3+" + "\n")
        f.write("Week 3 -" + " " + str(round(0.75 * float(tm), 2)) + "x5, " + str(round(0.85 * float(tm), 2)) + "x3, " + str(round(0.95 * float(tm), 2)) + "x1+" + "\n")
        f.write("Deload -" + " " + str(round(0.40 * float(tm), 2)) + "x5, " + str(round(0.50 * float(tm), 2)) + "x5, " + str(round(0.60 * float(tm), 2)) + "x5" + "\n" + "\n")
