"""Q2842 工具入参的规范化闸:类型矫正 别名归一与越界钳制。

LLM 交上来的参数经常是「差不多对」:数字带引号 字段用别名 越界取值。
与其让工具层各自报错,不如过一道规范化闸:按 schema 矫正类型 归一
别名 钳制范围 补缺省,矫正动作全部留痕,静默改参不等于没改。
"""

SCHEMA = {
    "top_k": {"type": "int", "alias": ["k", "limit"], "min": 1, "max": 20, "default": 5},
    "query": {"type": "str", "strip": True},
    "fuzzy": {"type": "bool", "truthy": ["yes", "true", "1"]},
}


def normalize(raw, schema, notes):
    out = {}
    for name, spec in schema.items():
        found = name in raw
        v = raw.get(name)
        if not found:
            for a in spec.get("alias", []):
                if a in raw:
                    v = raw[a]
                    found = True
                    notes.append("别名:" + a + "->" + name)
                    break
        if not found:
            if "default" in spec:
                out[name] = spec["default"]
                notes.append("缺省:" + name + "=" + str(spec["default"]))
            continue
        if spec["type"] == "int":
            v = int(v)
            lo, hi = spec.get("min"), spec.get("max")
            if lo is not None and v < lo:
                notes.append("钳制:" + name + ":" + str(v) + "->" + str(lo))
                v = lo
            if hi is not None and v > hi:
                notes.append("钳制:" + name + ":" + str(v) + "->" + str(hi))
                v = hi
        elif spec["type"] == "str" and spec.get("strip"):
            v = str(v).strip()
        elif spec["type"] == "bool":
            if isinstance(v, str):
                v = v.strip().lower() in spec.get("truthy", ["true"])
                notes.append("布尔矫正:" + name)
        out[name] = v
    return out


def main():
    notes = []
    args = normalize({"k": "10", "query": "  退款政策  ", "fuzzy": "yes"},
                     SCHEMA, notes)
    assert args == {"top_k": 10, "query": "退款政策", "fuzzy": True}, args
    # 缺 top_k 走缺省,limit 是别名之一,越界被钳到 20
    notes2 = []
    args2 = normalize({"limit": "50", "query": "发票"}, SCHEMA, notes2)
    assert args2["top_k"] == 20, args2
    assert any("缺省" in n or "钳制" in n for n in notes2), notes2
    assert args2["query"] == "发票"
    print("矫正后:", args)
    print("留痕:", notes)
    print("别名加钳制:", args2["top_k"], notes2[:2])


if __name__ == "__main__":
    main()
