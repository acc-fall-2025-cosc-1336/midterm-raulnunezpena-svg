from question_b import get_fahrenheit

def main():
    print("Celsius\tFahrenheit")
    print("-------------------")
    
    for celsius in range(21):  # 0 through 20 inclusive
        fahrenheit = get_fahrenheit(celsius)
        print(f"{celsius}\t{fahrenheit:.1f}")

if __name__ == "__main__":
    main()
