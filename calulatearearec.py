def calculate_area_rectangle(length,width):
   return length * width

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = calculate_area_rectangle(length, width)

print("The area of the rectangle is:", area)
