try:
    triangle_side_a = float(input('Set triangle side size: '))
    triangle_height = float(input('Set triangle height length: '))
    triangle_square = float(triangle_side_a*triangle_height)/2
    print(triangle_square)
# Error info
except ValueError:
    print('Do not enter letters or symbols. Please, restart the program and enter number')
