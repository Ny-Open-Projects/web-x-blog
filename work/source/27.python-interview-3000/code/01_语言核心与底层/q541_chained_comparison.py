calls = []

def observed(label, value):
    calls.append(label)
    return value

if __name__ == "__main__":
    calls.clear()
    result = observed("a", 1) < observed("b", 5) < observed("c", 10)
    print(result, "evaluated:", calls)    # a b c:中间值只算一次

    calls.clear()
    result2 = observed("a", 1) < observed("b", 0) < observed("c", 10)
    print(result2, "evaluated:", calls)   # c 被短路跳过

    print(1 < 2 < 3)                      # 区间判断的惯用法
    print(3 > 2 == 2)                     # 链式:3>2 and 2==2 → True
    print((3 > 2) == 2)                   # 括号改变语义 → False
