# Spanish Quiz
#### Video Demo:  <https://www.youtube.com/watch?v=h0UVE0HDGyM&ab_channel=meimon>
#### Description: This project is a Spanish Language Quiz program. It allows users to sign up, log in, and take a quiz to test their knowledge of basic Spanish. The quiz includes multiple-choice questions, and users must score at least 80% to pass.

#### Description:
The Spanish Language Quiz Project is a command-line-based quiz application designed to help users learn and test their knowledge of basic Spanish vocabulary. The quiz includes questions on common Spanish words and their meanings.

## Files:

### 1. project.py
This file contains the main logic of the quiz application. It manages user interactions, such as signing up, logging in, and navigating through the quiz. The `main()` function serves as the entry point to the program.

### 2. test_project.py
The `test_project.py` file contains unit tests for the functions defined in `main.py`. These tests use the `pytest` framework to ensure the correctness of the implemented functions.

### 3. user_credentials.txt
The `user_credentials.txt` file is used to store user information, including usernames and hashed passwords. This file is created when a user signs up and is utilized for user authentication during login.

### 4. README.md
This documentation file provides an overview of the project, file descriptions, and instructions on how to use the application. It also includes a link to the video demo for a visual representation of the project.

## Functions Overview

### 1. `main()`
- Entry point to the program.
- Manages user interactions, including signup, login, and quiz navigation.

### 2. `sign_up()`
- Prompts the user to create an account with a valid username and password.
- Validates username and password according to specified rules.

### 3. `login()`
- Allows returning users to log in with their credentials.
- Validates entered username and password.

### 4. `quiz_intro()`
- Displays an introduction to the quiz before starting.

### 5. `display_questions(questions)`
- Presents quiz questions to the user.
- Collects and evaluates user responses, providing feedback.

### 6. `display_score(points, total_question, questions)`
- Shows the user's score at the end of the quiz.
- Offers an option to retake the quiz if the score is below the passing threshold.

## How to Use

1. **Sign Up**: To create an account, select option 1 from the main menu. Follow the prompts to enter a username and password. The username and password must consist of letters or numbers only, and both should be 6-10 characters long. Upon successful signup, the system will save your credentials, and you can proceed to log in.

2. **Log In**: If you already have an account, choose option 2 from the main menu. Enter your username and password when prompted. Upon successful login, you will gain access to the quiz section.

3. **Quiz**: Once logged in, choose option 2 to start the quiz. You will be presented with multiple-choice questions related to basic Spanish phrases. Select the letter corresponding to your chosen answer (A, B, C, or D). After answering all questions, you'll receive a score based on the number of correct answers.

4. **Scoring**: Your score will be displayed at the end of the quiz, indicating the percentage of correct answers. To pass and successfully complete the quiz, you need to achieve a score of at least 80%. If you fall below this threshold, you have the option to retake the quiz for a better score.

5. **Retake Quiz**: In case you want to improve your score or reinforce your knowledge, select option 2 to retake the quiz. You can retake the quiz as many times as needed to achieve the desired level of proficiency in basic Spanish phrases.

Feel free to explore and enjoy the Spanish Language Quiz to enhance your language skills!

