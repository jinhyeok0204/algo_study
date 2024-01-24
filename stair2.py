def main():
    stairs = list(map(int, input().split()))

    width, height = 0,0
    for i in range(len(stairs)):
        if i % 2:
            height += stairs[i]
        else:
            width += stairs[i]

    points = [(0, height)]
    for i in range(len(stairs) - 1):
        x, y = points[i][0], points[i][1]

        if i % 2:
            points.append((x, y - stairs[i]))
        else:
            points.append((x + stairs[i], y))


    while True:
        try:
            x, y = map(int, input().split())
            if x > width or y > height:
                print("out")
                continue

            step = 0
            temp_x = 0
            for i in range(0, len(stairs), 2):
                temp_x += stairs[i]
                step += 1
                if x <= temp_x:
                    break
            point_num = 2 * step - 1

            if temp_x == x:
                if points[point_num+1][1] <= y <= points[point_num][1]:
                    print("on")
                elif points[point_num][1] < y:
                    print("out")
                else:
                    print("in")
            else:
                if points[point_num][1] == y:
                    print("on")
                elif points[point_num][1] < y:
                    print("out")
                else:
                    print("in")


        except Exception as e:
            print(e)

main()