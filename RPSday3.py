import tkinter as tk
from PIL import Image, ImageTk
import random

# 6. Function to handle button clicks
def play_choice(choice):
    computer_choice = get_computer_choice()
    result = determine_winner(choice, computer_choice)
    result_message = f'You chose {choice}.\nComputer chose {computer_choice}.\n{result}'
    
    # Clear any previous images
    for widget in image_frame.winfo_children():
        widget.pack_forget()

    # Display the image only if the player chooses Rock
    if choice == 'Rock':
        image_label1.pack(side = tk.LEFT, padx = 10)
    elif choice == 'Paper':
        image_label3.pack(side = tk.LEFT, padx = 10)
    elif choice == 'Scissors':
        image_label2.pack(side = tk.LEFT, padx = 10)
    #Display the image only if the computer chooses Scissors
    if computer_choice == 'Scissors':
        image_label2.pack(side = tk.LEFT, padx = 10)
    elif computer_choice == 'Rock':
        image_label1.pack(side = tk.LEFT, padx = 10)
    elif computer_choice == 'Paper':
        image_label3.pack(side = tk.LEFT, padx = 10)
    # Display the win image only if the player wins
    if result == 'You WIN!':
        image_labelW.pack(side = tk.LEFT, padx = 10)
    elif result == 'You LOSE!':
        image_labelL.pack(side = tk.LEFT, padx = 10)
    elif result == 'It is a TIE!':
        image_labelA.pack(side = tk.LEFT, padx = 10)


# 7. Function to determine and display the winner
def determine_winner(player, computer):
    if player == computer:
        return 'It is a TIE!'
    elif (player == 'Rock' and computer == 'Scissors' or
          player == 'Paper' and computer == 'Rock' or
          player == 'Scissors' and computer == 'Paper'):
        return 'You WIN!'
    else:
        return 'You LOSE!'

# 8. Function to get computer choice
def get_computer_choice():
    choices = ['Rock', 'Paper', 'Scissors']
    return random.choice(choices)

# 1. Creating a window
root = tk.Tk()
root.title('ROCK PAPER SCISSORS')

# 2. Set state of the window
root.state('zoomed')

# 3. Create label for instructions
label = tk.Label(root, text='Choose Rock, Paper or Scissors:', font=('Helvetica', 35))
label.pack(pady=20)


# 9.1. Creating Frame
image_frame = tk.Frame(root)
image_frame.pack(side=tk.TOP, pady=20)

# 9.2. Loading the images using PIL
#Rock
image_path1 = 'E:/python code/RPS/Rock.png'
image1 = Image.open(image_path1)
image1 = image1.resize((300, 300))
photo1 = ImageTk.PhotoImage(image1)
#Scissors
image_path2 = 'E:/python code/RPS/Scissors.png'
image2 = Image.open(image_path2)
image2 = image2.resize((300, 300))
photo2 = ImageTk.PhotoImage(image2)
#Paper
image_path3 = 'E:/python code/RPS/Paper.png'
image3 = Image.open(image_path3)
image3 = image3.resize((300, 300))
photo3 = ImageTk.PhotoImage(image3)
#youWin
image_pathW = 'E:/python code/RPS/youWin.png'
imageW = Image.open(image_pathW)
imageW = imageW.resize((300, 300))
photoW = ImageTk.PhotoImage(imageW)
#youLose
image_pathL = 'E:/python code/RPS/youLose.png'
imageL = Image.open(image_pathL)
imageL = imageL.resize((300, 300))
photoL = ImageTk.PhotoImage(imageL)
#itsAtie
image_pathA = 'E:/python code/RPS/itsAtie.png'
imageA = Image.open(image_pathA)
imageA = imageA.resize((300, 300))
photoA = ImageTk.PhotoImage(imageA)

# 9.3. Creating labels to display images
#Rock
image_label1 = tk.Label(image_frame, image=photo1)
image_label1.image = photo1
#Scissors
image_label2 = tk.Label(image_frame, image=photo2)
image_label2.image = photo2
#Paper
image_label3 = tk.Label(image_frame, image=photo3)
image_label3.image = photo3
#youWin
image_labelW = tk.Label(image_frame, image=photoW)
image_labelW.image = photoW
#youLose
image_labelL = tk.Label(image_frame, image=photoL)
image_labelL.image = photoL
#itsAtie
image_labelA = tk.Label(image_frame, image=photoA)
image_labelA.image = photoA


# 5.1. Creating frame for the buttons in 5.2
button_frame = tk.Frame(root)
button_frame.pack(side=tk.BOTTOM, pady=20)
button_width = 15

# 5.2. Creating buttons For Rock, Paper and Scissors
button_rock = tk.Button(button_frame, text='Rock', font=('Helvetica', 25), width=button_width, command=lambda: play_choice('Rock'))  # passing 'Rock' in play_choice() function
button_rock.pack(side=tk.LEFT, padx=20)

button_paper = tk.Button(button_frame, text='Paper', font=('Helvetica', 25), width=button_width, command=lambda: play_choice('Paper'))  # passing 'Paper' in play_choice() function
button_paper.pack(side=tk.LEFT, padx=20)

button_scissors = tk.Button(button_frame, text='Scissors', font=('Helvetica', 25), width=button_width, command=lambda: play_choice('Scissors'))  # passing 'Scissors' in play_choice() function
button_scissors.pack(side=tk.LEFT, padx=20)

# 4. To make sure the window created does not time out
root.mainloop()
