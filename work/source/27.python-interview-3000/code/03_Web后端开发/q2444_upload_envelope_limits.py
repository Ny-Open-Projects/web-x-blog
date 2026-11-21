"""表单信封的双重上限: 字段数与总字节(纯标准库)。"""


def scan_envelope(parts, max_fields, max_total_bytes):
    """parts: (字段名, 字节值) 序列。双重上限逐项检查, 触线立即拒绝。"""
    total = 0
    for i, (name, value) in enumerate(parts, start=1):
        total += len(name.encode()) + len(value)
        if i > max_fields:
            return False, "field_limit", {
                "reason": "字段数超限", "fields_seen": i, "max_fields": max_fields}
        if total > max_total_bytes:
            return False, "size_limit", {
                "reason": "总大小超限", "bytes_seen": total,
                "max_total_bytes": max_total_bytes, "field": name}
    return True, "ok", {"fields": len(parts), "bytes": total}


def make_parts(n, value_size):
    return [("field-{}".format(i), b"x" * value_size) for i in range(n)]


# 场景一: 20 个小字段, 限额 50 字段 100KB -> 通过
parts_small = make_parts(20, 64)
expect_total = sum(len(name.encode()) + len(value) for name, value in parts_small)
ok, kind, info = scan_envelope(parts_small, max_fields=50, max_total_bytes=100 * 1024)
print("场景一 -> {} {} {}".format(ok, kind, info))
assert ok and info["bytes"] == expect_total

# 场景二: 80 个字段触发字段数上限
ok, kind, info = scan_envelope(make_parts(80, 8), max_fields=50, max_total_bytes=1024 * 1024)
print("场景二 -> {} {} {}".format(ok, kind, info))
assert not ok and kind == "field_limit" and info["fields_seen"] == 51

# 场景三: 少量超大值触发总大小上限
ok, kind, info = scan_envelope([("blob", b"z" * 300 * 1024)],
                               max_fields=50, max_total_bytes=100 * 1024)
print("场景三 -> {} {} 字段={} 字节={}".format(
    ok, kind, info["field"], info["bytes_seen"]))
assert not ok and kind == "size_limit" and info["bytes_seen"] > 100 * 1024

# 场景四: 空表单也放行, 两个上限互不替代
ok, kind, info = scan_envelope([], max_fields=50, max_total_bytes=1024)
print("场景四 -> {} {} {}".format(ok, kind, info))
assert ok and info == {"fields": 0, "bytes": 0}
print("要点: 字段数上限防 海量小字段 打爆解析器, 总大小上限防 单个大值 吃满磁盘, "
      "两者逐项检查才能在最小代价处失败")
