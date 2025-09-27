while True:
    num = input("Enter number between 5 and 9 (or type 'quit' to exit): ")

    if num.lower() == "quit":
        break

    if num.isdigit():
        num = int(num)
        if num < 5 or num > 9:
            raise ValueError("You have entered an Out Of Range value.")
        else:
            print(f"Valid input: {num}")
    else:
        raise ValueError("You have entered a string instead of a number.")

    
    
