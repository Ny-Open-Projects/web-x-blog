---
title: [Q675] MQTT 通配符路由:+ 与 # 的匹配器实现
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q675 · MQTT 通配符路由:+ 与 # 的匹配器实现

> 难度:★★☆ | 标签:MQTT, 通配符, 路由

**问**:MQTT 的主题通配符规则是什么?写一个匹配器要小心哪些边界?

**答**:两级通配符:`+` 匹配恰好一层(`sensor/+/temp` 命中 sensor/1/temp 但不命中 sensor/1/x/temp);`#` 匹配剩余全部层级且必须放末尾(`sensor/#` 命中 sensor 与 sensor/a/b)。发布方不能用通配符,只有订阅方可以。实现边界:`+`/`#` 是"层"级别而非字符串级别(a+b 不算通配);`sport/#` 也匹配 `sport` 本身(# 可匹配零层);`/` 开头的主题首层是空串。broker 的订阅量大时,匹配要从"遍历全部过滤器"优化成主题树(trie)。

```python
# file: code/02_并发与网络工程/q675_topic_match.py


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
```

**追问**:1) `$SYS/` 开头的系统主题为什么要特殊处理?——`#` 按规则会匹配到 `$SYS`,但协议规定 `$` 开头的主题不匹配首层通配符(避免普通订阅者收到 broker 内部监控数据),实现时首层是 `$` 前缀的要在匹配器里排除。2) 匹配器的性能与数据结构?——订阅量大时逐条遍历 O(N) 成瓶颈,标准优化是主题 trie:按层建树、订阅挂节点、发布沿主题走树收集;+/# 是特殊子节点,通配订阅位置一目了然。3) 边界语义最容易错的三处?——# 匹配零层(sport/# 命中 sport 本身);+ 是「层」不是字符串(a+ 不算通配);/ 开头主题首层是空串(sensor//temp 合法);$ 前缀首层特殊(见原问)。4) 生产陷阱?——发布方误用通配符(协议禁止,broker 必须拒绝而不是静默当字面量);通配订阅 $SYS 收海量监控消息拖垮客户端;层级分隔符与业务路径重载,过滤规则越来越拧巴。

---
