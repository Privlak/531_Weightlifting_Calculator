# Module for writing the output
import os

# Username prompt
username = input('Enter your name: ')
username_capitalized = username.capitalize()
print()

# Creating a list of exercises
print('Enter the exercises you want to calculate your training max for, one per line! ')
print()
print('Enter "done" (without the quotes) to end the list.')
print()
print('Enter "back" (without the quotes) to go back and rewrite the exercise.')
print()

exercises = []
current_index = 0 
while True:
    e = input(f'Exercise {current_index + 1}: ')
    if e == 'done':
        break
    elif e == 'back':
        if current_index > 0:
            current_index -= 1
            del exercises[current_index]
            print(f'Returning to exercise {current_index + 1}')
            continue
        else:
            print('You are already at the first exercise!')
            continue
    exercises.append(e)
    if e == '':
        exercises.remove(e)
        print('You need to enter an exercise, or if you are done - write "done"')
    current_index += 1

# Capitalize the exercises 
for c in range(len(exercises)):
    exercises[c] = exercises[c].title()

print()
print(exercises)
print()

# Creating a list of training max values
print('Enter your training maxes in the same order as your exercises (check list above), one per line! ')
print()
print('If you dont know your training max, enter "tm" (without the quotes).')
print()
print('Enter "done" (without the quotes) to end the list.')
print()
print('Enter "back" (without the quotes) to go back and rewrite the training max.')
print()

training_max = []
current_index = 0
while True:
    tm = input(f'Training max {current_index + 1}: ')
    if tm == 'done':
        break
    elif tm == 'back':
        if current_index > 0:
            current_index -= 1
            del training_max[current_index]
            print(f'Returning to training max for exercise {current_index + 1}')
            continue
        else:
            print('You are already at the first exercise training max!')
            continue
    training_max.append(tm)
    if tm == '':
        training_max.remove(tm)
        print('You need to enter a number, or if you are done - write "done"')
    if tm == 'tm':
        training_max.remove(tm)
        while True:
            weight_lifted = input('What is the highest weight you successfully lifted for this exercise? (Type "back" to go back) ')
            if weight_lifted.lower() == "back":
                break
            try:
                weight_lifted = float(weight_lifted)
                break
            except ValueError:
                print("Invalid input. Please enter a number or 'back'.")
        while True:
            n_reps = input('How many times did you lift it in a single set? (Type "back" to go back) ')
            if n_reps.lower() == "back":
                break
            try:
                n_reps = float(n_reps)
                break
            except ValueError:
                print("Invalid input. Please enter a number or 'back'.")
        if weight_lifted == "back" or n_reps == "back":
            continue
        tm = float(round((n_reps * weight_lifted * 0.0333 + weight_lifted))) # tm = float(round((n_reps * weight_lifted * 0.0333 + weight_lifted)*0.9)) ; Currently using 100%, usually 0.9
        training_max.append(tm)
       
    current_index += 1

# Create a directory and write the monthly program to '{username_capitalized}_531.txt'
if not os.path.exists('Gym'):
    os.mkdir('Gym')
    
with open(f'Gym/{username_capitalized}_531.txt', 'w') as f:
    f.write('Training maxes: ' + '\n')
    for e, tm in zip(exercises, training_max):
        f.write(e + '-' + str(tm) + 'kg' + '\n')
    f.write('\n')
    for e, tm in zip(exercises, training_max):
        f.write(e + '\n')
        f.write('Week 1 -' + ' ' + str(round(0.65 * float(tm), 2)) + 'x5, ' + str(round(0.75 * float(tm), 2)) + 'x5, ' + str(round(0.85 * float(tm), 2)) + 'x5+' + '\n')
        f.write('Week 2 -' + ' ' + str(round(0.70 * float(tm), 2)) + 'x3, ' + str(round(0.80 * float(tm), 2)) + 'x3, ' + str(round(0.90 * float(tm), 2)) + 'x3+' + '\n')
        f.write('Week 3 -' + ' ' + str(round(0.75 * float(tm), 2)) + 'x5, ' + str(round(0.85 * float(tm), 2)) + 'x3, ' + str(round(0.95 * float(tm), 2)) + 'x1+' + '\n')
        f.write('Week 4 -' + ' ' + str(round(0.75 * float(tm), 2)) + 'x5, ' + str(round(0.85 * float(tm), 2)) + 'x3, ' + str(round(0.95 * float(tm), 2)) + 'x1' + '\n' + '\n')
