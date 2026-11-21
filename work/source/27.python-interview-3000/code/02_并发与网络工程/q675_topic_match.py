

def topic_matches(flt: str, topic: str) -> bool:
    """MQTT 主题过滤器匹配。"""
    f_parts = flt.split("/")
    t_parts = topic.split("/")
    for i, fp in enumerate(f_parts):
        if fp == "#":
            return i == len(f_parts) - 1  # # 必须是最后一层, 匹配剩余全部 (可为零层)
        if i >= len(t_parts):
            return False
        if fp == "+":
            continue  # 匹配任意单层
        if fp != t_parts[i]:
            return False
    return len(f_parts) == len(t_parts)


CASES = [
    # (过滤器, 主题, 期望)
    ("sport/+", "sport/", True),
    ("sport/+", "sport/football", True),
    ("sport/+", "sport/football/score", False),
    ("sport/#", "sport", True),              # # 匹配零层
    ("sport/#", "sport/football/score", True),
    ("+/tennis/#", "sport/tennis/player1/score", True),
    ("#", "a/b/c", True),
    ("a/+/c", "a//c", True),                  # 空层也匹配 +
    ("a/+/c", "a/b/c/d", False),
    ("sensor/1/temp", "sensor/1/temp", True),
    ("sensor/1/temp", "sensor/1/hum", False),
    ("#", "empty", True),
]


class TopicTrie:
    """订阅量大的 broker 用 trie 把匹配从 O(n) 过滤器降到 O(主题长度)。"""

    def __init__(self) -> None:
        self.root: dict = {}
        self.subs: dict = {}

    def add(self, client: str, flt: str) -> None:
        node = self.root
        for part in flt.split("/"):
            node = node.setdefault(part, {})
        node.setdefault("$subs", set()).add(client)

    def match(self, topic: str) -> set:
        found: set = set()
        parts = topic.split("/")

        def walk(node: dict, i: int) -> None:
            if "$subs" in node:
                found.update(node["$subs"])
            if i >= len(parts):
                if "#" in node:
                    found.update(node["#"]["$subs"])
                return
            if "#" in node:  # # 在中间也是该子树所有订阅者
                found.update(node["#"].get("$subs", set()))
                return
            if parts[i] in node:
                walk(node[parts[i]], i + 1)
            if "+" in node:
                walk(node["+"], i + 1)

        walk(self.root, 0)
        return found


if __name__ == "__main__":
    for flt, topic, expect in CASES:
        got = topic_matches(flt, topic)
        mark = "OK " if got == expect else "FAIL"
        print(f"  [{mark}] {flt!r} vs {topic!r} → {got}")
        assert got == expect

    trie = TopicTrie()
    trie.add("app1", "sensor/+")
    trie.add("app2", "sensor/1/#")
    trie.add("app3", "other/x")
    print("trie 匹配 sensor/1/temp:", trie.match("sensor/1/temp"))
    assert trie.match("sensor/1/temp") == {"app1", "app2"}
