"""成本估算与三级预算护栏:请求级拒绝、会话级降级、日级熔断。"""


class BudgetGuard:
    PRICES = {"big": (0.06, 0.12), "small": (0.006, 0.012)}  # 每千 token 输入/输出价

    def __init__(self, session_limit=2.0, daily_limit=5.0):
        self.session_cost = 0.0
        self.daily_cost = 0.0
        self.session_limit = session_limit
        self.daily_limit = daily_limit

    def estimate(self, model, in_tokens, out_tokens):
        pin, pout = self.PRICES[model]
        return (in_tokens * pin + out_tokens * pout) / 1000

    def check(self, model, in_tokens, out_tokens):
        """返回 放行模型;超预算时降级或熔断。"""
        cost = self.estimate(model, in_tokens, out_tokens)
        if self.daily_cost + cost > self.daily_limit:
            return None, "daily_circuit_break"
        if self.session_cost + cost > self.session_limit:
            return "small", "downgrade_to_small"
        return model, "ok"

    def record(self, model, in_tokens, out_tokens):
        cost = self.estimate(model, in_tokens, out_tokens)
        self.session_cost += cost
        self.daily_cost += cost
        return cost


if __name__ == "__main__":
    guard = BudgetGuard(session_limit=0.5)
    for i in range(6):
        model, reason = guard.check("big", 2000, 1000)
        if model is None:
            print(f"轮次 {i}: 日预算熔断,停止服务")
            break
        if reason == "downgrade_to_small":
            model = "small"
            print(f"轮次 {i}: 会话超限,降级到 small 模型")
        real = guard.record(model, 2000, 1000)
        print(f"轮次 {i}: 使用 {model},本次成本 {real:.4f}")
    assert guard.daily_cost > 0
    print("护栏状态: 会话", round(guard.session_cost, 4), "日", round(guard.daily_cost, 4))
