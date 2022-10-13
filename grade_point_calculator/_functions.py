import time


class CALCULATE:

    def __init__(self, choice):
        self.choice = choice

    def altogether(self):
        print("Click '1' to Begin the program. Click '2' to suggest upgrades to the program.")
        choice = input()
        if choice == '1':
            self.gp_calculator()
        elif choice == '2':
            self.make_suggestion()
            pass
        else:
            print("Unrecognizable input. Please retry this process.")
            self.altogether()

    def gp_calculator(self):
        print("What would you like me to calculate? GPA or CGPA?")
        time.sleep(0.2)
        print("Please input '1' for GPA and '2' for CGPA.")
        choice = input("Please know that inputting any thing other than the above would restart this process. \n")
        if choice == '1':
            self.calculate_gpa()

        elif choice == '2':
            self.calculate_cgpa()

        else:
            self.gp_calculator()

    def make_suggestion(self):
        pass

    def calculate_gpa(self):
        print(">>>>GPA CALCULATOR<<<<")
        time.sleep(0.5)
        print("This means that you'll be calculating for a single semester.")
        time.sleep(1)
        choice = input("Please click '1' to continue, or '2' to calculate CGPA instead.\n")
        if choice == '1':
            pass
        elif choice == '2':
            print("Redirecting you to the cgpa calculator!")
            time.sleep(1)
            print(f"...")
            time.sleep(1)
            self.calculate_cgpa()
        else:
            print("Wrong input.")
            self.calculate_gpa()

    def calculate_cgpa(self):
        print(">>>>CGPA CALCULATOR<<<<")
        time.sleep(0.5)
        print("This means that you'll be calculating for a couple semesters.")
        time.sleep(1)
        print("You would also be able to add an extra semester or remove one in this program, if necessary.")
        time.sleep(1)
        choice = input("Please click '1' to continue, or '2' to calculate GPA instead.\n")
        if choice == '1':
            print("How many sessions do you want to calculate? (N.B: 1 session = 2 semesters)")
            choice = 0
            choice = int(input())
            choice = choice * 2
            print(f"You said {choice} semesters.")
            time.sleep(0.5)
            print("'1', Add a semester. '2', Remove a semester. '3', Continue calculation.")

        elif choice == '2':
            print("Redirecting you to the gpa calculator!")
            time.sleep(1)
            print("...")
            time.sleep(1)
            self.calculate_gpa()
        else:
            print("Wrong input.")
            self.calculate_cgpa()
