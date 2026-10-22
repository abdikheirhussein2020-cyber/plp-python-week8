
import random


# Tool 1: A calculator that performs basic arithmetic.
def calculator():
    print("\n--- Simple Calculator ---")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numbers.")
        return

    operation = input("Choose an operation (+, -, *, /): ")

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            print("Sorry, division by zero is not allowed.")
            return
        result = num1 / num2
    else:
        print(f"Sorry, {operation} is not a valid operation.")
        return

    print(f"The answer is: {result}")


# Tool 2: A to-do list that lets users manage their tasks.
def todo_list():
    tasks = []

    while True:
        print("\n--- To-Do List ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to the main menu")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            task = input("Enter your task: ").strip()

            if task:
                tasks.append(task)
                print(f"Task '{task}' has been added.")
            else:
                print("Task cannot be empty.")

        elif choice == "2":
            if not tasks:
                print("Your to-do list is empty.")
            else:
                print("\nYour tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")

        elif choice == "3":
            if not tasks:
                print("There are no tasks to remove.")
            else:
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")

                try:
                    number = int(
                        input("Enter the task number to remove: ")
                    )

                    if 1 <= number <= len(tasks):
                        removed = tasks.pop(number - 1)
                        print(f"Task '{removed}' has been removed.")
                    else:
                        print("That task number does not exist.")

                except ValueError:
                    print("Please enter a valid whole number.")

        elif choice == "4":
            print("Returning to the main menu.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


# Tool 3: A guessing game with five attempts.
def guessing_game():
    secret_number = random.randint(1, 20)
    attempts_left = 5

    print("\n--- Number Guessing Game ---")
    print("Guess a number between 1 and 20.")
    print(f"You have {attempts_left} attempts.")

    while attempts_left > 0:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        if guess < 1 or guess > 20:
            print("Choose a number between 1 and 20.")
            continue

        attempts_left -= 1

        if guess == secret_number:
            print(f"Congratulations! You guessed {secret_number}!")
            break
        elif guess < secret_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")

        if attempts_left > 0:
            print(f"You have {attempts_left} attempts left.")
    else:
        print(f"Game over! The number was {secret_number}.")


# Main menu: Repeats until the user chooses to quit.
def main():
    print("Welcome to the Python Toolkit!")

    while True:
        print("\nPlease choose a tool:")
        print("1. Simple Calculator")
        print("2. To-Do List")
        print("3. Number Guessing Game")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            calculator()
        elif choice == "2":
            todo_list()
        elif choice == "3":
            guessing_game()
        elif choice == "4":
            print("Thank you for using the Python Toolkit. Goodbye!")
            break
        else:
            print(
                f"Sorry, '{choice}' is not a valid choice. "
                "Please enter a number from 1 to 4."
            )


if __name__ == "__main__":
    main()
