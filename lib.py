import numpy as np
import py5
import math

class Vec:
    def __init__(self, x, y):
        """Initialize a vector with x and y components."""
        self.x = x
        self.y = y

    def __add__(self, other):
        """Add two vectors."""
        return Vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Subtract another vector from this vector."""
        return Vec(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        """Multiply the vector by a scalar."""
        return Vec(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        """Divide the vector by a scalar."""
        return Vec(self.x / scalar, self.y / scalar)

    def __repr__(self):
        """Return the official string representation of the vector."""
        return f"Vec({self.x}, {self.y})"
    
    def __str__(self):
        """Return the informal string representation of the vector."""
        return f"({self.x}, {self.y})"
    
    def __eq__(self, other):
        """Check if two vectors are equal."""
        return self.x == other.x and self.y == other.y
    
    def __ne__(self, other):
        """Check if two vectors are not equal."""
        return not self.__eq__(other)
    
    def to_matrix(self):
        """Return the vector as a 2x1 numpy matrix."""
        return np.array([[self.x], [self.y]])

    def to_tuple(self):
        """Return the vector as a tuple (x, y)."""
        return (self.x, self.y)
    
    def magnitude(self):
        """Return the magnitude (length) of the vector."""
        return math.hypot(self.x, self.y)

    def normalized(self):
        """Return a normalized (unit) vector in the same direction."""
        mag = self.magnitude()
        if mag == 0:
            return Vec(0, 0)
        return Vec(self.x / mag, self.y / mag)

    def to_polar(self):
        """Return the polar coordinates (r, theta) of the vector."""
        r = self.magnitude()
        theta = math.atan2(self.y, self.x)
        return (r, theta)

    @staticmethod
    def from_matrix(matrix):
        """
        Create a Vec object from a 2x1 numpy array.
        
        Args:
            matrix (np.ndarray): A 2x1 numpy array.
        
        Returns:
            Vec: A new Vec object with x and y from the array.
        """
        return Vec(float(matrix[0, 0]), float(matrix[1, 0]))

def get_vector(pt):
    """
    Get the field vector at a given point.
    
    Args:
        pt (Vec): The point at which to get the field vector.
    
    Returns:
        Vec: The field vector at the given point.
    """
    x = pt.x - pt.y
    y = pt.x
    return Vec.normalized(Vec(x, y)) * 10

def get_field():
    '''draw vector using processing, at i*10 and j*10 to fill in 800x600 window'''
    field = np.empty((80, 60), dtype=object)

    for i in range(field.shape[0]):
        for j in range(field.shape[1]):
            field[i, j] = get_vector(Vec(i / 10, j / 10)).to_tuple()

    return field

def draw_vector(x1, y1, x2, y2, head_size=7):
    # Draw the shaft
    py5.line(x1, y1, x2, y2)
    # Calculate angle of the arrow
    angle = math.atan2(y2 - y1, x2 - x1)
    # Calculate points for the arrowhead lines
    arrow_angle = math.radians(15)  # 30 degree arrowhead
    x3 = x2 - head_size * math.cos(angle - arrow_angle)
    y3 = y2 - head_size * math.sin(angle - arrow_angle)
    x4 = x2 - head_size * math.cos(angle + arrow_angle)
    y4 = y2 - head_size * math.sin(angle + arrow_angle)
    # Draw the arrowhead as two lines instead of a triangle
    py5.line(x2, y2, x3, y3)
    py5.line(x2, y2, x4, y4)

