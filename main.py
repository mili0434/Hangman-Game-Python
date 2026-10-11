import tkinter as tk
from tkinter import messagebox
import random

# -------------------- SETTINGS --------------------
BG = "#121826"
PANEL = "#1B2435"
PURPLE = "#7C3AED"
LIGHT_PURPLE = "#A78BFA"
WHITE = "#FFFFFF"
MUTED = "#CBD5E1"
RED = "#FCA5A5"

WORDS = ["APPLE", "PYTHON", "TIGER", "MANGO", "CHAIR"]

# -------------------- MAIN WINDOW --------------------
root = tk.Tk()
root.title("Hangman - Word Challenge")
root.geometry("900x600")
root.configure(bg=BG)
root.resizable(False, False)

# Statistics are kept while the program is open.
stats = {"played": 0, "wins": 0, "losses": 0}


def clear_screen():
    """Remove all widgets from the current screen."""
    for widget in root.winfo_children():
        widget.destroy()


def show_home():
    """Display the main menu."""
    clear_screen()
    root.title("Hangman - Word Challenge")

    tk.Label(
        root, text="HANGMAN", font=("Arial", 42, "bold"),
        bg=BG, fg=LIGHT_PURPLE
    ).pack(pady=(75, 5))

    tk.Label(
        root, text="THE ULTIMATE WORD CHALLENGE",
        font=("Arial", 14), bg=BG, fg=MUTED
    ).pack(pady=8)

    tk.Label(
        root, text="Guess the word. Save your chances. Win the game!",
        font=("Arial", 12), bg=BG, fg="#94A3B8"
    ).pack(pady=12)

    tk.Button(
        root, text="PLAY GAME", font=("Arial", 14, "bold"),
        bg=PURPLE, fg=WHITE, activebackground=LIGHT_PURPLE,
        width=22, pady=9, command=play_game
    ).pack(pady=(20, 10))

    tk.Button(
        root, text="HOW TO PLAY", font=("Arial", 12, "bold"),
        bg="#243047", fg=WHITE, width=22, pady=7,
        command=how_to_play
    ).pack(pady=7)

    tk.Button(
        root, text="STATISTICS", font=("Arial", 12, "bold"),
        bg="#243047", fg=WHITE, width=22, pady=7,
        command=show_statistics
    ).pack(pady=7)

    tk.Button(
        root, text="QUIT GAME", font=("Arial", 11),
        bg="#243047", fg=RED, width=22, pady=6,
        command=root.destroy
    ).pack(pady=7)


def how_to_play():
    messagebox.showinfo(
        "How to Play",
        "1. Guess one letter at a time.\n"
        "2. Type a letter and press GUESS.\n"
        "3. A correct guess reveals the letter.\n"
        "4. Each incorrect guess uses one life.\n"
        "5. You can make 6 incorrect guesses.\n"
        "6. Reveal the whole word to win!"
    )


def show_statistics():
    played = stats["played"]
    wins = stats["wins"]
    losses = stats["losses"]
    win_rate = (wins / played * 100) if played else 0

    messagebox.showinfo(
        "Game Statistics",
        f"Games played: {played}\n"
        f"Wins: {wins}\n"
        f"Losses: {losses}\n"
        f"Win rate: {win_rate:.1f}%"
    )


def play_game():
    clear_screen()
    root.title("Hangman - Word Challenge")

    secret_word = random.choice(WORDS)
    guessed_letters = set()
    wrong_guesses = 0
    game_over = False
    stats["played"] += 1

    # Main heading
    tk.Label(
        root, text="GUESS THE WORD", font=("Arial", 27, "bold"),
        bg=BG, fg=LIGHT_PURPLE
    ).pack(pady=(18, 8))

    # Two-column layout keeps the controls inside the window.
    content = tk.Frame(root, bg=BG)
    content.pack(fill="both", expand=True, padx=28, pady=8)

    left_panel = tk.Frame(content, bg=PANEL, width=360, height=400)
    left_panel.pack(side="left", fill="both", expand=True, padx=(0, 12))
    left_panel.pack_propagate(False)

    right_panel = tk.Frame(content, bg=PANEL, width=450, height=400)
    right_panel.pack(side="right", fill="both", expand=True, padx=(12, 0))
    right_panel.pack_propagate(False)

    tk.Label(
        left_panel, text="YOUR CHANCES", font=("Arial", 14, "bold"),
        bg=PANEL, fg=MUTED
    ).pack(pady=(12, 2))

    canvas = tk.Canvas(
        left_panel, width=300, height=270,
        bg=PANEL, highlightthickness=0
    )
    canvas.pack(pady=3)

    # Gallows
    canvas.create_line(35, 245, 180, 245, fill=WHITE, width=4)
    canvas.create_line(65, 245, 65, 25, fill=WHITE, width=4)
    canvas.create_line(65, 25, 200, 25, fill=WHITE, width=4)
    canvas.create_line(200, 25, 200, 55, fill=WHITE, width=4)

    # Each incorrect guess adds one body part.
    def draw_hangman(stage):
        if stage == 1:
            canvas.create_oval(180, 55, 220, 95, outline=RED, width=3)
        elif stage == 2:
            canvas.create_line(200, 95, 200, 155, fill=RED, width=3)
        elif stage == 3:
            canvas.create_line(200, 110, 170, 135, fill=RED, width=3)
        elif stage == 4:
            canvas.create_line(200, 110, 230, 135, fill=RED, width=3)
        elif stage == 5:
            canvas.create_line(200, 155, 175, 195, fill=RED, width=3)
        elif stage == 6:
            canvas.create_line(200, 155, 225, 195, fill=RED, width=3)

    tk.Label(
        right_panel, text="WORD", font=("Arial", 12, "bold"),
        bg=PANEL, fg=MUTED
    ).pack(pady=(18, 4))

    word_label = tk.Label(
        right_panel, text=" ".join("_" for _ in secret_word),
        font=("Arial", 24, "bold"), bg=PANEL, fg=WHITE
    )
    word_label.pack(pady=8)

    lives_label = tk.Label(
        right_panel, text="Incorrect guesses left: 6",
        font=("Arial", 13), bg=PANEL, fg=MUTED
    )
    lives_label.pack(pady=5)

    result_label = tk.Label(
        right_panel, text="Enter one letter to begin.",
        font=("Arial", 11), bg=PANEL, fg=LIGHT_PURPLE,
        wraplength=380
    )
    result_label.pack(pady=8)

    tk.Label(
        right_panel, text="YOUR LETTER", font=("Arial", 11, "bold"),
        bg=PANEL, fg=MUTED
    ).pack(pady=(8, 3))

    letter_entry = tk.Entry(
        right_panel, font=("Arial", 18), width=5, justify="center"
    )
    letter_entry.pack(pady=4)
    letter_entry.focus_set()

    # These buttons are created before check_guess is used.
    button_row = tk.Frame(right_panel, bg=PANEL)
    button_row.pack(pady=8)

    guess_button = tk.Button(
        button_row, text="GUESS", font=("Arial", 11, "bold"),
        bg=PURPLE, fg=WHITE, width=10, pady=5
    )
    guess_button.pack(side="left", padx=5)

    play_again_button = tk.Button(
        button_row, text="PLAY AGAIN", font=("Arial", 10, "bold"),
        bg="#243047", fg=WHITE, width=11, pady=5,
        command=play_game
    )
    # It appears only after the current round ends.

    navigation_row = tk.Frame(right_panel, bg=PANEL)
    navigation_row.pack(pady=6)

    tk.Button(
        navigation_row, text="HOME", font=("Arial", 10),
        bg="#243047", fg=WHITE, width=10,
        command=show_home
    ).pack(side="left", padx=5)

    tk.Button(
        navigation_row, text="STATISTICS", font=("Arial", 10),
        bg="#243047", fg=WHITE, width=10,
        command=show_statistics
    ).pack(side="left", padx=5)

    def check_guess(event=None):
        nonlocal wrong_guesses, game_over

        if game_over:
            return

        letter = letter_entry.get().strip().upper()
        letter_entry.delete(0, tk.END)

        if len(letter) != 1 or not letter.isalpha():
            result_label.config(text="Please enter one letter (A-Z).")
            return

        if letter in guessed_letters:
            result_label.config(text=f"You already tried {letter}.")
            return

        guessed_letters.add(letter)

        if letter in secret_word:
            result_label.config(text=f"Correct! {letter} is in the word.")
        else:
            wrong_guesses += 1
            draw_hangman(wrong_guesses)
            result_label.config(text=f"Sorry! {letter} is not in the word.")

        displayed_word = " ".join(
            char if char in guessed_letters else "_"
            for char in secret_word
        )
        word_label.config(text=displayed_word)

        lives_left = 6 - wrong_guesses
        lives_label.config(text=f"Incorrect guesses left: {lives_left}")

        if all(char in guessed_letters for char in secret_word):
            game_over = True
            stats["wins"] += 1
            result_label.config(text="You won! Great job!")
            messagebox.showinfo("You Win!", f"You guessed the word: {secret_word}")
        elif wrong_guesses >= 6:
            game_over = True
            stats["losses"] += 1
            result_label.config(text=f"Game over! The word was {secret_word}.")
            messagebox.showinfo("Game Over", f"The word was: {secret_word}")

        if game_over:
            guess_button.config(state="disabled")
            letter_entry.config(state="disabled")
            play_again_button.pack(side="left", padx=5)

    guess_button.config(command=check_guess)
    letter_entry.bind("<Return>", check_guess)


# Show the home screen when the program starts.
show_home()
root.mainloop()
