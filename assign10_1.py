# Name: Erik Chao
# Assignment 10.1: Create Your Own Class
# Purpose: To use all the knowledge we understand to create our own class while implementing methods
# Acknowledgements:

# Global Variables

'''Create a coffee machine?
Have a coffee machine class, with different methods of implementing different ingridients into methods'''

'''Create a computer?
Have a computer class, with different methods of implementing different parts into methods'''


class CoffeeMachine:
    power = False
    def __init__(self):
        self.__total_ingredient = {"Milk": 0, "Coffee": 0, "Sugar": 0, "Chocolate": 0}
    


    # Displaying total amount of ingredients, the get() function
    def display_ingredient(self):
        return self.__total_ingredient

    def get_ingredient(self):
        self.total = sum(list(self.__total_ingredient.values()))
        return self.total

    def set_ingredient(self, ingredient_name, amount):
        ingredient_name = ingredient_name.title()
        self.__total_ingredient[ingredient_name] += amount

    def get_drinktypes(self):
        self.latte = {"Milk": 1, "Coffee": 1, "Sugar": 1}
        self.espresso = {"Coffee": 2}
        self.americano = {"Coffee": 1}
        self.mocha = {"Milk": 1, "Coffee": 1, "Sugar": 1, "Chocolate": 1}
        print(
            f"These are the different types of drink and their required ingredients:\nLatte: {self.latte}\nEspresso: {self.espresso}\nAmericano: {self.americano}\nMocha: {self.mocha}")

    def __str__(self):
        return (f"Total Ingredients ({self.total}): {str(self.__total_ingredient)}.")

    def create_coffee(self, type):
        if CoffeeMachine.power == False:
            print("Please turn on the Coffee Machine first!")

        else:
            if type == "latte":
                self.__total_ingredient["Milk"] -= 1
                if self.__total_ingredient["Milk"] < 0:
                    print(
                        "You can't make any lattes, you have no milk! Please add some more.")
                    self.__total_ingredient["Milk"] += 1
                    return
                self.__total_ingredient["Coffee"] -= 1
                if self.__total_ingredient["Coffee"] < 0:
                    print(
                        "You can't make any lattes, you have no coffee! Please add some more.")
                    self.__total_ingredient["Coffee"] += 1
                    return
                print("Latte has been served!")
                print(f"You have {self.__total_ingredient} left.")

            elif type == "americano":
                self.__total_ingredient["Coffee"] -= 1
                if self.__total_ingredient["Coffee"] < 0:
                    print(
                        "You can't make any americanos, you have no coffee! Please add some more.")
                    self.__total_ingredient["Coffee"] += 1

                    return
                print("Americano has been served!")
                print(f"You have {self.__total_ingredient} left.")

            elif type == "espresso":
                self.__total_ingredient["Coffee"] -= 2
                if self.__total_ingredient["Coffee"] < 0:
                    print(
                        "You can't make any espressos, you have no coffee! Please add some more.")
                    self.__total_ingredient["Coffee"] += 2
                    return
                print("Espresso has been served!")
                print(f"You have {self.__total_ingredient} left.")

            elif type == "mocha":
                self.__total_ingredient["Coffee"] -= 1
                if self.__total_ingredient["Coffee"] < 0:
                    print(
                        "You can't make any mochas, you have no coffee! Please add some more.")
                    self.__total_ingredient["Coffee"] += 1

                    return
                self.__total_ingredient["Milk"] -= 1
                if self.__total_ingredient["Milk"] < 0:
                    print(
                        "You can't make any mochas, you have no milk! Please add some more.")
                    self.__total_ingredient["Milk"] += 1
                    return
                self.__total_ingredient["Chocolate"] -= 1
                if self.__total_ingredient["Chocolate"] < 0:
                    print(
                        "You can't make any mochas, you have no chocolate! Please add some more.")
                    self.__total_ingredient["Chocolate"] += 1
                    return
                self.__total_ingredient["Sugar"] -= 1
                if self.__total_ingredient["Sugar"] < 0:
                    print("You can't make any mochas, you have no sugar! Please add some more.")
                    self.__total_ingredient["Sugar"] += 1
                    return
                print("Mocha has been served!")
                print(f"You have {self.__total_ingredient} left.")

    def turn_power(self, switch):
        if switch == "on":
            CoffeeMachine.power = True
            print("Power is on!")
        elif switch == "off":
            CoffeeMachine.power = False
            print("Power is off!")

# Main
# Make main function a user inputted system
# Asks user for what type of coffee they want, how much ingredients are left, turn machine off or on
def main():
    # Defining class to be easily used in main function
    x = CoffeeMachine()
    # Created while loop for easier access to main menu 
    while True:
        # If power is off, CoffeeMachine will not create drinks for user
        if x.power == False:
            print("Power: Off")
        else:
            print("Power: On")
        # String input for user
        y = input("Welcome to Erik's Coffee Machine!\nPlease enter your desired option:\n - Turn on/off machine('on'/'off')\n - Add Ingredients('add')\n - Display Ingredients('display')\n - Drink Types('drinks')\n - Make Drinks('make')\n - Exit('exit')\n-->")
        if y == 'on':
            x.turn_power("on")
        elif y == 'off':
            x.turn_power("off")
        # If user inputted 'add' brings them to multiple inputs as arguments for add_ingredient()
        elif y == 'add':
            try:
                item = input("What ingredient would you like to add?\n - Milk('milk')\n - Coffee('coffee')\n - Sugar('sugar')\n - Chocolate('chocolate')\n-->")
                amount = int(input("How many would you like to add?\n-->"))
                x.set_ingredient(item, amount)
                # Confirming item and amount for user to visually see
                print(f"Added {amount} {item}.")
            except ValueError:
                print("Please enter an integer.")
        elif y == 'display':
            try:
                # Displays all ingredients that have been added and how much they can use
                display = x.display_ingredient()
                print(display)
            # Goes through AttributeError if there are no values in the ingredient dict
            except AttributeError:
                print("Please set a desired amount of ingredients first.")
        elif y == 'drinks':
            # Prints out drink types, created by get_drinktypes()
            x.get_drinktypes()
        # User inputs what drinks they want, then call .create_coffee() with input as argument
        elif y == 'make':
            try:
                m1 = (input("What drink would you like to make?\n - Latte('latte')\n - Espresso('espresso')\n - Americano('americano')\n - Mocha('mocha')\n-->"))
                x.create_coffee(m1)
            except AttributeError:
                print("Please set a desired amount of ingredients first.")
        
        elif y =='exit':
            return
        # Add add.ingredient(), be sure to make it so it updates the ingredient dict
        else:
            print("Please enter the correct input.")


if __name__ == "__main__":
    main()
