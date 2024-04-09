admins = []
users = []
questions = []

def display_menu():
    print("\n\nWelcome to Quiz Management System!")
    print("\n1. Admin Sign Up")
    print("2. User Sign Up")
    print("3. Admin Login")
    print("4. User Login")
    print("5. Quit")

def admin_sign_up():
    print("\nAdmin Sign Up")
    username = input("Enter your desired username: ")
    password = input("Enter your password: ")
    
    if not username.strip() or not password.strip():
        print("Username or password cannot be empty. Going back to menu.")
        return
    
    admins.append({'username': username, 'password': password})
    print("Admin Account Successfully Created!")

def user_sign_up():
    print("\nUser Sign Up")
    username = input("Enter your desired username: ")
    password = input("Enter your password: ")
    
    if not username.strip() or not password.strip():
        print("Username or password cannot be empty. Going back to menu.")
        return
    
    users.append({'username': username, 'password': password})
    print("User Account Successfully Created!")

def admin_login():
    print("\nAdmin Login")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    for admin in admins:
        if admin['username'] == username and admin['password'] == password:
            print("Sign in Successfully!")
            admin_menu(username)
            return
    
    print("Invalid username or password")

def user_login():
    print("\nUser Login")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    for user in users:
        if user['username'] == username and user['password'] == password:
            print("Sign in Successfully!")
            user_menu(username)
            return
    
    print("Invalid username or password")

def admin_menu(username):
    print(f"\n\nHi Admin {username}")
    while True:
        print("\n1. Add Questions")
        print("2. Remove Questions")
        print("3. Reset Questions")
        print("4. Logout")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_questions()
        elif choice == '2':
            remove_questions()
        elif choice == '3':
            reset_questions()
        elif choice == '4':
            print("Logging out.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def user_menu(username):
    print(f"\nHi {username}")
    while True:
        print("\nUser Menu")
        print("1. Take Quiz")
        print("2. Logout")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            take_quiz()
        elif choice == '2':
            print("Logging out.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def add_questions():
    print("\nAdd Questions")
    question = input("Enter the question you want to add: ")
    answer = input("Enter the answer: ")
    
    if not question.strip() or not answer.strip():
        print("Question or answer cannot be empty.")
        return
    
    questions.append({'question': question, 'answer': answer})
    print("Question Successfully Added!")

def remove_questions():
    print("\nRemove Questions")
    question_to_remove = input("Enter the question you want to remove: ")
    
    removed = False
    for question in questions:
        if question['question'] == question_to_remove:
            questions.remove(question)
            removed = True
            print("Question Successfully Removed!")
            break
    
    if not removed:
        print("Question Invalid!")

def reset_questions():
    print("\nReset Questions")
    confirmation = input("Are you sure you want to reset all the Questions and Answers? Type CONFIRM if yes: ")
    if confirmation.strip().lower() == "confirm":
        questions.clear()
        print("All questions and answers have been reset.")
    else:
        print("Reset canceled. Returning to Admin Menu.")

def take_quiz():
    print("\nTake Quiz")
    if questions:
        score = 0
        total_questions = len(questions)
        for idx, question in enumerate(questions, start=1):
            print(f"\nQuestion {idx}: {question['question']}")
            user_answer = input("Your Answer: ").strip().lower()
            if user_answer == question['answer'].lower():
                score += 1
        percentage_score = (score / total_questions) * 100
        print(f"\nYour score: {score}/{total_questions}")
        print(f"Percentage Score: {percentage_score:.2f}%")
        if percentage_score >= 70:
            print("Congratulations! You passed the quiz.")
        else:
            print("Sorry, you did not pass the quiz. Try again next time.")
    else:
        print("No Quiz to take.")


def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            admin_sign_up()
        elif choice == '2':
            user_sign_up()
        elif choice == '3':
            admin_login()
        elif choice == '4':
            user_login()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
    
