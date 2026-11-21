if __name__ == "__main__":
    grid_bad = [[0] * 3] * 2               # 两行是同一个对象
    grid_bad[0][0] = 9
    print("bad :", grid_bad)               # [[9, 0, 0], [9, 0, 0]]
    print("same row object:", id(grid_bad[0]) == id(grid_bad[1]))

    grid_ok = [[0] * 3 for _ in range(2)]  # 每行新建
    grid_ok[0][0] = 9
    print("good:", grid_ok)
    print("distinct rows:", id(grid_ok[0]) != id(grid_ok[1]))

    flags = [False] * 5                    # 不可变元素:乘法安全
    flags[2] = True
    print("immutable elements fine:", flags)
