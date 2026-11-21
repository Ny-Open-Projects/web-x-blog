"""Prompt 自动回滚:滑窗质量连续 k 窗低于基线容差,自动切回基线并防抖。"""


class AutoRollback:
    def __init__(self, baseline_score=0.90, drop=0.05, windows=3):
        self.baseline = baseline_score
        self.drop = drop
        self.need = windows
        self.bad_streak = 0
        self.active = "candidate"
        self.actions = []

    def observe(self, window_score):
        if self.active != "candidate":
            return "already_rolled_back"         # 回滚后不再振荡
        if window_score < self.baseline - self.drop:
            self.bad_streak += 1
            if self.bad_streak >= self.need:
                self.active = "baseline"
                self.actions.append("rollback")
                return "rolled_back"
            return "watching"
        self.bad_streak = 0                      # 健康窗清零,防偶发抖动误杀
        return "healthy"


if __name__ == "__main__":
    rb = AutoRollback(baseline_score=0.90, drop=0.05, windows=3)
    assert rb.observe(0.92) == "healthy"
    assert rb.observe(0.80) == "watching", "低 1 窗:观察"
    assert rb.observe(0.93) == "healthy", "好窗清零"
    seq = [rb.observe(s) for s in (0.83, 0.84, 0.82)]
    assert seq == ["watching", "watching", "rolled_back"], "连续 3 低窗触发回滚"
    assert rb.active == "baseline" and rb.actions == ["rollback"]
    assert rb.observe(0.50) == "already_rolled_back", "回滚后流量守在基线"
    print("自动回滚通过:连续 3 窗劣化才回滚,单窗好转清零防抖,回滚后守稳")
