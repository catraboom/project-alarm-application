import customtkinter as ctk
import tkinter as tk 
from tkinter import *
import threading
from playsound import playsound
import time

# Creating a menu
menu = ctk.CTk()
menu.title("ALARme")
menu.geometry('600x400')
menu.resizable(False, False)

# Settings asset photoimage
settings_asset = PhotoImage(file=r'ASSETS\SettingsAsset.png')
settings_asset_adjusted = settings_asset.subsample(4, 4)

# More asset photoimage
more_asset = PhotoImage(file=r'ASSETS\SMoreAssets.png')
more_asset_adjusted = more_asset.subsample(5, 5)

# Timer asset photoimage
timer_asset = PhotoImage(file=r'ASSETS\STimerAssets.png')
timer_asset_adjusted = timer_asset.subsample(4, 4)

# Alarm asset photoimage
alarm_asset = PhotoImage(file=r'ASSETS\AlarmAssets.png')
alarm_asset_adjusted = alarm_asset.subsample(3, 3)

# Stopwatch asset photoimage
stopwatch_asset = PhotoImage(file=r'ASSETS\StopwatchAssets.png')
stopwatch_asset_adjusted = stopwatch_asset.subsample(4, 4)

# Calendar asset photoimage
calendar_asset = PhotoImage(file=r'ASSETS\SCalendarAssets.png')
calendar_asset_adjusted = calendar_asset.subsample(4, 4)

# Open timer window function
def open_timer_window():
    timer_window = ctk.CTkToplevel(menu)
    timer_window.geometry("300x200")
    timer_window.resizable(False, False)
    timer_window.title("Timer")
    label = ctk.CTkLabel(timer_window, text="Timer",
                         font=('Helvetica', 25))
    label.pack(pady=10)

# Playsound function to prevent the window from becoming non-responsive
    def play_sound():
        playsound("SOUNDS\Clear Dance Train Melody.mp3")

# Timer countdown function
    def update_timer():
        global running, times
        if running:
            if times > 0:
                min, sec = divmod(times, 60)
                hr, min = divmod(min, 60)
                hours.set(f"{hr:02d}")
                minutes.set(f"{min:02d}")
                seconds.set(f"{sec:02d}")
                times -= 1
                timer_window.after(1000, update_timer)
            else:
                hours.set("00")
                minutes.set("00")
                seconds.set("00")
                running = False
                threading.Thread(target=play_sound).start()

# Start timer function
    def start_timer():
        global running, times
        running = True
        times = int(hours.get()) * 3600 + int(minutes.get()) * 60 + int(seconds.get())
        update_timer()

# Pause timer function
    def pause_timer():
        global running
        running = False

# Stop timer function
    def reset_timer():
        global running, times
        running = False
        times = 0
        hours.set("00")
        minutes.set("00")
        seconds.set("00")

# Hours entry field
    hours=StringVar()
    ctk.CTkEntry(timer_window, 
                 width=40,
                 textvariable=hours,  
                 font=('Helvetica', 25)).place(x=30,
                                               y=50)
    hours.set("00")
# First colon separation label
    colon_1=ctk.CTkLabel(timer_window, text=":",
                         font=('Helvetica', 50)).place(x=90,
                                                       y=35)
# Minutes entry field
    minutes=StringVar()
    ctk.CTkEntry(timer_window, 
                 width=40,
                 textvariable=minutes,  
                 font=('Helvetica', 25)).place(x=130,
                                               y=50)
    minutes.set("00")

# Second colon separation label
    colon_2=ctk.CTkLabel(timer_window, text=":",
                         font=('Helvetica', 50)).place(x=195,
                                                       y=35)
    
# Seconds entry field
    seconds=StringVar()
    ctk.CTkEntry(timer_window, 
                 width=40,
                 textvariable=seconds, 
                 font=('Helvetica', 25)).place(x=235,
                                               y=50)
    seconds.set("00")

# Enter time subtitle
    enter_time=ctk.CTkLabel(timer_window, text="Enter time hh/mm/ss",
                            font=('Helvetica', 15)).pack(pady=50)
    
# Start timer button
    start_timer=ctk.CTkButton(timer_window, text="Start",
                              width=65,
                              height=25,
                              fg_color="blue",
                              font=('Helvetica', 15),
                              command=start_timer).place(x=30,
                                                         y=140)
    
# Pause timer button
    pause_timer=ctk.CTkButton(timer_window, text="Pause",
                              width=65,
                              height=25,
                              fg_color="green",
                              font=('Helvetica', 15),
                              command=pause_timer).place(x=115,
                                                         y=140)

# Stop timer button
    stop_timer=ctk.CTkButton(timer_window, text="Reset",
                              width=65,
                              height=25,
                              fg_color="red",
                              font=('Helvetica', 15),
                              command=reset_timer).place(x=200,
                                                         y=140)

# Open alarm window function
def open_alarm_window():
    alarm_window = ctk.CTkToplevel(menu)
    alarm_window.geometry("300x300")
    alarm_window.resizable(False, False)
    alarm_window.title("Alarm")
    label = ctk.CTkLabel(alarm_window, text="Alarm",
                         font=('Helvetica', 25))
    label.pack(pady=10)

# Open stopwatch window function
def open_stopwatch_window():
    stopwatch_window = ctk.CTkToplevel(menu)
    stopwatch_window.geometry("300x300")
    stopwatch_window.resizable(False, False)
    stopwatch_window.title("Stopwatch")
    label = ctk.CTkLabel(stopwatch_window, text="Stopwatch",
                         font=('Helvetica', 25))
    label.pack(pady=10)

# Open calendar window function
def open_calendar_window():
    calendar_window = ctk.CTkToplevel(menu)
    calendar_window.geometry('300x300')
    calendar_window.resizable(False, False)
    calendar_window.title('Calendar')
    label = ctk.CTkLabel(calendar_window, text="Calendar",
                         font=('Helvetica', 25))
    label.pack(pady=10)

# Open more window function
def open_more_window():
    more_window = ctk.CTkToplevel(menu)
    more_window.geometry('300x300')
    more_window.resizable(False, False)
    more_window.title('More')
    label = ctk.CTkLabel(more_window, text='More features',
                         font=('Helvetica', 25,))
    label.pack(pady=10)

# Open settings window function
def open_settings_window():
    settings_window = ctk.CTkToplevel(menu)
    settings_window.resizable(False, False)
    settings_window.geometry('300x350')
    settings_window.title('Settings')
    label = ctk.CTkLabel(settings_window, text="Settings",
                         font=('Helvetica', 25))
    label.pack(pady=5)

# Change background subtitle
    change_background_label = ctk.CTkLabel(settings_window, text="Change Menu Background",
                                           font=('Helvetica', 20,))
    change_background_label.pack(pady=5)

# Colour preset buttons
    button_7 = ctk.CTkButton(settings_window, text="Light Red",
                             text_color='black',
                             fg_color='#FF474C',
                             command=set_background_red)
    button_7.pack(pady=10)
    button_8 = ctk.CTkButton(settings_window, text="Light Blue",
                             text_color='black',
                             fg_color='lightblue',
                             command=set_background_blue)
    button_8.pack(pady=10)
    button_9 = ctk.CTkButton(settings_window, text="Light Green",
                             text_color='black',
                             fg_color='lightgreen',
                             command=set_background_green)
    button_9.pack(pady=10)

# Custom background subtitle
    custom_background_label = ctk.CTkLabel(settings_window, text="Custom Menu Background",
                                           font=('Helvetica', 20))
    custom_background_label.pack(pady=5)

# Enter hexadecimal code
    hex_code = ctk.CTkLabel(settings_window, text="Enter valid hexadecimal code",
                                           font=('Helvetica', 15))
    hex_code.pack(pady=5)

# Custom background entry boxes
    entries=([ctk.CTkEntry(settings_window, width=2) for _ in range(6)])
    for entry in entries:
        entry.pack(side="left", padx=3)

# Get hexadecimal code information for the entries
    def change_color():
        hex_code = ''.join([entry.get().upper() for entry in entries])
        if len(hex_code) != 6 or not all(validate_hex(c) for c in hex_code):
            return
        try:
            menu.config(background=f'#{hex_code}')
            button_1.configure(bg_color=f'#{hex_code}')
            button_2.configure(bg_color=f'#{hex_code}')
            button_3.configure(bg_color=f'#{hex_code}')
            button_4.configure(bg_color=f'#{hex_code}')
            button_5.configure(bg_color=f'#{hex_code}')
            button_6.configure(bg_color=f'#{hex_code}')
            title_label.configure(bg_color=f'#{hex_code}')
        except tk.TclError:
            pass
    
# Validate hex code
    def validate_hex(char):
        if char in '0123456789ABCDEFabcdef':
            return True
        return False
      
# Custom background confirmation
    confirm_background = ctk.CTkButton(settings_window, text="Confirm",
                                       fg_color="blue",
                                       command=change_color)
    confirm_background.pack(side='left', padx=5)

# Change the menu background colour functions
def set_background_red():
    menu.config(background='#FF474C')
    button_1.configure(bg_color='#FF474C')
    button_2.configure(bg_color='#FF474C')
    button_3.configure(bg_color='#FF474C')
    button_4.configure(bg_color='#FF474C')
    button_5.configure(bg_color='#FF474C')
    button_6.configure(bg_color='#FF474C')
    title_label.configure(bg_color='#FF474C')
    
def set_background_blue():
    menu.config(background='lightblue')
    button_1.configure(bg_color='lightblue')
    button_2.configure(bg_color='lightblue')
    button_3.configure(bg_color='lightblue')
    button_4.configure(bg_color='lightblue')
    button_5.configure(bg_color='lightblue')
    button_6.configure(bg_color='lightblue')
    title_label.configure(bg_color='lightblue')

def set_background_green():
    menu.config(background='lightgreen')    
    button_1.configure(bg_color='lightgreen')
    button_2.configure(bg_color='lightgreen')
    button_3.configure(bg_color='lightgreen')
    button_4.configure(bg_color='lightgreen')
    button_5.configure(bg_color='lightgreen')
    button_6.configure(bg_color='lightgreen')
    title_label.configure(bg_color='lightgreen')

# Menu title
title_label = ctk.CTkLabel(menu, text='ALARme',
                           text_color='white',
                           font=("Helvetica", 25))
title_label.pack(pady=1)

# Menu buttons
button_1 = ctk.CTkButton(menu, text='Timer',
                         fg_color='green',
                         text_color='white',
                         corner_radius=10,
                         height=50,
                         width=200,
                         font=('Helvetica', 20),
                         command=open_timer_window,
                         image=timer_asset_adjusted)
button_1.pack(pady=10)

button_2 = ctk.CTkButton(menu, text='Alarm',
                         fg_color='orange',
                         text_color='white',
                         corner_radius=10,
                         height=50,
                         width=200,
                         font=('Helvetica', 20),
                         command=open_alarm_window,
                         image=alarm_asset_adjusted)
button_2.pack(pady=10)

button_3 = ctk.CTkButton(menu, text='Stopwatch',
                         fg_color='red',
                         text_color='white',
                         corner_radius=10,
                         height=50,
                         width=200,
                         font=('Helvetica', 20),
                         command=open_stopwatch_window,
                         image=stopwatch_asset_adjusted)
button_3.pack(pady=10)

button_4 = ctk.CTkButton(menu, text='Calendar',
                         fg_color='purple',
                         text_color='white',
                         corner_radius=10,
                         height=50,
                         width=200,
                         font=('Helvetica', 20),
                         command=open_calendar_window,
                         image=calendar_asset_adjusted
                        )
button_4.pack(pady=10)

button_5 = ctk.CTkButton(menu, text='More',
                         fg_color='blue',
                         text_color='white',
                         corner_radius=10,
                         height=50,
                         width=200,
                         font=('Helvetica', 20),
                         command=open_more_window,
                         image=more_asset_adjusted)
button_5.pack(side='left', pady=10, padx=50)

button_6 = ctk.CTkButton(menu, text='Settings',
                         fg_color='grey',
                         text_color='black',
                         corner_radius=10,
                         height=50,
                         width=200,
                         font=('Helvetica', 20),
                         command=open_settings_window,
                         image=settings_asset_adjusted)
button_6.pack(side='right', pady=10, padx=50)

# Run
menu.mainloop()