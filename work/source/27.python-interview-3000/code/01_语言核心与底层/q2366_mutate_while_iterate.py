"""遍历列表时修改:跳元素的根源与三种安全写法。"""

if __name__ == "__main__":
    data = [1, 2, 2, 3, 2, 4]
    broken = list(data)
    for i, v in enumerate(broken):
        if v == 2:
            broken.pop(i)
    print("边删边遍历会漏删:", broken)

    a = [1, 2, 2, 3, 2, 4]
    for v in list(a):
        if v == 2:
            a.remove(v)
    print("遍历副本:", a)

    b = [1, 2, 2, 3, 2, 4]
    b = [v for v in b if v != 2]
    print("推导式重建:", b)

    c = [1, 2, 2, 3, 2, 4]
    for i in range(len(c) - 1, -1, -1):
        if c[i] == 2:
            del c[i]
    print("倒序删除:", c)

    d = [1, 2]
    for v in d:
        if len(d) < 5:
            d.append(v + 2)
    print("边加边遍历会追新元素:", d)
