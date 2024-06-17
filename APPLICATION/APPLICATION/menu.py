
# ***** IMPORTS *****

# Importing modules to customise GUI, manage assets and access system data.
import customtkinter as ctk
import tkinter as tk 
from tkinter import *
import threading
from playsound import playsound
import time
import datetime

# ***** GLOBAL VARIABLES *****

# Global variables for stopwatch allow the timer to not be running initially and also the hours, minutes and seconds to be set at zero initially.
running_stopwatch= False
stophours, stopminutes, stopseconds = 0, 0, 0

# ***** MENU SETUP *****

# Creating a main menu of a fixed size.
menu = ctk.CTk()
menu.title("ALARme")
menu.geometry('300x400')
menu.resizable(False, False)

# Main menu heading label, displaying the application's name.
menu_title_label = ctk.CTkLabel(menu, text='ALARme',
                           text_color='white',
                           font=("Helvetica", 25))
menu_title_label.pack(pady=1)

# ***** ASSET SETUP *****

# Timer asset Photoimage which has been scaled appropriately to fit the label.
timer_asset = PhotoImage(file=r'ASSETS\STimerAssets.png')
timer_asset_adjusted = timer_asset.subsample(4, 4)

# Alarm asset Photoimage which has been scaled appropriately to fit the label.
alarm_asset = PhotoImage(file=r'ASSETS\AlarmAssets.png')
alarm_asset_adjusted = alarm_asset.subsample(3, 3)

# Stopwatch asset Photoimage which has been scaled appropriately to fit the label.
stopwatch_asset = PhotoImage(file=r'ASSETS\StopwatchAssets.png')
stopwatch_asset_adjusted = stopwatch_asset.subsample(4, 4)

# Calendar asset Photoimage which has been scaled appropriately to fit the label.
calendar_asset = PhotoImage(file=r'ASSETS\SCalendarAssets.png')
calendar_asset_adjusted = calendar_asset.subsample(4, 4)

# Settings asset Photoimage which has been scaled appropriately to fit the label.
settings_asset = PhotoImage(file=r'ASSETS\SettingsAsset.png')
settings_asset_adjusted = settings_asset.subsample(4, 4)

# ***** TIMER SETUP *****

# Open timer window function, executed upon the corresponding button command.
def open_timer_window():
    timer_window = ctk.CTkToplevel(menu)
    timer_window.geometry("300x200")
    timer_window.resizable(False, False)
    timer_window.title("Timer")
    timer_window_label = ctk.CTkLabel(timer_window, text="Timer",
                         font=('Helvetica', 25))
    timer_window_label.pack(pady=10)

# Playsound function is being used to prevent the window from becoming non-responsive.
    def play_sound_timer():
        playsound("SOUNDS\Clear Dance Train Melody.mp3")

# Timer countdown function that allows the application to subtract one second off the remaining time until the time is equal to zero.
    def update_timer():
        global running_timer, times
        if running_timer:
            if times > 0:
                min, sec = divmod(times, 60)
                hr, min = divmod(min, 60)
                timerhours.set(f"{hr:02d}")
                timerminutes.set(f"{min:02d}")
                timerseconds.set(f"{sec:02d}")
                times -= 1
                timer_window.after(1000, update_timer)
            else:
                timerhours.set("00")
                timerminutes.set("00")
                timerseconds.set("00")
                running_timer = False
                threading.Thread(target=play_sound_timer).start()

# Start timer function that allows the countdown to run.
    def start_timer():
        global running_timer, times
        running_timer = True
        times = int(timerhours.get()) * 3600 + int(timerminutes.get()) * 60 + int(timerseconds.get())
        update_timer()

# Pause timer function which pauses the timer on the current/last saved time data.
    def pause_timer():
        global running_timer
        running_timer = False

# Reset timer function which resets the timer back to zero.
    def reset_timer():
        global running_timer, times
        running_timer = False
        times = 0
        timerhours.set("00")
        timerminutes.set("00")
        timerseconds.set("00")

# Hours entry field to allow users to insert desired hours data.
    timerhours=StringVar()
    ctk.CTkEntry(timer_window, 
                 width=40,
                 textvariable=timerhours,  
                 font=('Helvetica', 25)).place(x=30,
                                               y=50)                                              
    timerhours.set("00")
    
# First colon separation label to visually separate the hours and minutes.
    timer_colon_1=ctk.CTkLabel(timer_window, text=":",
                         font=('Helvetica', 50)).place(x=90,
                                                       y=35)
                                                       
# Minutes entry field to allow users to insert minutes data.
    timerminutes=StringVar()
    ctk.CTkEntry(timer_window, 
                 width=40,
                 textvariable=timerminutes,  
                 font=('Helvetica', 25)).place(x=130,
                                               y=50)                           
    timerminutes.set("00")

# Second colon separation label to visually separate the minutes and seconds.
    timer_colon_2=ctk.CTkLabel(timer_window, text=":",
                         font=('Helvetica', 50)).place(x=195,
                                                       y=35)
                                                       
# Seconds entry field to allow users to insert seconds data.
    timerseconds=StringVar()
    ctk.CTkEntry(timer_window, 
                 width=40,
                 textvariable= timerseconds, 
                 font=('Helvetica', 25)).place(x=235,
                                               y=50)                                     
    timerseconds.set("00")

# Enter time label to instruct users on how to enter their time data.
    timer_enter_time=ctk.CTkLabel(timer_window, text="Enter time hh/mm/ss",
                            font=('Helvetica', 15))
    timer_enter_time.pack(pady=50)
    
# Start timer button which executes the start_timer function.
    start_timer=ctk.CTkButton(timer_window, text="Start",
                              width=65,
                              height=25,
                              fg_color="blue",
                              font=('Helvetica', 15),
                              command=start_timer).place(x=30,
                                                         y=140)
                                                         
# Pause timer button which executes the pause_timer function.
    pause_timer=ctk.CTkButton(timer_window, text="Pause",
                              width=65,
                              height=25,
                              fg_color="green",
                              font=('Helvetica', 15),
                              command=pause_timer).place(x=115,
                                                         y=140)
                                                         
# Reset timer button which executes the reset_timer function.
    reset_timer=ctk.CTkButton(timer_window, text="Reset",
                              width=65,
                              height=25,
                              fg_color="red",
                              font=('Helvetica', 15),
                              command=reset_timer).place(x=200,
                                                         y=140)

# Main menu timer button, can be used to open the timer sub-window above.
menu_timer_button = ctk.CTkButton(menu, text='Timer',
                         fg_color='green',
                         text_color='white',
                         corner_radius=10,
                         height=50,
                         width=200,
                         font=('Helvetica', 20),
                         command=open_timer_window,
                         image=timer_asset_adjusted)
menu_timer_button.pack(pady=10)

# ***** ALARM SETUP *****

# Open alarm window function, executed upon the corresponding button command.
def open_alarm_window():
    alarm_window = ctk.CTkToplevel(menu)
    alarm_window.geometry("300x305")
    alarm_window.resizable(False, False)
    alarm_window.title("Alarm")
    alarm_window_label = ctk.CTkLabel(alarm_window, text="Alarm",
                         font=('Helvetica', 25))
    alarm_window_label.pack(pady=10)

# Playsound function is being used to prevent the window from becoming non-responsive.
    def play_sound_alarm():
        playsound("SOUNDS\YJJ City Train Departure Melody.mp3")

# This label gives context to the time depicted to its right.
    current_time= ctk.CTkLabel(alarm_window, text="Current time:",
                               font=('Helvetica', 20)).place(x=30,
                                                             y=50)

# Clock function strings together the system's time data and displays it to users.
    def alarmclock():
        alarm_clock_time= time.strftime("%H:%M:%S %p")
        current_time_display.configure(text=alarm_clock_time)
        current_time_display.after(1000, alarmclock)

# This label takes the time data from the function above to display time data.
    current_time_display= ctk.CTkLabel(alarm_window, text="",
                                       font=('Helvetica', 20, "bold"))
    current_time_display.place(x=160,
                               y=50)
    alarmclock()

# This label gives context to the day of the week depicted to its right
    day_of_week= ctk.CTkLabel(alarm_window, text="Current day:",
                               font=('Helvetica', 20)).place(x=35,
                                                             y=85)
    
# Day of week function obtains system's day of the week data and displays it to users.
    def dow():
        alarm_dow= time.strftime("%A")
        dow_display.configure(text=alarm_dow)
        current_time_display.after(1000, dow)

# This label takes the day of week data from the function above to display the day of the week.
    dow_display= ctk.CTkLabel(alarm_window, text="",
                                       font=('Helvetica', 20, "bold"))
    dow_display.place(x=160,
                      y=85)
    dow()

# Hours entry field to allow users to insert desired hours data.
    alarmhours=StringVar()
    ctk.CTkEntry(alarm_window, 
                 width=40,
                 textvariable=alarmhours,  
                 font=('Helvetica', 25)).place(x=30,
                                               y=130)                                              
    alarmhours.set("00")
    
# First colon separation label to visually separate the hours and minutes.
    alarm_colon_1= ctk.CTkLabel(alarm_window, text=":",
                         font=('Helvetica', 50)).place(x=90,
                                                       y=115)
                                                       
# Minutes entry field to allow users to insert minutes data.
    alarmminutes=StringVar()
    ctk.CTkEntry(alarm_window, 
                 width=40,
                 textvariable=alarmminutes,  
                 font=('Helvetica', 25)).place(x=130,
                                               y=130)                           
    alarmminutes.set("00")

# Second colon separation label to visually separate the minutes and seconds.
    alarm_colon_2=ctk.CTkLabel(alarm_window, text=":",
                         font=('Helvetica', 50)).place(x=195,
                                                       y=115)
                                                       
# Seconds entry field to allow users to insert seconds data.
    alarmseconds=StringVar()
    ctk.CTkEntry(alarm_window, 
                 width=40,
                 textvariable= alarmseconds, 
                 font=('Helvetica', 25)).place(x=235,
                                               y=130)                                     
    alarmseconds.set("00")

# Enter time label to instruct users on how to enter their time data.
    alarm_enter_time=ctk.CTkLabel(alarm_window, text="Enter time hh/mm/ss",
                            font=('Helvetica', 15))
    alarm_enter_time.place(x=80,
                           y=180)

# Select day of week option menu, includes all 7 options.
    dow_option_menu= ctk.CTkOptionMenu(alarm_window,
                                       fg_color="green",
                                       dropdown_fg_color="green",
                                       width=130,
                                       height=25,
                                       values=["Monday",
                                               "Tuesday",
                                               "Wednesday",
                                               "Thursday",
                                               "Friday",
                                               "Saturday",
                                               "Sunday"])
    dow_option_menu.place(x=10,
                          y=220)

# Repeat? Checkbox allows users to specify whether they want to repeat the alarm every week.
    repeat_var= tk.BooleanVar()
    repeat_checkbox= ctk.CTkCheckBox(alarm_window, text="Repeat?",
                                     fg_color="red",
                                     font=('Helvetica', 15),
                                     variable=repeat_var)
    repeat_checkbox.place(x=110,
                          y=265)

# Start alarm function will start the alarm when the day of the week and time during that day is selected.
    def start_alarm():
        alarm_time = f"{alarmhours.get()}:{alarmminutes.get()}:{alarmseconds.get()}"
        alarm_day = dow_option_menu.get()
        repeat = repeat_var.get()

# Check alarm function will check if the day/time of the alarm matches up.
        def check_alarm(alarm_day):
            now = datetime.datetime.now()
            current_time = now.strftime("%H:%M:%S")
            current_day = now.strftime("%A")
            if current_time == alarm_time and current_day == alarm_day:
                threading.Thread(target=play_sound_alarm).start()
                if repeat:
                    next_week = now + datetime.timedelta(days=7)
                    alarm_day = next_week.strftime("%A")
            alarm_window.after(1000, lambda: check_alarm(alarm_day))
        check_alarm(alarm_day)
    
# Start alarm button which executes the start_alarm function.
    start_alarm_button=ctk.CTkButton(alarm_window, text="Start",
                              width=130,
                              height=25,
                              fg_color="blue",
                              font=('Helvetica', 15),
                              command=start_alarm)
    start_alarm_button.place(x=160,
                             y=220)
    
# Main menu alarm button, can be used to open the settings sub-window above.
menu_alarm_button = ctk.CTkButton(menu, text='Alarm',
                         fg_color='orange',
                         text_color='white',
                         corner_radius=10,
                         height=50,
                         width=200,
                         font=('Helvetica', 20),
                         command=open_alarm_window,
                         image=alarm_asset_adjusted)
menu_alarm_button.pack(pady=10)

# ***** STOPWATCH SETUP *****

# Open stopwatch window function, executed upon the corresponding button command.
def open_stopwatch_window():
    stopwatch_window = ctk.CTkToplevel(menu)
    stopwatch_window.geometry("300x400")
    stopwatch_window.resizable(False, False)
    stopwatch_window.title("Stopwatch")
    stopwatch_window_label = ctk.CTkLabel(stopwatch_window, text="Stopwatch",
                         font=('Helvetica', 25))
    stopwatch_window_label.pack(pady=10)

# Start stopwatch function will allow the application to count up by one when executed by the start button.
    def start_stopwatch():
        global running_stopwatch
        if not running_stopwatch:
            update_stopwatch()
            running_stopwatch= True

# Pause stopwatch function will stop the application from counting up by one when executed by the pause button.   
    def pause_stopwatch():
        global running_stopwatch
        if running_stopwatch:
            stopwatch_display.after_cancel(update_time)
            running_stopwatch = False

# Reset stopwatch function will reset the hours, minutes and seconds back to zero and stop counting when executed by the reset button.
    def reset_stopwatch():
        global running_stopwatch
        if running_stopwatch:
            stopwatch_display.after_cancel(update_time)
            running_stopwatch = False
        global stophours, stopminutes, stopseconds
        stophours, stopminutes, stopseconds = 0, 0, 0
        stopwatch_display.configure(text='00:00:00')

# Update stopwatch function will update the time displayed by adding a second to the timer every second. Self executing until time = 0.
    def update_stopwatch():
        global stophours, stopminutes, stopseconds
        stopseconds += 1
        if stopseconds == 60:
            stopminutes += 1
            stopseconds = 0
        if stopminutes == 60:
            stophours += 1
            stopminutes = 0
        stophours_string = f'{stophours}' if stophours > 9 else f'0{stophours}'
        stopminutes_string = f'{stopminutes}' if stopminutes > 9 else f'0{stopminutes}'
        stopseconds_string = f'{stopseconds}' if stopseconds > 9 else f'0{stopseconds}'
        stopwatch_display.configure(text=stophours_string + ':' + stopminutes_string + ':' + stopseconds_string)
        global update_time
        update_time = stopwatch_display.after(1000, update_stopwatch)

# Upon pressing the lap button, the latest time data is retrieved and inserted into the lapped_display entry field.
    def lap_stopwatch():
        current_time = stopwatch_display.cget("text")
        current_laps = lapped_display.get()
        lapped_display.set(current_laps + " " + current_time)

# Upon closing the stopwatch sub-window, pause/reset stopwatch data is erased to prevent them from reappearing upon reopening.
    def close_stopwatch_window():
        reset_stopwatch()
        stopwatch_window.destroy()
    stopwatch_window.protocol("WM_DELETE_WINDOW", close_stopwatch_window)

# Stopwatch display which will execute the corresponding function._stopwatch.
    stopwatch_display= ctk.CTkLabel(stopwatch_window, text="00:00:00",
                                                    width=40,  
                                                    font=('Helvetica', 60),)
    stopwatch_display.place(x=30, y=50)                                                

# Start stopwatch button which will execute the corresponding function.
    start_stopwatch_button= ctk.CTkButton(stopwatch_window, text="Start",
                                   width=55,
                                   height=25,
                                   fg_color="blue",
                                   font=('Helvetica', 15),
                                   command=start_stopwatch)
    start_stopwatch_button.place(x=25,y=350)                                             

# Pause stopwatch button which will execute the corresponding function.
    pause_stopwatch_button= ctk.CTkButton(stopwatch_window, text="Pause",
                                   width=55,
                                   height=25,
                                   fg_color="green",
                                   font=('Helvetica', 15),
                                   command=pause_stopwatch)
    pause_stopwatch_button.place(x=90, y=350)                         

# Reset stopwatch button which will execute the corresponding function.
    reset_stopwatch_button= ctk.CTkButton(stopwatch_window, text="Reset",
                                   width=55,
                                   height=25,
                                   fg_color="red",
                                   font=('Helvetica', 15),
                                   command=reset_stopwatch)
    reset_stopwatch_button.place(x=155, y=350)         
                               
# Lap stopwatch button which will execute the corresponding function.
    lap_stopwatch_button= ctk.CTkButton(stopwatch_window, text="Lap",
                                    width=55,
                                    height=25,
                                    fg_color="purple",
                                    font=('Helvetica', 15),
                                    command=lap_stopwatch)
    lap_stopwatch_button.place(x=220, y=350)

# Lapped time display which will execute the corresponding function.
    lapped_display=StringVar()
    ctk.CTkEntry(stopwatch_window, 
                 width=240,
                 height=180,
                 textvariable=lapped_display, 
                 font=('Helvetica', 25)).place(x=30,
                                               y=140)
    lapped_display.set("")

# Main menu stopwatch button, can be used to open the settings sub-window above.
menu_stopwatch_button = ctk.CTkButton(menu, text='Stopwatch',
                         fg_color='red',
                         text_color='white',
                         corner_radius=10,
                         height=50,
                         width=200,
                         font=('Helvetica', 20),
                         command=open_stopwatch_window,
                         image=stopwatch_asset_adjusted)
menu_stopwatch_button.pack(pady=10)

# ***** CALENDAR SETUP *****

# Open calendar window function, executed upon the corresponding button command.
def open_calendar_window():
    calendar_window = ctk.CTkToplevel(menu)
    calendar_window.geometry('300x300')
    calendar_window.resizable(False, False)
    calendar_window.title('Calendar')
    calendar_window_label = ctk.CTkLabel(calendar_window, text="Calendar",
                         font=('Helvetica', 25))
    calendar_window_label.pack(pady=10)

# Main menu calendar button, can be used to open the settings sub-window above.
menu_calendar_button = ctk.CTkButton(menu, text='Calendar',
                         fg_color='purple',
                         text_color='white',
                         corner_radius=10,
                         height=50,
                         width=200,
                         font=('Helvetica', 20),
                         command=open_calendar_window,
                         image=calendar_asset_adjusted)
menu_calendar_button.pack(pady=10)

# ***** SETTINGS SETUP *****

# Open settings window function, executed upon the corresponding button command.
def open_settings_window():
    settings_window = ctk.CTkToplevel(menu)
    settings_window.resizable(False, False)
    settings_window.geometry('300x350')
    settings_window.title('Settings')
    settings_window_label = ctk.CTkLabel(settings_window, text="Settings",
                         font=('Helvetica', 25))
    settings_window_label.pack(pady=5)

# Change background label to instruct users on how to change their menu background to a preset colour.
    change_background_label = ctk.CTkLabel(settings_window, text="Change Menu Background",
                                           font=('Helvetica', 20,))
    change_background_label.pack(pady=5)

# The three colour preset buttons which will execute the corresponding global functions.
# Light red.
    light_red_preset = ctk.CTkButton(settings_window, text="Light Red",
                             text_color='black',
                             fg_color='#FF474C',
                             command=set_background_red)   
    light_red_preset.pack(pady=10)

# Light blue.
    light_blue_preset = ctk.CTkButton(settings_window, text="Light Blue",
                             text_color='black',
                             fg_color='lightblue',
                             command=set_background_blue)
    light_blue_preset.pack(pady=10)

# Light green.
    light_green_preset = ctk.CTkButton(settings_window, text="Light Green",
                             text_color='black',
                             fg_color='lightgreen',
                             command=set_background_green)
    light_green_preset.pack(pady=10)

# Custom background label to instruct users on how to change their menu background to a custom colour.
    custom_background_label = ctk.CTkLabel(settings_window, text="Custom Menu Background",
                                           font=('Helvetica', 20))
    custom_background_label.pack(pady=5)

# Enter hexadecimal code label to instruct users on how to format the hexadecimal code in the entry fields below.
    hex_code_label = ctk.CTkLabel(settings_window, text="Enter valid hexadecimal code",
                                           font=('Helvetica', 15))
    hex_code_label.pack(pady=5)

# Six identical custom background entry boxes are created for users to one hexadecimal character to create a valid string of six.
    entries=([ctk.CTkEntry(settings_window, width=2) for _ in range(6)])
    for entry in entries:
        entry.pack(side="left",
                   padx=3)

# Get hexadecimal code information from the data the user's entered into the six entry fields, then change menu background colour to the specified custom, also editing the button/label background colours to match.
    def change_color():
        hex_code = ''.join([entry.get().upper() for entry in entries])
        if len(hex_code) != 6 or not all(validate_hex(c) for c in hex_code):
            return
        try:
            menu.config(background=f'#{hex_code}')
            menu_timer_button.configure(bg_color=f'#{hex_code}')
            menu_alarm_button.configure(bg_color=f'#{hex_code}')
            menu_stopwatch_button.configure(bg_color=f'#{hex_code}')
            menu_calendar_button.configure(bg_color=f'#{hex_code}')
            menu_settings_button.configure(bg_color=f'#{hex_code}')
            menu_title_label.configure(bg_color=f'#{hex_code}')
        except tk.TclError:
            pass
    
# Validate hexadecimal code to make it is in the hexadecimal range of 0-F.
    def validate_hex(char):
        if char in '0123456789ABCDEFabcdef':
            return True
        return False
    
# Custom background confirmation button which will execute the corresponding global function.
    confirm_background = ctk.CTkButton(settings_window, text="Confirm",
                                       fg_color="blue",
                                       command=change_color)
    confirm_background.pack(side='left',
                            padx=5)

# Three functions which change the menu background colour to the specified preset, also editing the button/label background colours to match (these are global functions and need to be inserted at the end).
# Light red.
def set_background_red():
    menu.config(background='#FF474C')
    menu_timer_button.configure(bg_color='#FF474C')
    menu_alarm_button.configure(bg_color='#FF474C')
    menu_stopwatch_button.configure(bg_color='#FF474C')
    menu_calendar_button.configure(bg_color='#FF474C')
    menu_settings_button.configure(bg_color='#FF474C')
    menu_title_label.configure(bg_color='#FF474C')

# Light blue.   
def set_background_blue():
    menu.config(background='lightblue')
    menu_timer_button.configure(bg_color='lightblue')
    menu_alarm_button.configure(bg_color='lightblue')
    menu_stopwatch_button.configure(bg_color='lightblue')
    menu_calendar_button.configure(bg_color='lightblue')
    menu_settings_button.configure(bg_color='lightblue')
    menu_title_label.configure(bg_color='lightblue')

# Light green.
def set_background_green():
    menu.config(background='lightgreen')    
    menu_timer_button.configure(bg_color='lightgreen')
    menu_alarm_button.configure(bg_color='lightgreen')
    menu_stopwatch_button.configure(bg_color='lightgreen')
    menu_calendar_button.configure(bg_color='lightgreen')
    menu_settings_button.configure(bg_color='lightgreen')
    menu_title_label.configure(bg_color='lightgreen')

# Main menu settings button, can be used to open the settings sub-window above.
menu_settings_button = ctk.CTkButton(menu, text='Settings',
                         fg_color='grey',
                         text_color='white',
                         corner_radius=10,
                         height=50,
                         width=200,
                         font=('Helvetica', 20),
                         command=open_settings_window,
                         image=settings_asset_adjusted)
menu_settings_button.pack(pady=10)

# ***** MAINLOOP *****

# Run
menu.mainloop()
