"""有序去重保持首现:dict.fromkeys、手工 seen 与流式三写法。"""


def dedup(items):
    """可哈希元素的一行保序去重。"""
    return list(dict.fromkeys(items))


def dedup_by(items, key=None):
    """不可哈希元素按 key 去重,key 缺省用元素本身。"""
    key = key or (lambda x: x)
    seen = set()
    out = []
    for item in items:
        marker = key(item)
        if marker not in seen:
            seen.add(marker)
            out.append(item)
    return out


if __name__ == "__main__":
    data = ["b", "a", "b", "c", "a", "d"]
    print("dict.fromkeys:", dedup(data))
    print("手工循环:", dedup_by(data))

    rows = [{"id": 2, "v": "x"}, {"id": 1, "v": "y"}, {"id": 2, "v": "z"}]
    print("按字段去重:", dedup_by(rows, key=lambda r: r["id"]))

    print("set 直转打乱顺序:", list(set(data)), "≠ 首现序", dedup(data))

    def dedup_iter(it):
        seen = set()
        for item in it:
            if item not in seen:
                seen.add(item)
                yield item
    print("流式去重:", list(dedup_iter(data)))
