from question_a import is_prime

def main():
    while True:
        user_input = input("Enter a number (or 'q' to quit): ")

        if user_input.lower() == 'q':
            print("Goodbye!")
            break

        try:
            number = int(user_input)
            if is_prime(number):
                print(f"{number} is a prime number.")
            else:
                print(f"{number} is not a prime number.")
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
