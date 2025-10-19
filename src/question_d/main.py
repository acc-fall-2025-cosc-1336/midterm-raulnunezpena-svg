from question_d import get_mph

def main():
    kilometers = int(input("Enter kilometers: "))
    minutes = int(input("Enter minutes: "))

    result = get_mph(kilometers, minutes)
    print("Miles per hour:", result)

if __name__ == "__main__":
    main()
