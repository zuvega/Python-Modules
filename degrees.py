import math

def radians_to_degrees(radians):
    degrees = math.degrees(radians)
    return degrees

user_radians = float(input("Enter an angle in radians: "))

converted_degrees = radians_to_degrees(user_radians)
print(f"{user_radians} radians is equal to {converted_degrees} degrees.")
