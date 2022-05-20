def area_of_triangle(side_a, side_b, side_c):
    semi_parameter = 0.5*(side_a + side_b + side_c)
    area = (semi_parameter*(semi_parameter-side_a)*(semi_parameter-side_b)*(semi_parameter-side_c))**0.5
    return area

print("Area of triangle = ", area_of_triangle(3, 4, 5))
