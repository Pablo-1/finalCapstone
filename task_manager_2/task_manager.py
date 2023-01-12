#=====importing libraries===========
from datetime import datetime

# ========== DEFINING FUNCTIONS===========================

# ----------------------------------------------------

def reg_user():

    # asking user to input new user's name          
    while True :
        new_name = input("Please enter new username: ")
        j = 1
        with open("user.txt", "r") as f:
            for line in f:
                line = f.readline()
                if new_name in line:
                    print("User already exists. Please try again.")
                    j = 0
            if j == 1:
                break

    # asking for new password     
    new_password = input("Please enter new password: ")

    # loop asking to confirm the the password
    # loop will continue to ask for correct password in case wrong confirmation is entered
    while True:
        pass_conf = input("Please confirm password: ")
        if pass_conf == new_password:
            with open("user.txt", "a") as f:
                f.write(f" \n{new_name}, {new_password}")
                break
        else:
            print("You have enterred incorrect password, please try again: ")

#----------------------------------------------------

def add_task():    
    # getting input from the user
    name = input("Please enter a username of the person the task is asigned to: ")
    task_title = input("Please enter title of the task: ")
    task_descr = input("Please enter the task description: ")
    due_date = input("Please enter task due date: ")
    curr_date = input("Please enter current date: ")
    # writing recieved information into the file
    with open("tasks.txt", "a") as f:
        f.write(f"{name}, {task_title}, {task_descr}, {due_date}, {curr_date}, No\n")

#----------------------------------------------------

def view_all():
    # opening file in read only mode
    with open("tasks.txt", "r") as f:
        # loop counting over every line in file
        for line in f:
            line = line.rstrip(" \n") # stripping \n - new line characters from end of the line
            single_line = line.split(", ") # splitting a line into a list of single words
            # printing result in multiline format
            print(f'''
-------------------------------------------------------------------
    Task:                                {single_line[1]} 
    Assigned to:                         {single_line[0]}
    Date assigned:                       {single_line[4]}
    Due date:                            {single_line[3]}
    Task complete:                       {single_line[5]}
    Task description:
    {single_line[2]}   
-------------------------------------------------------------------
                    ''') 

#--------------------------------------------------------

def view_mine():
    # opening the file in read only mode
    with open("tasks.txt", "r") as f:
    # loop counting over every line in file
        i = 1
        task_number = [-1]
        for line in f:
            line = line.rstrip(" \n") # stripping \n - new line characters from end of the line
            single_line = line.split(", ") # splitting a line into a list of single words
            if name == single_line[0]: # checking if name of the person logged in is the same as person on the task
                task_number.append(i)
                # printing result in multiline format
                print(f'''
-------------------------------------------------------------------
    Task number:                         {task_number[i]}
    Task:                                {single_line[1]} 
    Assigned to:                         {single_line[0]}
    Date assigned:                       {single_line[4]}
    Due date:                            {single_line[3]}
    Task complete:                       {single_line[5]}
    Task description:
    {single_line[2]}   
-------------------------------------------------------------------
                    ''') 
                i += 1
        # asking user to choose task number they want to work on
        k = 0
        task = int(input("Please enter task number you want to work on : ")) 
        while k != 1:
            for i in task_number:
                if task == i  and task != 0:
                    k = 1
                    break
            if k != 1:
                task = int(input("Please enter correct task number:  "))
        # if user chooses -1 which is in position task_number[0] the loop wil break and go back to main menu

        # when user chooses other task asigned to them
        counter = 0
        if task in task_number:
            with open("tasks.txt", "r") as f:
                lines = f.readlines()
                for item in lines:
                    # if name f the user apears in line of the file counter goes up by one 
                    if name in item:
                        counter += 1
                        # if counter matches task number that means that we have foud the task chosen to be edited 
                        if task == counter:
                            # asking user to choose what operation they want to undertake on the record 
                            # loop with condition k != 1 detects incorrect input
                            seperate_line = lines[task - 1]
                            seperate_line = seperate_line.split(", ")
                            seperate_line[5] = seperate_line[5].strip("\n")
                            k = 0
                            while k != 1:
                                opertation = input("Please choose if you want to mark the task as completed or edit it (comp/edit): ")
                                # marking record as complete
                                if opertation == "comp" and seperate_line[5] != "Yes" :
                                    seperate_line[5] = "Yes\n"
                                    lines[task - 1] = ", ".join(seperate_line)
                                    k = 1
                                    
                                # editing due date or assigned name
                                elif opertation == "edit" and seperate_line[5] != "Yes":
                                    # loop with condition l != 1 detects incorrect input
                                    l = 0
                                    while l != 1:    
                                        name_or_date = input("Please enter weather you want to change assignment name or due date (name/date): ")
                                        # editing name
                                        if name_or_date == "name":
                                            seperate_line[0] = input("Please enter new name: ")
                                            lines[task - 1] = ", ".join(seperate_line)
                                            k = 1
                                            l = 1
                                        # editing due date
                                        elif name_or_date == "date":
                                            seperate_line[3] = input("Please enter new date: ")
                                            lines[task - 1] = ", ".join(seperate_line)
                                            k = 1
                                            l = 1
                                        else:
                                            # in case of incorrect input
                                            print("You have enteres incorrect option, please try again. ")
                                            l = 0
                                elif seperate_line[5] == "Yes":
                                    print("The task has already been completed. ")
                                    break
                                else:
                                    # in case of incorrect input
                                    print("You have entered incorrect option, try again. ")
                                    k = 0
            # putting next line character after Yes or No that indicates completenes of the task
            for items in lines:
                if "No" in item:
                    item.replace("No", "No\n")
                elif "Yes" in item:
                    item.replace("Yes", "Yes\n")

            # writing edited information into file 
            with open("tasks.txt", "r+") as f:
                for items in lines:
                    f.write(items)

#-----------------------------------------------------------------------------------

def reports():
    # opening tasks file to read data 
    with open("tasks.txt", "r") as f:
        data = f.readlines()

    # determining current date using datetime
    date = datetime.now()
    # converting date to string format to match date in the file
    date = date.strftime("%d %b %Y")
    # converting date back to datetime in order to be able to compare it with the date from file
    date = datetime.strptime(date, "%d %b %Y")

    # initialising varables to store information in
    tasks = 0
    com_tasks = 0
    n_com_tasks = 0
    overdue = 0
    # loop that goes trough all of the lines in data list
    for items in data:
        items = items.split(", ")
        tasks += 1
        if items[5] == "Yes\n":
            com_tasks += 1
        else:
            n_com_tasks += 1
        date_file = datetime.strptime(items[3], "%d %b %Y")
        if date_file < date and items[5] == "No\n":
            overdue += 1

    # calculating required percentages 
    per_incomplete =  (n_com_tasks/tasks) * 100
    per_overdue = (overdue/tasks) * 100

    # opening new file in "w" mode to write data into   
    with open("task_overview.txt", "w") as f:
        f.write(f'''
                    TASKS OVERVIEW
        
        ---------------------------------------------------
        Total number of tasks:          {tasks}
        Completed tasks:                {com_tasks}
        Uncompleted tasks:              {n_com_tasks}
        Overdue tasks:                  {overdue}
        Incomplete tasks %:             {per_incomplete}
        Overdue task %:                 {per_overdue}
        ----------------------------------------------------
            ''')

    # list containing users
    users = []
    # total tasks
    tasks = 0
    # used to calculate total tasks per user
    user_t = 0
    # list holding tasks per user values
    user_tp = []
    # number of tasks completed
    comp = 0
    # number of tasks not completed
    not_comp = 0
    # lists holding information about tasks being completed or not
    user_tasks_comp = []
    # list with tasks not completed
    user_tasks_not_comp = []
    # list with tasks overdue
    user_tasks_overdue = []


    # loop that goes trough all of the lines in data list
    # and writes user names into the users list as they appear in each line
    for items in data:
        items = items.split(", ")
        tasks += 1
        users.append(items[0])

    # loop calculating number of tasks per user
    for i in range(0, len(users)):
        user_t = 0
        for j in range(0, len(users)):
            if users[i] == users[j]:
                user_t += 1
        # tasks per user
        user_tp.append(user_t)

    # dictionary with information about total tasks per user
    users_dict = dict(zip(users, user_tp))

    # loop going over lines in data list
    # calculating tasks completed, not completed, tasks overdue
    i = 0
    for items in data:
        items = items.split(", ")
        if users[i] == items[0]:
            if items[5] == "Yes\n":
                comp +=1
                user_tasks_comp.insert(i, 1)
                user_tasks_not_comp.insert(i, 0)
                i += 1
            elif items[5] == "No\n":
                not_comp += 1
                user_tasks_not_comp.insert(i, 1)
                user_tasks_comp.insert(i, 0)
                i += 1
            else:
                i += 1
            date_file = datetime.strptime(items[3], "%d %b %Y")
            if date_file < date and items[5] == "No\n":
                user_tasks_overdue.insert(i, 1)
            else:
                user_tasks_overdue.insert(i, 0)

    # calculating percentage of completed tasks per user
    completed_percentage = dict()
    task_per = 0
    for key, value in users_dict.items():
        for i in range(0, len(users)):
            if key == users[i] and user_tasks_comp[i] == 1:
                task_per += 1
        completed_percentage[key] = (task_per/tasks)*100
        task_per = 0

    # calculating percentage of not completed tasks per user
    not_com_percentage = dict()
    task_per = 0
    for key, value in users_dict.items():
        for i in range(0, len(users)):
            if key == users[i] and user_tasks_not_comp[i] == 1:
                task_per += 1
        not_com_percentage[key] = (task_per/tasks)*100
        task_per = 0

    # calculating percentage of tasks not completed and overdue
    not_com_over_percentage = dict()
    task_per = 0
    for key, value in users_dict.items():
        for i in range(0, len(users)):
            if key == users[i] and user_tasks_overdue[i] == 1:
                task_per += 1
        not_com_over_percentage[key] = (task_per/tasks)*100
        task_per = 0


    # writing information into the file user_overview
    with open("user_overview.txt", "w") as f:
        f.write(f'''
        ---------------------------------------TASKS BREAKDOWN---------------------------------
        Total number of users:                                                  {len(users_dict)}
        Total number of tasks:                                                  {tasks}
        ------------------------------------TOTAL TASKS PER USER %-----------------------------
        ''')
        for key, value in users_dict.items():
            f.write(f'''
        Total number of tasks for {key} is:                                     {value}
        Percentage of total tasks assigned to {key} is:                         {(value/tasks)*100}''')
        f.write('''
        
        --------------------------------------COMPLETED TASKS %-------------------------------
        ''')
        for key, value in completed_percentage.items():
            f.write(f'''
        Percentage of total tasks assigned to {key} that have been completed:   {value}''')
        f.write('''
        
        ------------------------------------NOT COMPLETED TASKS %-----------------------------
        ''')
        for key, value in not_com_percentage.items():
            f.write(f'''
        Percentage of total tasks assigned to {key} that haven't been completed: {value}''')
        f.write('''
        
        --------------------------------NOT COMPLETED TASKS OVERDUE %-------------------------
        ''')
        for key, value in not_com_over_percentage.items():
            f.write(f'''
        Percentage of total tasks assigned to {key} that are overdue:             {value}''')

#-------------------------------------------------------------

def statistics():
    # reading from user.txt file
    with open("user.txt", "r") as f:
    # loop counting over every line in file
        user_count = 0
        for line in f:
            user_count += 1 
    # reading from tasks.txt file
    with open("tasks.txt", "r") as f:
    # loop counting over every line in file
        task_count = 0
        for line in f:
            task_count += 1 
    print(f'''
---------------------------------      
Number of tasks:         {task_count}
Number of users:         {user_count}
---------------------------------
        ''')  
#----------------------------------------------------------------
def disp_reports():
    # reading and displaying information on the screen
    with open("task_overview.txt", "r") as f:
        for line in f:
            print(line.strip("\n"))
    # reading and displaying information on the screen
    with open("user_overview.txt", "r") as f:
        for line in f:
            print(line.strip("\n"))
    
    print("\n")





#=========================Login Section=====================
''' Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''
# initialising empty lists to hold names and passwords from user.txt
user_names = []
passwords = []

# opening user.txt, reading names and passwords and storing it in seperate lists
with open("user.txt", "r") as f:
    for line in f:   # going over every single line in the file
        line = line.rstrip(" \n") # stripping new line characters from the end of the line
        single_line = line.split(", ") # splitting line into the single_line list of separate words 
        user_names.append(single_line[0])
        passwords.append(single_line[1])

    
# asking user for username and password
# loop asking for user name 
k = 0
name = input("Please enter your user name: ")   
while k != 1:
    for i in user_names:
        if i == name:
            k = 1
            break
    if k != 1:
        name = input("Please enter correct user name: ")

# determining position of username within the user_names list 
# in order to match it with the password and storing it in the match variable
match = 0
for i in range(0, len(user_names)):
    if name == user_names[i]:
        break
    else:
        match += 1

# loop asking for password
k = 0
password = input("Please enter your password: ")   
while k != 1:
    for i in passwords:
        if i == password and passwords[match] == password:
            k = 1
            break
    if k != 1:
        password = input("Please enter correct password: ")




while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    
    # admin menu with additional stats option
    if name == "admin":
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
gr - generate reports
dr - generate and display reports
ds - display statistics
e - Exit
: ''').lower()
    else:
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()





    if menu == 'r':
        
        '''In this block you will write code to add a new user to the user.txt file
        - You can follow the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same.
            - If they are the same, add them to the user.txt file,
            - Otherwise you present a relevant message.'''
        
        if name == "admin":
            # calling function reg user
            reg_user()
        else:
            print("\nYour credencials do not allow to register users. Please choose other option: \n")
            
        



    elif menu == 'a':
        
        '''In this block you will put code that will allow a user to add a new task to task.txt file
        - You can follow these steps:
            - Prompt a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.
            - Then get the current date.
            - Add the data to the file task.txt and
            - You must remember to include the 'No' to indicate if the task is complete.'''
        # calling add_task
        add_task()    


    elif menu == 'va':
        
        '''In this block you will put code so that the program will read the task from task.txt file and
            print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
            You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 
            - It is much easier to read a file using a for loop.'''
        # calling view_all
        view_all()
        

    elif menu == 'vm':
        
        '''In this block you will put code the that will read the task from task.txt file and
            print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
            ou can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same print it in the format of Output 2 in the task PDF'''
        # calling vie_mine
        view_mine()

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    # Compulsory Task 2, stats menu
    elif menu == "ds":
        # calling statistics
        statistics()
    

    elif menu == "gr":
        # calling reports
        reports()
    
    elif menu == "dr":
        reports()
        disp_reports()

    else:
        print("You have made a wrong choice, Please Try again")
        