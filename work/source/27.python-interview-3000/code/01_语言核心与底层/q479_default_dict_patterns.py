from collections import defaultdict, Counter

text = "the quick brown fox jumps over the lazy dog the fox"

if __name__ == "__main__":
    # 1. 计数:Counter 最短
    print(Counter(text.split()).most_common(2))

    # 2. 分组:defaultdict 的标准姿势
    by_len = defaultdict(list)
    for w in text.split():
        by_len[len(w)].append(w)
    print(dict(by_len))

    # 3. setdefault:返回「已存在的或新建的」容器
    pairs = [("a", 1), ("b", 2), ("a", 3)]
    grouped = {}
    for k, v in pairs:
        grouped.setdefault(k, []).append(v)
    print(grouped)

    # 4. 副作用:defaultdict 读取也会长出键
    d = defaultdict(int)
    _ = d["ghost"]
    print("ghost in d:", "ghost" in d)
