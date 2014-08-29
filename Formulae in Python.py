__author__ = 'joseph'
from numbers import Number

def square_perimeter(side :Number )-> Number:
    """
    Calculate perimeter of a square from side lenght.
    @param side: the side lenght
    @return: the perimeter (same units as side lenght)
    >>> square_perimeter(4)
    16
    """
    return 4*side

def square_area(side):
    """
    Calculate area of a square from side lenght
    @param side: the side lenght
    @return: the area (units^2 from side)
    >>> square_area(4)
    16
    """
    return side*side

print ( square_perimeter(4) )

def rectangular_perimeter(side1,side2 ):
   return 2*side1+2*side2
print(rectangular_perimeter(2,3))

def rectangular_area(side1,side2 : Number) -> Number:
    return side1*side2
print(rectangular_area(4,2))

if __name__ == "__main__":
    sampleSide1,sampleSide2 = 2,7
    print(" rectangular area:",
          rectangular_area(sampleSide1,sampleSide2),"\n",
          "square area:",
          square_area(sampleSide2)
    )
