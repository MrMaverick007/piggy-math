import tkinter as tk
import operator
import random

root = tk.Tk()
root.title("Piggy Math")
root.geometry("700x500")

MODES = {
    "*": "Multiplication",
    "/": "Division",
    "+": "Addition",
    "-": "Subtraction",
    "+-*/": "Mix"
}

ops = {
    "*": operator.mul,
    "/": operator.truediv,
    "+": operator.add,
    "-": operator.sub,
}

mode = ""
after_id = None

def show(screen):
    game_problem_label.config(text="")
    screen.tkraise()

current_x, current_y, current_z = 0, 0, 0

def create_problem():
    global mode, current_x, current_y, current_z
    x = random.randint(bounds[0], bounds[1])
    y = random.randint(bounds[0], bounds[1])
    op_symbol = mode
    if mode == "+-*/":
        op_symbol = random.choice(["*", "/", "+", "-"])
    current_x, current_y, current_z = x, y, round(ops[op_symbol](x, y), 2)
    game_problem_label.config(text=f"{x} {op_symbol} {y}", fg="white")

def restore_problem(temp):
    game_problem_label.config(text=temp, fg="white")
    game_submit_entry.config(state="normal")
    game_submit_entry.focus()

def check_answer(e):
    global after_id
    if game_submit_entry.get() == "":
        return
    user_answer = float(game_submit_entry.get())
    if user_answer == current_z:
        game_problem_label.config(text="Correct!", fg="green")
        game_submit_entry.delete(0, tk.END)
        if after_id:
            root.after_cancel(after_id)
        after_id = root.after(1500, create_problem)
    else:
        temp = game_problem_label.cget("text")
        game_problem_label.config(text="Wrong! Try again", fg="red")
        game_submit_entry.delete(0, tk.END)
        game_submit_entry.config(state="disabled")
        if after_id:
            root.after_cancel(after_id)
        after_id = root.after(2000, lambda: restore_problem(temp))

def switch_to_game(pick):
    global mode
    mode = pick
    text = MODES[pick]
    show(game_screen)
    game_title.config(text=text)

def start_game():
    if (game_bound_entry_one.get() == "" or game_bound_entry_two.get() == ""
        or game_bound_entry_one.get() == game_bound_entry_two.get()
        or int(game_bound_entry_one.get()) > int(game_bound_entry_two.get())):
        game_bound_label.config(text="Please Enter Valid Bounds", fg="red")
    else:
        game_bound_label.config(text="Enter Bounds", fg="white")
        bounds[0] = int(game_bound_entry_one.get())
        bounds[1] = int(game_bound_entry_two.get())
        game_submit_entry.place(relx=0.5, rely=0.42, anchor='n', relwidth=0.15)
        game_decimal_hint.place(relx=0.5, rely=0.52, anchor='n')
        create_problem()

# check if input is valid
def make_validator(max_len):
    def validate_input(new_value):
        if new_value == "":
            return True
        return new_value.isdigit() and len(new_value) <= max_len
    return validate_input

def make_answer_validator(max_len):
    def validate_input(new_value):
        if new_value == "":
            return True
        try:
            float(new_value)
            return len(new_value) <= max_len
        except ValueError:
            return False
    return validate_input

bound_limit = (root.register(make_validator(5)), "%P")
answer_limit = (root.register(make_answer_validator(10)), "%P")

# arithmetic screen
bounds = [0, 0]
game_screen = tk.Frame(root)
game_screen.place(relwidth=1, relheight=1)

game_back_button = tk.Button(game_screen, text="← Back", font=("Arial", 10), command=lambda: show(play_screen))
game_back_button.place(relx=0.01, rely=0.01)

game_title = tk.Label(game_screen, font=("Arial", 30))
game_title.place(relx=0.5, rely=0.05, anchor='n')

game_problem_label = tk.Label(game_screen, font=("Arial", 30))
game_problem_label.place(relx=0.5, rely=0.25, anchor='n')

game_submit_entry = tk.Entry(game_screen, bg="white", fg="black", validate="key", validatecommand=answer_limit)
game_submit_entry.bind("<Return>", check_answer)

game_decimal_hint = tk.Label(game_screen, text="Round to 2 decimal places", font=("Arial", 9), fg="gray")

game_bound_label = tk.Label(game_screen, font=("Arial", 15), text="Enter Bounds")
game_bound_label.place(relx=0.5, rely=0.6, anchor='n')

game_bound_entry_one = tk.Entry(game_screen, bg="white", fg="black", validate="key", validatecommand=bound_limit)
game_bound_entry_one.insert(0, "1")
game_bound_entry_one.place(relx=0.42, rely=0.7, anchor='n', relwidth=0.072)

game_bound_entry_two = tk.Entry(game_screen, bg="white", fg="black", validate="key", validatecommand=bound_limit)
game_bound_entry_two.insert(0, "12")
game_bound_entry_two.place(relx=0.58, rely=0.7, anchor='n', relwidth=0.072)

game_start_button = tk.Button(game_screen, text="Start Game", font=("Arial", 15), command=start_game)
game_start_button.place(relx=0.5, rely=0.83, anchor='n')

# play screen
PLAY_BUTTON_WIDTH = 10

play_screen = tk.Frame(root)
play_label = tk.Label(play_screen, text="Play!", font=("Arial", 30))
play_label.place(relx=0.5, rely=0.1, anchor='n')
play_screen.place(relwidth=1, relheight=1)

play_back_button = tk.Button(play_screen, text="← Back", font=("Arial", 10), command=lambda: show(title_screen))
play_back_button.place(relx=0.01, rely=0.01)

tk.Button(play_screen, text="Multiplication", font=("Arial", 15), width=PLAY_BUTTON_WIDTH,
          command=lambda: switch_to_game("*")).place(relx=0.5, rely=0.28, anchor='n')
tk.Button(play_screen, text="Addition", font=("Arial", 15), width=PLAY_BUTTON_WIDTH,
          command=lambda: switch_to_game("+")).place(relx=0.5, rely=0.4, anchor='n')
tk.Button(play_screen, text="Subtraction", font=("Arial", 15), width=PLAY_BUTTON_WIDTH,
          command=lambda: switch_to_game("-")).place(relx=0.5, rely=0.52, anchor='n')
tk.Button(play_screen, text="Division", font=("Arial", 15), width=PLAY_BUTTON_WIDTH,
          command=lambda: switch_to_game("/")).place(relx=0.5, rely=0.64, anchor='n')
tk.Button(play_screen, text="Mix", font=("Arial", 15), width=PLAY_BUTTON_WIDTH,
          command=lambda: switch_to_game("+-*/")).place(relx=0.5, rely=0.76, anchor='n')

# title screen
title_screen = tk.Frame(root)
title_screen.place(relwidth=1, relheight=1)

tk.Label(title_screen, text="Piggy Math!", font=("Arial", 30)).place(relx=0.5, rely=0.2, anchor='n')
tk.Label(title_screen, text="Math Trainer", font=("Arial", 15)).place(relx=0.5, rely=0.35, anchor='n')
tk.Button(title_screen, text="Play Game!", font=("Arial", 15),
          command=lambda: show(play_screen)).place(relx=0.5, rely=0.45, anchor='n')

show(title_screen)
root.mainloop()