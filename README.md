# Node

## How to use

Features:
- Weather: shows the weather based on your location geocoded by ip
- Profile: change your preferred name by clicking "Hello, <name>"
- To-do list: mark todos as complete/incomplete, overdue tasks are colored red, sorted by due date, click on tasks to edit them
- Notes: write notes, archive them, or delete them; search by keyword
- Calendar: add and edit events

To run the server locally, first run the following:

```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Then open http://localhost:8000/

Also should be currently deployed at https://project-101-node.herokuapp.com/



## Requirements

### Sprint 2

- Create login and user account system

### Sprint 3

- Figure out how to get the app to interact with other apps and systems
- Make sure Dashboard can display that information and update itself
- Get the dashboard to keep track of the weather

### Sprint 4

- Add a scheduler (schedules one day of events)
- No calendar yet
- Add a note creation, storage, and display system

### Sprint 5

- Add a calendar for multi-day scheduling
- Add a notification system

### Sprint 6

- Add email notification and display system
- Add toggle and other features to notification system

### Final Polish

- Finish customizing the notification system
- Make scheduling and organizing easy
- Make the app easy to use in general

I hope travis works..
