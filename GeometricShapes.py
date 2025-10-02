import math

def rotate_point(point, angle_degrees, center_point=(0, 0)):
    """Rotates a point (x, y) around a center_point by a given angle (in degrees)."""
    angle_radians = math.radians(angle_degrees)
    cx, cy = center_point
    px, py = point

    # Translate point to origin
    temp_x = px - cx
    temp_y = py - cy

    # Rotate point
    rotated_x = temp_x * math.cos(angle_radians) - temp_y * math.sin(angle_radians)
    rotated_y = temp_x * math.sin(angle_radians) + temp_y * math.cos(angle_radians)

    # Translate point back
    return rotated_x + cx, rotated_y + cy

def rotate_polygon(polygon, angle_degrees, center_point=(0, 0)):
    """Rotates a polygon (list of points) around a center_point."""
    rotated_polygon = []
    for point in polygon:
        rotated_polygon.append(rotate_point(point, angle_degrees, center_point))
    return rotated_polygon

# Example usage:
my_polygon = [(0, 0), (1, 0), (1, 1), (0, 1)] # A square
rotated_polygon = rotate_polygon(my_polygon, 45, center_point=(0.5, 0.5))
print(f"Original polygon: {my_polygon}")
print(f"Rotated polygon: {rotated_polygon}")
