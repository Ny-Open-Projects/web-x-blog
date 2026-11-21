"""多轮工具结果的增量摘要:原始结果滚动合并为事实台账,上下文只保留台账。"""


class ResultLedger:
    def __init__(self):
        self.facts = {}

    def absorb(self, turn, tool, result):
        """把一条工具结果增量合并进台账:次数累加 值择新 来源去重。"""
        for entity, value in result.items():
            f = self.facts.setdefault(entity, {"seen": 0, "value": None,
                                               "tools": [], "last_turn": 0})
            f["seen"] += 1
            f["value"] = value
            if tool not in f["tools"]:
                f["tools"].append(tool)
            f["last_turn"] = turn

    def render(self, budget):
        """渲染为紧凑台账,超预算时按最近活跃优先保留,返回挤掉的实体数。"""
        items = sorted(self.facts.items(), key=lambda kv: -kv[1]["last_turn"])
        lines, used = [], 0
        for name, f in items:
            line = "%s: 值=%s 查了%d次 来源=%s 最近=T%d" % (
                name, f["value"], f["seen"], "+".join(f["tools"]), f["last_turn"])
            if used + len(line) > budget:
                break
            lines.append(line)
            used += len(line)
        return "\n".join(lines), len(items) - len(lines)


if __name__ == "__main__":
    ledger = ResultLedger()
    ledger.absorb(1, "web_search", {"订单状态": "已发货"})
    ledger.absorb(3, "db_query", {"订单状态": "已发货", "物流单号": "SF123"})
    ledger.absorb(5, "web_search", {"订单状态": "已签收"})

    f = ledger.facts["订单状态"]
    assert f["seen"] == 3 and f["value"] == "已签收", "值必须择最新一次"
    assert f["tools"] == ["web_search", "db_query"], "来源去重但保留出现顺序"
    f2 = ledger.facts["物流单号"]
    assert f2["seen"] == 1 and f2["last_turn"] == 3

    text, dropped = ledger.render(budget=60)
    assert "已签收" in text and "订单状态" in text, "最近活跃的实体优先保留"
    assert dropped >= 1, "预算不够时必须有实体被挤出且数量如实上报"
    small, dropped2 = ledger.render(budget=24)
    assert dropped2 > dropped or len(small.splitlines()) == 1, "预算越小挤掉越多"
    print("增量台账通过:3 次查询合并为 2 条事实,值择新 来源去重 预算裁剪")
