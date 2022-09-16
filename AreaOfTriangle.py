try:
    triangle_side_a = float(input('Enter triangle side A length (centimeters): '))  # Triangle side A length input
    triangle_height = float(input('Enter triangle height length (centimeters): '))    # Triangle height length input
    triangle_square = float((triangle_side_a*triangle_height)/2)    # S=(a*h)/2
    print(f'Area of triangle is {triangle_square} sq.cm')
# Error info
except ValueError:
    print('Do not enter letters or symbols. Please, restart the program and enter number')
