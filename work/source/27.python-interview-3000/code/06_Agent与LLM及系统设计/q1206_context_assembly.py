"""上下文装配:Jaccard 去重 -> 预算截断 -> 首尾重点排布 -> 装配报告。"""


def jaccard(a, b):
    sa, sb = set(a.split()), set(b.split())
    return len(sa & sb) / (len(sa | sb) or 1)


def assemble(candidates, budget_chars=120, top_n=8, dup_threshold=0.6):
    # 1 去重:高分优先,近重复丢弃
    kept, dropped = [], []
    for score, text in sorted(candidates, reverse=True):
        if len(kept) >= top_n:
            dropped.append((text, "top_n 超限"))
            continue
        if any(jaccard(text, k_text) > dup_threshold for _, k_text in kept):
            dropped.append((text, "近重复"))
            continue
        kept.append((score, text))
    # 2 预算截断
    final, used = [], 0
    for score, text in kept:
        if used + len(text) > budget_chars:
            dropped.append((text, "预算超限"))
            continue
        final.append(text)
        used += len(text)
    # 3 首尾重点排布:第 1 名放开头,第 2 名放结尾
    if len(final) >= 2:
        final = [final[0]] + final[2:] + [final[1]]
    numbered = [f"[{i+1}] {t}" for i, t in enumerate(final)]
    return numbered, dropped, used


if __name__ == "__main__":
    cands = [
        (0.95, "退货运费 由 买家 承担"),
        (0.90, "退货运费 由 买家 承担 特殊 说明"),      # 近重复
        (0.85, "七天 无理由 退货 期限 说明"),
        (0.70, "质量问题 运费 商家 承担"),
        (0.50, "无关 片段 关于 会员 积分"),
        (0.40, "又 一个 无关 片段 内容"),
    ]
    numbered, dropped, used = assemble(cands, budget_chars=100)
    print("装配结果:")
    for n in numbered:
        print("  ", n)
    print("丢弃:", [(t[:12], why) for t, why in dropped])
    texts = [n[4:] for n in numbered]
    assert texts[0].startswith("退货运费"), "最高分放开头"
    assert any("质量问题" in t for t in texts), "次高分在结尾强化"
    assert any(why == "近重复" for _, why in dropped), "近重复被合并"
    assert used <= 100
    print(f"预算 {used}/100 字符,装配报告完整可排障")
