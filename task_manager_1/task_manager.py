#=====importing libraries===========
'''This is the section where you will import libraries'''

#====Login Section====
'''Here you will write code that will allow a user to login.
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
stats - displaying statistics
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
            # asking user to input new name and password
            new_name = input("Please enter new username: ")
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
            
        # getting input from the user
        name = input("Please enter a username of the person the task is asigned to: ")
        task_title = input("Please enter title of the task: ")
        task_descr = input("Please enter the task description: ")
        due_date = input("Please enter task due date: ")
        curr_date = input("Please enter current date: ")
        # writing recieved information into the file
        with open("tasks.txt", "a") as f:
                    f.write(f" \n{name}, {task_title}, {task_descr}, {due_date}, {curr_date}, No")




        

    elif menu == 'va':
        
        '''In this block you will put code so that the program will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 
            - It is much easier to read a file using a for loop.'''
        # opening the file in read only mode
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
        

    elif menu == 'vm':
        
        '''In this block you will put code the that will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same print it in the format of Output 2 in the task PDF'''
        # opening the file in read only mode
        with open("tasks.txt", "r") as f:
        # loop counting over every line in file
            for line in f:
                line = line.rstrip(" \n") # stripping \n - new line characters from end of the line
                single_line = line.split(", ") # splitting a line into a list of single words
                if name == single_line[0]: # checking if name of the person logged in is the same as person on the task
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

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    # Compulsory Task 2, stats menu
    elif menu == "stats":
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
    

    else:
        print("You have made a wrong choice, Please Try again")
        