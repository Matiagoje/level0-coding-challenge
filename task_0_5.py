def area_of_triangle(side_a, side_b, side_c):
    semi_perimeter = 0.5*(side_a + side_b + side_c)
    area = (semi_perimeter*(semi_perimeter-side_a)*(semi_perimeter-side_b)*(semi_perimeter-side_c))**0.5
    return area

print("Area of triangle = ", area_of_triangle(3, 4, 5))
