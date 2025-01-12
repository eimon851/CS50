import os
import re
import sys

# Define the set of questions
questions = [
    {
        'text': 'What does "Hola" mean?',
        'options': ['Goodbye', 'Hello', 'Thank you', 'Excuse me'],
        'correct_answer': 'B'
    },
    {
        'text': 'What does "Adiós" mean?',
        'options': ['Please', 'No', 'Yes', 'Goodbye'],
        'correct_answer': 'D'
    },
    {
        'text': 'What does "Gracias" mean?',
        'options': ['Sorry', 'Thank you', 'Yes', 'Excuse me'],
        'correct_answer': 'B'
    },
    {
        'text': 'What does "Por favor" mean?',
        'options': ['Good morning', 'Please', 'Sorry', 'Ben'],
        'correct_answer': 'B'
    },
    {
        'text': 'What does "Muchu Gusto" mean?',
        'options': ['Nice to meet you', 'Where', 'You', 'Been'],
        'correct_answer': 'A'
    }
]

def main():
    create_credentials_file()
    while True:
        clear_screen()
        print("+------------------------------------+")
        print("|  Welcome to the Language Quiz:     |")
        print("|         Spanish Edition            |")
        print("+------------------------------------+")
        print("|  1. Sign up                        |")
        print("|  2. Login                          |")
        print("|  3. Exit                           |")
        print("+------------------------------------+")

        try:

            choice = input("Select the desired number from the given options [1-3]: ")

            if choice == '1':
                sign_up()
            elif choice == '2':
                login()
            elif choice == '3':
                exit_program()

        except EOFError:
            print("\nExiting the program.")
            sys.exit()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_credentials_file():
    # Create the user credentials file if it doesn't exist
    filename = "user_credentials.txt"
    if not os.path.isfile(filename):
        with open(filename, "w") as file:
            pass  # File is created with no content

def sign_up():
    clear_screen()
    print("+---------------------------------------+")
    print("|              Sign Up                  |")
    print("|                                       |")
    print("| To create an account, please follow   |")
    print("| these rules:                          |")
    print("| - Username and password must consist  |")
    print("|   of letters or numbers only.         |")
    print("| - Both should be 6-10 characters long.|")
    print("|                                       |")
    print("| *To return to homepage, press Ctrl-d* |")
    print("+---------------------------------------+")

    while True:
        username = input("Username: ")
        if username == '':
            print("Returning to the homepage.")
            input("Press Enter to continue...")
            return  # Return to the main menu

        if validate_username(username):
            if username_exists(username):
                print("Username already exists. Please choose a different one.")
            else:
                print("Valid username. Now enter your password:")
                while True:
                    password = input("Password: ")
                    if validate_password(password):
                        save_credentials(username, password)
                        print("Username and password saved successfully!")
                        input("Press Enter to continue...")
                        return  # Return to the main menu
                    else:
                        print("Invalid password. Please follow the rules.")
        else:
            print("Invalid username. Please follow the rules.")


def validate_username(username):
    pattern = re.compile(r'^[a-zA-Z0-9]{6,10}$')
    match = pattern.fullmatch(username)
    return match is not None

def validate_password(password):
    pattern = re.compile(r'^[a-zA-Z0-9]{6,10}$')
    match = pattern.fullmatch(password)
    return match is not None

def username_exists(username):
    # Check if the username already exists in the file
    with open("user_credentials.txt", "r") as file:
        for line in file:
            existing_username, _ = line.strip().split(",")
            if username == existing_username:
                return True
    return False

def check_password(username, entered_password):
    filename = "user_credentials.txt"

    with open(filename, "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split(",")
            if username == stored_username:
                return entered_password == stored_password

    return False

def save_credentials(username, password, filename="user_credentials.txt"):
    # Save the username and password to the file
    with open(filename, "a") as file:
        file.write(f"{username},{password}\n")

def login():
    clear_screen()
    print("+---------------------------------------+")
    print("|               Log in                  |")
    print("| *To return to homepage, press Ctrl-d* |")
    print("+---------------------------------------+")

    while True:
        username = input("Username: ")
        if username == '':
            print("Returning to the homepage.")
            input("Press Enter to continue...")
            return  # Return to the main menu

        if validate_username(username):
            if username_exists(username):
                password = input("Password: ")
                if check_password(username, password):
                    print("Login successful!")
                    input("Press Enter to continue...")
                    quiz_intro()
                    display_questions(questions)
                    return  # Return to the main menu or go to a different section
                else:
                    print("Incorrect password. Please try again.")
            else:
                print("Username not found. Please try again or press Ctrl-d to return to the homepage.")
        else:
            print("Invalid username. Please follow the rules or press Ctrl-d to return to the homepage.")

def quiz_intro():
    clear_screen()
    print("+--------------------------------------------------+")
    print("|          Welcome to your Spanish Quiz            |")
    print("| You will be given 5 basic questions on unit 1.   |")
    print("| These questions will all be in multiple choice.  |")
    print("|     Must get at least 80% to pass this quiz     |")
    print("+--------------------------------------------------+")

    input("Press Enter to begin your quiz: ")

def display_questions(questions):
    clear_screen()
    letter_options = ["A", "B", "C", "D"]
    total_question = len(questions)
    points = 0

    for i in range(total_question):
        current_question = questions[i]
        correct_answer = current_question.get("correct_answer")

        print(f"Question {i + 1}:\n\n{current_question.get('text')}")
        for j, option in enumerate(current_question.get("options")):
            print(f"{letter_options[j]}. {option}")

        user_answer = input("\nYour answer: ").upper()

        if user_answer == correct_answer:
            points += 1
            leave = input("Correct! Press enter to continue...")
        else:
            print(f"Incorrect. The correct answer was {correct_answer}")
            leave = input("\nPress enter to continue...")

        if leave == "":
            clear_screen()

    display_score(points, total_question, questions)

def display_score(points, total_question, questions):
    clear_screen()
    print("Quiz Completed!\n")
    print(f"You answered {points} out of {total_question}")
    percentage = points / total_question * 100
    print(f"Your score: {int(percentage)}%")

    if percentage < 80:
        fail = input("You've failed... press enter to retake quiz! ")
        if fail == "":
            display_questions(questions)
    else:
        success = input("Congratulations you've passed! Press enter to return to home screen! ")
        if success == "":
            main()


def exit_program():
    # Logic to exit the program
    print("Exiting the program.")
    sys.exit()

if __name__ == "__main__":
    main()
