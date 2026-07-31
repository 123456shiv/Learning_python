marks=int(input("Enter the marks: "))

match  marks:
    case marks if marks >= 90:
        print("Percentage:", marks)
        print("Your Grade is A")

    case marks if marks >= 80:
        print("Percentage:", marks)
        print("Your Grade is B")

    case marks if marks >= 70:
        print("Percentage:", marks)
        print("Your Grade is C")

    case marks if marks >= 60:
        print("Percentage:", marks)
        print("Your Grade is D")

    case marks if marks >= 50:
        print("Percentage:", marks) 
        print("Your Grade is E")

    case marks if marks < 50:
        print("Percentage:", marks)
        print("Your Grade is F you are Fail,try next time")

    case _:
        print("Invalid marks. Please enter a valid number between 0 and 100.")

