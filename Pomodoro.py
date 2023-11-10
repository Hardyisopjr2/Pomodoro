from tkinter import *
import math
import pyttsx3
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"
reps = 0
time = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    window.after_cancel(time)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer")
    reps=0
    checkbox.config(text="")
    engine.say(text="Timer resetted successfully")
    engine.runAndWait()

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps+=1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps%2!=-0:
        count_down(work_sec)
        timer.config(text="Work", fg=GREEN)
        engine.say(text="Work Time")
        engine.runAndWait()
    elif reps==8:
        count_down(long_break_sec)
        timer.config(text="Break", fg=RED)
        engine.say(text=f"Get a long break of {LONG_BREAK_MIN} minutes")
        engine.runAndWait()
    elif reps%2==0:
        count_down(short_break_sec)
        timer.config(text="Break", fg=PINK)
        engine.say(text=f"Get a short break of {SHORT_BREAK_MIN} minutes")
        engine.runAndWait()

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global time
    count_min = math.floor(count/60)
    count_sec = count%60

    if count_sec<10:
        count_sec=f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count>0:
        time = window.after(1000, count_down, count-1)
    else:
        start_timer()
        checkbox.config(text=int(reps/2)*CHECK_MARK)

# ---------------------------- UI SETUP ------------------------------- #
engine = pyttsx3.init()
window = Tk()
window.title("Pomodoro")
window.config(padx=150, pady=75, bg=YELLOW)

timer = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 40, "bold"), bg=YELLOW)
timer.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tom_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tom_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)

checkbox = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20))
checkbox.grid(column=1, row=3)

window.mainloop()