from tabulate import tabulate
#========The beginning of the class==========
class Shoe:
    # initializing class attributes
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
    # get cost method
    def get_cost(self):
        return self.cost
    # get quantity method
    def get_quantity(self):
        return self.quantity
    # printing method
    def __str__(self):
        return f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}"

#=============Shoe list===========
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data():
    
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
    # initializing empty shoe 1 list 
    shoe1 = []
    try:
        # reading information from inventory file and saving it in the lines list
        with open("inventory.txt", "r") as f:
            f.seek(0)
            for lines in f:
                lines = f.readlines()
            # reading every item(line) in lines list, stripping new line character and putting result in shoe1 list
            for line in lines:
                line = line.strip("\n")
                shoe1.append(line)
        # temporary variable to hold country, product, cost, quantity values
        temp = ""
        # loop appending Shoe() items to shoe_list
        for item in shoe1:
            # if statement skips last line which is empty after stripping end of line character
            if item != "":
                temp = item
                temp = temp.split(",")
                country = temp[0]
                code = temp[1]
                product = temp[2]
                cost = temp[3]
                quantity = temp[4]
                # appending shoe class item to shoe_list
                shoe = Shoe(country, code, product, cost, quantity)
                shoe_list.append(shoe)
    # exception if file is not found
    except FileNotFoundError:
        print("File does not exist.")
    return shoe_list

def capture_shoes():
    
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    # asking user to input all of information that will be stored as class Shoe attributes
    print("Please input shoe information: ")
    country = input("Country of production: ")
    code = input("Item code: ").upper()
    product = input("Please type in model: ")
    cost = input("Please enter cost: ")
    quantity = input("Please enter quantity: ")
    # appending shoe_list
    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)
    # updating inventory file
    with open("inventory.txt", "a") as f:
        f.write("\n" + str(shoe))

def view_all():
    # temporary lists used to hold values from shoe_list in order to print with tabulate
    table = []
    sep = []
    for shoe in shoe_list:
        sep = [shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity]
        table.append(sep)
    # printing all items from shoe_list in a table using tabulate
    print(tabulate(table, headers = ["Country","Code","Product","Cost","Quantity"],tablefmt="simple_grid"))

def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    # loop determining item with the lowest stock
    lowest_quantity = []       
    for item in shoe_list:
        lowest_quantity.append(int(item.quantity))
    # finding index of the lowest stock item
    index = min(lowest_quantity)
    # printing out lowest stock item
    for item in shoe_list:
        # if index (determined as being the lowest value) is equal to item.quantity attribute 
        # that means we have found our shoe (item) which then can be printed out 
        if index == int(item.quantity):
            shoe_to_restock = item
            print(f"Item to restock {shoe_to_restock}\n")
            print(f"Quantity left {shoe_to_restock.quantity}\n")

    # restocking options
    while True:
        # asking user to pick option to restock or leave without amending the item
        how_much = input(
            '''Would you like to restock:
                -  If yes please type in quantity you want to restock:
                -  If no please type N:
            ''' ).upper()
        # if option to restock is taken the line in inventory file is being updated
        if how_much.isdigit():# if input has been determined to be a digit
            shoe_to_restock.quantity = how_much # .quantity attribute is being changed to the one inputted by the user
            with open("inventory.txt", "r") as f:
                i = 0
                lines = f.readlines()
                # reading information from the file
                for line in lines:
                    # i variable to make sure we don't go out of range when checking lines
                    i += 1
                    # if shoe_to_restock (determined earlier to be the one with the lowest stock) is found in a given line
                    # line is being stripped from end of line character, split into separate list items, item[4] which is quantity
                    # is being amended after which list is being put together with .join statement and stripped of unnecessary \
                    # characters, end of line character is being added 
                    if shoe_to_restock.code in line:
                        line = line.strip("\n")
                        line = line.split(",")
                        line[4] = shoe_to_restock.quantity
                        line = ",".join(line)
                        line = line.strip("'")
                        line = line.replace("'", "")
                        line = line.replace(", ", ",")
                        lines[i-1] = line + "\n"
            # final, amended lines list is being written to the inventory.txt file
            with open("inventory.txt", "w") as f:
                f.writelines(lines)
                f.write("\n")
            break
        # if the user chooses not to restock
        elif how_much == "N":
            break
        else:
            print("You have entered incorrect value, please try again. \n")




def search_shoe():
    # asking user to input shoe code
    code = input("Please enter the shoe code: ").upper()
    # going trough all of the shoe_list items to check if they contain given code as item.code (Shoe class attribute)
    for item in shoe_list:
        if code in item.code:
            print(f"The item: {item}")


def value_per_item():
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    # initializing empty lists to hold cost, number of items and make data respectively
    cost = []
    number_of_items = []
    make = []
    # appending the lists
    for shoe in shoe_list:
            make.append(shoe.product)
            cost.append(shoe.cost)
            number_of_items.append(shoe.quantity)
    # printing out value per item
    print("Price for pair of: ")
    # temporary lists to hold calculated values
    tab = [] # tab holds all of the values
    item = [] # item holds a single to be appended to the tab list
    for i in range(len(cost)):
        item = [make[i], round(int(cost[i])/int(number_of_items[i]), 2)]
        tab.append(item)
    # printing items and corresponding calculated values in a table using tabulate
    print(tabulate(tab, headers=["make", "value"],tablefmt="simple_grid"))

def highest_qty():
    
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    # initializing quantity list to store quantities of all shoe_list items
    quantity = []
    # appending .quantity attribute to quantity list
    for shoe in shoe_list:
        quantity.append(int(shoe.quantity))
    # index of highest stock item in quantity list
    highest = max(quantity)
    # printing out result
    for shoe in shoe_list:
        # if shoe class item quantity in a shoe_list is the same as highest variable 
        # that means we have found our shoe and we can print out the result
        if highest == int(shoe.quantity):
            print (f"{shoe} is on sale")

#================================
# populating shoe list using read_shoe_data function
read_shoes_data()

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
# menu loop with menu options
while True:
    print('''
    -------------------------------------------------------------
    Welcome to Inventory software.

    Please choose from one of the options below:
    cs - capture shoes
    va - view all items in stock
    re - restock item with lowest quantity in stock
    ss - search shoe
    vp - display value of single pair of shoes currently in stock
    hq - display shoes in hightest quantity currently in stock
    e - exit
    -------------------------------------------------------------
    ''')
    # user inputs option from the menu is being converted to lower case
    menu = input("Option :").lower()

    # statements below checking what has been inputted by the user
    if menu == "cs":
        capture_shoes()

    elif menu == "va":
        view_all()
    
    elif menu == "re":
        re_stock()

    elif menu == "ss":
        search_shoe()
    
    elif menu == "vp":
        value_per_item()
    
    elif menu == "hq":
        highest_qty()
    
    elif menu == "e":
        print("Program ended.")
        exit()

    # in case incorrect input
    else:
        print("You have entered incorrect option. Please try again.")