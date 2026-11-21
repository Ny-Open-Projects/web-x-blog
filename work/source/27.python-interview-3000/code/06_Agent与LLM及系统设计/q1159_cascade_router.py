"""级联路由:小模型前置分类 + 置信度阈值 + 校验失败自动升级,统计省钱比。"""


class SmallModel:
    def generate(self, q):
        hard = any(k in q for k in ["推导", "架构", "设计", "证明"])
        conf = 0.4 if hard else 0.9
        return {"answer": f"小模型答:{q}", "confidence": conf, "tokens": 200}


class BigModel:
    def generate(self, q):
        return {"answer": f"大模型答:{q}", "confidence": 0.98, "tokens": 1500}


class Cascade:
    PRICE = {"small": 0.002, "big": 0.03}      # 每千 token

    def __init__(self, small, big, threshold=0.7):
        self.small, self.big, self.threshold = small, big, threshold
        self.stats = {"small_served": 0, "escalated": 0, "cost": 0.0}

    def _cost(self, model, tokens):
        c = tokens / 1000 * self.PRICE[model]
        self.stats["cost"] += c
        return c

    def handle(self, q):
        r = self.small.generate(q)
        self._cost("small", r["tokens"])
        if r["confidence"] >= self.threshold:
            self.stats["small_served"] += 1
            return r["answer"], "small"
        self.stats["escalated"] += 1
        self._cost("small", r["tokens"])        # 升级链路:分类也要计费
        b = self.big.generate(q)
        self._cost("big", b["tokens"])
        return b["answer"], "big"


if __name__ == "__main__":
    c = Cascade(SmallModel(), BigModel())
    questions = ["发票怎么开", "订单几点发货", "设计一个高并发架构", "退款多久到账",
                 "推导一下这个算法的复杂度", "改收货地址", "写一个限流方案的设计"]
    served_by = [c.handle(q)[1] for q in questions]
    s, big, cost = c.stats["small_served"], c.stats["escalated"], c.stats["cost"]
    all_big = len(questions) * 1500 / 1000 * Cascade.PRICE["big"]
    print(f"小模型直答 {s} 题,升级 {big} 题,实际成本 {cost:.4f},全大模型 {all_big:.4f}")
    print("节省比例:", f"{1 - cost / all_big:.0%}")
    assert served_by.count("big") == 3 and s == 4, "难题必须升级"
    assert cost < all_big, "级联必须省钱"
