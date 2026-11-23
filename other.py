prices = {"apple": 1.20, "banana": 0.50, "orange": 0.80}

choice = ""
while choice != "exit":
    choice = input("Enter a fruit name (or 'exit'): ").lower()

    if choice == "exit":
        print("Goodbye!")
    elif choice in prices:
        print(f"The price of {choice} is ${prices[choice]:.2f}")
    else:
        print("Fruit not found.")
