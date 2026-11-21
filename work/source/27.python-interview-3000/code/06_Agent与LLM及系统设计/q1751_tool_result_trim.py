"""工具结果结构化裁剪:按字段优先级在预算内保留,丢掉的字段登记进 _dropped。"""
import json

FIELD_PRIORITY = {
    "web_search": {"title": 0, "url": 0, "snippet": 1, "content": 2, "related": 3},
    "db_query": {"rows": 0, "count": 1, "schema": 2, "debug": 3},
}


def est_chars(value):
    return len(value) if isinstance(value, str) else len(json.dumps(value, ensure_ascii=False))


class ToolResultTrimmer:
    def __init__(self, budget):
        self.budget = budget

    def trim(self, tool, result):
        prio = FIELD_PRIORITY.get(tool, {})
        keys = sorted(result, key=lambda k: (prio.get(k, 9), k))
        kept, dropped, used = {}, [], 0
        for k in keys:
            cost = est_chars(result[k]) + len(k) + 2
            if used + cost <= self.budget:
                kept[k] = result[k]
                used += cost
            else:
                dropped.append(k)
        if dropped:
            kept["_dropped"] = dropped          # 截断标记:模型可感知信息不完整
        return kept, used


if __name__ == "__main__":
    raw = {"title": "退货政策", "url": "https://x/policy", "snippet": "7 天无理由",
           "content": "全文" * 200, "related": ["a", "b", "c", "d"]}

    kept, used = ToolResultTrimmer(budget=70).trim("web_search", raw)
    assert kept["title"] == "退货政策" and kept["snippet"] == "7 天无理由"
    assert kept["_dropped"] == ["content", "related"], "低优先级大字段先被丢"
    assert used <= 70, "预算必须被遵守"

    full, _ = ToolResultTrimmer(budget=4000).trim("web_search", raw)
    assert "_dropped" not in full, "预算充足时不应丢弃任何字段"

    loose, _ = ToolResultTrimmer(budget=70).trim("unknown_tool", {"x": "y"})
    assert loose == {"x": "y"}, "无优先级表时原样保留"
    print("结构化裁剪通过:预算内保高优字段,丢弃登记 _dropped,无表工具不误伤")
