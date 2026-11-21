"""工具注册表兼容性检查:参数与返回结构的破坏性变更检测,升级前先过闸。"""


def diff_params(old, new):
    findings = []
    for name in sorted(old):
        if name not in new:
            findings.append({"kind": "removed", "param": name, "breaking": True})
            continue
        if old[name].get("type") != new[name].get("type"):
            findings.append({"kind": "type_changed", "param": name, "breaking": True})
        if not old[name].get("required") and new[name].get("required"):
            findings.append({"kind": "made_required", "param": name, "breaking": True})
    for name in sorted(new):
        if name not in old:
            breaking = bool(new[name].get("required"))
            findings.append({"kind": "added_required" if breaking else "added_optional",
                             "param": name, "breaking": breaking})
    return findings


def diff_returns(old, new):
    findings = []
    for f in sorted(old.get("fields", [])):
        if f not in new.get("fields", []):
            findings.append({"kind": "return_field_removed", "field": f, "breaking": True})
    return findings


def gate(old_schema, new_schema):
    findings = diff_params(old_schema["params"], new_schema["params"]) + \
        diff_returns(old_schema.get("returns", {}), new_schema.get("returns", {}))
    breaking = [f for f in findings if f["breaking"]]
    return {"breaking": breaking, "compatible": not breaking, "all": findings}


if __name__ == "__main__":
    v1 = {"params": {"sql": {"type": "str", "required": True},
                     "limit": {"type": "int", "required": False}},
          "returns": {"fields": ["rows", "count"]}}

    # 兼容升级:加可选参数,返回加字段
    v2 = {"params": {"sql": {"type": "str", "required": True},
                     "limit": {"type": "int", "required": False},
                     "timeout": {"type": "int", "required": False}},
          "returns": {"fields": ["rows", "count", "took_ms"]}}
    g2 = gate(v1, v2)
    assert g2["compatible"] and g2["breaking"] == []

    # 破坏性:删参数 新增必填 返回砍字段
    v3 = {"params": {"sql": {"type": "str", "required": True},
                     "max_rows": {"type": "int", "required": True}},
          "returns": {"fields": ["rows"]}}
    g3 = gate(v1, v3)
    kinds = sorted(f["kind"] for f in g3["breaking"])
    assert kinds == ["added_required", "removed", "return_field_removed"], kinds
    assert not g3["compatible"]

    # 破坏性:改类型 可选变必填
    v5 = {"params": {"sql": {"type": "bytes", "required": True},
                     "limit": {"type": "int", "required": True}},
          "returns": {"fields": ["rows", "count"]}}
    g5 = gate(v1, v5)
    assert sorted(f["kind"] for f in g5["breaking"]) == ["made_required", "type_changed"]
    assert not g5["compatible"]

    # 误报防线:required True -> False 是放宽,不是破坏
    v4 = {"params": {"sql": {"type": "str", "required": False},
                     "limit": {"type": "int", "required": False}},
          "returns": {"fields": ["rows", "count"]}}
    assert gate(v1, v4)["compatible"]
    print("兼容闸通过:新增可选放行,删除 改类型 变必填 砍返回字段四类破坏全拦下")
