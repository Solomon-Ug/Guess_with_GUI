import tkinter as tk
from tkinter import messagebox
import random

class GuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")
        self.master.geometry("350x260")
        self.master.resizable(False, False)
        
        # Game State Variables
        self.secret_number = 0
        self.attempts_left = 7
        
        self.setup_ui()
        self.start_game()
        
    def setup_ui(self):
        # Title
        self.title_label = tk.Label(self.master, text="Guess the Number!", font=("Segoe UI", 16, "bold"))
        self.title_label.pack(pady=(15, 5))
        
        # Instructions
        self.instruction_label = tk.Label(self.master, text="Enter a number between 1 and 100", font=("Segoe UI", 10))
        self.instruction_label.pack()
        
        # Entry Field
        self.guess_entry = tk.Entry(self.master, font=("Segoe UI", 14), width=10, justify="center")
        self.guess_entry.pack(pady=10)
        self.guess_entry.bind('<Return>', lambda event: self.check_guess())
        
        # Submit Button
        self.submit_btn = tk.Button(self.master, text="Submit Guess", command=self.check_guess, bg="#4CAF50", fg="white", font=("Segoe UI", 10, "bold"), cursor="hand2")
        self.submit_btn.pack(pady=5)
        
        # Feedback Label
        self.feedback_label = tk.Label(self.master, text="", font=("Segoe UI", 10, "bold"))
        self.feedback_label.pack(pady=5)
        
        # Attempts Remaining Label
        self.attempts_label = tk.Label(self.master, text="", font=("Segoe UI", 10, "italic"))
        self.attempts_label.pack()
        
        # Restart Button
        self.restart_btn = tk.Button(self.master, text="Restart Game", command=self.start_game, font=("Segoe UI", 9), cursor="hand2")
        self.restart_btn.pack(pady=10)

    def start_game(self):
        """Initializes or resets the game state."""
        self.secret_number = random.randint(1, 100)
        self.attempts_left = 7
        
        # Reset UI elements
        self.guess_entry.config(state=tk.NORMAL)
        self.guess_entry.delete(0, tk.END)
        self.submit_btn.config(state=tk.NORMAL)
        self.restart_btn.config(state=tk.DISABLED)
        
        self.feedback_label.config(text="Game started! Good luck.", fg="#333333")
        self.update_attempts_display()
        self.guess_entry.focus()

    def update_attempts_display(self):
        """Updates the text showing remaining attempts."""
        self.attempts_label.config(text=f"Attempts remaining: {self.attempts_left}")

    def check_guess(self):
        """Validates the input and checks it against the secret number."""
        if self.attempts_left <= 0:
            return

        guess_str = self.guess_entry.get().strip()
        
        # Check if empty
        if not guess_str:
            self.feedback_label.config(text="Please enter a number.", fg="#D32F2F")  # Red
            return
            
        # Check if valid integer
        try:
            guess = int(guess_str)
        except ValueError:
            self.feedback_label.config(text="Invalid input! Enter a whole number.", fg="#D32F2F")  # Red
            self.guess_entry.delete(0, tk.END)
            return
            
        # Check if within range
        if guess < 1 or guess > 100:
            self.feedback_label.config(text="Number must be between 1 and 100.", fg="#D32F2F")  # Red
            self.guess_entry.delete(0, tk.END)
            return
            
        # Process valid guess
        self.attempts_left -= 1
        self.update_attempts_display()
        
        if guess == self.secret_number:
            self.feedback_label.config(text=f"Correct! The number was {self.secret_number}.", fg="#388E3C")  # Green
            self.end_game()
            messagebox.showinfo("You Win!", f"Congratulations! You guessed the number in {7 - self.attempts_left} attempts.")
        elif guess < self.secret_number:
            self.feedback_label.config(text="Too low! Try a higher number.", fg="#1976D2")  # Blue
        else:
            self.feedback_label.config(text="Too high! Try a lower number.", fg="#F57C00")  # Orange
            
        self.guess_entry.delete(0, tk.END)
        
        # Check for game over
        if self.attempts_left == 0 and guess != self.secret_number:
            self.feedback_label.config(text=f"Game Over! The number was {self.secret_number}.", fg="#D32F2F")  # Red
            self.end_game()
            messagebox.showinfo("Game Over", f"You are out of attempts. The secret number was {self.secret_number}.")
            
    def end_game(self):
        """Disables inputs to prepare for game restart."""
        self.guess_entry.config(state=tk.DISABLED)
        self.submit_btn.config(state=tk.DISABLED)
        self.restart_btn.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    app = GuessingGame(root)
    root.mainloop()
