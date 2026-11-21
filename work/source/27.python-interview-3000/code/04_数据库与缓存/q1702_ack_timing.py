"""幂等消费的 ack 时序: 处理 标记 提交三步的崩溃窗口分析"""

def run_case(order, crash_after):
    """order 是步骤顺序; crash_after 表示该步完成后崩溃, 观察是否重投"""
    log, side_effects = [], 0
    state = {"marked": False, "acked": False}

    def delivery(tag):
        nonlocal side_effects
        for step in order:
            if step == "process":
                if state["marked"]:
                    log.append(f"  [{tag}] 命中幂等标记, 跳过处理")
                else:
                    side_effects += 1
                    log.append(f"  [{tag}] 处理业务")
            elif step == "mark":
                state["marked"] = True
                log.append(f"  [{tag}] 落幂等标记")
            elif step == "ack":
                state["acked"] = True
                log.append(f"  [{tag}] ack")
            if crash_after == step and tag == "第1次":
                return

    delivery("第1次")
    if crash_after:
        if not state["acked"]:
            log.append("  --- 崩溃, 消息重投 ---")
            delivery("第2次")
        else:
            log.append("  --- 崩溃, 但消息已 ack, 不重投 ---")
    return side_effects, log

for name, order in (("正确时序 处理-标记-ack", ("process", "mark", "ack")),
                    ("危险时序 ack-处理", ("ack", "process"))):
    for crash in ("process", "mark", "ack"):
        n, log = run_case(order, crash)
        print(f"{name} | 崩溃于 {crash} 之后: 业务副作用 {n} 次")
        for line in log:
            print(line)
        print()

print("结论: 幂等标记必须与业务副作用同事务, ack 放在标记之后;")
print("      先 ack 后处理是最危险时序, 崩溃在窗口内消息直接丢失, 业务永远没执行")
