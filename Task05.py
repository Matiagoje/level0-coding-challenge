from math import sqrt

side_a = 3
side_b = 4
side_c = 5

def area_of_triangle(side_a, side_b, side_c):
    semi_parameter = 0.5*(side_a + side_b + side_c)
    area = sqrt(semi_parameter*(semi_parameter-side_a)*(semi_parameter-side_b)*(semi_parameter-side_c))
    print("Area of triangle = ", area)

area_of_triangle(side_a, side_b, side_c)

