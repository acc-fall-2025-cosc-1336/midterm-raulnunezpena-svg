from question_c import use_local_variable
def main():
    num = 50
    use_local_variable(num)
    print(f"In main after function call, num = {num}")  


if __name__ == "__main__":
   
    main()
