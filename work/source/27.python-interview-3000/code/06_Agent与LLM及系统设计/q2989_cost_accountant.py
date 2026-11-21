"""Q2989 成本核算器:按 输入/输出/缓存 三层计价与预算告警。

LLM 账单三层:输入 token 按模型单价、输出 token 更贵、命中缓存的
输入按折扣价(常见 1 折)。核算器要按 请求/模型/天 三个粒度汇总,
并在日预算触线时给结构化告警而不是静默超支。所有价格以「每百万
token」计,内部换算成每次调用的钱。
"""


class CostAccountant:
    def __init__(self, price_table, daily_budget):
        """price_table: model -> {input, output, cached, per_request}
        单位:元 / 百万 token;per_request 单位:元/次。"""
        self.prices = price_table
        self.daily_budget = daily_budget
        self.records = []

    def record(self, ts_day, model, input_tokens, output_tokens,
               cached_tokens=0):
        p = self.prices[model]
        billable_input = max(input_tokens - cached_tokens, 0)
        cost = (billable_input / 1e6 * p["input"]
                + output_tokens / 1e6 * p["output"]
                + cached_tokens / 1e6 * p["cached"]
                + p["per_request"])
        self.records.append({"day": ts_day, "model": model,
                             "input": input_tokens,
                             "output": output_tokens,
                             "cached": cached_tokens,
                             "cost": round(cost, 6)})
        return cost

    def totals_by_day(self):
        out = {}
        for r in self.records:
            out[r["day"]] = round(out.get(r["day"], 0.0) + r["cost"], 6)
        return out

    def totals_by_model(self, day):
        out = {}
        for r in self.records:
            if r["day"] == day:
                out[r["model"]] = round(out.get(r["model"], 0.0)
                                        + r["cost"], 6)
        return out

    def budget_alert(self, day):
        spent = self.totals_by_day().get(day, 0.0)
        ratio = spent / self.daily_budget
        level = "ok"
        if ratio >= 1.0:
            level = "breach"
        elif ratio >= 0.8:
            level = "warn"
        return {"day": day, "spent": round(spent, 4),
                "budget": self.daily_budget, "ratio": round(ratio, 4),
                "level": level}

    @staticmethod
    def cache_saving(record, price_table):
        """命中缓存省了多少钱:全价输入减去缓存价。"""
        p = price_table[record["model"]]
        return round(record["cached"] / 1e6 * (p["input"] - p["cached"]), 6)


PRICES = {
    "glm-air": {"input": 0.5, "output": 2.0, "cached": 0.05,
                "per_request": 0.001},
    "glm-pro": {"input": 4.0, "output": 16.0, "cached": 0.4,
                "per_request": 0.01},
}


def main():
    acc = CostAccountant(PRICES, daily_budget=1.0)

    c1 = acc.record("2026-11-05", "glm-air", input_tokens=100_000,
                    output_tokens=2_000)
    expect1 = (100_000 / 1e6 * 0.5 + 2_000 / 1e6 * 2.0 + 0.001)
    assert abs(c1 - expect1) < 1e-9, (c1, expect1)

    # 大流量走 pro 且带缓存:缓存部分按折扣计
    c2 = acc.record("2026-11-05", "glm-pro", input_tokens=500_000,
                    output_tokens=8_000, cached_tokens=400_000)
    expect2 = (100_000 / 1e6 * 4.0 + 8_000 / 1e6 * 16.0
               + 400_000 / 1e6 * 0.4 + 0.01)
    assert abs(c2 - expect2) < 1e-9

    saving = CostAccountant.cache_saving(acc.records[-1], PRICES)
    assert abs(saving - 400_000 / 1e6 * (4.0 - 0.4)) < 1e-9

    # 按模型/按天汇总与预算告警
    by_model = acc.totals_by_model("2026-11-05")
    assert set(by_model) == {"glm-air", "glm-pro"}
    assert by_model["glm-pro"] > by_model["glm-air"]
    alert = acc.budget_alert("2026-11-05")
    assert alert["level"] in ("ok", "warn", "breach")
    assert alert["spent"] == round(c1 + c2, 4)

    # 超预算:级别落到 breach
    acc.record("2026-11-06", "glm-pro", input_tokens=200_000,
               output_tokens=20_000)
    alert2 = acc.budget_alert("2026-11-06")
    assert alert2["spent"] > acc.daily_budget
    assert alert2["level"] == "breach", alert2
    print("两笔成本: %.4f / %.4f 元" % (c1, c2))
    print("缓存节省: %.4f 元 | 告警级别: %s" % (saving, alert2["level"]))
    print("按天汇总:", acc.totals_by_day())


if __name__ == "__main__":
    main()
