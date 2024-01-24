def main():
    stairs = list(map(int, input().split()))

    width, height = calc_width_and_height(stairs)
    points = make_points(height, stairs)

    while True:
        try:
            x, y = map(int, input().split())
            temp_x, point_num = decide_point_num(stairs, x)
            decide_relation(points, temp_x, x, y, point_num)
        except(Exception):
            break

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def make_points(height: int, stairs: list) -> list:
    points = [Point(0, height)]
    for i in range(len(stairs) - 1):

        x, y = points[i].x, points[i].y

        if is_odd(i):
            points.append(Point(x + stairs[i], y))
        else:
            points.append(Point(x, y - stairs[i]))
    return points


def calc_width_and_height(stairs: list) -> (int, int):
    width, height = 0, 0
    for i in range(len(stairs)):
        if is_odd(i):
            width += stairs[i]
        else:
            height += stairs[i]
    return width, height


def decide_point_num(stairs: list,  x: int):
    step = 0
    temp_x = 0
    for i in range(0, len(stairs), 2):
        temp_x += stairs[i]
        step += 1
        if x <= temp_x:
            break
    point_num = 2 * step - 1
    return temp_x, point_num


def decide_relation(points: list, temp_x: int, x: int, y: int, num: int):
    if Point(x, y) in points:
        print("on")
        return
    if temp_x == x:
        if points[num+1].y <= y <= points[num].y:
            print("on")
        elif points[num].y < y:
            print("out")
        else:
            print("in")
    else:
        if points[num].y == y:
            print("on")
        elif points[num].y < y:
            print("out")
        else:
            print("in")




if __name__ == "__main__":
    main()
