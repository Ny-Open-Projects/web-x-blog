"""Q2565 上下文注入的优先级仲裁:多来源抢同一槽位。

系统策略、租户画像、检索结果、历史摘要都想往上下文里塞内容,
按固定优先级仲裁:同槽位高优先级先占,同内容去重只留一份,
被挤掉的要留痕,方便事后解释上下文里为什么没有它。
"""
import json

PRIORITY = {"system": 0, "tenant": 1, "retrieved": 2, "history": 3}


def arbitrate(items):
    ordered = sorted(items, key=lambda x: PRIORITY[x["source"]])
    slots = {}
    for it in ordered:
        h = json.dumps(it["content"], ensure_ascii=False, sort_keys=True)
        rec = slots.setdefault(it["slot"],
                               {"kept": it, "hashes": {h}, "dup": [], "dropped": []})
        if rec["kept"] is not it:
            if h in rec["hashes"]:
                rec["dup"].append(it["source"])
            else:
                rec["hashes"].add(h)
                rec["dropped"].append(it["source"])
    return slots


def main():
    items = [
        {"source": "history", "slot": "facts", "content": "用户在杭州"},
        {"source": "retrieved", "slot": "facts", "content": "用户在杭州"},
        {"source": "tenant", "slot": "style", "content": "正式语气"},
        {"source": "system", "slot": "style", "content": "正式语气"},
        {"source": "history", "slot": "style", "content": "口语化"},
    ]
    slots = arbitrate(items)
    assert slots["style"]["kept"]["source"] == "system", slots["style"]
    assert slots["style"]["dup"] == ["tenant"], slots["style"]
    assert slots["style"]["dropped"] == ["history"], slots["style"]
    assert slots["facts"]["kept"]["source"] == "retrieved"
    assert slots["facts"]["dup"] == ["history"]
    print("style 胜者:", slots["style"]["kept"]["source"],
          "重复:", slots["style"]["dup"], "被挤:", slots["style"]["dropped"])
    print("facts 胜者:", slots["facts"]["kept"]["source"], "重复:", slots["facts"]["dup"])


if __name__ == "__main__":
    main()
