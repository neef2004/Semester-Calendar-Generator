from icalendar import Calendar, Event
from datetime import datetime, timedelta, time
from dataclasses import dataclass, field
from typing import List, Optional
import pytz

@dataclass
class Course:
    name:Optional[str] = field(default = None)
    location: Optional[str] = field(default = None)
    days: List[str] = field(default = None)
    start_time: Optional[time] = field(default = None)
    end_time: Optional[time] = field(default = None)
    notes: Optional[str] = field(default = None)
   
    def __str__(self):
        days_to_str = ", ".join(self.days)
        return f"Course Name: {self.name}   Course Location: {self.location}\nCourse Meeting Days: {days_to_str}\nStart Time: {self.start_time}   End Time: {self.end_time}\nNotes: {self.notes}"

@dataclass
class Term:
    start_date: Optional[datetime] = field(default = None)
    end_date: Optional[datetime] = field(default = None)

    def __str__(self):
        return f"Start Date: {self.start_date.date()}    End Date: {self.end_date.date()}"

timezones = {
    1: "America/New_York",
    2: "America/Chicago",
    3: "America/Denver",
    4: "America/Los_Angeles"
}

weekdays = {
    1: "MO",
    2: "TU",
    3: "WE",
    4: "TH",
    5: "FR"
}

def read_int(lower_bound: int, upper_bound: int) -> int:
    selection = -1
    while(True):
        try:
            selection = int(input("Enter a Number: "))
            if(lower_bound <= selection <= upper_bound):
                return selection
            else:
                print(f"Invalid Input: Enter a number between {lower_bound} and {upper_bound}")
        except ValueError:
            print("Invalid Input: Enter an Integer")

def read_time(prompt: str) -> str:
    while True:
        user_input = input(prompt)
        try:
            time = datetime.strptime(user_input, "%H:%M").time()
            return time
        except ValueError:
            print("Invalid formatting. Enter in HH:MM (24-hour clock)")

def create_course() -> Course:
    new_course = Course()
    new_course.name = input("***Enter Course Name: ")
    new_course.location = input("***Enter Course Location: ")
    print("***Enter number of meeting days")
    course_frequency = read_int(1, 5)
    new_course.days = []
    valid_days = {1, 2, 3, 4, 5}
    print("1.) Monday   2.) Tuesday    3.) Wendsday    4.) Thursday    5.) Friday")
    for i in range(course_frequency):
        while True:
            day = read_int(1, 5)
            if(day in valid_days):
                new_course.days.append(weekdays.get(day))
                valid_days.discard(day)
                break
            else:
                print("This day is already in the schedule for this course")

    start_time = -1
    end_time = -1
    print("***Enter Start and End Times in HH:MM format (24-hour clock)")
    while(start_time >= end_time):
        start_time = read_time("Start Time: ")
        end_time = read_time("End Time: ")
        if(start_time >= end_time):
            print("Start time must be before end time.")
    
    new_course.start_time = start_time
    new_course.end_time = end_time

    new_course.notes = input("***Any additional Notes: ")

    print(f"You added 1 course.\nName: {new_course.name}\nLocation: {new_course.location}\nStart Time: {new_course.start_time}\nEnd Time: {new_course.end_time}\nNotes: {new_course.notes}")
    return new_course

def edit_schedule(schedule: List[Course]):
    editor_selection = -1
    while(editor_selection != 4):
        print("1.) Add Course    2.) Remove Course    3.) Edit Course Info    4.) Finish")
        editor_selection = read_int(1, 4)
        if(editor_selection == 1):
            schedule.append(create_course())
        elif(editor_selection == 2):
            if(len(schedule) == 0):
                print("No Courses to be removed")
            else:
                display_schedule(schedule)
                print("Enter ID of course to be removed")
                schedule.pop(read_int(0, len(schedule) - 1)) # -1 to account for zero indexing
        elif(editor_selection == 3):
            if(len(schedule) == 0):
                print("No courses to be edited")
            else:
                display_schedule(schedule)
                print("Enter ID of course to be edited")
                edit_course_id = read_int(0, len(schedule) - 1)
                print("====================================")
                print(f"Course ID: {edit_course_id}")
                print(schedule[edit_course_id])
                print("====================================")
                edit_course_selection = -1
                while(edit_course_selection != 6):
                    print("1.) Edit Name    2.) Edit Location    3.) Edit Days\n4.) Edit Times    5.) Edit Notes    6.) Finish")
                    edit_course_selection = read_int(1, 6)
                    if(edit_course_selection == 1):
                        schedule[edit_course_id].name = input("Enter New Name: ")
                        print("====================================")
                        print(schedule[edit_course_id])
                        print("====================================")
                    elif(edit_course_selection == 2):
                        schedule[edit_course_id].location = input("Enter New Location: ")
                        print("====================================")
                        print(schedule[edit_course_id])
                        print("====================================")
                    elif(edit_course_selection == 3):
                        print("Enter number of meeting days")
                        course_frequency = read_int(1, 5)
                        meeting_days = []
                        valid_days = {1, 2, 3, 4, 5}
                        print("1.) Monday   2.) Tuesday    3.) Wendsday    4.) Thursday    5.) Friday")
                        for i in range(course_frequency):
                            while True:
                                day = read_int(1, 5)
                                if(day in valid_days):
                                    meeting_days.append(weekdays.get(day))
                                    valid_days.discard(day)
                                    break
                                else:
                                    print("This day is already in the schedule for this course")
                        schedule[edit_course_id].days = meeting_days
                        print("====================================")
                        print(schedule[edit_course_id])
                        print("====================================")
                    elif(edit_course_selection == 4):
                        schedule[edit_course_id].start_time = read_time("New Start Time: ")
                        schedule[edit_course_id].end_time = read_time("New End Time: ")
                        print("====================================")
                        print(schedule[edit_course_id])
                        print("====================================")
                    elif(edit_course_selection == 5):
                        schedule[edit_course_id].notes = input("Enter New Note: ")
                        print("====================================")
                        print(schedule[edit_course_id])
                        print("====================================")
                        
def edit_terms(breaks: List[Term]):
   
    breaks_selection = -1
    while(breaks_selection != 0):
        print("Enter 1 to add a break, 2 to remove a break, or 0 to continue.")
        breaks_selection = read_int(0, 2)
        if(breaks_selection == 1):
            print("Enter start date of break.")
            break_start_date = read_date()
            print("Enter end date of break.")
            break_end_date = read_date()
            sem_break = Term(start_date=break_start_date, end_date=break_end_date)
            breaks.append(sem_break)
            display_breaks(breaks)
        if(breaks_selection == 2):
            if(len(breaks) == 0):
                print("No breaks to be removed")
            else:
                display_breaks(breaks)
                print("Enter Break ID to be removed or -1 to go back")
                remove_break = read_int(-1, len(breaks) - 1)
                if(remove_break != -1):
                    breaks.pop(remove_break)
                    display_breaks(breaks)

def display_schedule(schedule: List[Course]):
    course_id = 0
    for course in schedule:
        print("====================================")
        print(f"Course ID: {course_id}")
        print(course)
        course_id += 1
    print("====================================")

def display_breaks(breaks: list[Term]):
    break_id = 0
    for sem_break in breaks:
        print("====================================")
        print(f"Break ID: {break_id}")
        print(sem_break)
        break_id += 1
        print("====================================")

def read_date() -> datetime:
    while(True):
        date_str = input("Enter a Date (YYYY-MM-DD): ")
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d")
            return date
        except ValueError:
            print("Invalid date format.")

def add_course_to_calendar(calendar: Calendar, course: Course, semester: Term, breaks: List[Term], timezone: pytz.timezone):
    event = Event()


    excluded_dates = []
    for sem_break in breaks:
        current_date = timezone.localize(sem_break.start_date)
        while(current_date <= timezone.localize(sem_break.end_date)):
            excluded_dates.append(datetime.combine(current_date.date(), course.start_time))
            current_date += timedelta(days=1)

    start_date = semester.start_date
    while(weekdays.get(start_date.weekday() + 1) not in course.days):#to find first date of occurence
        start_date += timedelta(days=1)

    event.add('dtstart', datetime.combine(start_date.date(), course.start_time))
    event.add('dtend', datetime.combine(start_date.date(), course.end_time))
    event.add('summary', course.name)
    event.add('location', course.location)
    event.add('description', course.notes)
    event.add('rrule', {'freq': 'weekly', 'byday': course.days, 'until': semester.end_date})
    event.add('exdate', excluded_dates)

    calendar.add_component(event)
    

print("welcome to this quick and easy iCal generator")
# Set the timezone
print("Choose your time zone")
general_US_zone = -1

while(general_US_zone < 1 or general_US_zone > 4 ):
    print("1.) New York   2.) Chicago   3.) Denver   4.) Los Angeles")
    general_US_zone = read_int(1, 4)

timezone = pytz.timezone(timezones.get(general_US_zone))

semester = Term()
print("**When does the semester start?")
sem_start = read_date()
print("**When does the semester end?")
sem_end = read_date()
semester.start_date = sem_start
semester.end_date = sem_end

menu_selection = -1
schedule = []
breaks = []
while(menu_selection != 5):
    print("1.) Display schedule    2.) Edit schedule    3.) Add Breaks    4.) Generate .ics file    5.) Quit")
    menu_selection = read_int(1, 5)
    if(menu_selection == 1): #display the schwedule
        display_schedule(schedule)
    
    elif(menu_selection == 2): #edit the schedule
        edit_schedule(schedule)

    elif(menu_selection == 3):
        edit_terms(breaks) #edit the semester term

    elif(menu_selection == 4):
        calendar = Calendar()
        calendar.add('prodid', '-//Schedule//')
        calendar.add('version', '2.0')

        for course in schedule:
            add_course_to_calendar(calendar, course, semester, breaks, timezone)
    
        calendar_name = input("Enter a name for the .ics file: ")
        calendar_path = calendar_name + ".ics"
        with open(calendar_path, 'wb') as f:
            f.write(calendar.to_ical())

        print(f"iCal file saved as {calendar_path}")
