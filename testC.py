import math

def getAngle(knee, hip, shoulder):
    ang = math.degrees(math.atan2(shoulder[1]-hip[1], shoulder[0]-hip[0]) - math.atan2(knee[1]-hip[1], knee[0]-hip[0]))
    return ang + 360 if ang < 0 else ang

def checkangle(K,point_angle):
    for i in range(len(K)-1):
        if i == len(K)-2:
            if getAngle(K[i],K[i+1],K[1]) > 180:
                point_angle.append(i+1)
        else:
            if getAngle(K[i],K[i+1],K[i+2]) > 180:
                point_angle.append(i+1)
    return point_angle

def calculate_polygon_area(vertices):
    n = len(vertices)
    area = 0.0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i+1) % n]  # Lấy đỉnh kế tiếp (hoặc đỉnh đầu tiên nếu i là đỉnh cuối cùng)
        area += x1*y2 - x2*y1
    return abs(area) / 2.0

vertices = [[59, -40],[-10,-40],[-20, -79], [-63, 24], [-31, 61], [52, 26]]
area = calculate_polygon_area(vertices)
print("Diện tích đa giác:", area)
