"""回调乱序与旧事件的拒收: 按实体裁决单调性(纯标准库)。"""


def apply_event(store, event):
    """每实体维护 updated_at 与 seq 两个单调水位。

    裁决: updated_at 更大才应用; 相等时 seq 更大才应用; 旧事件拒收但同样应答 200,
    让发送方停止重试, 旧数据绝不覆盖新数据。
    """
    ent = store.setdefault(event["entity"], {"state": None, "updated_at": -1, "seq": -1})
    newer = (event["updated_at"] > ent["updated_at"]
             or (event["updated_at"] == ent["updated_at"] and event["seq"] > ent["seq"]))
    if not newer:
        return "stale_drop"
    ent["state"] = event["state"]
    ent["updated_at"] = event["updated_at"]
    ent["seq"] = event["seq"]
    return "applied"


store = {}
assert apply_event(store, {"entity": "o1", "state": "shipped", "updated_at": 300, "seq": 3}) == "applied"
assert apply_event(store, {"entity": "o1", "state": "paid", "updated_at": 200, "seq": 2}) == "stale_drop", "旧事件拒收"
assert store["o1"]["state"] == "shipped", "拒收后状态不被回退"
assert apply_event(store, {"entity": "o1", "state": "closed", "updated_at": 300, "seq": 4}) == "applied", "同秒靠 seq 决胜负"
assert apply_event(store, {"entity": "o1", "state": "ghost", "updated_at": 300, "seq": 4}) == "stale_drop", "完全相同的水位视为重投"

# 乱序批次: 到达顺序 5,3,4,6 -> 最终状态必须是 6
trail = []
for ev in ({"entity": "o2", "state": "s5", "updated_at": 500, "seq": 5},
           {"entity": "o2", "state": "s3", "updated_at": 300, "seq": 3},
           {"entity": "o2", "state": "s4", "updated_at": 400, "seq": 4},
           {"entity": "o2", "state": "s6", "updated_at": 600, "seq": 6}):
    trail.append(apply_event(store, ev))
assert store["o2"]["state"] == "s6" and trail == ["applied", "stale_drop", "stale_drop", "applied"]
print("到达序 5,3,4,6 -> 应用 5 拒 3 拒 4 应用 6, 终态 s6")
print("拒收也是 200: 乱序不是错误, 让对端停止重试即可")
