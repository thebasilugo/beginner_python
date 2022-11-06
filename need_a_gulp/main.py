# Welcome to Need a gulp!

## imports/packages
import time
import random
from _functions import GULP

## initializations
cash_in_wallet = 0.00
stock = [0, 0, 0, 0, 0, 0]
stock_names = ["Milk Chocolate", "Coffee", "Latte", "Cappuccino", "Espresso", "Wallet"]
stock_prices = [5.99, 8.66, 9.47, 11.28, 12.28, cash_in_wallet]
# The array below would be used to create a random char to append to the pin
# dict_char=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

user_name = input("Welcome to Need a gulp, I'm Slushious. What is your name? \n")
user_input = 0
staff_id = 0
purch_amt = 0
name = '0'
price = 0

gulp = GULP(stock_names, stock_prices, name, price, stock, cash_in_wallet, user_name, user_input, staff_id, purch_amt)
#

# Staff_login = Number of login attempts for 'staff' to ensure that they are actually staff.
staff_login = 3
###################

if user_name != 'thebasilugo':
    print("Oh, I thought you were my programmer, Ugochukwu. Anyways, Welcome to Need a gulp, " + user_name + "!")

    # Name of user successfully obtained
    print("So, " + user_name + ", are you a staff or a customer?")
    user_input = input("Please use '1' for staff and '2' for customer. \n")
    if user_input == '1':
        print("Welcome, staff. Well you know how things are done here in Need a gulp.")

        while staff_login > 0:
            user_input = input("Please input the employee password below to access the dashboard. \n").lower()
            time.sleep(1)
            if user_input == 'need-a-gulp-rocks':
                print("Correct password!")
                gulp.employee_dashboard()
                break

            else:
                staff_login = staff_login - 1
                time.sleep(0.5)
            print(f"Wrong password, Try again! {str(staff_login)} tries left!")
            if staff_login == 1:
                time.sleep(0.5)
                print("Wrong password, Try again! " + str(staff_login) + " try left!")
            if staff_login == 0:
                time.sleep(0.5)
                print("Unfortunately, you failed the password thrice. You would be logged in as a customer.")
                gulp.customer_dashboard()

    elif user_input == '2':
        print(f"Welcome, {user_name}. You have logged in as a customer.")
        time.sleep(0.5)
    # Customers should have a dashboard too
        gulp.customer_dashboard()

    else:
        print("Sorry, " + user_name + ". Your input is invalid. Please Try again.")
        

        # Should be able to refer back to beginning so code can be efficiently run over time.
        # Should maybe have an "End" to end process, instead of forcing customers to buy.

elif user_name == 'thebasilugo':
    print("Welcome chief, I hope you're having a lovely day.")
    cash_in_wallet = 200

    # Should automatically log 'thebasilugo' in as a staff (or executive, if dashboard should exist)
    gulp.employee_dashboard()
