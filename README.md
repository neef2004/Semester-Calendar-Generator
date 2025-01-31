# Semester-Calendar-Generator

📅 Semester Calendar Generator

A command-line tool that allows students to manually input their class schedules and generate an .ics file for use in Apple Calendar and other calendar apps.

🚀 Features
	•	📝 Terminal-based input – Users manually enter course details step by step.
	•	📆 iCal file generation – Creates a .ics file for easy calendar import.
	•	🔄 Repeatable schedules – Supports recurring classes (e.g., M/W/F or T/Th).
	•	🔒 Local processing – No internet connection required.

🛠 Installation

Clone the Repository

	`git clone https://github.com/neef2004/Semester-Calendar-Generator.git
	cd Semester-Calendar-Generator`

Ensure dependencies are installed:

	`pip install -r requirements.txt`

📖 Usage

Run the Program

	`python3 iCalGenerator.py`

🔎 Follow the Input Prompts
	•	The program will ask for course name, meeting days, start and end times, and location.
	•	Example interaction listed at the bottom

📖 Future Improvements
	•	OCR Support – Allow users to upload images of their class schedules instead of manually entering data.
	•	Google Calendar Integration – Option to sync directly with Google Calendar.
 	•	Web Interface – Build a web-based tool for easier schedule entry.
	
 
 welcome to this quick and easy iCal generator
	Choose your time zone
	1.) New York   2.) Chicago   3.) Denver   4.) Los Angeles
	Enter a Number: 1
	**When does the semester start?
	Enter a Date (YYYY-MM-DD): 2025-01-21
	**When does the semester end?
	Enter a Date (YYYY-MM-DD): 2025-05-16
	1.) Display schedule    2.) Edit schedule    3.) Add Breaks    4.) Generate .ics file    5.) Quit
	Enter a Number: 2
	1.) Add Course    2.) Remove Course    3.) Edit Course Info    4.) Finish
	Enter a Number: 1
	***Enter Course Name: math
	***Enter Course Location: lecture hall 2
	***Enter number of meeting days
	Enter a Number: 3
	1.) Monday   2.) Tuesday    3.) Wendsday    4.) Thursday    5.) Friday
	Enter a Number: 1
	Enter a Number: 3
	Enter a Number: 5
	***Enter Start and End Times in HH:MM format (24-hour clock)
	Start Time: 13:00
	End Time: 14:15
	***Any additional Notes: bring calculator, readings due at the end of the day
	You added 1 course.
	Name: math
	Location: lecture hall 2
	Start Time: 13:00:00
	End Time: 14:15:00
	Notes: bring calculator, readings due at the end of the day
	1.) Add Course    2.) Remove Course    3.) Edit Course Info    4.) Finish
	Enter a Number: 4
	1.) Display schedule    2.) Edit schedule    3.) Add Breaks    4.) Generate .ics file    5.) Quit
	Enter a Number: 1
	====================================
	Course ID: 0
	Course Name: math   Course Location: lecture hall 2
	Course Meeting Days: MO, WE, FR
	Start Time: 13:00:00   End Time: 14:15:00
	Notes: bring calculator, readings due at the end of the day
	====================================
	1.) Display schedule    2.) Edit schedule    3.) Add Breaks    4.) Generate .ics file    5.) Quit
	Enter a Number: 4
	Enter a name for the .ics file: my_schedule
	iCal file saved as my_schedule.ics
	1.) Display schedule    2.) Edit schedule    3.) Add Breaks    4.) Generate .ics file    5.) Quit
	Enter a Number: 5
