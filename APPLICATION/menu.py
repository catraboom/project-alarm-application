
# ***** IMPORTS *****

# Importing modules to customise GUI, manage assets and access system data.

import customtkinter as ctk
import tkinter as tk 
from tkinter import *
import threading
import time
import datetime
from tkcalendar import Calendar
import pygame
import os as os

# ***** GLOBAL VARIABLES *****

# Global variables for stopwatch allow the timer to not be running initially and also the hours, minutes and seconds to be set at zero initially and also count laps up by one.
running_stopwatch= False
stopwatch_hours, stopwatch_minutes, stopwatch_seconds = 0, 0, 0
lap_counter = 0

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

# ***** SAVE/LOAD DATA *****

# Save function associates the background colour with an initialisation file.
def save_background_colour(colour):
    with open('INITIALISATION\Sbackground_colour.txt', 'w') as file:
        file.write(colour)

# Load function associates the background colour with an initialisation file.
def load_background_colour():
    if os.path.exists('INITIALISATION\Sbackground_colour.txt'):
        with open('INITIALISATION\Sbackground_colour.txt', 'r') as file:
            return file.read().strip()
    return None

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

# Initialize Pygame's mixer to allow the sound to play and also stop playing when the sub-window is closed.
    pygame.mixer.init()

# Timer countdown function that allows the application to subtract one second off the remaining time until the time is equal to zero.
    def update_timer():
        global running_timer, timer_times
        if running_timer:
            if timer_times > 0:
                timer_minutes, timer_seconds = divmod(timer_times, 60)
                timer_hours, timer_minutes = divmod(timer_minutes, 60)
                timer_hours_entry.set(f"{timer_hours:02d}")
                timer_minutes_entry.set(f"{timer_minutes:02d}")
                timer_seconds_entry.set(f"{timer_seconds:02d}")
                timer_times -= 1
                timer_window.after(1000, update_timer)
            else:
                timer_hours_entry.set("00")
                timer_minutes_entry.set("00")
                timer_seconds_entry.set("00")
                running_timer = False
                threading.Thread(target=play_sound_timer).start()

# Play sound function using pygame to prevent the sub-window from becoming non-responsive.
    def play_sound_timer():
        pygame.mixer.music.load("SOUNDS/Clear Dance Train Melody.mp3")
        pygame.mixer.music.play()

# Stop sound function using pygame to allow the sound to stop playing when the sub-window is closed like before with play sound.
    def stop_sound_timer():
        pygame.mixer.music.stop()
    
# Start timer function that allows the countdown to run.
    def start_timer():
        global running_timer, timer_times
        running_timer = True
        timer_times = int(timer_hours_entry.get()) * 3600 + int(timer_minutes_entry.get()) * 60 + int(timer_seconds_entry.get())
        update_timer()

# Pause timer function which pauses the timer on the current/last saved time data.
    def pause_timer():
        global running_timer
        running_timer = False

# Reset timer function which resets the timer back to zero.
    def reset_timer():
        global running_timer, timer_times
        running_timer = False
        timer_times = 0
        timer_hours_entry.set("00")
        timer_minutes_entry.set("00")
        timer_seconds_entry.set("00")

# Hours entry field to allow users to insert desired hours data.
    timer_hours_entry=StringVar()
    ctk.CTkEntry(timer_window, 
                 width=40,
                 textvariable=timer_hours_entry,  
                 font=('Helvetica', 25)).place(x=30,
                                               y=80)                                              
    timer_hours_entry.set("00")
    
# First colon separation label to visually separate the hours and minutes.
    timer_colon_1_label=ctk.CTkLabel(timer_window, text=":",
                         font=('Helvetica', 50)).place(x=90,
                                                       y=65)
                                                       
# Minutes entry field to allow users to insert minutes data.
    timer_minutes_entry=StringVar()
    ctk.CTkEntry(timer_window, 
                 width=40,
                 textvariable=timer_minutes_entry,  
                 font=('Helvetica', 25)).place(x=130,
                                               y=80)                           
    timer_minutes_entry.set("00")

# Second colon separation label to visually separate the minutes and seconds.
    timer_colon_2_label=ctk.CTkLabel(timer_window, text=":",
                         font=('Helvetica', 50)).place(x=195,
                                                       y=65)
                                                       
# Seconds entry field to allow users to insert seconds data.
    timer_seconds_entry=StringVar()
    ctk.CTkEntry(timer_window, 
                 width=40,
                 textvariable= timer_seconds_entry, 
                 font=('Helvetica', 25)).place(x=235,
                                               y=80)                                     
    timer_seconds_entry.set("00")

# Enter time label to instruct users on how to enter their time data.
    timer_enter_time_label=ctk.CTkLabel(timer_window, text="Enter time hh/mm/ss",
                                        font=('Helvetica', 15))
    timer_enter_time_label.place(x=80,
                                 y=40)
    
# Start timer button which executes the start_timer function.
    start_timer_button=ctk.CTkButton(timer_window, text="Start",
                                     width=65,
                                     height=25,
                                     fg_color="blue",
                                     font=('Helvetica', 15),
                                     command=start_timer).place(x=30,
                                                                y=140)
                                                         
# Pause timer button which executes the pause_timer function.
    pause_timer_button=ctk.CTkButton(timer_window, text="Pause",
                                     width=65,
                                     height=25,
                                     fg_color="green",
                                     font=('Helvetica', 15),
                                     command=pause_timer).place(x=118,
                                                                y=140)
                                                         
# Reset timer button which executes the reset_timer function.
    reset_timer_button=ctk.CTkButton(timer_window, text="Reset",
                                     width=65,
                                     height=25,
                                     fg_color="red",
                                     font=('Helvetica', 15),
                                     command=reset_timer).place(x=208,
                                                                y=140)

# On close function to stop the sound when the sub-window is closed.
    def on_closing_timer():
        stop_sound_timer()
        timer_window.destroy()
    timer_window.protocol("WM_DELETE_WINDOW", on_closing_timer)

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

# Initialize Pygame's mixer to allow the sound to play and also stop playing when the sub-window is closed.
    pygame.mixer.init()

# This label gives context to the time depicted to its right.
    current_time_label= ctk.CTkLabel(alarm_window, text="Current time:",
                                     font=('Helvetica', 20)).place(x=30,
                                                                   y=50)

# Clock function strings together the system's time data and displays it to users.
    def alarm_clock():
        alarm_clock_time= time.strftime("%H:%M:%S %p")
        current_time_display_label.configure(text=alarm_clock_time)
        current_time_display_label.after(1000, alarm_clock)

# This label takes the time data from the function above to display time data.
    current_time_display_label= ctk.CTkLabel(alarm_window, text="",
                                             font=('Helvetica', 20, "bold"))
    current_time_display_label.place(x=160,
                               y=50)
    alarm_clock()

# This label gives context to the day of the week depicted to its right
    day_of_week_label= ctk.CTkLabel(alarm_window, text="Current day:",
                                    font=('Helvetica', 20)).place(x=35,
                                                             y=85)
    
# Day of week function obtains system's day of the week data and displays it to users.
    def dow():
        alarm_dow= time.strftime("%A")
        dow_display_label.configure(text=alarm_dow)
        current_time_display_label.after(1000, dow)

# This label takes the day of week data from the function above to display the day of the week.
    dow_display_label= ctk.CTkLabel(alarm_window, text="",
                                    font=('Helvetica', 20, "bold"))
    dow_display_label.place(x=160,
                            y=85)
    dow()

# Hours entry field to allow users to insert desired hours data.
    alarm_hours_entry=StringVar()
    ctk.CTkEntry(alarm_window, 
                 width=40,
                 textvariable=alarm_hours_entry,  
                 font=('Helvetica', 25)).place(x=30,
                                               y=160)                                              
    alarm_hours_entry.set("00")
    
# First colon separation label to visually separate the hours and minutes.
    alarm_colon_1_label= ctk.CTkLabel(alarm_window, text=":",
                                      font=('Helvetica', 50)).place(x=90,
                                                                    y=145)
                                                       
# Minutes entry field to allow users to insert minutes data.
    alarm_minutes_entry=StringVar()
    ctk.CTkEntry(alarm_window, 
                 width=40,
                 textvariable=alarm_minutes_entry,  
                 font=('Helvetica', 25)).place(x=130,
                                               y=160)                           
    alarm_minutes_entry.set("00")

# Second colon separation label to visually separate the minutes and seconds.
    alarm_colon_2_label=ctk.CTkLabel(alarm_window, text=":",
                                     font=('Helvetica', 50)).place(x=195,
                                                                   y=145)
                                                    
# Seconds entry field to allow users to insert seconds data.
    alarm_seconds_entry=StringVar()
    ctk.CTkEntry(alarm_window, 
                 width=40,
                 textvariable= alarm_seconds_entry, 
                 font=('Helvetica', 25)).place(x=235,
                                               y=160)                                     
    alarm_seconds_entry.set("00")

# Enter time label to instruct users on how to enter their time data.
    alarm_enter_time_label=ctk.CTkLabel(alarm_window, text="Enter time hh/mm/ss",
                                        font=('Helvetica', 15))
    alarm_enter_time_label.place(x=80,
                                 y=120)

# Select day of week option menu, includes all 7 options.
    dow_option_menu= ctk.CTkOptionMenu(alarm_window,
                                       fg_color="green",
                                       dropdown_fg_color="green",
                                       button_color="green",
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
        alarm_time = f"{alarm_hours_entry.get()}:{alarm_minutes_entry.get()}:{alarm_seconds_entry.get()}"
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

# Play sound function using pygame to prevent the sub-window from becoming non-responsive.
    def play_sound_alarm():
        pygame.mixer.music.load("SOUNDS\YJJ City Train Departure Melody.mp3")
        pygame.mixer.music.play()

# Stop sound function using pygame to allow the sound to stop playing when the sub-window is closed like before with play sound.
    def stop_sound_alarm():
        pygame.mixer.music.stop()
    
# Start alarm button which executes the start_alarm function.
    start_alarm_button=ctk.CTkButton(alarm_window, text="Start",
                                     width=130,
                                     height=25,
                                     fg_color="blue",
                                     font=('Helvetica', 15),
                                     command=start_alarm)
    start_alarm_button.place(x=160,
                             y=220)

# On close function to stop the sound when the sub-window is closed.
    def on_closing_alarm():
        stop_sound_alarm()
        alarm_window.destroy()
    alarm_window.protocol("WM_DELETE_WINDOW", on_closing_alarm)
   
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
            stopwatch_display_label.after_cancel(update_time)
            running_stopwatch = False

# Reset stopwatch function will reset the hours, minutes and seconds back to zero and stop counting when executed by the reset button.
    def reset_stopwatch():
        global running_stopwatch, lap_counter
        if running_stopwatch:
            stopwatch_display_label.after_cancel(update_time)
            running_stopwatch = False
        global stopwatch_hours, stopwatch_minutes, stopwatch_seconds
        stopwatch_hours, stopwatch_minutes, stopwatch_seconds = 0, 0, 0
        stopwatch_display_label.configure(text='00:00:00')
        lap_counter = 0
        lapped_display.configure(state="normal")
        lapped_display.delete(1.0, tk.END)
        lapped_display.configure(state="disabled")

# Update stopwatch function will update the time displayed by adding a second to the timer every second. Self executing until time = 0.
    def update_stopwatch():
        global stopwatch_hours, stopwatch_minutes, stopwatch_seconds
        stopwatch_seconds += 1
        if stopwatch_seconds == 60:
            stopwatch_minutes += 1
            stopwatch_seconds = 0
        if stopwatch_minutes == 60:
            stopwatch_hours += 1
            stopwatch_minutes = 0
        stopwatch_hours_string = f'{stopwatch_hours}' if stopwatch_hours > 9 else f'0{stopwatch_hours}'
        stopwatch_minutes_string = f'{stopwatch_minutes}' if stopwatch_minutes > 9 else f'0{stopwatch_minutes}'
        stopwatch_seconds_string = f'{stopwatch_seconds}' if stopwatch_seconds > 9 else f'0{stopwatch_seconds}'
        stopwatch_display_label.configure(text=stopwatch_hours_string + ':' + stopwatch_minutes_string + ':' + stopwatch_seconds_string)
        global update_time
        update_time = stopwatch_display_label.after(1000, update_stopwatch)

# Upon pressing the lap button, the latest time data is retrieved and inserted into the lapped_display entry field.
    def lap_stopwatch():
        global lap_counter
        lap_counter += 1
        current_time = stopwatch_display_label.cget("text")
        lapped_display.configure(state="normal")  
        lapped_display.insert(tk.END, f"Lap {lap_counter}: {current_time}\n") 
        lapped_display.configure(state="disabled")

# Upon closing the stopwatch sub-window, pause/reset stopwatch data is erased to prevent them from reappearing upon reopening.
    def close_stopwatch_window():
        reset_stopwatch()
        stopwatch_window.destroy()
    stopwatch_window.protocol("WM_DELETE_WINDOW", close_stopwatch_window)

# Stopwatch display which will execute the corresponding function._stopwatch.
    stopwatch_display_label= ctk.CTkLabel(stopwatch_window, text="00:00:00",
                                          width=40,  
                                          font=('Helvetica', 60))
    stopwatch_display_label.place(x=30,
                                  y=50)                                                

# Start stopwatch button which will execute the corresponding function.
    start_stopwatch_button= ctk.CTkButton(stopwatch_window, text="Start",
                                          width=55,
                                          height=25,
                                          fg_color="blue",
                                          font=('Helvetica', 15),
                                          command=start_stopwatch)
    start_stopwatch_button.place(x=25,
                                 y=350)                                             

# Pause stopwatch button which will execute the corresponding function.
    pause_stopwatch_button= ctk.CTkButton(stopwatch_window, text="Pause",
                                          width=55,
                                          height=25,
                                          fg_color="green",
                                          font=('Helvetica', 15),
                                          command=pause_stopwatch)
    pause_stopwatch_button.place(x=90,
                                 y=350)                         

# Reset stopwatch button which will execute the corresponding function.
    reset_stopwatch_button= ctk.CTkButton(stopwatch_window, text="Reset",
                                          width=55,
                                          height=25,
                                          fg_color="red",
                                          font=('Helvetica', 15),
                                          command=reset_stopwatch)
    reset_stopwatch_button.place(x=155,
                                 y=350)         
                               
# Lap stopwatch button which will execute the corresponding function.
    lap_stopwatch_button= ctk.CTkButton(stopwatch_window, text="Lap",
                                        width=55,
                                        height=25,
                                        fg_color="purple",
                                        font=('Helvetica', 15),
                                        command=lap_stopwatch)
    lap_stopwatch_button.place(x=220,
                               y=350)

# Lapped time display which will execute the corresponding function.
    lapped_display=ctk.CTkTextbox(stopwatch_window, 
                                  fg_color="#808080",
                                  width=240, 
                                  height=180, 
                                  font=('Helvetica', 26))
    lapped_display.place(x=30,
                         y=140)
    lapped_display.configure(state="disabled")      

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
    calendar_window.geometry('300x500')
    calendar_window.resizable(False, False)
    calendar_window.title('Calendar')
    calendar_window_label = ctk.CTkLabel(calendar_window, text="Calendar",
                         font=('Helvetica', 25))
    calendar_window_label.pack(pady=10)

# Date info function displays the date in dd/mm/yy to the right of the specified date label, as the calendar module's GUI is a bit messy. 
# Furthermore, it will handle whether an event is being displayed on a specific date or not, when executed by the add event button.
    def date_info(event):
        specified_date=calendar.get_date()
        specified_date_label.configure(text=f"Specified date: " + specified_date)
        if specified_date in events:
            event_title_entry.set(events[specified_date].get("title", ""))
            event_description_entry.set(events[specified_date].get("description", ""))
        else:
            event_title_entry.set("Title")
            event_description_entry.set("Description")

# Add event function adds an event to a specific date, saving it in the sub-window's session.
    def add_event():
        specified_date = calendar.get_date()
        title = event_title_entry.get().strip()
        description = event_description_entry.get().strip()
        if title or description:
            events[specified_date] = {"title": title, "description": description}
            
# Create a dictionary to store events created by the user in the session.
    events = {}

# Specified date subtitle, giving context to the date information to the right.
    current_date_time=datetime.datetime.now()
    specified_date_label=ctk.CTkLabel(calendar_window, text="Specified date: " + current_date_time.strftime("%m/%d/%y"),
                                      font=('Helvetica', 18))
    specified_date_label.place(x=10,
                               y=315)

# Event title subtitle, giving context to the entry field below.
    event_title_label=ctk.CTkLabel(calendar_window, text="Enter event title",
                                   font=('Helvetica', 12)).place(x=10,
                                                                 y=345)

# Event description subtitle, giving context to the entry field below.
    event_description_label=ctk.CTkLabel(calendar_window, text="Enter description title",
                                         font=('Helvetica', 12)).place(x=10,
                                                                       y=395)

# This entry field allows the user to input the title of the event they are adding.
    event_title_entry=StringVar()
    ctk.CTkEntry(calendar_window,
                 width=100,
                 font=('Helvetica', 15),
                 textvariable=event_title_entry).place(x=10,
                                                       y=370)                                       
    event_title_entry.set("Title")
    
# This entry field allows the user to input the description of the event they are adding
    event_description_entry=StringVar()
    ctk.CTkEntry(calendar_window,
                 width=280,
                 font=('Helvetica', 15),
                 textvariable=event_description_entry).place(x=10,
                                                             y=420)                                       
    event_description_entry.set("Description")

# Add event button which allows the user to confirm whether they want to add an event to a specific date, executing the date information function.
    add_event_button=ctk.CTkButton(calendar_window, text="Add event",
                                fg_color="blue",
                                font=('Helvetica', 18),
                                width=100,
                                command=add_event)
    add_event_button.place(x=10,
                           y=460)

# Import calendar module and associate it with the calendar window.
    calendar=Calendar(calendar_window,
                    showweeknumbers=False,
                    showothermonthdays=False,
                    background="#2E2E2E",
                    foreground="white",
                    normalbackground="#D9D9D9",
                    weekendbackground="#2E2E2E",
                    weekendforeground="white",
                    font=('Helvetica', 25))
    calendar.place(relx=0,
                   rely=0.12,
                   relwidth=1,
                   relheight=0.5)
    calendar.bind("<<CalendarSelected>>", date_info)

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

# Apply background function applies the background colour to the main menu's background and its widgets.
def apply_background_colour(colour):
    menu.config(background=colour)
    menu_timer_button.configure(bg_color=colour)
    menu_alarm_button.configure(bg_color=colour)
    menu_stopwatch_button.configure(bg_color=colour)
    menu_calendar_button.configure(bg_color=colour)
    menu_settings_button.configure(bg_color=colour)
    menu_title_label.configure(bg_color=colour)
    save_background_colour(colour)

# Validate hexadecimal code to make it is in the hexadecimal range of 0-F.
def validate_hex(char):
    if char in '0123456789ABCDEFabcdef':
        return True
    return False

# Get hexadecimal code information from the data the user's entered into the six entry fields, then change menu background colour to the specified custom, also editing the button/label background colours to match.
def change_colour(hex_entries):
    hex_code = ''.join([entry.get().upper() for entry in hex_entries])
    if len(hex_code) != 6 or not all(validate_hex(c) for c in hex_code):
        return
    try:
        colour = f'#{hex_code}'
        apply_background_colour(colour)
    except tk.TclError:
        pass

# Three functions which change the menu background colour to the specified preset, also editing the button/label background colours to match.
# Light red.
def set_background_red():
    apply_background_colour('#FF474C')

# Light blue.
def set_background_blue():
    apply_background_colour('lightblue')

# Light green.
def set_background_green():
    apply_background_colour('lightgreen')

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
    change_background_label.place(x=35,
                                  y=40)

# The three colour preset buttons which will execute the corresponding global functions.
# Light red.
    light_red_preset_button = ctk.CTkButton(settings_window, text="Light Red",
                                        text_color='black',
                                        fg_color='#FF474C',
                                        command=set_background_red)   
    light_red_preset_button.place(x=80,
                                  y=85)

# Light blue.
    light_blue_preset_button = ctk.CTkButton(settings_window, text="Light Blue",
                                            text_color='black',
                                            fg_color='lightblue',
                                            command=set_background_blue)
    light_blue_preset_button.place(x=80,
                                   y=125)

# Light green.
    light_green_preset_button = ctk.CTkButton(settings_window, text="Light Green",
                                            text_color='black',
                                            fg_color='lightgreen',
                                            command=set_background_green)
    light_green_preset_button.place(x=80,
                                    y=165)

# Custom background label to instruct users on how to change their menu background to a custom colour.
    custom_background_label = ctk.CTkLabel(settings_window, text="Custom Menu Background",
                                           font=('Helvetica', 20))
    custom_background_label.place(x=32,
                                  y=205)
    
# Enter hexadecimal code label to instruct users on how to format the hexadecimal code in the entry fields below.
    hex_code_label = ctk.CTkLabel(settings_window, text="Enter valid hexadecimal code",
                                  font=('Helvetica', 15))
    hex_code_label.place(x=50,
                         y=235)
# The x and y positions of each of the 6 entry boxes, relative to each other
    x_position = 40  
    y_position = 270  

# Six identical custom background entry boxes are created for users to one hexadecimal character to create a valid string of six.
    hex_entries=([ctk.CTkEntry(settings_window, width=2) for _ in range(6)])
    for i, entry in enumerate(hex_entries):
        entry.place(x=x_position, y=y_position)
        x_position += 40
    
# Custom background confirmation button which will execute the corresponding global function.
    confirm_background_button = ctk.CTkButton(settings_window, text="Confirm",
                                            fg_color="blue",
                                            command=lambda: change_colour(hex_entries))
    confirm_background_button.place(x=80,
                                    y=310)

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

# Load and apply the saved background color everytime when the application restarts.
saved_colour = load_background_colour()
if saved_colour:
    apply_background_colour(saved_colour)

# ***** MAINLOOP *****

# Run
menu.mainloop()