

class Bucket:
    def __init__(self, name):
        self.name = name

    def __hash__(self):
        return hash(self.name)          # hash 参与了可变字段:埋雷

    def __eq__(self, other):
        return isinstance(other, Bucket) and self.name == other.name


if __name__ == "__main__":
    b = Bucket("cold")
    cache = {b: 100}
    b.name = "hot"                      # 内容漂移
    print("lookup by key:", b in cache)
    try:
        cache[b]                        # hash 已变,桶对不上
    except KeyError:
        print("KeyError -> hash drifted, entry is a ghost")
    print("len still:", len(cache), "| scan finds:",
          sum(1 for k in cache if k is b))
