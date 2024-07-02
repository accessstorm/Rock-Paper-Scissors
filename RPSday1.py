import tkinter as tk
from tkinter import messagebox
import random

# 6. Function to handle button clicks
def play_choice(choice):
    choices = ['Rock', 'Paper', 'Scissors']
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

# 2. Set size of the window
root.geometry('400x300')

# 3. Create label for instructions
label = tk.Label(root, text = 'Choose Rock Paper or Scissors', font = ('Helvetica', 14))
label.pack(pady = 20)

# 5. Creating buttons For Rock, Paper and Scissors
button_rock = tk.Button(root, text='Rock', font=('Helventica', 12), command=lambda: play_choice('Rock')) #passing 'Rock' in play_choice() function
button_rock.pack(pady = 5)

button_rock = tk.Button(root, text='Paper', font=('Helventica', 12), command=lambda: play_choice('Paper')) #passing 'Paper' in play_choice() function
button_rock.pack(pady = 5)

button_rock = tk.Button(root, text='Scissors', font=('Helventica', 12), command=lambda: play_choice('Scissors')) #passing 'scissors' in play_choice() function
button_rock.pack(pady = 5)

# 4. To make sure the window created does not time out
root.mainloop()
