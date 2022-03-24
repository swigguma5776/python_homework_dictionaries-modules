from IPython.display import clear_output

def square_root():
    length = int(input("What is the length of your house in inches? "))
    width = int(input("What is the width of your house in inches? "))

    area= (length/12) * (width/12)
    format_area = "{:.2f}".format(area)
    print(f"The area of your house is approximately {format_area} square feet.")
    

    again = input("Would you like to check again (type y/n)? ")
    clear_output()
    if again.lower() == 'y':
        square_root()
    else:
        print("Hope we were able to help. Have a great day!")
    

# square_root()

from math import pi

def circumference():
    radius = int(input("What is the radius of your circle in inches? "))
    
    if radius > 0:
        circum = 2 * radius * pi
        format_circum = "{:.2f}".format(circum)
        print(f"The circumference of your cirlce is: {format_circum} inches")
    else:
        print("Please provide a positive number for your radius")
    

    again = input("Would you like to check the circumference of another circle (type y/n)? ")
    clear_output()
    if again.lower() == 'y':
        circumference()
    else:
        print("Have a good day!")

# circumference()