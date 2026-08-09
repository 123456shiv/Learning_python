def reverse_text(text):
    return text[::-1]

# Keep it as a string
user_input = input("Enter text or a number to reverse: ")
reversed_text = reverse_text(user_input)
print("The reversed text is:", reversed_text)