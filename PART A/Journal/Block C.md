### 16/06/24: Calendar:

Window:

![Screenshot 2024-06-17 225208](https://github.com/catraboom/project-alarm-application/assets/124100757/e913bc49-e2f4-4808-8f54-b1926280f393)

_Calendar window is clearly depicted. [Demonstration.](https://youtu.be/4-TOXf7Q4ek)_

New code:


```
# Show date function displays the date in dd/mm/yy to the right of the specified date label, as the calendar module's GUI is a bit messy.
# Furthermore, it will handle whether an event was confirmed by the user on a specific date or not, when executed by the add event button.
    def show_date(event): *1
        specified_date=calendar.get_date() *a
        specified_date_label.configure(text=f"Specified date: " + specified_date)
        if specified_date in events: *b
            event_title_entry.set(events[specified_date].get("title", ""))
            event_description_entry.set(events[specified_date].get("description",
                                                                   ""))                        
        else: *c
            event_title_entry.set("Title")
            event_description_entry.set("Description")

# Add event function adds an event to a specific date, saving it in the sub-window's session.
    def add_event(): *2
        specified_date = calendar.get_date() *a
        title = event_title_entry.get().strip()
        description = event_description_entry.get().strip()
        if title or description: *b 
            events[specified_date] = {"title": title, "description": description}
            event_title_entry.set("")
            event_description_entry.set("")
           
# Create a dictionary to store the events created by the user in the session.
    events = {} *3

# Specified date subtitle, giving context to the date information to the right.
    specified_date_label=ctk.CTkLabel(calendar_window, text="Specified date: ",*4
                                      font=('Helvetica', 18))
    specified_date_label.place(x=10,
                              y=315)

# Event title subtitle, giving context to the entry field below (same for description subtitle but with different text and horizontal coordinates).
    event_title_label=ctk.CTkLabel(calendar_window, text="Enter event title", *5
                                   font=('Helvetica', 12)).place(x=10, y=345)
…
# This entry field allows the user to input the title of the event they are adding (same for description entry field but with different set text and horizontal coordinates).
    event_title_entry=StringVar() *6
    ctk.CTkEntry(calendar_window,
                 width=100,
                 font=('Helvetica', 15),
                 textvariable=event_title_entry).place(x=10,
                                                       y=370)                                      
    event_title_entry.set("Title")
…
# Add event button which allows the user to confirm whether they want to add an event to a specific date, executing the date information function.
    add_event_button=ctk.CTkButton(calendar_window, text="Add event", *7
                                   fg_color="blue",
                                   font=('Helvetica', 18),
                                   width=100,
                                   command=add_event)
    add_event_button.place(x=10,
                           y=460)

# Import calendar module and associate it with the calendar window.
    calendar=Calendar(calendar_window, *8
                      showweeknumbers=False,
                      showothermonthdays=False,
                      background="#2E2E2E",
                      foreground="white",
                      normalbackground="#D9D9D9",
                      weekendbackground="#2E2E2E",
                      weekendforeground="white",
                      font=('Helvetica', 25))
    calendar.place(relx=0, rely=0.12, relwidth=1, relheight=0.5)
    calendar.bind("<<CalendarSelected>>", show_date)
…
```


Code explanation:



1. Date info function both allows the user to easily observe their selected date and create an event on a specific date.
   
    a. Gets information regarding the date selected by the user and then configures the `specified_date_label `to enable it to display this data instead.
   
    b. If the date specified by the user has also been selected as an event, then grab both title and description data and store it in `events`.
   
    c. If the date specified by the user isn’t also selected as an event, then default the title and description entry fields.
   
2. Add event function saves the event into the date specified by the user until the sub-window is terminated.
   
    a. Gets information about the date, title and description (while removing trailing spaces) specified by the user.
   
    b. If either a title or description has been entered by the user, bind the specified date to these two data points by saving them into `events`. Also, default the fields to this information upon reopening that date.
   
3. This is a dictionary where all the events during the session can be saved and accessed at any point.
4. The specified date label is customised and inserted into the sub-window.
5. The event and description labels are customised and inserted into the sub-window.
6. The event and description entry fields are customised and inserted into the sub-window.
7. The add event is customised and inserted into the sub-window.
8. The calendar module is imported, customised and inserted into the sub-window.

Justification:

This new code:



* Creates a calendar application which allows the user to click any date on the application, enter a title or description for the event and save it to the device temporarily.
* It employs the basic Tkinter calendar module, which offers a sufficient basis to develop my calendar application due to its wide range of customisability.

Improvements:

This code will be improved in later iterations in terms of:



* Aspects including aesthetics, optimisation, bug fixing and organisation will now all be addressed in my project, as I have completed development of all the features I want to implement.
    * This will be achieved over the course of the following week, ideally before this assessment is due.

Sources:



* [Custom Tkinter documentation:](https://customtkinter.tomschimansky.com/)*
* [The ultimate introduction to modern GUIs in Python [ with tkinter ]:](https://www.youtube.com/watch?v=mop6g-c5HEY)<sup>🟡</sup>
* [Python tkCalendar - Creating a Date Picker Calendar in Tkinter:](https://www.youtube.com/watch?v=Nbh0KXHEDUo)<sup>🟣</sup>


### 17/06/24: Aesthetic reconsiderations:

Window:

![Screenshot 2024-06-18 094620](https://github.com/catraboom/project-alarm-application/assets/124100757/c6497fe7-dae0-4677-b8cb-39ec47676da4)

_Before._

![Screenshot 2024-06-18 114003](https://github.com/catraboom/project-alarm-application/assets/124100757/f2a898f1-155f-427d-b8b8-b1a6345fe665)

_After, with the stopwatch changing the most through the lapped display. [Demonstration.](https://youtu.be/xKZmlapG_JY)_

Edited/reorganised code:


```
# Global variables for stopwatch allow the timer to not be running initially and also the hours, minutes and seconds to be set at zero initially and also count laps up by one.
…
lap_counter = 0 *1
…
# Upon pressing the lap button, the latest time data is retrieved and inserted into the lapped_display entry field.
    def lap_stopwatch(): *2
        global lap_counter
        lap_counter += 1
        current_time = stopwatch_display.cget("text")
        lapped_display.configure(state="normal") *a
        lapped_display.insert(tk.END, f"Lap {lap_counter}: {current_time}\n")
        lapped_display.configure(state="disabled")
…
# Reset stopwatch function will reset the hours, minutes and seconds back to zero and stop counting when executed by the reset button.
    def reset_stopwatch(): *3
        global running_stopwatch, lap_counter
        if running_stopwatch:
            stopwatch_display.after_cancel(update_time)
            running_stopwatch = False
        global stophours, stopminutes, stopseconds
        stophours, stopminutes, stopseconds = 0, 0, 0
        stopwatch_display.configure(text='00:00:00')
        lap_counter = 0 *a
        lapped_display.configure(state="normal") *b
        lapped_display.delete(1.0, tk.END)
        lapped_display.configure(state="disabled")
…
# Lapped time display which will execute the corresponding function.
    lapped_display=ctk.CTkTextbox(stopwatch_window, *4
                                  fg_color="#808080",
                                  width=240,
                                  height=180,
                                  font=('Helvetica', 26))
    lapped_display.place(x=30, y=140)
    lapped_display.configure(state="disabled") 
…
# The x and y positions of each of the 6 entry boxes, relative to each other
    x_position = 40 *5
    y_position = 270
…
# Six identical custom background entry boxes are created for users to one hexadecimal character to create a valid string of six.
    entries=([ctk.CTkEntry(settings_window, width=2) for _ in range(6)]) *6
    for i, entry in enumerate(entries): *a
        entry.place(x=x_position, y=y_position) *b
        x_position += 40 *c
…
```


Code explanation:



1. Global variables for the stopwatch’s lapped time variables are defined at the beginning of the project.
2. Lap stopwatch function has been edited to add lap and the lap’s position relative to other laps before the time data.
   
    a. Create a formatted string with the “Lap”, lap number and the time data while preventing the user from editing this lap data using the text box.
   
3. Reset stopwatch function has been edited to also reset the lap time.
   
    a. Set lap times back to zero.
   
    b. Delete the information currently shown on the text box while preventing the user from editing this lap data using the text box.
   
4. Edited the lapped display from an entry field to a text box to allow for lapped times to be inserted below each other to ensure readability.
5. The horizontal and vertical coordinate variables of the entry fields are specified.
6. For each of the 6 entries, they can more easily be spaced and placed within the sub-window.
   
    a. For each entry, a pair of values is generated to place the entries within the sub-window both horizontally and vertically.
   
    b. Place the 6 entry fields using the specified horizontal and vertical coordinates specified beforehand.
   
    c. Vary each of the entry fields x positions by 40.

Additional changes:



* The entry fields and descriptive box for them are vertically flipped for the timer and alarm to ensure consistency in widget placements.
* In the settings menu, the padding between buttons is edited by using the place method rather than pack method to organise widgets.

Justification:

This new code:



* Improves upon the general aesthetics of the project by reorganising and respacing widgets.
* More specifically, the stopwatch’s lapped display has been redesigned with a text box rather than entry fields to give context to lapped times and allow them to be placed underneath each other to improve upon aesthetics.

Improvements:

This code will be improved in later iterations in terms of:



* Through organising areas of code to make each line of code as readable to the stakeholders as possible.

Sources:



* [Custom Tkinter documentation:](https://customtkinter.tomschimansky.com/)*


### 18/06/24: Code organisation #2:

New code:


```
# Renamed the times, min, sec and hr by prefixing them with timer, removing the abbreviations and adding underscores.
timer_times *1
timer_minutes
timer_seconds
timer_hours 
…
# Renamed the stopseconds, stopminutes and stopseconds by suffixing them with watch and adding underscores.
stopwatch_seconds *3
stopwatch_minutes
stopwatch_hours
…
```


Edited/reorganised code:



1. Renamed the times, min, sec and hr variables used extensively in the timer’s logic to make their association with the timer’s functions more explicit.
2. Renamed the stopseconds, stopminutes and stopseconds variables used in the alarm’s logic to make their association with the alarm’s functions more explicit.

Additional changes:



* All buttons get `_button `after.
* All labels get `_label `after.
* All entry boxes get `_entry `after.
* This better organises these widgets and their associated functions.
* Furthermore, if a widget’s customisation/insertion arguments are separated by a comma, it will now generally get its own line (excluding between root and text because this allows the text’s importance to be clearer to stakeholders).

Justification:

This new code:



* Further organises the code by primarily adding underscores where needed.
* Additionally, prefixation is added to some important variables to make their association with different sections of the code more apparent.

Improvements:

This code will be improved in later iterations in terms of:



* Allowing the background colour of the main menu to be saved by the user, loading upon reopening the application.

Sources:



* [Custom Tkinter documentation:](https://customtkinter.tomschimansky.com/)*


### 18/06/24: Saving files locally:

Window:

![Screenshot 2024-06-20 183909](https://github.com/catraboom/project-alarm-application/assets/124100757/4cc0ad01-30fc-4045-8a9f-46d60fd0096f)

_Main menu’s background saving. [Demonstration.](https://youtu.be/Mv5EQOVNG2A)_

New code:


```
# ***** IMPORTS *****

# Importing modules to customise GUI, manage assets and access system data.
…
import os as os *1
…
# ***** SAVE/LOAD DATA *****

# Save function associates the background colour with an initialisation file.
def save_background_colour(colour): *2
    with open('INITIALISATIONSbackground_colour.txt', 'w') as file:
        file.write(colour)

# Load function associates the background colour with an initialisation file.
def load_background_colour(): *3
    if os.path.exists('INITIALISATIONSbackground_colour.txt'):
        with open('INITIALISATIONSbackground_colour.txt', 'r') as file:
            return file.read().strip()
    return None
…

# ***** SETTINGS SETUP *****

# Apply background function applies the background colour to the main menu's background and its widgets.
def apply_background_colour(colour): *4
    menu.config(background=colour) 
    menu_timer_button.configure(bg_color=colour)
    menu_alarm_button.configure(bg_color=colour)
    menu_stopwatch_button.configure(bg_color=colour)
    menu_calendar_button.configure(bg_color=colour)
    menu_settings_button.configure(bg_color=colour)
    menu_title_label.configure(bg_color=colour)
    save_background_colour(colour)

# Validate hexadecimal code to make it is in the hexadecimal range of 0-F.
def validate_hex(char): *5
    if char in '0123456789ABCDEFabcdef':
        return True
    return False

# Get hexadecimal code information from the data the user's entered into the six entry fields, then change menu background colour to the specified custom, also editing the button/label background colours to match.
def change_colour(hex_entries):
    hex_code = ''.join([entry.get().upper() for entry in hex_entries])
    if len(hex_code) != 6 or not all(validate_hex(c) for c in hex_code):
        return
    try: *a
        colour = f'#{hex_code}'
        apply_background_colour(colour)
    except tk.TclError:
        pass

# Three functions have been simplified, allowing them to be more compact.
# Light red.
def set_background_red(): *b
    apply_background_colour('#FF474C')
…
# Custom background confirmation button which will execute the corresponding global function.
    confirm_background_button = ctk.CTkButton(settings_window, text="Confirm", *6
                                              fg_color="blue",
                                              command=lambda:
                                              change_colour(hex_entries)) *a
    confirm_background_button.place(x=80,
                                    y=310)
…
# Load and apply the saved background colour everytime when the application restarts.
saved_colour = load_background_colour() *7
if saved_colour:
    apply_background_colour(saved_colour)
…
```


Code explanation:



1. Import the operating system to allow the initialisation file to be inserted into the computer.
2. This function saves the background colour to the initialisation file by writing/overwriting the variable within it.
3. This function loads the background colour that is saved to the initialisation file, ignoring heading and trailing spaces.
4. This function applies the colour changes specified by the user to the main menu’s background and associated widgets.
5. Reorganised the preset/custom colour change functions and validate hexadecimal code function by removing their indentation and inserting them above the sub-window.

    a. The custom colour try statement has been simplified to activate the apply changes function and replace the parameters with hexadecimal code.
   
    b. The light red, light blue and light green colour presets have been simplified so they simply activate the apply changes function and replace the parameters with preset.
   
6. The confirm background button has been edited to more efficiently execute the change colour function.
   
    a. This improves performance by using an anonymous function to execute the change colour function’s relatively simple expressions.

8. This statement allows the saved background colour to be loaded and then applied to the sub-window and associated widgets.

Justification:

This new code:



* Saves the preset or custom background colour specified by the user to an initialisation file in the repository, allowing it to be loaded when the user reopens the application.
* Through doing this, I was also able to simplify and compact the preset and custom background functions by allowing them to call a common function that applies the colour to the background and associated widgets.

Improvements:

This code will be improved in later iterations in terms of:



* Fixing general bugs and also optimising areas of the code to allow the application to perform efficiently without errors.

Sources:



* [Custom Tkinter documentation:](https://customtkinter.tomschimansky.com/)*


### 19/06/24: Bug fixing:

Window:

![Screenshot 2024-06-19 204100](https://github.com/catraboom/project-alarm-application/assets/124100757/5610ab10-05ca-40c5-9504-6f5fe5a20356)

_Code with bugs. [Demonstration of old code.](https://youtu.be/dtE_YQ50lGc)_

_Code after fixing and optimisation. [Demonstration of new code.](https://youtu.be/i2we4c0b6LM)_

Edited/reorganised code:


```
# ***** IMPORTS *****

# Importing modules to customise GUI, manage assets and access system data (same for alarm).
…
import pygame *1
…
# Initialize Pygame's mixer to allow the sound to play and also stop playing when the sub-window is closed (same for alarm).
    pygame.mixer.init() *2
…
# Play sound function using pygame to prevent the sub-window from becoming non-responsive (same for alarm).
    def play_sound_timer(): *3
        pygame.mixer.music.load("SOUNDS/Clear Dance Train Melody.mp3")
        pygame.mixer.music.play()

# Stop sound function using pygame to allow the sound to stop playing when the sub-window is closed like before with play sound (same for alarm).
    def stop_sound_timer(): *4
        pygame.mixer.music.stop()
…
# On close function to stop the sound when the sub-window is closed (same for alarm).
    def on_closing_timer(): *5
        stop_sound_timer()
        timer_window.destroy()
    timer_window.protocol("WM_DELETE_WINDOW", on_closing_timer)
…
# Add event function is edited so that the information doesn't disappear upon adding an event to a specific date.
    def add_event(): *6
        specified_date = calendar.get_date()
        title = event_title_entry.get().strip()
        description = event_description_entry.get().strip()
        if title or description: *a
            events[specified_date] = {"title": title, "description": description}
…
```


Code explanation:



1. Import the pygame module, as from here we can import pygame’s mixer.
2. Initialise the pygame mixer to allow sound to be played from a file location.
3. This simple function loads the sound file and allows it to be played when called by other functions.
4. This simple function allows the sound file to be stopped.
5. This simple function allows the user to completely terminate the sound file’s operation after the sub-window is closed.
6. The add event function has been edited to prevent the title and description from temporarily disappearing upon pressing the add event button.

    a. The if statement was edited so that upon pressing the add event button, the title and description would be updated to match the user specified title and description.

Justification:

This new code:



* Fixes upon the bugs evident in the video linked by allowing the timer and alarm sounds to stop playing upon closing the sub-window
* Furthermore, it also prevents the title and description from temporarily disappearing upon pressing the add event button in the calendar sub-window.

Sources:



* [Custom Tkinter documentation:](https://customtkinter.tomschimansky.com/)*


### 14/06/24 BLOCK C evaluation:



* The assessment tasks that negatively affected my time management in the last block were amplified this time around.
* However, apart from the calendar app, not much new code was added and instead existing code was edited and fixed to improve the user experience.
* I also didn’t need to use the extra time from Block A to complete this, finishing this block in the allocated time. 
* This leaves more time to documentation and refining the project as a whole to abide by the marking guidelines.

Overall, this block faced many of the issues evident in the last block but either way I was able to pull through in the allotted time and complete the project.
