def init(name, age):
    print("Initializing program...")
    print(f"Name: {name}")
    print(f"Age: {age}")

def main():
    print("Welcome to my program!")
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    init(name, age)
    print("Program initialized.")

if __name__ == "__main__":
    main()
