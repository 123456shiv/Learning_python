signal = input("Enter traffic signal color (red, yellow, green): ").lower()

match signal:
    case "red":
        print("\033[31mRED\033[0m")
        print("Action: Stop")

    case "yellow":
        print("\033[33mYELLOW\033[0m")
        print("Action: Wait")

    case "green":
        print("\033[32mGREEN\033[0m")
        print("Action: Go")

    case _:
        print("Invalid traffic signal color!")