a = int(input("Enter a number between 1 and 10: "))

match a:
    case 1:
        print("You enterd a charger")
    case 3:
        print("You won $3")
    case 6:
        print("You won $5")
    case _:
        print("Better luck next time")    