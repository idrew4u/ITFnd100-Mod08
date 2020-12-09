# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# ALi, Dec. 8, 2020,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []
objFile = None
dicRow = {}
strChoice = ""
strProduct = ""
strPrice = ""

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        ALi, Dec. 8, 2020, Modified code to complete assignment 8
    """
    pass
    # TODO: Add Code to the Product class
    # -- Constructor --
    def __int__(self, product_name, product_price):
        # -- Attributes --
        self.product_name = product_name
        self.product_price = product_price

    # -- Properties --
    # product_name
    @property
    def product_name(self): # (getter or accessor)
        return str(self.__product_name)

    @product_name.setter
    def product_name(self, value):  # (setter or mutator)
        if str(value).isnumeric() == False:
            self.__product_name = value
        else:
            raise Exception("Names cannot be numbers")

    # product_price
    @property
    def product_price(self): # (getter or accessor)
        return str(self.__product_price)

    @product_price.setter
    def product_price(self, value): # (settor or mutator)
        self.__product_price = value

    def __str__(self):
        return self.product_name + "," + self.product_price
# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        ALi, Dec. 8, 2020, Modified code to complete assignment 8
    """
    pass
    # TODO: Add Code to process data from a file
    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """
        Desc - Reads data from a file into a list of dictionary rows
        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        file = open(file_name, "r")
        for line in file:
            data = line.split(",")
            row = {"Product": data[0].strip(), "Price": data[1].strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows

    # TODO: Add Code to process data to a file
    @staticmethod
    def save_data_to_file(file_name, list_of_rows):
        """
        Desc - Writes data from a file into a list of dictionary rows
        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: nothing
        """
        pass

        objFile = open(file_name, "w")
        for dicRow in list_of_rows:
            objFile.write(dicRow["Product"] + "," + dicRow["Price"] + "\n")
        objFile.close()

    @staticmethod
    def add_row_to_list(product, price, list_of_rows):
        """
        Desc - Reads data from a file into a list of dictionary rows
        :param product: (string) with name of product:
        :param price: (string) with the price of product:
        :param list_of_rows: (list) you want filled with file data:
        :return: nothing
        """
        dicRow = {"Product": product, "Price": price}
        list_of_rows.append(dicRow)

    # Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring
    """ Performs Input and Output tasks """
    pass
    # TODO: Add code to show menu to user
    @staticmethod
    def show_menu():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Show current list
        2) Input new product
        3) Save Data to File        
        4) Exit Program
        ''')
        print() # Add an extra line for looks

    # TODO: Add code to get user's choice
    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    # TODO: Add code to show the current data from the file to user
    @staticmethod
    def print_current_products_in_list(list_of_rows):
        """ Shows the current Products in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Products and their Prices are: *******")
        for row in list_of_rows:
            print(row["Product"] + " (" + row["Price"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    # TODO: Add code to get product data from user
    @staticmethod
    def input_new_product_and_price():
        """ Adds Products and Prices from user's input to list

        :return: string
        """
        strProduct= str(input("What is the product name? ")).strip() # get product from user
        strPrice = str(input("What is the price of the product? ")).strip() # get price from user

        FileProcessor.add_row_to_list(strProduct, strPrice, lstOfProductObjects)
        IO.print_current_products_in_list(lstOfProductObjects)
        return strProduct, strPrice

    @staticmethod
    def save_file():
        # loads current data in the list
        IO.print_current_products_in_list(lstOfProductObjects)
        # confirms that user wants to save
        if("y" == str(input("Save new data to file? (y/n): ")).strip().lower()):
            # saves data to file and returns user to menu
            FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
            input("Data has been saved. Press the Enter key to return to menu.")
        elif("n" == str(input("Save new data to file? (y/n): ")).strip().lower()):
            # does not save data and returns user to menu
            input("New data was NOT saved. Press the Enter key to return to menu.")
        else:
            # does not save data and returns user to menu
            input("Invalid input. Press the Enter key to return to menu.")

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of product objects when script starts
FileProcessor.read_data_from_file(strFileName, lstOfProductObjects)

# Show user a menu of options
while(True):
    IO.show_menu()
# Get user's menu option choice
    strChoice = IO.input_menu_choice()

    # Show user current data in the list of product objects
    if (strChoice.strip() == "1"):
        IO.print_current_products_in_list(lstOfProductObjects)
        continue

    # Let user add data to the list of product objects
    elif(strChoice.strip() == "2"):
        IO.input_new_product_and_price()
        continue

    # let user save current data to file and exit program
    elif(strChoice == "3"):
        IO.save_file()
        continue

    elif(strChoice == "4"):
        break

# Main Body of Script  ---------------------------------------------------- #

