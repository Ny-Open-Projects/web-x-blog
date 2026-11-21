"""选择性保留:对历史消息打分(时效/密度/角色/相关性),在预算内保留高分消息。"""
import re


def score(msg, query, now_idx):
    role, content = msg[0], msg[1]
    recency = (now_idx - msg[2]) / (now_idx + 1)          # 越新越高
    density = min(len(re.findall(r"\d|叫|偏好|预算|必须", content)), 3) / 3
    role_w = 1.0 if role == "user" else 0.6
    overlap = len(set(content) & set(query)) / (len(set(query)) or 1)
    return 0.35 * recency + 0.3 * density + 0.15 * role_w + 0.2 * overlap


def select_history(history, query, budget_chars):
    indexed = [(r, c, i) for i, (r, c) in enumerate(history)]
    ranked = sorted(indexed, key=lambda m: score(m, query, len(history)), reverse=True)
    kept, used = [], 0
    for r, c, i in ranked:
        if used + len(c) > budget_chars:
            continue
        kept.append((i, r, c))
        used += len(c)
    return [m[1:] for m in sorted(kept)], used


if __name__ == "__main__":
    history = [
        ("user", "今天天气不错啊哈哈"),
        ("user", "我叫小王,预算一千五,去北京"),
        ("assistant", "好的,已为你找到 3 个航班"),
        ("user", "顺便推荐点吃的"),
        ("assistant", "北京烤鸭很有名"),
        ("user", "记住我必须靠窗座位"),
    ]
    kept, used = select_history(history, "北京的航班 预算 靠窗", budget_chars=60)
    for r, c in kept:
        print(f"[{r}] {c}")
    assert any("预算" in c for _, c in kept), "高密度消息应保留"
    assert any("靠窗" in c for _, c in kept), "任务相关消息应保留"
    assert used <= 60
    print(f"预算 60 字符,保留 {len(kept)} 条,占用 {used}")
