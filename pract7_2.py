import math

def find_min_angle_point(x1, x2, y1, y2, z1, z2):
    angle_x = math.atan2(x2, x1)
    angle_y = math.atan2(y2, y1)
    angle_z = math.atan2(z2, z1)
    
    min_angle = min(angle_x, angle_y, angle_z)
    
    if min_angle == angle_x:
        return f"Точка X({x1}, {x2})"
    elif min_angle == angle_y:
        return f"Точка Y({y1}, {y2})"
    else:
        return f"Точка Z({z1}, {z2})"

print("Введите координаты точки X:")
x1, x2 = map(float, input().split())
print("Введите координаты точки Y:")
y1, y2 = map(float, input().split())
print("Введите координаты точки Z:")
z1, z2 = map(float, input().split())

result = find_min_angle_point(x1, x2, y1, y2, z1, z2)
print(f"\n{result}")