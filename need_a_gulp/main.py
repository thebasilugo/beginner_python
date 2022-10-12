import time
from _functions import GULP

cash_in_wallet = 0.00
stock = [6]
stock_names = ["Milk Chocolate", "Coffee", "Latte", "Cappuccino", "Espresso", "Wallet"]
stock_prices = [5.99, 8.66, 9.47, 11.28, 12.28, cash_in_wallet]

user_name = input("Welcome to Need a gulp, I'm Slushious. What is your name? \n")

gulp = GULP(stock_names, stock_prices, stock, cash_in_wallet, user_name)
#
# Welcome to Need a gulp!

# Staff_login = Number of login attempts for 'staff' to ensure that they are actually staff.
staff_login = 3

###################

if user_name != 'thebasilugo':
    print("Oh, I thought you were my programmer, Ugochukwu. Anyways, Welcome to Need a gulp, " + user_name + "!")

    # Name of user successfully obtained
    # Request the categorization of user.
    print("So, " + user_name + ", are you a staff or a customer?")
    user_input_any = input("Please use '1' for staff and '2' for customer. \n")
    if user_input_any == '1':
        print("Welcome, staff. Well you know how things are done here in Need a gulp.")

        while staff_login > 0:
            staff_input = input("Please input the employee password below to access the dashboard. \n").lower()
            time.sleep(1)
            if staff_input == 'need_a_gulp_rocks':
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

    elif user_input_any == '2':
        print(f"Welcome, {user_name}. You have logged in as a customer.")
        time.sleep(0.5)
    # Customers should have a dashboard too
        gulp.customer_dashboard()

    else:
        print("Sorry, " + user_name + ". Your input is invalid. Please Try again.")

    # Should be able to refer to beginning of code (using a function) so code can be efficiently run over time.
    # Should maybe have a "End" to end the process, instead of forcing customers to buy refreshments.

elif user_name == 'thebasilugo':
    print("Welcome chief, I hope you're having a lovely day.")

    # Should automatically log 'thebasilugo' in as a staff (or executive, if dashboard should exist)
    gulp.employee_dashboard()
