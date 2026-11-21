"""Q2574 会话导入的校验与版本降级:缺省、未知字段与旧版迁移。

导入端三道闸:未来版本直接拒绝;旧版本做一次性迁移;未知字段
保留警告不静默丢弃,缺失字段补缺省,迁移结果必须逐字段可断言。
"""

SUPPORTED = 2


def import_session(blob, warnings):
    known = {"schema_version", "tenant", "messages", "anchors", "history", "pinned"}
    for key in blob:
        if key not in known:
            warnings.append("unknown-field:" + key)
    v = blob.get("schema_version", 1)
    if v > SUPPORTED:
        raise ValueError("schema_version " + str(v) + " 高于当前支持 " + str(SUPPORTED))
    if v < SUPPORTED:
        if v == 1:
            blob = {"schema_version": 2,
                    "tenant": blob.get("tenant", "unknown"),
                    "messages": [{"role": m.get("role", "user"),
                                  "text": m.get("content", "")}
                                 for m in blob.get("history", [])],
                    "anchors": blob.get("pinned", [])}
            warnings.append("migrated:v1->v2")
        else:
            raise ValueError("无法迁移的旧版本:" + str(v))
    out = {"schema_version": SUPPORTED,
           "tenant": blob.get("tenant", "unknown"),
           "messages": blob.get("messages", []),
           "anchors": blob.get("anchors", [])}
    if not out["anchors"]:
        warnings.append("default:anchors=empty")
    return out


def main():
    warnings = []
    old = {"schema_version": 1, "tenant": "t9",
           "history": [{"role": "user", "content": "hi"}],
           "pinned": ["h0"], "theme": "dark"}
    s = import_session(old, warnings)
    assert s["messages"] == [{"role": "user", "text": "hi"}], s
    assert s["anchors"] == ["h0"], s
    assert "migrated:v1->v2" in warnings and "unknown-field:theme" in warnings
    warnings2 = []
    try:
        import_session({"schema_version": 3}, warnings2)
        raise SystemExit(1)
    except ValueError as exc:
        print("未来版本拒绝:", exc)
    print("v1 迁移结果:", s)
    print("警告:", warnings)


if __name__ == "__main__":
    main()
