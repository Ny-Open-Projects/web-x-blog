"""长轮询的丢事件竞态: 游标过滤才是正确姿势(纯标准库)。"""

EVENTS = []


def publish(text):
    EVENTS.append({"id": len(EVENTS) + 1, "text": text})


def poll(cursor, hold_has_new=False):
    """cursor 是客户端已见的最大事件 id; hold_has_new 模拟挂起期间有事件到达。"""
    new = [e for e in EVENTS if e["id"] > cursor]
    if not new and hold_has_new:
        publish("挂起期间到达")
        new = [e for e in EVENTS if e["id"] > cursor]
    return {"events": new, "next_cursor": new[-1]["id"] if new else cursor, "held": not new}


# 正常路径: 挂起期间事件到达, 长轮询立即唤醒
r1 = poll(0, hold_has_new=True)
print("挂起唤醒:", r1)

# 竞态: 两次轮询之间涌入多条事件, 取"最新一条"的坏实现会丢事件
publish("e1")
publish("e2")
publish("e3")
buggy = EVENTS[-1:]
good = [e for e in EVENTS if e["id"] > 0]
print("坏实现 latest-1 拿到:", [e["text"] for e in buggy], "丢了", len(good) - len(buggy), "条")
print("游标过滤拿到:", [e["text"] for e in good], "next_cursor:", good[-1]["id"])
print("结论: 长轮询必须传游标做增量过滤, 超时空响应也要回带 next_cursor")
