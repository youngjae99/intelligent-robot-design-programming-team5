import random
from datetime import datetime
random.seed(datetime.now().timestamp())


grid_map = [[0] * 5 for _ in range(5)]*5  # 1: red, 2: box
visited = [[False]*5 for _ in range(5)]
visited_back = [[False]*5 for _ in range(5)]

dir_r = [0, 1, 0, -1]  # 북동남서
dir_c = [1, 0, -1, 0]

red_detected = []
box_detected = []

found_all = False
returned = False


def make_grid():  # 랜덤 -> 모든 경우의 수?
    coordinates = set()
    while len(coordinates) < 4:
        r = random.randint(0, 4)
        c = random.randint(0, 4)
        coordinates.add((r, c))

    cds_list = list(coordinates)
    for i in range(0, 2):
        rr, rc = cds_list[i]
        grid_map[rr][rc] = 1
        br, bc = cds_list[i+2]
        grid_map[br][bc] = 2

    for i in range(0, 5):
        for j in range(0, 5):
            print(grid_map[i][j], end=" ")
        print("")


def in_range(r, c):
    return False if r < 0 or r > 4 or c < 0 or c > 4 else True


def is_red(r, c):
    return True if grid_map[r][c] == 1 else False


def red_completed():
    red_cnt = len(red_detected)
    if red_cnt == 2:
        return True
    elif red_cnt > 3:
        return ValueError("What the..")
    else:
        return False


def box_completed():
    box_cnt = len(box_detected)
    if box_cnt == 2:
        return True
    elif box_cnt > 3:
        return ValueError("What the..")
    else:
        return False


def is_box(r, c):
    return True if grid_map[r][c] == 2 else False


def print_pos():
    print("===============================================")
    if len(red_detected) == 2 and len(box_detected) == 2:
        print("red positions:")
        for (x, y) in red_detected:
            print("(row={}, col={})".format(x, y))
        print("box positions:")
        for (x, y) in box_detected:
            print("(row={}, col={})".format(x, y))
    else:
        return ValueError("What the..")


def come_back(r, c):
    visited_back[r][c] = True
    print("(Back) Visited: (row={}, col={})".format(r, c))

    if r == 0 and c == 0:
        global returned
        returned = True
        print_pos()

    for i in range(3, -1, -1):
        if returned:
            return

        nr = r + dir_r[i]
        nc = c + dir_c[i]

        if in_range(nr, nc) and not is_box(nr, nc) and not visited_back[nr][nc]:
            come_back(nr, nc)


def dfs(r, c):
    visited[r][c] = True
    print("Visited: (row={}, col={})".format(r, c))

    if is_red(r, c) and (r, c) not in red_detected:
        red_detected.append((r, c))

    if red_completed() and box_completed():
        global found_all
        found_all = True
        print("Found all two reds and boxes at (row={}, col={})".format(r, c))
        print("===============================================")
        come_back(r, c)

    for i in range(4):
        if found_all:
            return

        nr = r + dir_r[i]
        nc = c + dir_c[i]

        if not in_range(nr, nc):
            continue
        elif visited[nr][nc]:
            continue
        elif is_box(nr, nc):
            if (nr, nc) not in box_detected:
                box_detected.append((nr, nc))
        else:
            dfs(nr, nc)


make_grid()
dfs(0, 0)
