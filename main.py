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
#     timer_text = 00:00
    canvas.itemconfig(timer_text, text="00:00")

#     title_label = "Timer"
    timer_label.config(text="Timer")
#     reset check_marks
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps+=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60


    if reps % 8 == 0:
        # if it's the 8th rep: (work time)
        timer_label.config(text="Break", fg=RED)
        count_down(long_break_sec)

    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        # if it's the 2nd, 4th, 6th rep: (short_break time)
        count_down(short_break_sec)

    else:
        # if it's the 1st, 3rd, 5th, 7th rep: (work time)
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    # convert time from sec to min:sec
    count_min = math.floor(count/60)
    count_sec  = count % 60
    # if count_sec == 0:
    #     count_sec == "00"
    # so that sec will get in 07 sec, rather than just 7
    if count_sec < 10:
        count_sec = f"0{count_sec}"


    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        tick_mark = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            tick_mark += "✔"
        check_marks.config(text =tick_mark )

# ---------------------------- UI SETUP ------------------------------- #



window = Tk()
window.title("Pamodoro")
window.config(padx=100, pady=-100, bg = YELLOW)
reps = 0

#  TO ADD TIME in tkinter has build method after
#  after(ms, function,*args) ms is after a mili second , fuction to be called , * args infinite argumnets can be passed through function)

# def say_something(a,b,c):
#     print(a)
#     print(b)
#     print(c)
#
# window.after(1000, say_something(4,6,7))
#
# op: after a milli second
# 4
# 6
# 7


canvas = Canvas(width=200, height=224, bg =YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text = "00:00", fill = "white", font = (FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)



timer_label = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", font=("Arial", 10), highlightthickness=0, command= start_timer)
start_button.grid(column=0, row=3)

rest_button = Button(text="Reset", font=("Arial", 10), highlightthickness=0, command= reset_timer)
rest_button.grid(column=2, row=3)

check_marks = Label(text="", fg = GREEN, bg= YELLOW, font=("Arial", 15))
check_marks.grid(column=1, row=3)




window.mainloop()