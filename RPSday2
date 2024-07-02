import tkinter as tk
from tkinter import messagebox
import random

# 6. Function to handle button clicks
def play_choice(choice):
    computer_choice = get_computer_choice()
    result = determine_winner(choice, computer_choice)
    result_message = f'You chose {choice}.\nComputer chose {computer_choice}.\n {result}'
    tk.messagebox.showinfo('Result:', result_message)

# 7. Function to determine and display the winner
def determine_winner(player, computer):
    if player == computer:
        return 'Its a TIE!'
    elif (player == 'Rock' and computer == 'Scissors' or player == 'Paper' and computer == 'Rock' or player == 'Scissors' and computer == 'Paper'):
        return 'You WIN!'
    else:
        return 'You LOSE!'
        
# 8. Function to get computer choice
def get_computer_choice():
    choices = ['Rock', 'Paper', 'Scissors']
    return random.choice(choices)

# 1. Creating a window
root  = tk.Tk()
root.title('ROCK PAPER SCISSORS')

# 2. Set state of the window
root.state('zoomed')


# 3. Create label for instructions
label = tk.Label(root, text = 'Choose Rock, Paper or Scissors:', font = ('Helvetica', 35))
label.pack(pady = 20)



# 5.1. Creating frame for the buttons in 5.2
button_frame = tk.Frame(root)
button_frame.pack(side =tk.BOTTOM, pady = 20)
button_width = 15

# 5.2. Creating buttons For Rock, Paper and Scissors
button_rock = tk.Button(button_frame, text='Rock', font=('Helventica', 25), width = button_width, command=lambda: play_choice('Rock')) #passing 'Rock' in play_choice() function
button_rock.pack(side = tk.LEFT, padx = 20)

button_rock = tk.Button(button_frame, text='Paper', font=('Helventica', 25), width = button_width, command=lambda: play_choice('Paper')) #passing 'Paper' in play_choice() function
button_rock.pack(side = tk.LEFT, padx = 20)

button_rock = tk.Button(button_frame, text='Scissors', font=('Helventica', 25), width = button_width, command=lambda: play_choice('Scissors')) #passing 'scissors' in play_choice() function
button_rock.pack(side = tk.LEFT, padx = 20)

# 4. To make sure the window created does not time out
root.mainloop()
