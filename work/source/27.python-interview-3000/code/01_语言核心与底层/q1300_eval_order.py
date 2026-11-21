log = []


def note(tag, value):
    log.append(tag)
    return value


if __name__ == "__main__":
    row = [0, 0, 0]
    row[note("idx", 2)] = note("rhs", 7)        # 普通赋值:右先左后
    print("plain assign:", log, "| row:", row)

    log.clear()
    row[note("aug-idx", 1)] += note("aug-rhs", 5)   # 增广:目标先求值
    print("augmented   :", log, "| row:", row)

    log.clear()
    def f(a, b, c):
        return (a, b, c)
    print("arg order   :", f(note("1st", 1), note("2nd", 2), note("3rd", 3)))
    print("dict literal:", {note("k1", "a"): note("v1", 1),
                            note("k2", "b"): note("v2", 2)})
