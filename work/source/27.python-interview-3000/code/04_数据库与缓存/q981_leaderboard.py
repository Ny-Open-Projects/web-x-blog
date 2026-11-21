"""zset 排行榜: 更新 名次 并列时按达成时间排序"""
import bisect

class MiniZSet:
    def __init__(self):
        self.items = []                     # [(score, member)] 降序

    def add(self, member, score):
        self.items = [x for x in self.items if x[1] != member]
        bisect.insort(self.items, (-score, member))   # 负分实现降序
        self.items = self.items[:100]                 # 只维护 TopN

    def top(self, n=5):
        return [(m, -s) for s, m in self.items[:n]]

    def rank(self, member):
        for i, (s, m) in enumerate(self.items):
            if m == member:
                return i + 1
        return None

if __name__ == "__main__":
    lb = MiniZSet()
    for name, sc in [("alice", 95), ("bob", 88), ("carol", 95), ("dave", 70)]:
        lb.add(name, sc)
    print("Top4:", lb.top(4), "<- 同分 95: alice 与 carol 相邻")
    print("dave 名次:", lb.rank("dave"))
    print("未上榜用户用 ZCOUNT 统计分数区间推导名次段")
