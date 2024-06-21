### 04/06/24: Stopwatch GUI:

Window:

![Screenshot 2024-06-05 212312](https://github.com/catraboom/project-alarm-application/assets/124100757/4eb2eb03-cdca-4d2b-8942-cc4924bba980)

_Stopwatch window’s GUI clearly depicted._

New code:


```
# Stopwatch display
    stopwatch_display= ctk.CTkLabel(stopwatch_window, text="00:00:00", *1
                                                    width=40,  
                                                    font=('Helvetica', 60),).place(x=30,
                                                                                   y=50)

# Lapped time display
    lapped_display=StringVar() *3
    ctk.CTkEntry(stopwatch_window,
                 width=240,
                 height=180,
                 textvariable=lapped_display,
                 font=('Helvetica', 25)).place(x=30,
                                               y=140)
    lapped_display.set("")

# Start stopwatch button (same for pause, reset and lap buttons but with different text, fg_color and horizontal coordinates)
    start_stopwatch= ctk.CTkButton(stopwatch_window, text="Start", *2
                                   width=55,
                                   height=25,
                                   fg_color="blue",
                                   font=('Helvetica', 15)).place(x=25,
                                                              y=350)
…
```


Code explanation:



1. The stopwatch’s display is customised and inserted into the sub-window (currently at 00:00:00 to indicate that it hasn't started yet).
2. The lapped times entry field is customised and inserted into the sub-window (Users can utilise this entry field to write notes or click the lap button to imprint current time data).
3. The start, pause, reset and lap buttons are customised and inserted into the sub-window.

Justification:

This new code:



* Creates a simple stopwatch GUI that is aesthetically pleasing and fits the stylistic considerations of the previous settings and timer subwindows.
* Furthermore, later functionalities are easily observable through this GUI’s layout, making it easier to highlight bugs. 
* Due to technical difficulties, I couldn’t complete the logic as well as the GUI for this entry.

Improvements:

This code will be improved in later iterations in terms of:



* Addressing the technical difficulties I faced, preventing me from developing the logic.
    * To tackle this, I will organise the entire code block in the next entry to make errors more easy to troubleshoot.
* Only after this, I will work on the logic within the stopwatch application.

Sources:



* [Custom Tkinter documentation:](https://customtkinter.tomschimansky.com/)*


### 06/06/24: Code organisation #1:

Edited/reorganised code: 



```
# ***** ASSET SETUP ***** # *1

# Timer asset Photoimage which has been scaled appropriately to fit the label. *2
timer_asset = PhotoImage(file=r'ASSETS\STimerAssets.png') 
…
# Alarm asset Photoimage which has been scaled appropriately to fit the label. *2, *3
alarm_asset = … 
# Stopwatch asset Photoimage which has been scaled appropriately to fit the label. *2
stopwatch_asset= …
# Calendar asset Photoimage which has been scaled appropriately to fit the label. *2
calendar_asset= …
# More asset Photoimage which has been scaled appropriately to fit the label. *2
more_asset= …
# Settings asset Photoimage which has been scaled appropriately to fit the label. *2
settings_asset= …
…
# ***** TIMER SETUP ***** *1

# Open timer window function, executed upon the corresponding button command. *2
def open_timer_window():
    timer_window = ctk.CTkToplevel(menu)
    timer_window.geometry("300x200")
    timer_window.resizable(False, False)
    timer_window.title("Timer")
    timer_window_label = ctk.CTkLabel(timer_window, text="Timer", *4
                         font=('Helvetica', 25))
    timer_window_label.pack(pady=10)
…
menu_timer_button = ctk.CTkButton(menu, text='Timer', *5
                         fg_color='green',
                         text_color='white',
                         corner_radius=10,
                         height=50,
                         width=200,
                         font=('Helvetica', 20),
                         command=open_timer_window,
                         image=timer_asset_adjusted)
menu_timer_button.pack(pady=10) *6

# ***** ALARM SETUP ***** *1, *3

    alarm_window_label = …

# ***** STOPWATCH SETUP ***** *1

    stopwatch_window_label = …


# ***** CALENDAR SETUP ***** *1

    calendar_window_label = …

# ***** MORE SETUP ***** *1

    more_window_label = …

# ***** SETTINGS SETUP ***** *1

    settings_window_label = …
…
# The three colour preset buttons which will execute the corresponding global functions. *2
# Light red.
    light_red_preset = ctk.CTkButton(settings_window, text="Light Red", *7
                             text_color='black',
                             fg_color='#FF474C',
                             command=set_background_red)
    light_red_preset.pack(pady=10) *6

# Light blue.
    light_blue_preset = … *3

# Light green.
    light_green_preset = …
…
```


Code explanation:



1. Capitalised comments that are buffered above and below provide clear headings for key features.
2. Comments for components within key features are given more information to clearly outline the functionality. 
3. Key features are now listed in this order: timer, alarm, stopwatch, calendar, more and settings to keep the code organised.
4. Timer, alarm, stopwatch, calendar, more and settings subwindow title label’s have been renamed from “`label`” to more specific `[key feature]_window_label.`
5. Timer, alarm, stopwatch, calendar, more and settings buttons have been renamed from `button_[1/2/3/4/5/6]` to more specific `menu_[key feature]_button.`
6. The buttons are packed to the window after customisation rather than in customisation (eg. `command=set_background_red).pack(pady=10)`) to prevent “NoneType” error which arose during the development of stopwatch logic.
7. Light red, light blue and light green colour presets have been renamed from `button_[7/8/9]`

    to more specific `light_[colour]_preset.`


Additional changes:



* Renamed most of the code descriptions to make them more specific and detailed.

Justification:

This new code:



* Organised the code primarily to order the key features in this pattern: timer, alarm, stopwatch, calendar, more and settings including adding their corresponding main menu buttons within them rather than all at the end.
* Added capitalised comments to more easily differentiate key features.
* Edited existing comments to make them more descriptive (a few changes were shown here).
* Renamed many buttons/labels etc. to keep them organised and prevent generalisation (a few changes were shown here).

Improvements:

This code will be improved in later iterations in terms of:



* Adding logic to the stopwatch as through organisation, I have identified the reason for the “NoneType” error which prevented the stopwatch functions from executing correctly.
* Later refinements to code’s setup may also be implemented.

Sources:



* [Custom Tkinter documentation:](https://customtkinter.tomschimansky.com/)*


### 08/06/24: Stopwatch logic:

Window:

![Screenshot 2024-06-07 114528](https://github.com/catraboom/project-alarm-application/assets/124100757/1faaf942-2e74-4048-b36a-35debbab29a4)

_Stopwatch window is clearly depicted. [Demonstration.](https://youtu.be/yO6hZOubhYk)_

New code:


```
# Global variables for stopwatch allow the timer to not be running initially and also the hours, minutes and seconds to be set at zero initially.
running_stopwatch= False *1
stophours, stopminutes, stopseconds = 0, 0, 0
…
# Start stopwatch function will allow the application to count up by one when executed by the start button.
    def start_stopwatch(): *2
        global running_stopwatch
        if not running_stopwatch: *a
            update_stopwatch()
            running_stopwatch= True

# Pause stopwatch function will stop the application from counting up by one when executed by the pause button.  
    def pause_stopwatch(): *3
        global running_stopwatch
        if running_stopwatch: *a
            stopwatch_display.after_cancel(update_time)
            running_stopwatch = False

# Reset stopwatch function will reset the hours, minutes and seconds back to zero and stop counting when executed by the reset button.
    def reset_stopwatch(): *4
        global running_stopwatch
        if running_stopwatch: *a
            stopwatch_display.after_cancel(update_time)
            running_stopwatch = False
        global stophours, stopminutes, stopseconds *b
        stophours, stopminutes, stopseconds = 0, 0, 0
        stopwatch_display.configure(text='00:00:00')

# Update stopwatch function will update the time displayed by adding a second to the timer every second. Self executing until time = 0.
    def update_stopwatch(): *5
        global stophours, stopminutes, stopseconds
        stopseconds += 1
        if stopseconds == 60: *a
            stopminutes += 1
            stopseconds = 0
        if stopminutes == 60: *b
            stophours += 1
            stopminutes = 0
        stophours_string = f'{stophours}' if stophours > 9 else f'0{stophours}' *c
        stopminutes_string = f'{stopminutes}' if stopminutes > 9 else f'0{stopminutes}'
        stopseconds_string = f'{stopseconds}' if stopseconds > 9 else f'0{stopseconds}'
        stopwatch_display.configure(text=stophours_string + ':' + stopminutes_string +      
        ':' + stopseconds_string) *d
        global update_time
        update_time = stopwatch_display.after(1000, update_stopwatch) *e

# Upon pressing the lap button, the latest time data is retrieved and inserted into the lapped_display entry field.
    def lap_stopwatch(): *6
        current_time = stopwatch_display.cget("text")
        current_laps = lapped_display.get()
        lapped_display.set(current_laps + " " + current_time)

# Upon closing the stopwatch sub-window, pause/reset stopwatch data is erased to prevent them from reappearing upon reopening.
    def close_stopwatch_window(): *7
        reset_stopwatch()
        stopwatch_window.destroy()
    stopwatch_window.protocol("WM_DELETE_WINDOW", close_stopwatch_window)
…
# Stopwatch display which will execute the corresponding function._stopwatch.
    stopwatch_display= ctk.CTkLabel(stopwatch_window, text="00:00:00", *8
                                                    width=40,  
                                                    font=('Helvetica', 60),)
    stopwatch_display.place(x=30, y=50)         
                             
# Start stopwatch button which will execute the corresponding function (same for pause, reset and lap buttons but with different text, fg_color and different horizontal and vertical coordinates).
    start_stopwatch_button= ctk.CTkButton(stopwatch_window, text="Start", *9
                                   width=55,
                                   height=25,
                                   fg_color="blue",
                                   font=('Helvetica', 15),
                                   command=start_stopwatch)
    start_stopwatch_button.place(x=25,y=350)          
…
# Lapped time display which will execute the corresponding function.
    lapped_display=StringVar() *10
    ctk.CTkEntry(stopwatch_window,
                 width=240,
                 height=180,
                 textvariable=lapped_display,
                 font=('Helvetica', 25)).place(x=30,
                                               y=140)
    lapped_display.set("")
…
```


Code explanation:



1. Global variables for the stopwatch’s running and time variables are defined at the beginning of the project.
2. Function which starts the counting sequence for the stopwatch.
   
    a. If the stopwatch is running, execute the update time function.

3. Function which pauses the counting sequence for the stopwatch.
   
    a. If the stopwatch is running, set running to false by stopping the update time function from executing.
   
4. Function which resets the hours, minutes and seconds back to zero.
   
    a. If the stopwatch is running, set running to false by stopping the update time function from executing.
   
    b. Then, set hours, minutes and seconds all back to zero.
   
5. Function which updates the time for the stopwatch by one second.
   
    a. If the number of seconds equals 60, instead increase the number of minutes to 1 and set the seconds back to zero.
   
    b. If the number of minutes equals 60, instead increase the number of hours to 1 and set the minutes back to zero.
   
    c. Create strings out of the hours, minutes and seconds data, accounting for when either of them are less than 9, where the string now has a 
zero leading.
   
    d. Create a complete string with the hours, minutes and seconds data.
   
    e. Run this function every 1000 milliseconds or 1 second.
   
6. Function which gets the current hours, minutes and seconds data from the stopwatch and inserts it into the lapped time display, separated by a space.
7. Function which when the window is closed, run the reset stopwatch function before destroying the window.
8. Stopwatch display label is customised and inserted into the sub-window.
9. Start, pause, reset and lap buttons are customised and inserted into the sub-window.
10. Lapped display entry field is customised and inserted into the sub-window.

Justification:

This new code:



* Creates a stopwatch application which allows the user to click the start button and allows the application to count upwards by 1 second at a time.
* The pause and reset button allows the user to control the duration of their stopwatch.
* Furthermore, the lap button allows the user to insert the current time data into the entry field or type their own notes. 

Improvements:

This code will be improved in later iterations in terms of:



* Optimisation.
* The aesthetic considerations of the entry field as currently it is primitive and unintuitive.
* Functionality through completing more sub-windows.

Sources:



* [Custom Tkinter documentation:](https://customtkinter.tomschimansky.com/)*
* [The ultimate introduction to modern GUIs in Python [ with tkinter ]:](https://www.youtube.com/watch?v=mop6g-c5HEY)<sup>🟡</sup>
* [Python Tkinter GUI Stopwatch:](https://www.youtube.com/watch?v=mdfuJPGLhPM)<sup>🟠</sup>


### 10/06/24 Deleting more features:

Window:

![Screenshot 2024-06-08 140849](https://github.com/catraboom/project-alarm-application/assets/124100757/ef92dba7-3c8d-422e-9d74-68c0decea276)

_Due to the absence of the more features button, the horizontal padding for the settings button can be removed and thus the main menu window can be compacted._

Edited/reorganised code:


```
# Creating a main menu of a fixed size.
menu = ctk.CTk()
menu.title("ALARme")
menu.geometry('300x400') *1
…
# Light green (similar change for other colour presets and custom colour functions).
def set_background_green(): *2  
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
                         text_color='white', *3
                         corner_radius=10,
                         height=50,
                         width=200,
                         font=('Helvetica', 20),
                         command=open_settings_window,
                         image=settings_asset_adjusted)
menu_settings_button.pack(pady=10) *4
…
# AND exemption of other code referencing the more button.
```


Code explanation:



1. Main menu’s horizontal geometry has been reduced to compact the window.
2. Functions for colour presets and custom colour have been edited to exclude the `menu_more_button.configure(bg_color=preset/custom).`
3. Slight aesthetic change to settings button, changing text colour from black to white to fit the aesthetic of the other main menu buttons.
4. Removed restriction which bound the settings button to the right of the screen and horizontal padding to allow the main menu to be compacted.

Justification:

This new code:



* Removes the more button and sub-window due to time constraints.
    * This allows me to focus upon optimising and fixing current code.
* Overall, the difficulty to implement these features isn’t worth it.
* Furthermore, the new implementation timeline provides enough functionality to users.

Improvements:

This code will be improved in later iterations in terms of:



* Implementing the alarm sub-window’s functionality.


### 11/06/24: Alarm GUI:

Window:

![Screenshot 2024-06-14 000649](https://github.com/catraboom/project-alarm-application/assets/124100757/1784704f-f066-4e07-ab4b-422d8088122e)
![Screenshot 2024-06-14 000752](https://github.com/catraboom/project-alarm-application/assets/124100757/35ee320b-91a5-4d79-b24b-0e87176b0025)

_Alarm window’s GUI clearly depicted. Left shows that the repeat alarm checkbox is active, right shows that the option menu is active._

New code:


```
# This label gives context to the time depicted to its right.
    current_time= ctk.CTkLabel(alarm_window, text="Current time:", *1
                               font=('Helvetica', 20)).place(x=30, y=50)

# Clock function strings together the system's time data and displays it to users.
    def alarmclock():  *2
        alarm_clock_time= time.strftime("%H:%M:%S %p") *a
        current_time_display.configure(text=alarm_clock_time) *b
        current_time_display.after(1000, alarmclock) *c

# This label takes the time data from the function above to display time data.
    current_time_display= ctk.CTkLabel(alarm_window, text="", *3
                                       font=('Helvetica', 20, "bold"))
    current_time_display.place(x=160, y=50)
    alarmclock() *a

# Hours entry field (same for minutes and seconds but with different horizontal coordinates; taken directly from the timer).
    alarmhours=StringVar() *4
    ctk.CTkEntry(alarm_window,
                 width=40,
                 textvariable=alarmhours,  
                 font=('Helvetica', 25)).place(x=30,
                                               y=90)
    alarmhours.set("00") 

# First colon separation label (same for second colon but with different horizontal coordinates; taken directly from the timer).
    alarm_colon_1=ctk.CTkLabel(alarm_window, text=":", *5
                         font=('Helvetica', 50)).place(x=90,
                                                       y=75)
…
…
# Enter time label to instruct users on how to enter their time data (taken directly from the timer).
    alarm_enter_time=ctk.CTkLabel(alarm_window, text="Enter time hh/mm/ss", *6
                            font=('Helvetica', 15))
    alarm_enter_time.pack(pady=90)
   
# Select day of week option menu, includes all 7 options.
    dow_option_menu= ctk.CTkOptionMenu(alarm_window, *7
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
    dow_option_menu.place(x=10, y=180)

# Start alarm button which executes the start_alarm function.
    start_alarm=ctk.CTkButton(alarm_window, text="Start", *8
                              width=130,
                              height=25,
                              fg_color="blue",
                              font=('Helvetica', 15)).place(x=160,
                                                         y=180)

# Repeat? Checkbox allows users to specify whether they want to repeat the alarm every week.
    repeat_checkbox= ctk.CTkCheckBox(alarm_window, text="Repeat?", *9
                                     fg_color="red",
                                     font=('Helvetica', 15)).place(x=110,
                                                                   y=225)
…
```


Code explanation:



1. The current time subtitle is customised and inserted into the sub-window.
2. Simple function which accesses the device’s time data and displays it in a label next to the current time subtitle.
   
    a. The alarm clock’s time variable returns strings containing hour, minutes and seconds information from the device.
   
    b. Display this time information into the `current_time_display `label by configuring the text to the current time.
   
    c. Every 1000 milliseconds or 1 second, repeat the function and update the time displayed to the user.
   
3. The current time display is customised and inserted into the sub-window.

    a. `alarmclock() `is added after this label as the clock function is reliant upon this label to operate.

4. Alarm’s hours, minutes and seconds entry fields are customised and inserted into the sub-window (same explanation from the timer).
5. Alarm’s 2 semicolon labels are inserted into the sub-window, between the 3 specified entry fields (same explanation from the timer).
6. Instructions subtitle is customised and inserted into the sub-window (same explanation from the timer).
7. Day of the week option menu is customised and inserted into the sub-window, with all 7 options being clearly depicted.
8. Start alarm button is customised and inserted into the sub-window.
9. Repeat alarm checkbox is customised and inserted into the sub-window

Justification:

This new code:



* Creates a simple alarm GUI that is aesthetically pleasing and fits the stylistic considerations of the previous settings, timer and stopwatch subwindows.
* Due to time constraints for today, the logic for the alarm will be integrated separately.

Improvements:

This code will be improved in later iterations in terms of:



* Adding logic to the alarm application.

Sources:



* [Custom Tkinter documentation:](https://customtkinter.tomschimansky.com/)*
* [The ultimate introduction to modern GUIs in Python [ with tkinter ]:](https://www.youtube.com/watch?v=mop6g-c5HEY)<sup>🟡</sup>
* [How to Create Countdown Timer Using Python | Tkinter Python Project:](https://www.youtube.com/watch?v=KTlT9saZFYc)<sup>🔴</sup>


### 13/06/24: Alarm logic:

Window:

![Screenshot 2024-06-15 135741](https://github.com/catraboom/project-alarm-application/assets/124100757/65374932-4735-429f-8e06-954f71d81829)

_Alarm window is clearly depicted. [Demonstration](https://youtu.be/HnBzIjbd8Js) (some performance errors are observable, which will be fixed in later iterations)._

New code:


```
# This label gives context to the day of the week depicted to its right
    day_of_week= ctk.CTkLabel(alarm_window, text="Current day:", *1
                              font=('Helvetica', 20)).place(x=35,
                                                            y=85)
   
# Day of week function obtains system's day of the week data and displays it to users.
    def dow(): *2
        alarm_dow= time.strftime("%A")
        dow_display.configure(text=alarm_dow)
        current_time_display.after(1000, dow)

# This label takes the day of week data from the function above to display the day of the week.
    dow_display= ctk.CTkLabel(alarm_window, text="", *1
                              font=('Helvetica', 20, "bold"))
    dow_display.place(x=160,
                      y=85)
    dow()
…
# Repeat? Checkbox allows users to specify whether they want to repeat the alarm every week.
    repeat_var= tk.BooleanVar() *3
…
# Start alarm function will start the alarm when the day of the week and time during that day is selected.
    def start_alarm(): *4
        alarm_time = f"{alarmhours.get()}:{alarmminutes.get()}:{alarmseconds.get()}" *a
        alarm_day = dow_option_menu.get() *b
        repeat = repeat_var.get() *c

# Check alarm function will check if the day/time of the alarm matches up.
        def check_alarm(alarm_day): *5
            now = datetime.datetime.now() *a
            current_time = now.strftime("%H:%M:%S") *b
            current_day = now.strftime("%A") *c
            if current_time == alarm_time and current_day == alarm_day: *d
                threading.Thread(target=play_sound_alarm).start()
                if repeat: *e
                    next_week = now + datetime.timedelta(days=7)
                    alarm_day = next_week.strftime("%A")
            alarm_window.after(1000, lambda: check_alarm(alarm_day)) *f
        check_alarm(alarm_day) *g
…
# Calling commands when the start alarm button is pressed (added to the parameters of the start alarm button)
command=start_alarm *6
…
```


Code explanation:



1. Customised and inserted two labels for the current day display, almost identical to current time display but with different horizontal and vertical coordinates.
2. Simple function identical to previous current time function but instead of importing system’s `%H:%M:%S %p `data, `%A `is used.
3. Before checkbox customisation and insertion, a variable is created that determines whether the user has activated the checkbox or not.
4. Start alarm function will take the data entered by the user and run the next function.
   
    a. Gets the formatted string of the alarmhours, alarmminutes and alarmseconds data entered by the user.
   
    b. Gets the option selected by the user from the dropdown menu.
   
    c. Gets information regarding whether the checkbox has been activated or not (i.e. true or false).
   
5. Check alarm function is inserted within the start alarm function and activates after data mentioned above has been accessed by the program.
   
    a. Gets the current date and time from the system.
   
    b. Specifies current time from the information from `now` above.
   
    c. Specifies current day from the information from `now` above.

    d. If the current time and time provided by the user, as well as the current day and day provided by the user match up, then the alarm sound is 
played.
   
    e. After this is met and the repeat checkbox is set to true, then adds 7 days to the alarm day.
   
    f. After 1000 milliseconds or 1 second, the check alarm function is rerun.
   
    g. Allows the code line above to run until user and system time and day match up.
   
6. Added to the parameters of the start button to allow the start timer function to run when pressed.

Justification:

This new code:



* Creates an alarm application which allows the user to click the start button and allows the application to detect whether the user entered time and day data match the system’s time and day data.
* The repeat checkbox allows for the alarm to be activated weekly (since this project is a prototype, data won’t be saved upon exiting and therefore leaving this running for a whole week will be difficult).

Improvements:

This code will be improved in later iterations in terms of:



* Optimisation as currently the application checks the time and date every second.
    * This resource usage results in the program sometimes skipping seconds (as seen in the demonstration), made worse when running sub-windows in tandem.

Sources:



* [Custom Tkinter documentation:](https://customtkinter.tomschimansky.com/)*


### 14/06/24 BLOCK B evaluation:



* Due to having other assessments during this week, I couldn’t complete this block as quickly as I completed the last block, taking most of the allocated time.
* Due to organisation issues which I had to address and time constraints due to other assessments, I had to split the stopwatch and alarm’s logic and GUI into separate entries.
* However, by completing the first block early, I had plenty of leeway.
* Furthermore, I was still able to complete this block in the allotted time, meaning I can use the extra time from Block A to complete Blocks C instead.
* This block also represented my decision to delete more features due to time constraints.

Overall, this block was quite problematic but eventually was completed in the allotted time. By fixing the organisation issues in this block, I can make sure they don’t reappear in consequent blocks.
