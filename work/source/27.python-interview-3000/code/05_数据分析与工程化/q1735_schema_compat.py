"""schema 演进兼容矩阵:逐列判定新增/删除/改型,输出兼容结论与动作"""

OLD = {
    "uid": "string",
    "amount": "int",
    "city": "string",
    "unused": "string",
}
NEW = {
    "uid": "string",
    "amount": "bigint",     # 加宽,兼容
    "city": "string",
    "pay_status": "int",    # 新增
    # unused 被删除
}

WIDEN = {("int", "bigint"), ("float", "double"), ("int", "double")}


def judge(old, new):
    diffs = []
    for col in new:
        if col not in old:
            diffs.append((col, "added", "兼容:下游按需取用,读取端可空"))
    for col in old:
        if col not in new:
            diffs.append((col, "removed", "破坏:依赖它的下游直接失败,先确认无引用或保留占位列"))
    for col in set(old) & set(new):
        if old[col] != new[col]:
            if (old[col], new[col]) in WIDEN:
                diffs.append((col, "type_widen", "兼容:类型加宽,读取端需感知精度"))
            else:
                diffs.append((col, "type_change", "破坏:类型收窄或不兼容,需停写迁移"))
    return diffs


if __name__ == "__main__":
    diffs = judge(OLD, NEW)
    for col, kind, note in diffs:
        print(f"  [{kind:<11}] {col:<12} {note}")
    breaking = any(k in ("removed", "type_change") for _, k, _ in diffs)
    print("结论:", "含破坏性变更,不能直接上线,走两阶段:先双写新列,确认下游迁移后再删旧列" if breaking else "兼容,可直接上线")
    print("要点:兼容矩阵是发布门禁——加列与加宽直通,删列改名必须两阶段;读端永远按'可能多列缺列'防御式解析")
