import tkinter as tk
from tkinter import font as tkfont
import random

# --- Logic and Variables ---
secret_number = random.randint(1, 100)
attempts = 0
game_won = False

# --- Core Functions ---
def reset_game():
    global secret_number, attempts, game_won
    secret_number = random.randint(1, 100)
    attempts = 0
    game_won = False
    
    success_frame.place_forget()
    result_label.config(text="")
    guess_entry.delete(0, tk.END)
    attempts_value_label.config(text="0")

def check_guess():
    global attempts, game_won
    if game_won: return 
    
    try:
        guess = int(guess_entry.get())
        attempts += 1
        
        if guess < secret_number:
            result_label.config(text="TOO LOW!", fg="#FFB300")
        elif guess > secret_number:
            result_label.config(text="TOO HIGH!", fg="#FF5252")
        else:
            result_label.config(text="CORRECT!", fg="#4CAF50")
            game_won = True
            attempts_display_label.config(text=str(attempts))
            success_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
            
        attempts_value_label.config(text=str(attempts))
            
    except ValueError:
        result_label.config(text="Enter a valid number", fg="#FF5252")

# --- Initialize Root Window ---
root = tk.Tk()
root.title("Guessing Challenge")
root.geometry("800x600")
root.configure(bg="#121212")

# --- Custom Fonts ---
title_font = tkfont.Font(family="Arial", size=28, weight="bold")
card_font = tkfont.Font(family="Arial", size=18)
btn_font = tkfont.Font(family="Arial", size=16, weight="bold")

# --- Main Game Card Frame ---
card_frame = tk.Frame(root, width=600, height=400, bg="#1E293B", bd=2, relief="groove")
card_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Main Instruction Label (Moved up since Task header is gone)
instruction_label = tk.Label(card_frame, text="Guess the number\nbetween 1 and 100", font=title_font, fg="white", bg="#1E293B", justify=tk.CENTER)
instruction_label.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

# --- Input Area (Centered) ---
guess_text_label = tk.Label(card_frame, text="Enter Guess:", font=card_font, fg="white", bg="#1E293B")
guess_text_label.place(relx=0.35, rely=0.5, anchor=tk.E)

guess_entry = tk.Entry(card_frame, font=card_font, fg="#1E293B", bg="white", width=10, justify=tk.CENTER)
guess_entry.place(relx=0.6, rely=0.5, anchor=tk.CENTER)

# --- Buttons ---
btn_container = tk.Frame(card_frame, bg="#1E293B")
btn_container.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

tk.Button(btn_container, text="Submit ✓", font=btn_font, command=check_guess, width=10, bg="#4CAF50", fg="white", relief="flat").pack(side=tk.LEFT, padx=10)
tk.Button(btn_container, text="Reset ↺", font=btn_font, command=reset_game, width=10, bg="#FFC107", fg="#1E293B", relief="flat").pack(side=tk.LEFT, padx=10)
tk.Button(btn_container, text="Exit ✗", font=btn_font, command=root.quit, width=10, bg="#FF5252", fg="white", relief="flat").pack(side=tk.LEFT, padx=10)

# --- Result Area ---
result_label = tk.Label(card_frame, text="", font=card_font, bg="#1E293B")
result_label.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
tk.Label(card_frame, text="Attempts:", font=card_font, fg="white", bg="#1E293B").place(relx=0.4, rely=0.92, anchor=tk.CENTER)
attempts_value_label = tk.Label(card_frame, text="0", font=card_font, fg="white", bg="#1E293B")
attempts_value_label.place(relx=0.55, rely=0.92, anchor=tk.CENTER)

# --- Success Overlay ---
success_frame = tk.Frame(root, width=500, height=300, bg="#D4E157", bd=3, relief="raised")
success_frame.place_forget()
tk.Label(success_frame, text="🏆", font=("Arial", 60), bg="#D4E157").place(relx=0.5, rely=0.3, anchor=tk.CENTER)
tk.Label(success_frame, text="SUCCESS!", font=("Arial", 30, "bold"), fg="#1E293B", bg="#D4E157").place(relx=0.5, rely=0.6, anchor=tk.CENTER)
attempts_display_label = tk.Label(success_frame, text="0", font=("Arial", 40, "bold"), fg="#1E293B", bg="#D4E157")
attempts_display_label.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

root.mainloop()