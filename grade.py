marks = float(input("Enter your percentage: "))

if marks >= 90:
    print("Percentage:", marks)
    print("Your Grade is A")
    print("Excellent")

elif marks >= 80:
    print("Percentage:", marks)
    print("Your Grade is B")
    print("Good")

elif marks >= 70:
    print("Percentage:", marks)
    print("Your Grade is C")
    print("Average")

elif marks >= 60:
    print("Percentage:", marks)
    print("Your Grade is D")
    print("Below Average")

elif marks >= 50:
    print("Percentage:", marks)
    print("Your Grade is E")
    print("Poor")

else:
    print("Percentage:", marks)
    print("Your Grade is F")
    print("You are Fail,try next time")