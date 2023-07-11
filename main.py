from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps +=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 ==0:
        count_timer(long_break_sec)
        timer_label.config(text="Break", fg= RED)
    elif reps % 2 == 0:
        count_timer(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_timer(work_sec)
        timer_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_timer(count):

    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_timer, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("                 POMODORO")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

# creating canvas to paste image
canvas = Canvas(width=250, height=250, bg=YELLOW, highlightthickness=0)
# data to give in create img
tomato_img = PhotoImage(file="tomato.png")
# creating (img,text) at x, y coord
canvas.create_image(120, 120, image=tomato_img)
timer_text = canvas.create_text(120, 140, text="00:00", fill="white", font=(FONT_NAME, 20, "bold"))
# showing img
canvas.grid(column=1, row=1)


start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=3, row=2)

check = Label(fg=GREEN, bg=YELLOW)
check.grid(column=1, row=3)

window.mainloop()