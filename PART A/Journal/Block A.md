### 21/05/24: Implementing the basics:

Window:

![Screenshot 2024-05-27 221323](https://github.com/catraboom/project-alarm-application/assets/124100757/d065203a-072e-4c36-a8cb-f5fda29b60ce)

_All 6 buttons are clearly shown in this window, as well as the button spacing and the window’s title._

New code:


```
import customtkinter as ctk *1
import tkinter as tk 
from tkinter import *

# Creating a menu
menu = ctk.CTk() *2
menu.title('ALARme') *3
menu.geometry('600x400') *4
menu.resizable(False, False)

# eg. Button 1 (Same for other buttons 2-6 but with different texts, fg_color and text_color)
button_1 = ctk.CTkButton(menu, text='Timer', *5
                         fg_color='red',
                         text_color='white',
                         corner_radius=10)
button_1.pack(pady=10)
…
# Run
menu.mainloop() *6
```


Code explanation:



1. Custom Tkinter, Tkinter and modules within Tkinter are imported.
2. Menu is created.
3. Menu window’s title is created.
4. Menu’s geometry is set.
5. Button 1-6 are customised and inserted into the menu.
6. Menu mainloop is created.

Justification:

This new code:



* Creates the menu window and its title text (ALARme).
* Creates 6 simple buttons to represent the 6 important menus in the application; timer, alarm, stopwatch, calendar, more (for extra features I may implement) and settings.
    * These buttons were all customised in terms of foreground (fg), text and hover colour as well as the corner radius to create aesthetically pleasing buttons with tactility. 

Improvements:

This code will be improved in later iterations in terms of:



* Simple functionality will also be added to these buttons where they will take you to another window to perform further actions.

Sources:



* [Custom Tkinter documentation:](https://customtkinter.tomschimansky.com/)*


### 22/05/24: Refining the menu GUI #1:

Window:

![Screenshot 2024-05-29 173703](https://github.com/catraboom/project-alarm-application/assets/124100757/b8a54993-23fb-4a87-91ea-1c9757be6313)

_All 6 sub-windows are clearly depicted in this image, opened when the user clicks on the corresponding button. Furthermore, the text titles for each window (including menu) are implemented._

New code:


```
# Menu title
title_label = ctk.CTkLabel(menu, text='ALARme', font=('Helvetica', 25)) *1 title_label.pack(pady=1)
…
# eg. Open timer window function (Same for other functions but with different texts and window sizes)
def open_timer_window(): *2
    timer_window = ctk.CTkToplevel(menu) *a
    timer_window.geometry("300x300") *b
    timer_window.resizable(False, False)
    timer_window.title("Timer") *c
    label = ctk.CTkLabel(timer_window, text="Timer", font=('Helvetica', 25)) *d
    label.pack(pady=10)
…
# eg. Calling commands when the timer button is pressed (added to the parameters of each button; same for other buttons but with different functions)
command=open_timer_window *3
…
```


Code explanation:



1. Menu title is customised and inserted into the menu.
2. Functions that open sub-windows are created.

    a. Sub-window is created.
   
    b. Sub-window’s geometry is set.
   
    c. Sub-window’s title is created.
   
    d. Sub-window’s title is customised and inserted into the sub-window.
   
3. Added to the parameters of the buttons 1-6 to allow the sub-windows to be opened when the corresponding button is pressed.

Justification:

This new code:



* Improves upon the basic functionalities present in the first iteration in this project, allowing sub-windows to be executed to clearly represent each feature and allow for multi-tasking.
* Furthermore, slight aesthetic changes were made to the menu window, i.e., the addition of the text title.

<table>
  <tr>
  </tr>
</table>



Improvements:

This code will be improved in later iterations in terms of:



* Aesthetics.
* A more refined menu with appropriate backgrounds and icons to further distinguish each button and their purposes.

Sources:



* [Custom Tkinter documentation:](https://customtkinter.tomschimansky.com/)*


### 24/05/24: Refining the menu GUI #2+settings:

Window:

![Screenshot 2024-06-01 140529](https://github.com/catraboom/project-alarm-application/assets/124100757/3736848e-bf43-4814-a532-b8e710510dfd)

_Improved menu and completed settings sub-window. Furthermore, demonstration of the custom colour using the hexadecimal entry field in the settings menu._

![Screenshot 2024-06-21 110151](https://github.com/catraboom/project-alarm-application/assets/124100757/91ef04ad-e462-4de1-9d48-875754541598)

_Simplistic icons made with Adobe illustrator. From left to right, settings, calendar, stopwatch, timer, alarm and more._

New code:


```
# eg. Settings asset photoimage (Same for other images but with different paths)
settings_asset = PhotoImage(file=r'ASSETS\SettingsAsset.png') *1
settings_asset_adjusted = settings_asset.subsample(4, 4) *2
…
# Change background subtitle
    change_background_label = ctk.CTkLabel(settings_window, text="Change Menu *3
                                           Background",
                                           font=('Helvetica', 20))
    change_background_label.pack(pady=5)

# eg. Light-red Colour preset button (Same for other buttons 8-9 but with different texts, fg_color, text_color and command)
    button_7 = ctk.CTkButton(settings_window, text="Light Red", *4
                             text_color='black',
                             fg_color='#FF474C',
                             command=set_background_red)
    button_7.pack(pady=10)
…
# Custom background subtitle
    custom_background_label = ctk.CTkLabel(settings_window, text="Custom Menu *5
                                           Background",                     
                                           font=('Helvetica', 20))
    custom_background_label.pack(pady=5)
# Enter hexadecimal code
    hex_code = ctk.CTkLabel(settings_window, text="Enter valid hexadecimal code", *6
                            font=('Helvetica', 15))
    hex_code.pack(pady=5)

# Custom background entry boxes
    entries=([ctk.CTkEntry(settings_window, width=2) for _ in range(6)]) *7
    for entry in entries:
        entry.pack(side="left", padx=3)

# Get hexadecimal code information for the entries
    def change_color(): *8
        hex_code = ''.join([entry.get().upper() for entry in entries]) *a
        if len(hex_code) != 6 or not all(validate_hex(c) for c in hex_code): *b
            return
        try:
            menu.config(background=f'#{hex_code}') *c
            # Same for other buttons 2-6
            button_1.configure(bg_color=f'#{hex_code}') *d
…
            title_label.configure(bg_color=f'#{hex_code}') *e
        except tk.TclError: *f
            pass
   
# Validate hex code
    def validate_hex(char): *9
        if char in '0123456789ABCDEFabcdef': *a
            return True
        return False
     
# Custom background confirmation
    confirm_background = ctk.CTkButton(settings_window, text="Confirm", *10
                                       fg_color="blue",
                                       command=change_color)                                      
    confirm_background.pack(side='left', padx=5)

# eg. Change the menu background colour to light-red function (Same for other colours but with different hexadecimal code preset)
def set_background_red(): *11
    menu.config(background='#FF474C') *a
    # Same for other buttons 2-6
    button_1.configure(bg_color='#FF474C') *b
…
    title_label.configure(bg_color='#FF474C') *c
…
# eg. More image, height, width and bigger font added to asset button (added to the parameters of each button; same for other buttons 2-6 but with different paths)
image=more_asset_adjusted, *12
height=50,
width=200,
font=('Helvetica', 20)),
…
# eg. Button 5, i.e., the more button is rearranged by editing side, pady, padx (same for button 6, i.e., the settings button)
button_5.pack(side='left', pady=10, padx=50) *13
…
```


Code explanation:



1. The image's raw file location is classified.
2. The size of the image is manipulated to fit the dimensions of the button.
3. Subtitles for colour presets are customised and inserted into the sub-window.
4. Colour preset buttons are customised and inserted into the sub-window. Corresponding command from *11 is added.
5. Subtitles for custom colour are customised and inserted into the sub-window.
6. Subtitles for hexadecimal entry are customised and inserted into the sub-window.
7. Entries are created, consisting of 6 identical entry fields separated by horizontal padding.
8. Functions that change background colour to custom are created.

    a. Concatenates the 6 entry fields to create a singular input.
   
    b. If all 6 entry fields aren’t filled in, return false.
   
    c. Configure menu colour to specified hexadecimal colour.
   
    d. Configure buttons 1-6 background colour to specified hexadecimal colour.
   
    e. Configure menu title’s background colour to specified hexadecimal colour.
   
    f. Ignore any errors to prevent crashing.
   
9. Function that validates the hexadecimal code entered.

    a. Make sure only hexadecimal characters are entered to return true, otherwise return false.
    
10. Confirm button is customised and inserted into the sub-window.
11. Function that changes background colour to presets are created.

    a. Configure menu colour to preset.
    
    b. Configure buttons 1-6 background colour to preset.
    
    c. Configure menu title’s background colour to preset.
    
12. Added to the parameters of the buttons 1-6 to insert icons, increase their dimensions and fonts.
13. More and settings buttons are rearranged to the side of the screen with horizontal and vertical padding.

Justification:

This new code:



* Improves upon the aesthetics of the previous menu by inserting icons and rearranging the more and settings buttons to separate them from the more important aspects of the application. 
    * Furthermore, the sizes of buttons were increased to decrease the empty space and improve the visibility of the icons.
* The completion of the settings menu; with background customisation using presets or even custom colours.

Improvements:

This code will be improved in later iterations in terms of:



* Optimisation.
* Aesthetics.
* Functionality through completing more sub-windows.

Sources:



* [Custom Tkinter documentation:](https://customtkinter.tomschimansky.com/)*
* [The ultimate introduction to modern GUIs in Python [ with tkinter ]:](https://www.youtube.com/watch?v=mop6g-c5HEY)<sup>🟡</sup>


### 28/05/24: Timer:

Window:

![Screenshot 2024-06-01 221358](https://github.com/catraboom/project-alarm-application/assets/124100757/3ed972d4-3091-4b35-b856-1175f621d4f1)

_Timer window is clearly depicted. [Demonstration.](https://youtu.be/7jkZ-O8Waeg)_

New code:


```
import threading *1
from playsound import playsound
import time
…
# Playsound function to prevent the window from becoming non-responsive
    def play_sound(): *2
        playsound("SOUNDS\Clear Dance Train Melody.mp3")

# Timer countdown function 
    def update_timer(): *3
        global running, times *a
        if running: 
            if times > 0: *b
                min, sec = divmod(times, 60) *c
                hr, min = divmod(min, 60)
                # Same for minutes and seconds
                hours.set(f"{hr:02d}") *d
                times -= 1 *e
                timer_window.after(1000, update_timer) *f
            else:
                # Same for minutes and seconds
                hours.set("00") *g
                running = False
                threading.Thread(target=play_sound).start()

# Start timer function
    def start_timer(): *4
        global running, times
        running = True 
        times = int(hours.get()) * 3600 + int(minutes.get()) * 60 + int(seconds.get()) *a
        update_timer() *b

# Pause timer function
    def pause_timer(): *5
        global running *a
        running = False

# Reset timer function
    def reset_timer(): *6
        global running, times *a
        running = False
        times = 0 *b
        # Same for minutes and seconds
        hours.set("00")

# Hours entry field (same for minutes and seconds but with different horizontal coordinates)
    timerhours=StringVar() *7
    ctk.CTkEntry(timer_window,
                 width=40,
                 textvariable=timerhours,  
                 font=('Helvetica', 25)).place(x=30,
                                               y=50)
    hours.set("00")

# First colon separation label (same for second colon but with different horizontal coordinates)
    timer_colon_1=ctk.CTkLabel(timer_window, text=":", *8
                         font=('Helvetica', 50)).place(x=90,
                                                       y=35)
…
…
# Enter time subtitle
    enter_time=ctk.CTkLabel(timer_window, text="Enter time hh/mm/ss", *9
                            font=('Helvetica', 15)).pack(pady=50)
   
# Start timer button
    start_timer=ctk.CTkButton(timer_window, text="Start", *10
                              width=65,
                              height=25,
                              fg_color="blue",
                              font=('Helvetica', 15),
                              command=start_timer).place(x=30,
                                                         y=140)
   
# Pause timer button
    pause_timer=ctk.CTkButton(timer_window, text="Pause", *11
                              width=65,
                              height=25,
                              fg_color="green",
                              font=('Helvetica', 15),
                              command=pause_timer).place(x=115,
                                                         y=140)

# Reset timer button
    reset_timer=ctk.CTkButton(timer_window, text="Reset", *12
                              width=65,
                              height=25,
                              fg_color="red",
                              font=('Helvetica', 15),
                              command=reset_timer).place(x=200,
                                                         y=140)
…
```


Code explanation:



1. Playsound and threading and time modules within Python are imported.
2. Simple function which uses playsound to locate jingle’s sound file is created.
3. Function that enables the timer to countdown is created.
   
    a. Declares that running and time are global variables.
   
    b. If time is greater than zero, execute consequent code.
   
    c. Convert hours, minutes into seconds.
   
    d. Converts, hours, minutes and seconds data into formatted strings (f).
   
    e. Decreases time by 1 second.
   
    f. Calls the function every 1000 milliseconds or 1 second to reduce lag whilst counting down.
   
    g. When the hours, minutes and seconds all reach zero, it stops decreasing time and starts playing jingle in the background to reduce lag.
   
4. Function which starts the update_timer function is created.
   
    a. When running, calculates the total number of seconds from the users inputted hours, minutes and seconds.
   
    b. Runs the update_timer function.
   
5. Function which pauses the countdown is created.
   
    a. When running, pauses the update_timer function.
   
6. Function which resets the timer.
    
    a. When running, pauses the update_timer function.
   
    b. Sets the times to zero.
   
7. Timer’s hours, minutes and seconds entry fields are customised and inserted into the sub-window.
8. Timer’s 2 semicolon labels are inserted into the sub-window, between the 3 specified entry fields.
9. Instructions subtitle is customised and inserted into the sub-window.
10. Start button is customised and inserted into the sub-window.
11. Pause button is customised and inserted into the sub-window.
12. Reset button is customised and inserted into the sub-window.

Justification:

This new code:



* Creates a timer application which allows the user to input the duration of their timer in hours, minutes and seconds. 
* Furthermore, the start, pause and reset button allows the user to control the duration of their timer.
    * When the timer reaches zero, a ten second jingle would play to notify the user.

Improvements:

This code will be improved in later iterations in terms of:



* Optimisation.
* Customisable jingles using the settings menu.
* Functionality through completing more sub-windows.

Sources:



* [Custom Tkinter documentation:](https://customtkinter.tomschimansky.com/)*
* [The ultimate introduction to modern GUIs in Python [ with tkinter ]:](https://www.youtube.com/watch?v=mop6g-c5HEY)<sup>🟡</sup>
* [How to Create Countdown Timer Using Python | Tkinter Python Project:](https://www.youtube.com/watch?v=KTlT9saZFYc)<sup>🔴</sup>


### 02/06/24 BLOCK A evaluation:



* I was very focused during the two weeks I allocated for this block, allowing me to complete it in almost half the time I allocated to it. 
* However, then again this block wasn’t very complicated compared to the upcoming blocks.
* By completing this block so early, I can dedicate more time to the more complex aspects of this project, including the calendar and alarm system. 
* Furthermore, this gives me time to integrate advanced features into this application.

Overall, this was a very successful block and I hope to replicate this success in the future blocks.
