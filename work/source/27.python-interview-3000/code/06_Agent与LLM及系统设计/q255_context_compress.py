"""多级压缩管线:裁剪工具输出 -> 滚动摘要 -> 硬截断,保护 system 消息。"""


def token_est(messages) -> int:
    return sum(len(m["content"]) for m in messages) // 2


def compress(messages, budget: int) -> list[dict]:
    msgs = [dict(m) for m in messages]
    # 第一级:压缩旧的 tool 消息
    for m in msgs:
        if m["role"] == "tool" and len(m["content"]) > 20:
            m["content"] = m["content"][:20] + "...[已裁剪]"
    if token_est(msgs) <= budget:
        return msgs
    # 第二级:滚动摘要(此处用假摘要函数)
    system = msgs[0]
    rest = msgs[1:]
    keep = rest[-2:]
    summary = " ".join(m["content"][:8] for m in rest[:-2])
    msgs = [system, {"role": "system", "content": f"[历史摘要] {summary}"}] + keep
    # 第三级:硬截断
    while token_est(msgs) > budget and len(msgs) > 2:
        msgs.pop(2)
    return msgs


if __name__ == "__main__":
    raw = [{"role": "system", "content": "你是助手"}]
    for i in range(5):
        raw += [{"role": "user", "content": f"问题{i}" * 5},
                {"role": "tool", "content": "工具返回了一大段很长的结果数据" * 3}]
    print("压缩前 token≈", token_est(raw))
    out = compress(raw, budget=40)
    print("压缩后 token≈", token_est(out), "消息数", len(out))
    for m in out:
        print(" ", m["role"], m["content"][:24])
