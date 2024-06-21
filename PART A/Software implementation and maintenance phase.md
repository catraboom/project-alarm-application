### Pre-implementation evaluation:

Proposal evaluation:



* Overall, this proposal is still valid with some minor reconsiderations to improve time management and decrease the overall complexity of this project.
* My initial design was very radical; intending to completely revolutionise time management in digital environments.
* Since then, I have toned down this project to allow it to be more manageable.
* Instead of being a major improvement upon previous time management approaches, it will create a more intuitive and user friendly time management application which holistically incorporates all the important aspects.
    * This is mainly due to the fact that features like timers, stopwatches, alarms and calendars have been refined to a point where improving them is unnecessary. 
* Unfortunately, to keep the project manageable, I may have to completely disregard more features as they are difficult to incorporate into my project and will upset my time management. 
* This project will still have a minimalist aesthetic as the proposal suggests due to its simplicity.
* Furthermore, this project will still be a desktop application.

Lotus diagram evaluation:



* Lots of features were removed to allow this project to be more manageable.
* In terms of technology, only 3 of the 8 features will definitely be implemented, with the other 5 being possibilities.
    * If more features aren’t being integrated, then the NumPy, Pandas and Matplotlib databases don’t need to be implemented as well.
    * Furthermore, I won’t have enough time to integrate the Google play store and Microsoft store compatibilities.
* In terms of user experience, adjustable layouts will be removed as it doesn’t serve much purpose and would be difficult to implement.
* In terms of functions, only the stopwatch, timer, calendar and alarm (no advanced loops) features will be implemented as they are core features which are easy to integrate.
* In terms of data, only 6 of the 8 features will definitely be implemented, with the other 2 being possibilities.
    * If more features aren’t being implemented, then traffic data won’t be needed.
    * Furthermore, the notification shelf won’t be implemented as it is too complicated, considering my limited time.
* In terms of design, most if not all of these features will be implemented as they are simple.

<table>
  <tr>
   <td>
Tkinter
   </td>
   <td>Python
   </td>
   <td>CTk
   </td>
   <td>Themes
   </td>
   <td>Fonts
   </td>
   <td>Software
<p>
optimisation
   </td>
   <td>╳
   </td>
   <td>Advanced alarm loops
   </td>
   <td>╳
   </td>
  </tr>
  <tr>
   <td>╳
   </td>
   <td><strong><em>Technology</em></strong>
   </td>
   <td>╳
   </td>
   <td>╳
   </td>
   <td><strong><em>User Experience</em></strong>
   </td>
   <td>Options
   </td>
   <td>╳
   </td>
   <td><strong><em>Function</em></strong>
   </td>
   <td>Calendars
   </td>
  </tr>
  <tr>
   <td>╳
   </td>
   <td>╳
   </td>
   <td>╳
   </td>
   <td>Settings
   </td>
   <td>User configurable
   </td>
   <td>User customisable
   </td>
   <td>Stopwatch
   </td>
   <td>Timer
   </td>
   <td>╳
   </td>
  </tr>
  <tr>
   <td>╳
   </td>
   <td>Traffic 
   </td>
   <td>User
   </td>
   <td><strong><em>Technology</em></strong>
   </td>
   <td><strong><em>User Experience</em></strong>
   </td>
   <td><strong><em>Function</em></strong>
   </td>
   <td>Modern
   </td>
   <td>Simple
   </td>
   <td>Elegant
   </td>
  </tr>
  <tr>
   <td>Operating system
   </td>
   <td><strong><em>Data</em></strong>
   </td>
   <td>Time
   </td>
   <td><strong><em>Data</em></strong>
   </td>
   <td><strong><em>ALARM APP</em></strong>
   </td>
   <td><strong><em>Design</em></strong>
   </td>
   <td>Stickers
   </td>
   <td><strong><em>Design</em></strong>
   </td>
   <td>Labels
   </td>
  </tr>
  <tr>
   <td>╳
   </td>
   <td>Device
<p>
specifications
   </td>
   <td>Date
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>Image integration
   </td>
   <td>Banners
   </td>
   <td>Buttons
   </td>
  </tr>
</table>


_What my new lotus diagram would look like._

Feasibility report evaluation:



* Most of the details adhere to the considerations of my feasibility report.
* In terms of the objective, the software application won’t involve noting down reminders as it isn’t necessary with a calendar. However, the aim of being simplistic without sacrifice will still be achieved.
* In terms of goals, the final project’s logic and overall operation will be simple enough to allow the application to run on most devices optimally.
* In terms of outcomes, I will use a Gantt chart to assist my project’s development.
* In terms of identifying user needs, this application will be simple enough to allow for easy navigation.
* In terms of budgetary constraints, I will use free and open source software to develop this project.
* In terms of software, the application will still be built specifically for the Windows operating system.
* In terms of knowledge analysis, I won’t need to learn how to code with NumPy, Pandas and Matplotlib if more features aren’t being implemented. Therefore, I will only need to learn python, Tkinter and Custom Tkinter.
* In terms of social and ethical considerations, if more features aren’t being implemented, then location data won’t be needed but this cannot prevent the requirement for time and date data for the alarm and calendar respectively.


### Implementation planning:

Primary module list: 



* Python module.
* Tkinter (Tk) module.
* CustomTkinter (CTk) module.

Secondary module list:



* Settings module.
* Timer module.
* Stopwatch module.
* Alarm module.
* Calendar module.
* More features module (may not be implemented).

Dependency analysis:



* The Tkinter/CustomTkinter modules are based upon the python coding language, hence all 3 of these primary modules should be downloaded before the commencement of my project.
    * Secondary modules are dependent upon the primary modules.
* The settings, timer and stopwatch modules are purely dependent on the python logic.
* The alarm module’s functionality is also dependent on the device time and therefore requires access to this data otherwise this feature cannot be used effectively.
* The calendar module is dependent on the device date to correctly highlight the year, month, date etc. 
* If implemented, the more features module will contain various advanced features that rely on device time/date and also device location data to function properly depending on the feature being implemented.
* These aforementioned modules all rely on the primary modules for the logic and user experience.

Implementation order:



* After all the primary modules are installed, the secondary modules can be addressed.
* Starting with the easiest specific modules which include the settings, timer and stopwatch modules as they require simple logic. 
* Next, the alarm and calendar modules will be implemented due to their dependency on extra data.
* Lastly, the more features module will be implemented as these extra features are optional as the aforementioned modules are a greater priority. 
    * Ultimately, They may not be implemented due to time constraints.

Gantt chart:

![Screenshot 2024-06-20 102624](https://github.com/catraboom/project-alarm-application/assets/124100757/6397e257-6d50-4767-83e1-ab5ffcb10f40)

_My current Gantt chart, depicting all 3 blocks and estimated and actual times for completion, in this case 39 hours._


### Testing strategies:

Potential issues:



1. One major issue is a lack of optimisation due to my laziness and overall coding inexperience.
2. Another major issue is my lack of time due to procrastination and aforementioned laziness.
3. One minor issue is compatibility between devices, as features may break when compressing the project in a zip file format.

Solutions:



1. To solve the optimisation issue:
    * Analyse any bottlenecks in the software by checking the terminal and examining the loading times for each feature in milliseconds. From here, I can assist myself by looking at tutorials and asking generative AI for strategies to allow these features to run more optimally by either fixing and redoing codeblocks. 
    * Make more features, primarily functions run in parallel to other functions to prevent reliances on other features to perform, slowing down operation. Similarly, this can be assisted using tutorials and generative AI.
* While optimising these issues through fixing and redoing code blocks, I must continuously monitor software solutions to prevent any further bugs that can arise in other areas.
2. To minimise the time management issue:
    * I can adhere to my Gantt chart’s estimated completion dates, as they organise the development process and allow me to better manage my time and priorities during this project’s development.
    * Set study objectives every week through using the AGILE method and sprints to make sure I am completing a set number of tasks weekly, resisting my urge to procrastinate.
* Through following these time management strategies, I can make the best use of my limited time to produce a satisfactory project.
3. To solve the compatibility issue:
    * By optimising the code as aforementioned to minimise the size of the repository (i.e. by compressing images), the zip file can be easier to format and therefore download.
    * Test the repository side by side with another machine to assure that it runs efficiently without errors, which should be fixed if they arise.
* Through using these strategies I should be able to create an optimised application that runs efficiently on most devices.


### Maintenance considerations:

Future functionality compromises:



1. As the project ages, certain functionalities may break as later versions of python, Tkinter and Custom Tkinter are implemented.  
2. Furthermore, the aesthetics of the project, though unlikely, may become dated in the future.

Solutions:



1. To solve the functionality issue:
    * I can simply keep the code’s modules updated and keep installing new versions of python, Tkinter and Custom Tkinter. After downloading these, the code should be checked again to solve any new issues that arrive.
    * I could also keep the code in one specific version of python, Tkinter and Custom Tkinter but this can cause issues to arise surrounding compatibility with operating systems so this approach isn’t recommended.
2. To solve the aesthetic issue:
    * By following design trends, I can upgrade the aesthetics of labels, buttons and entry boxes.
* Upgrading aesthetics like this is an uncommon practice in software development and therefore overall these considerations aren’t as necessary as the functionality in this application as it ages.


### Social and ethical considerations:

Issue:



* This project could result in social and ethical dilemmas surrounding using device information, primarily date and time data.

Solution:



* Other than using social and ethical software development practices such as permission grants, this overall shouldn’t be a major problem as none of the data being collected is personal (i.e. it is device data).


### Critical considerations:

Justification:



* Overall, this project simplifies my initial proposal by removing extra functionality and instead focusing upon the key idea of my project: integrate many time management features into one holistic application.
    * Some extra functionalities like more features will be considered but aren’t necessary to this project mainly due to their implementation requirements.
* This may mean removing lots of unnecessary modules, as seen in the changes to my lotus diagram.
* Furthermore, most of the considerations in my feasibility report are also met.

Challenges:



1. A challenge I will have to overcome is my somewhat primitive knowledge on coding, especially with Tkinter and Custom Tkinter.
2. Another challenge I will have to face is fixing the code as I previously mentioned.
3. A less typical challenge I will have to overcome is Github commits, more specifically the extension not working on Visual Studio.
4. Keeping track of changes will be difficult as well.

Solutions:



1. To overcome this challenge, I will watch tutorials on certain aspects of logic. Furthermore, I can use tutorials like [The ultimate introduction to modern GUIs in Python [ with tkinter ]:](https://www.youtube.com/watch?v=mop6g-c5HEY)<sup>🟡</sup> which are very detailed (video mentioned is 18+ hours long) to better assist my understanding on Tkinter and Custom Tkinter more specifically.
2. I can fix my code by optimising it in the steps mentioned in testing strategies, which in summary involves analysing bottlenecks and running more functions in parallel.
3. I will search for a quick tutorial to fix this commit issue between Github and Visual Studio.
4. Using a Gantt chart and the timeline below, I can keep track of how my code evolves. Furthermore, once I fix the commit issue, I can use the repository’s commit history to outline changes to my project.
