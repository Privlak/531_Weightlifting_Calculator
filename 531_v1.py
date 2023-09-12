# Ideas to add (Ordered by priority):
# 1) The user doesnt know Training Max:
#    if tm == 'tm':  # TRAINING MAX = n(reps) * weight lifted * 0.0333 + weight lifted
#        training_max.remove(tm)
#        weight_lifted = float(input('Highest weight you successfully lifted for this exercise? '))
#        n_reps = float(input('How many times did you lift it in a single set? '))
#        tm = float((n_reps * weight_lifted * 0.0333 + weight_lifted)*0.9) # In 5/3/1, "working" tm is 80-90% of the real tm
#        training_max.append(tm)
# print('Enter "tm" (without the quotes) if you dont know your training max.')
# 2) Option to go back and rename exercise or write other training max
# 3) Username input and save the output to "Username_531_X.month.txt"

# Module to see the output in the CMD/PowerShell... for 20s
import time

# Creating a list of exercises
print('Enter the exercises you want to calculate your training max for, one per line! ')
print('Enter "done" (without the quotes) to end the list.')

exercises = []
while True:
    e = input('Exercise: ')
    if e == 'done':
        break
    exercises.append(e)
    if e == '':
        exercises.remove(e)
        print('You need to enter an exercise, or if you are done - write "done"')

# Capitalize the first letter of every element in the list
for c in range(len(exercises)):
    exercises[c] = exercises[c].title()

print('')
print(exercises)
print('')

# Creating a list of training max values
print('Enter your training maxes in the same order as your exercises (check list above), one per line! ')
print('Enter "done" (without the quotes) to end the list.')

training_max = []
while True:
    tm = input('Training max: ')
    if tm == 'done':
        break
    training_max.append(tm)
    if tm == '':
        training_max.remove(tm)
        print('You need to enter a number, or if you are done - write "done"')

print('')
for e, tm in zip(exercises, training_max):
    print(e, '-', tm, 'kg', sep='')
print('')

# Monthly program based on percentages of a training max for each exercise in the list
for e, tm in zip(exercises, training_max):
    print(e)
    print('Week 1 -', ' ', round(0.65 * float(tm), 2), 'x5,', round(0.75 * float(tm), 2), 'x5,',round(0.85 * float(tm), 2), 'x5+', sep='')
    print('Week 2 -', ' ', round(0.70 * float(tm), 2), 'x3,', round(0.80 * float(tm), 2), 'x3,',round(0.90 * float(tm), 2), 'x3+', sep='')
    print('Week 3 -', ' ', round(0.75 * float(tm), 2), 'x5,', round(0.85 * float(tm), 2), 'x3,',round(0.95 * float(tm), 2), 'x1+', sep='')
    print('Week 4 -', ' ', round(0.40 * float(tm), 2), 'x5,', round(0.50 * float(tm), 2), 'x5,',round(0.60 * float(tm), 2), 'x5',  sep='')
    print('')
   
# How many seconds does the output stay on   
time.sleep(20)










