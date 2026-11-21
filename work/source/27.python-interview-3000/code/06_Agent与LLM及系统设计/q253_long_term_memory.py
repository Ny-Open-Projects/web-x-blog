"""长期记忆:写入筛选、相似检索、冲突更新,embedding 用字符重叠模拟。"""
import time


class LongTermMemory:
    def __init__(self):
        self.entries: dict[str, dict] = {}  # key -> entry

    @staticmethod
    def _score(a: str, b: str) -> float:
        sa, sb = set(a), set(b)
        return len(sa & sb) / max(1, len(sa | sb))

    def write(self, fact: str, importance: float = 0.5):
        """写入前做冲突检测:与旧条目相似度过高则更新而非新增。"""
        for key, old in self.entries.items():
            if self._score(fact, old["fact"]) > 0.7:
                old["fact"], old["updated_at"], old["version"] = fact, time.time(), old["version"] + 1
                print(f"  [更新] 覆盖旧记忆 v{old['version']}: {key}")
                return key
        key = f"mem_{len(self.entries) + 1}"
        self.entries[key] = {"fact": fact, "importance": importance,
                             "updated_at": time.time(), "version": 1}
        return key

    def recall(self, query: str, k: int = 2, now: float = None) -> list[str]:
        now = now or time.time()
        ranked = sorted(
            self.entries.values(),
            key=lambda e: -(self._score(query, e["fact"]) * 0.8
                            + e["importance"] * 0.2))
        return [e["fact"] for e in ranked[:k]]


if __name__ == "__main__":
    mem = LongTermMemory()
    mem.write("用户是后端工程师,常用 Go")
    mem.write("用户偏好用中文交流")
    mem.write("用户常用 Go 和 Python")   # 与第一条冲突,应触发更新
    print("检索结果:", mem.recall("用户的编程语言偏好"))
