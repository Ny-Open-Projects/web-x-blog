"""模型灰度:用户哈希稳定分桶 + 影子对比 + 放量门禁 + 一键回滚。"""
import hashlib, json


def bucket(user_id, percent):
    h = int(hashlib.md5(user_id.encode()).hexdigest(), 16) % 100
    return "canary" if h < percent else "stable"


class FakeModel:
    def __init__(self, name, quality):
        self.name, self.quality = name, quality

    def generate(self, q):
        return {"model": self.name, "answer": f"[{self.name}] {q}", "score": self.quality}


class Router:
    def __init__(self, stable, canary, percent=0):
        self.models = {"stable": stable, "canary": canary}
        self.percent, self.shadows, self.metrics = percent, [], {"stable": [], "canary": []}

    def handle(self, user_id, q, shadow=True):
        b = bucket(user_id, self.percent)
        main = self.models[b].generate(q)
        self.metrics[b].append(main["score"])
        if shadow and b == "stable":               # 影子:stable 用户顺带跑 canary
            canary_out = self.models["canary"].generate(q)
            self.shadows.append({"user": user_id, "diff": canary_out["score"] - main["score"]})
        return main

    def avg(self, b):
        m = self.metrics[b]
        return sum(m) / len(m) if m else 0.0

    def should_promote(self, min_gain=0.02):
        if not self.shadows:
            return False
        gain = sum(s["diff"] for s in self.shadows) / len(self.shadows)
        return gain >= min_gain

    def rollback(self):
        self.percent = 0


if __name__ == "__main__":
    r = Router(FakeModel("gpt-old", 0.80), FakeModel("new-x", 0.86), percent=5)
    for i in range(200):
        r.handle(f"user-{i}", "问题", shadow=True)
    print(f"影子样本 {len(r.shadows)} 条,平均增益 {r.avg('canary') - r.avg('stable'):.3f}")
    assert r.should_promote(min_gain=0.02), "影子增益达门禁,允许放量"
    r.percent = 50
    users = [r.handle(f"user-{i}", "q", shadow=False)["model"] for i in range(400)]
    print("放量 50% 后模型分布:", {m: users.count(m) for m in set(users)})
    r.rollback()
    assert bucket("user-3", r.percent) == "stable"
    print("回滚后 100% 走 stable,分桶对用户稳定")
