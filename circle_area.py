# A simple Python program to calculate the area of a circle
import math

def calculate_area(radius):
    if radius < 0:
        return "Radius cannot be negative."
    return math.pi * radius ** 2

# Example usage
if __name__ == "__main__":
    radius = float(input("Enter the radius of the circle: "))
    print(f"The area of the circle is: {calculate_area(radius):.2f}")
