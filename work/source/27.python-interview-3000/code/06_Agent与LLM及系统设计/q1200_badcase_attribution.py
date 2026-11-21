"""badcase 四分归因:检索/排序/上下文/生成,自动判定并输出修复优先级。"""


def attribute(recall_top_k, final_context_ids, gold_chunk, answer_supported):
    """gold_chunk: golden 是否存在;recall_top_k: 召回列表;final_context_ids: 最终上下文"""
    if gold_chunk not in recall_top_k:
        return "retrieval_failure"
    if gold_chunk not in final_context_ids:
        return "ranking_or_budget_failure"
    if not answer_supported:
        return "generation_failure"
    return "other_or_ok"


def audit(cases):
    stats = {}
    for c in cases:
        label = attribute(c["recall"], c["recall"][: c["context_size"]],
                          c["gold"], c["supported"])
        stats[label] = stats.get(label, 0) + 1
        c["label"] = label
    total = len(cases)
    ranked = sorted(stats.items(), key=lambda x: -x[1])
    fixes = {"retrieval_failure": "改 chunk 策略或加查询改写",
             "ranking_or_budget_failure": "上 rerank 或扩上下文预算",
             "generation_failure": "改 prompt 或加忠实度校验",
             "other_or_ok": "复核标注"}
    print("归因分布与修复动作:")
    for label, n in ranked:
        print(f"  {label:<28} {n:>2} 条 ({n/total:.0%}) -> {fixes[label]}")
    return stats


if __name__ == "__main__":
    cases = [
        {"recall": ["d9", "d1"], "context_size": 1, "gold": "d1", "supported": True},
        {"recall": ["d1", "d9"], "context_size": 1, "gold": "d1", "supported": False},
        {"recall": ["d9", "d8"], "context_size": 2, "gold": "d1", "supported": False},
    ]
    # case1: d1 召回了但截断没进上下文 -> 排序/预算
    # case2: d1 进了上下文但答案无依据 -> 生成
    # case3: d1 根本没召回 -> 检索
    stats = audit(cases)
    assert stats["ranking_or_budget_failure"] == 1
    assert stats["generation_failure"] == 1
    assert stats["retrieval_failure"] == 1
    print("每类失败都能自动定位到对应修复动作")
