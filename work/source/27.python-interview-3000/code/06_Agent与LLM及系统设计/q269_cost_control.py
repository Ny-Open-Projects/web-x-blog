"""成本核算器:按模型分级路由并统计 token 费用,演示分级降本效果。"""

PRICING = {  # 每千 token 价格(演示值)
    "small": {"in": 0.5, "out": 1.5},
    "large": {"in": 5.0, "out": 15.0},
}


class CostTracker:
    def __init__(self):
        self.total = 0.0
        self.by_model: dict[str, float] = {}

    def bill(self, model: str, in_tokens: int, out_tokens: int):
        cost = (in_tokens / 1000 * PRICING[model]["in"]
                + out_tokens / 1000 * PRICING[model]["out"])
        self.total += cost
        self.by_model[model] = self.by_model.get(model, 0) + cost
        return cost


def route(task: str) -> str:
    """简单路由:分类/改写类用小模型,推理类用大模型。"""
    return "small" if task.startswith(("分类", "改写", "打标")) else "large"


def run_tasks(tasks: list[str], tracker: CostTracker):
    for task in tasks:
        model = route(task)
        in_t, out_t = (500, 30) if model == "small" else (2000, 500)
        cost = tracker.bill(model, in_t, out_t)
        print(f"  {task:<8} -> {model:<5} 费用 {cost:.4f}")


if __name__ == "__main__":
    tracker = CostTracker()
    run_tasks(["分类这条评论", "复杂推理解答数学证明", "改写这段文案", "复杂推理写行业分析"], tracker)
    print(f"总费用 {tracker.total:.4f},分布 {tracker.by_model}")
