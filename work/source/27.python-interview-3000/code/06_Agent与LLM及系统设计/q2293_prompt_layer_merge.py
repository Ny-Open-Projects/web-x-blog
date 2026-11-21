"""Prompt 片段分层组合:全局 租户 会话 请求四层 last-wins 合并,lock 键禁止被覆盖。"""
SECTION_ORDER = ["role", "tone", "rule", "style"]


def merge_layers(layers, locked_keys=()):
    merged, rejected = {}, []
    for level, frag in layers:
        for k, v in frag.items():
            if k in locked_keys and k in merged and merged[k] != v:
                rejected.append({"key": k, "level": level})
                continue
            merged[k] = v
    return merged, rejected


def render(merged):
    return "\n".join(merged[k] for k in SECTION_ORDER if k in merged)


if __name__ == "__main__":
    merged, rejected = merge_layers([
        ("global", {"role": "你是客服助手", "tone": "正式", "style": "简洁"}),
        ("tenant", {"tone": "亲切"}),
        ("session", {"rule": "只答退货问题"}),
        ("request", {"tone": "夸张", "role": "你是诗人"}),
    ], locked_keys=("role",))
    assert merged["tone"] == "夸张", "未锁键 last-wins 高层覆盖低层"
    assert merged["role"] == "你是客服助手"
    assert rejected == [{"key": "role", "level": "request"}], "锁定键拒绝覆盖并留痕"
    text = render(merged)
    assert text.index("客服助手") < text.index("夸张"), "渲染按固定小节序"
    merged2, rejected2 = merge_layers([("global", {"role": "A"}), ("tenant", {"role": "A"})],
                                      locked_keys=("role",))
    assert rejected2 == [], "同值重复不视为覆盖"
    print("片段组合通过:分层覆盖 锁定拒绝留痕 固定序渲染")
