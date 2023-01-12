Capstone Project Task Manager 

The final iteration of user task managing program.
The program manages user data stored in user.txt file and tasks data stored in tasks.txt.
This version offers all of the same options for a regular user as the previous version
and expands admin functionality.

The program offers the following functionality:

1. r - registering a new user - the option registers new user and stores information in the user.txt file
2. a - add task - adding new task for a specific user and storing it in task.txt file
3. va - ciew all tasks - option prints out all of the tasks storred in tasks.txt file 
4. vm - view mine - option displays tasks assigned to a user crrently logged in 
5. e - exit - exits program

For a user with admin credentials the program offers additional functionality:
1. ga - generate reports - the option will generate two new files: 
   - user_overview containing:
      - total number of tasks assigned to a user
      - the percentage of the total number of tasks that heve been assigned to that user
      - the percentage of the total number of tasks that have been assigned to that user
      - the percentage of the tasks assigned to that user that have been completed
      - the percentage of tasks assigned to that user that not yet have been completed and are overdue

   - second file task_overview containing:
      - total number of tasks that have been generated using task_manager.py
      - total number of completed tasks
      - total number of uncompleted tasks
      - total number of tasks that haven't been completed and that are overdue

2. dr - display reports - this option grnerates and displays above reports on the screen
3. ds - display statistics - displays total number of users and total number of tasks 
