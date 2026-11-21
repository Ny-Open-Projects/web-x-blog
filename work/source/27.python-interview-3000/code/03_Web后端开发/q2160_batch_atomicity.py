"""批量端点的两种执行模式: all-or-nothing 与尽力而为(纯标准库)。"""


def save(item):
    """模拟单条落库: 校验失败抛错。"""
    if item.get("qty", 0) < 0:
        raise ValueError("qty 不能为负: " + str(item.get("sku")))
    return {"sku": item["sku"], "qty": item["qty"]}


def execute_atomic(items):
    """事务式: 任一项失败则全部回滚, 返回 422 与首个错误定位。"""
    staged = []
    for index, item in enumerate(items):
        try:
            staged.append(save(item))
        except ValueError as exc:
            return 422, {"mode": "atomic", "saved": 0, "failed_index": index,
                         "error": str(exc)}
    return 201, {"mode": "atomic", "saved": staged}


def execute_best_effort(items):
    """尽力而为: 跳过失败项继续, 返回 200 与 per-item 明细。"""
    results = []
    for index, item in enumerate(items):
        try:
            results.append({"index": index, "ok": True, "resource": save(item)})
        except ValueError as exc:
            results.append({"index": index, "ok": False, "error": str(exc)})
    return 200, {"mode": "best_effort", "results": results}


batch = [{"sku": "A", "qty": 1}, {"sku": "B", "qty": -2}, {"sku": "C", "qty": 3}]
for fn in (execute_atomic, execute_best_effort):
    code, body = fn(batch)
    print("HTTP", code, body)
assert execute_atomic(batch)[0] == 422
assert len(execute_best_effort(batch)[1]["results"]) == 3
print("要点: 语义写进文档并由参数显式声明, 原子模式不出现部分成功响应, 尽力而为模式不静默丢失败项")
