# Functions for Need_A_Gulp
## imports
import time
import random

class GULP:

## initialization
    def __init__(self, stock_names, stock_prices, name, price, stock, cash_in_wallet, user_name, user_input, staff_id, purch_amt):
        self.stock_names = stock_names
        self.stock_prices = stock_prices
        self.name = name
        self.price = price
        self.stock = stock
        self.cash_in_wallet = cash_in_wallet
        self.user_name = user_name
        self.user_input = user_input
        self.staff_id = staff_id
        self.purch_amt = purch_amt
        


    def display_purchase(self, name, price):
        if self.cash_in_wallet > price:
            self.cash_in_wallet = self.cash_in_wallet - price
            time.sleep(0.5)
            print(f"You just purchased {self.name} for ${self.price}.")
            time.sleep(1)
            print(f"You now have ${self.cash_in_wallet} remaining.")
            self.user_input = input("1. Make another purchase\n2. End\n")
            if self.user_input == '1':
                self.customer_actual_dashboard()
            
            elif self.user_input == '2':
                print("Are you sure you want to quit? 'Y' for yes. Any other key would cancel it.")
                self.user_input = input().lower()
                if self.user_input == 'y':
                    print(f"Thank you for your patronage, {self.user_name}")
                    self.purchase_summary()

                else:
                    self.customer_dashboard()

            else: 
                print("Invalid input")
                self.customer_dashboard()


        elif price > self.cash_in_wallet:
            time.sleep(0.5)
            print(f"Sorry, insufficient balance. You have ${self.cash_in_wallet} in your wallet.")
            print("You'll be redirected to fund your wallet now.") 
            self.user_input= input("Is that okay? 'y' for yes, 'n' for no.\n").lower()
            if self.user_input == 'y':
                self.fund_wallet()

            elif self.user_input == 'n':
                print("This process would be terminated now. Thank you.")

            else:
                print("Invalid input. Please try again.")
                self.customer_actual_dashboard()

        else:
            print("Sorry, invalid input.")

    def employee_dashboard(self):
        staff_id = random.randint(0, 9999)
        print(f"Welcome to Need a gulp! Staff {self.user_name}. '{staff_id}' is your private staff id.")
        print(">>>>>MORE INFORMATION COMING SOON!<<<<<")
        time.sleep(1)
        self.employee_actual_dashboard()

    def employee_actual_dashboard(self):
        print("click '1' to purchase something, '2' to update prices or '3' to end.")
        self.user_input = input()
        if self.user_input == '1':
            time.sleep(1)
            self.customer_actual_dashboard()

        elif self.user_input == '2':
            self.list_update(self.name, self.price)
        
        elif self.user_input == '3':
            print("Come back soon.")

        else:
            print("Invalid input, Please try again.")
            self.employee_actual_dashboard()
    
    def list_update(self, name, price):
        print("Please use the menu below to update a price.")
        for i in range (len(self.stock_names)):
            for name in  self.stock_names:
                self.stock_names[name]
                print(f"{i+1}. {self.name}, {self.price}")
                name = name + 1
        pass

    def customer_dashboard(self):
        print(f"You have ${self.cash_in_wallet} in your wallet. Would you like to fund your wallet?")
        time.sleep(0.8)
        print("Click 'y', for 'Yes' and 'n' for 'No'.")
        fund_wallet_input = input().lower()
        if fund_wallet_input == 'y':
            self.fund_wallet()

        elif fund_wallet_input == 'n':
            self.customer_actual_dashboard()

        else:
            print("Invalid input. Try again.")
            time.sleep(0.5)
            self.customer_dashboard()
     
    #  def fund_wallet(self):
    #     add_funds = input("How much would you like to add to your account? $")
    #     if add_funds == int():
    #         confirm_add_funds = input(f"To be certain, did you mean ${add_funds}? 'y' for 'Yes'/ 'n' for 'No'. \n").lower()
    #         if confirm_add_funds == 'y':
    #             # Maybe add a password for security
    #             self.cash_in_wallet = self.cash_in_wallet + int(add_funds)
    #             print(f"Your wallet has been updated. Your new balance is ${self.cash_in_wallet}")
    #             self.customer_actual_dashboard()
            
    #         elif confirm_add_funds == 'n':
    #             print("Okay, then.")
    #             time.sleep(0.3)
    #             self.fund_wallet()

    #         else:
    #             print(f"{confirm_add_funds} is an invalid input, Please try again.")
    #             time.sleep(0.2)
    #             self.fund_wallet()

    #     else:
    #         print("Nice try. Please input an actual value")
    #         self.fund_wallet()

    def fund_wallet(self):
        add_funds = input("How much would you like to add to your account? $")
        confirm_add_funds = input(f"To be certain, did you mean ${add_funds}? 'y' for 'Yes'/ 'n' for 'No'. ").lower()
        if confirm_add_funds == 'y':
            # Maybe add a password for security
            self.cash_in_wallet = self.cash_in_wallet + int(add_funds)
            print(f"Your wallet has been updated. Your new balance is ${self.cash_in_wallet}")
            self.customer_actual_dashboard()

        elif confirm_add_funds == 'n':
            print("Okay, then.")
            time.sleep(0.3)
            self.fund_wallet()

        else:
            print(f"{confirm_add_funds} is an invalid input, Please try again.")
            time.sleep(0.2)
            self.fund_wallet()

    def customer_actual_dashboard(self):
        print("Please use the menu below to make a choice.")
        for i in range(len(self.stock)):
            print(f"{i + 1} > {self.stock_names[i]} : ${self.stock_prices[i]}")

        customer_input = input()

        if customer_input == '1':
            self.display_purchase('Milk Chocolate', 5.99)
            self.purch_amt()

        elif customer_input == '2':
            self.display_purchase('Coffee', 8.66)
            self.purch_amt()

        elif customer_input == '3':
            self.display_purchase('Latte', 9.47)
            self.purch_amt()

        elif customer_input == '4':
            self.display_purchase('Cappuccino', 11.28)
            self.purch_amt()

        elif customer_input == '5':
            self.display_purchase('Espresso', 12.28)
            self.purch_amt()

        elif customer_input == '6':
            print("1.Fund wallet \n2.<<Back.\n")
            customer_choice = input("So what would you like? ")
            if customer_choice == '1':
                self.fund_wallet()

            elif customer_choice == '2':
                self.customer_actual_dashboard()
            
            else:
                print("Invalid input. You will be redirected to the dashboard.")
                self.customer_actual_dashboard()
        else:
            print("Invalid input, please try again!")
            self.customer_actual_dashboard()
    
    def purch_amt(self):
        self.purch_amt = 0
        self.purch_amt = self.purch_amt + 1
        return self.purch_amt

    def purchase_summary(self):
        print(f"You made a total of {str(self.purch_amt)} purchase(s). They are:")
        # print(list_purch_amt)
        #This would be to display the total purchases.
        pass
