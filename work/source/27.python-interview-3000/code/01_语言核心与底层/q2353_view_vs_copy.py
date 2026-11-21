"""视图还是拷贝:dict 视图动态、切片快照、memoryview 零拷贝、map 惰性。"""

if __name__ == "__main__":
    d = {"a": 1}
    keys = d.keys()
    d["b"] = 2
    print("dict 视图动态:", list(keys))

    lst = [1, 2, 3]
    head = lst[:2]
    lst.append(4)
    print("切片是快照:", head)

    buf = bytearray(b"abcd")
    mv = memoryview(buf)
    buf[0] = 0x58
    print("memoryview 跟随底层:", mv[0], bytes(mv))

    src = [1, 2, 3]
    doubled = map(lambda v: v * 2, src)
    src.append(10)
    print("map 惰性包含新元素:", list(doubled))

    snapshot = list(d.keys())
    d["c"] = 3
    print("主动 list 后是快照:", snapshot)
