__author__ = 'joseph'

from math import *
import math


def triangular_area(side1, side2):
    """
    Calculate area of a triangle from the base and the height.
    :@param side1:the base length
    :@param side2:the height of the triangle
    :@return:the area (units^2 from side)
    >>>triangular_area(6, 9)
    27.0
    """
    return 1/2*side1*side2


def triangular_area_2(side1, side2, angle):
    """
    calculate the area of a triangle given two sides and an angle.
    :@param side1:a side length of the triangle
    :@param side2:another side length of the triangle
    :@param angle:included angle of the triangle
    :@return:triangular area (units^2 from side)
    >>>triangular_area_2(3, 7, 40)
    7.823688185033163
    """
    return 1/2*side1*side2*math.sin(angle)


def trapezium_area(side_a, side_b, side_c):
    """
    calculate the area of a trapezium using two sides and the height.
    :@param side_a:one of the sides of the trapezium
    :@param side_b:one of the sides of the trapezium
    :@param side_c:the height of the trapezium
    :@return:the area (units^2 from side)
    >>>trapezium_area(3, 4, 2)
    7.0
     """
    return 1/2*(side_a+side_b)*side_c


def trapezium_perimeter(side_a, side_b, side_c, side_d):
    """
    calculate the perimeter of a four sided trapezium
    :@param side_a:a side of the trapezium
    :@param side_b:a side length
    :@param side_c:a side length
    :@param side_d:a side length
    :@return:the perimeter (same units as side length)
    >>>trapezium_perimeter(3, 4, 5, 6)
    18
    """
    return side_a+side_b+side_c+side_d


def cube_volume(side1, side2, side3):
    """
    calculate the volume of a cube (three sides)
    :@param side1:the length
    :@param side2:the breadth
    :@param side3:the height
    :@return:volume of the cube (units^3 from side)
    >>>cube_volume(2, 2, 2)
    8
    """
    return side1*side2*side3


def sphere_area(radius):
    """
    calculate the area of sphere given its radius
    :@param radius: radius
    :@return:area of sphere (units^2 from radius)
    >>>sphere_area(5)
    314.1592653589793
    """
    return 4*pi*radius**2


def rectangular_prism_area(length, width, height):
    """
    calculate the area of a regular rectangular_prism
    :@param length: the length of the rectangular_prism
    :@param width: the width of the rectangular_prism
    :@param height:the height of the rectangular_prism
    :@return:area of rectangular_prism (units^2 from any of the sides)
    >>>rectangular_prism_area(4, 2, 7)
    100
    """
    return 2*(width*length+height*length+height*width)


def rectangular_perimeter(length, width):
    """
    calculate the perimeter of a rectangular block
    :@param length: the length of the block
    :@param width: the width of the block
    :@return:perimeter (same unit as either length or width)
    >>>rectangular_perimeter(5, 3)
    16
    """
    return 2*(length+width)


def cylindrical_volume(radius, height):
    """
    calculating the volume of a cylinder given the radius and height
    :@param radius: radius
    :@param height: height
    :@return:volume of cylinder (units^3 from any of the radius or height)
    >>>cylindrical_volume(2, 7)
    87.96459430051421
    """
    return pi*radius**2*height


def right_circular_cone_volume(radius, height):
    """
    calculate the volume of a right circular cone
    :@param radius:radius of the cone
    :@param height:height of the cone
    :@return:volume of a right circular cone (units^3 from any of the radius or height)
    >>>right_circular_cone_volume(2, 5)
    20.943951023931955
    """
    return pi*radius**2*height/3


def regular_hexagonal_area(side):
    """
    calculate the area of a regular hexagon
    :@param side: the side length of a regular hexagon
    :@return:area of a regular hexagon (units^2 of a side)
    >>>regular_hexagonal_area(4)
    41.569219381653056
    """
    return ((3*math.sqrt(3))/2)*side**2


def regular_tetrahedron_area(side):
    """
    to calculate the area of a regular tetrahedron
    :@param side:the side length of the given tetrahedron
    :@return:area of a regular tetrahedron (units^2 of s side)
    >>>regular_tetrahedron_area(5)
    43.30127018922193
    """
    return math.sqrt(3)*side**2


def regular_decagon_area(side):
    """
    calculate the area of a regular decagon
    :@param side:the side length of the decagon
    :@return:area of a regular decagon (unit^2 of a side of the decagon)
    >>>regular_decagon_area(4)
    123.10734148701015
    """
    return 5/2*side**2*(math.sqrt(5+2*(math.sqrt(5))))


if __name__ == "__main__":
    print("triangular area:", triangular_area(6, 9))


if __name__ == "__main__":
    print("triangular area_2:", triangular_area_2(3, 7, 40))


if __name__ == "__main__":
    print("trapezium area:", trapezium_area(3, 4, 2))


if __name__ == "__main__":
    print("trapezium perimeter:", trapezium_perimeter(3, 4, 5, 6))


if __name__ == "__main__":
    print("cube volume:", cube_volume(2, 2, 2))


if __name__ == "__main__":
    print("sphere area:", sphere_area(5))


if __name__ == "__main__":
    print("rectangular prism area:", rectangular_prism_area(4, 2, 7))


if __name__ == "__main__":
    print("rectangular perimeter:", rectangular_perimeter(5, 3))


if __name__ == "__main__":
    print("cylindrical volume:", cylindrical_volume(2, 7))


if __name__ == "__main__":
    print("right circular cone volume:", right_circular_cone_volume(2, 5))


if __name__ == "__main__":
    print("regular hexagonal area:", regular_hexagonal_area(4))


if __name__ == "__main__":
    print("regular tetrahedron area:", regular_tetrahedron_area(5))


if __name__ == "__main__":
    print("regular decagon area:", regular_decagon_area(4))
