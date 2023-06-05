import tkinter as tk
from tkinter import messagebox
from prompts import prompts

resume_index = 0
last_no_index = None

def display_message():
    messagebox.showinfo("Birthday Message", "Happy Birthday Euni! I love you")
    check_love()

def check_love():
    global resume_index, last_no_index
    while resume_index < len(prompts):
        prompt = prompts[resume_index]
        response = messagebox.askquestion("Prompt", prompt)
        if response == 'yes':
            messagebox.showinfo("Love Confession", "Yay! I love you too!")
            resume_index = 0  # Reset resume index
            resume_button.config(state=tk.NORMAL)  # Disable the resume button
            break
        elif response == 'no':
            last_no_index = resume_index  # Store the index of the last 'No' response
            resume_index += 1  # Move to the next prompt
            resume_button.config(state=tk.NORMAL)  # Enable the resume button
        else:
            break  # If the response is not 'yes' or 'no', exit the loop
    else:
        resume_button.config(state=tk.NORMAL)  # Enable the resume button if prompts are exhausted

def resume():
    global resume_index, last_no_index
    resume_index = last_no_index  # Set the resume index to the last 'No' index
    resume_button.config(state=tk.DISABLED)  # Disable the resume button
    check_love()

# Create the main window
window = tk.Tk()

# Set the window size
window.geometry("400x300")

# Set the background color to black
window.configure(bg="black")

# Create a button widget
button = tk.Button(window, text="Click Me", command=display_message, bg="white", fg="black")
button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Create a resume button
resume_button = tk.Button(window, text="Resume", command=resume, state=tk.DISABLED, bg="white", fg="black")
resume_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

# Start the main event loop
window.mainloop()
