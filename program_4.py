# Title: Population Data
# Author: Arianna Endres
# Date: 10/15/2025

# Program inputs two three-dimentional coordinates and calculates the distance between them.

import math

def main():

    # Input the coordinates. Restart the loop if input causes error.
    while True:
        try:
            print('Enter the first coordinate:')
            x1 = int(input('x: '))
            y1 = int(input('y: '))
            z1 = int(input('z: '))

            print('Enter the second coordinate:')
            x2 = int(input('x: '))
            y2 = int(input('y: '))
            z2 = int(input('z: '))

            break

        except ValueError:
            print('You have entered an invalid coordinate value. A coordinate can only be a number. '
                  'Please try again.')


    # Define the coordinates as tuples.
    first_coordinate = (x1, y1, z1)
    second_coordinate = (x2, y2, z2)

    # Call the distance function.
    distance_between_points = distance(x1, y1, z1, x2, y2, z2)

    # Print the results
    print(f'The distance between {first_coordinate} and {second_coordinate} is approximately {distance_between_points:.2f}.')

# Calculate the distance between two points by using the distance formula.
def distance(x1, y1, z1, x2, y2, z2):
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z1 - z2)**2)

# Call the main function.
if __name__ == '__main__':
    main()