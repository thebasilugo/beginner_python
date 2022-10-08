# Welcome to Need a gulp!
####################################################################
    # Request the name of the user.
user_name = input("Welcome to Need a gulp, I'm Slushious. What is your name? \n").lower()
if user_name != 'thebasilugo':
    print("Oh, I thought you were my programmer, Ugochukwu. Anyways, Welcome to Need a gulp, " + user_name + "!")

   # Request the categorization of user.
    print("So, " + user_name + ", are you a staff or a customer?")
    user_input_any = input("Please use '1' for staff and '2' for customer. \n")
    if user_input_any == '1':
        print("Welcome, staff.")
        # Staffs should have a dashboard

    elif user_input_any == '2':
        print("Welcome, customer.")
        # Customer's should have a dashoard too

    else:
        print("Sorry, " + user_name + ". Your input is invalid. Please Try again.")
    # Should be able to refer to beginning of code (using a function) so code can be efficiently run over time.
    # Should maybe have a "End" to end the process, instead of forcing customers to buy refreshments.

elif user_name == 'thebasilugo':
    print("Welcome Chief, I hope you're having a lovely day.")
    #should automatically log 'thebasilugo' in as a staff (or executive, if executive_dashboard should exist)
