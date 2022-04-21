from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"


SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 2
REPS = 8
minutes = '00'
timer_off = False

# ---------------------------- TIMER RESET ------------------------------- #
def reset_pomodoro():
    global timer_off
    main_title['text'] = 'Timer'
    main_title['fg'] = "#9bdeac"
    timer_label['text'] = '00:00'
    clear_all_check_marks = Label(text='         ', bg=YELLOW)
    clear_all_check_marks.place(x=228,y=41)
    timer_off = True



# ---------------------------- TIMER MECHANISM ------------------------------- #
def countdown(work_min):
    global timer_label
    global timer_off
    if timer_off == False:
        main_title['text'] = '▶ Work'
        main_title['fg'] = "#9bdeac"
        main_title.place(x=20, y=-45)
        work_sec = work_min * 60
        while work_sec > -1 and timer_off == False:
            seconds = work_sec % 60
            minutes = work_sec // 60
            if len(str(seconds)) == 1:
                seconds = '0' + str(seconds)
            # canvas.create_text(100, 140, text=f'{minutes}:{seconds}', fill='white', font=(FONT_NAME, 35, 'bold'), tags='timer')
            timer_label['text']=f'{minutes}:{seconds}'
            timer_label.place(x=50, y=112)
            window.update()
            time.sleep(1)
            work_sec -= 1


def breaktime(brkeak_time):
    global timer_off
    if timer_off == False:
        main_title.place(x=20, y=-45)
        main_title['fg'] = "#e7305b"
        main_title['text'] = '■ Break'
        work_sec = brkeak_time * 60

        while work_sec > -1:
            seconds = work_sec % 60
            minutes = work_sec // 60
            if len(str(seconds)) == 1:
                seconds = '0' + str(seconds)
            # canvas.create_text(100, 140, text=f'{minutes}:{seconds}', fill='white', font=(FONT_NAME, 35, 'bold'), tags='timer')
            timer_label = Label(text=f'{minutes}:{seconds}', fg='white', font=(FONT_NAME, 35, 'bold'), background='#F26849')
            timer_label.place(x=50, y=112)
            window.update()
            time.sleep(1)
            work_sec -= 1


def start_pomodoro():
    global REPS
    global WORK_MIN
    global LONG_BREAK_MIN
    global SHORT_BREAK_MIN
    global timer_off
    timer_off = False
    WORK_MIN = int(work_min_entry.get())
    REPS = int(reps_entry.get())

    for n in range(1,REPS):
        countdown(WORK_MIN)
        #check_mark['text'] ='✓️'
        check_mark = Label(text='✓', fg=GREEN, bg=YELLOW)
        check_mark.place(x=228+(n*2), y=41)
        if n % 4 == 0 and n != REPS:
            breaktime(LONG_BREAK_MIN)
        elif n % 4 != 0 and n != REPS:
            breaktime(SHORT_BREAK_MIN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro Timer')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=300, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)  # half width and half heigth of canvas
# canvas.config(state=NORMAL)
# canvas.create_text(100,140, text=f'{minutes}:{seconds}', fill='white', font=(FONT_NAME, 35, 'bold'), tags='timer')
canvas.pack()

# timer_label = Label(text=f'{minutes}:{seconds}', fg='white', font=(FONT_NAME, 35, 'bold'))
# timer_label.place(x=100, y=112)

main_title = Label(text='Timer', fg=GREEN, font=(FONT_NAME, 40, 'bold'))
main_title.config(background=YELLOW)
main_title.place(x=40, y=-45)

start_button = Button(text='Start', highlightbackground=YELLOW, command=start_pomodoro)
start_button.place(x=-40, y=205)

stop_button = Button(text='Reset', highlightbackground=YELLOW, command=reset_pomodoro)
stop_button.place(x=170, y=205)

timer_label = Label(text=f'00:00', fg='white', font=(FONT_NAME, 35, 'bold'), background='#F26849')
timer_label.place(x=50, y=112)

work_min_label = Label(text='Work time', background=YELLOW, fg='black', font=(FONT_NAME, 14, 'bold'))
work_min_label.place(x=230, y=-26)

work_min_entry = Entry(width=3, background='#f7f5dd')
work_min_entry.place(x=310, y=-30)

reps_label = Label(text='Pomodoros', background=YELLOW, fg='black', font=(FONT_NAME, 14, 'bold'))
reps_label.place(x=230, y=2)

reps_entry = Entry(width=3, background='#f7f5dd')
reps_entry.place(x=310, y=-2)

completed_pomodoros_label = Label(text='You completed', background=YELLOW, fg='black', font=(FONT_NAME, 14, 'bold'))
completed_pomodoros_label.place(x=230, y=26)

check_mark = Label(text='', fg=GREEN, bg=YELLOW)
check_mark.place(x=228, y=41)

window.mainloop()