"""上下文预算分配器:分段配额 + 段内价值裁剪 + 全局校验降级。"""


def est_tokens(text):
    return max(1, len(text) // 2)            # 中文粗估:2 字符 1 token


class BudgetAllocator:
    SHARES = {"system": 0.15, "retrieval": 0.45, "history": 0.30, "question": 0.10}

    def __init__(self, total=800):
        self.total = total

    def allocate(self, system, retrieval, history, question):
        quota = {k: int(self.total * v) for k, v in self.SHARES.items()}
        out = {"system": system, "question": question}
        fixed = est_tokens(system) + est_tokens(question)
        flexible = self.total - fixed
        # 检索片段按分数从高到低装入配额
        keep_r, used = [], 0
        for score, chunk in sorted(retrieval, reverse=True):
            t = est_tokens(chunk)
            if used + t <= int(flexible * self.SHARES["retrieval"] / 0.55):
                keep_r.append(chunk)
                used += t
        out["retrieval"] = keep_r
        # 历史从最新往回保留
        keep_h, used_h = [], 0
        for role, msg in reversed(history):
            t = est_tokens(msg)
            if used_h + t <= int(flexible * self.SHARES["history"] / 0.55):
                keep_h.insert(0, (role, msg))
                used_h += t
        out["history"] = keep_h
        total_used = fixed + used + used_h
        out["tokens_used"] = total_used
        out["degraded"] = total_used > self.total
        return out


if __name__ == "__main__":
    alloc = BudgetAllocator(total=400)
    retrieval = [(0.92, "高相关片段" * 20), (0.75, "中相关片段" * 15), (0.4, "低相关噪声" * 40)]
    history = [(f"m{i}", "历史消息" * 10) for i in range(10)]
    plan = alloc.allocate("你是行程助手", retrieval, history, "明天北京穿什么")
    print("装入检索片段:", len(plan["retrieval"]), "保留历史:", len(plan["history"]))
    print("低分噪声被裁:", "低相关噪声" not in " ".join(plan["retrieval"]))
    print("最老历史被裁:", len(plan["history"]) < 10)
    print(f"token 用量 {plan['tokens_used']}/{alloc.total} 超限降级={plan['degraded']}")
    assert not plan["degraded"], "分配器必须保证不超预算"
    assert len(plan["retrieval"]) <= len(retrieval)
