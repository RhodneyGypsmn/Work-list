#This is a comment
name = input("What is your name? ")
birth_year = int(input("What is your birth year? "))
current_year = 2024
age = current_year - birth_year
residence = input("Where do u stay? ")
POW = input("Where do you work from? ")
salary = input("How much do earn? ")
hobby = input("What is your hobby? ")
#Am going to print the desirable message for the applicant.
print(f"Hello, {name}, of {age} years living in {residence} and working in {POW} getting a salary of USH {salary} and enjoying {hobby}. You have been admitted by Rhodney Gypsmn advocates to their job interview scheduled on 12th January 2025. You will be required to carry all the requirements as stated on our posters.  Thank you. Management.")

correct_password = "gablan"
is_authenticanted = False
password = input("Enter your password; ")
if password == correct_password: 
    is_authenticanted = True 
if is_authenticanted: 
    print("Access granted!") 
else:
    print("Access denied!") 
