"""字符串比较是码点字典序:大小写、数字与汉字的真实顺序。"""

if __name__ == "__main__":
    words = ["banana", "Apple", "apple", "Banana", "10", "2"]
    print("码点排序:", sorted(words))
    print("忽略大小写:", sorted(words, key=str.lower))
    print("数字串数值序:", sorted(["10", "2", "1", "100"], key=int))

    pairs = [("Z", "a"), ("中", "a"), ("0", ":"), ("A", "_")]
    for lo, hi in pairs:
        print(f"{lo!r} < {hi!r}:", lo < hi, "| 码点:", ord(lo), ord(hi))

    words2 = ["straße", "STRASSE", "strasse"]
    print("lower 键:", [w.lower() for w in words2])
    print("casefold 键:", [w.casefold() for w in words2])
