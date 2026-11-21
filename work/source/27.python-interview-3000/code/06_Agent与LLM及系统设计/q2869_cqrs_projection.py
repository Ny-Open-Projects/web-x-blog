"""Q2869 CQRS 读写分离概念:命令侧校验 投影与读模型的最终一致。

命令侧只管校验和追加事件,读侧用投影把事件折成查询友好的读模型。
两边天然异步:写入刚落,读模型还没投影,查到的是旧值——这正是
CQRS 的代价,也是它把写负载与读负载彻底解耦的收益。
"""

CAPACITY = 2


def handle_command(cmd, events):
    """命令侧:校验通过才追加事件,拒绝不留痕。"""
    if cmd["action"] == "enroll":
        enrolled = sum(1 for e in events
                       if e[1] == cmd["course"] and e[0] != "cancel")
        if enrolled >= CAPACITY:
            return False, "课程已满"
    events.append((cmd["action"], cmd["course"], cmd["student"]))
    return True, "ok"


def project(events):
    """读侧投影:事件折叠成 course -> 学生名单 的读模型。"""
    model = {}
    for action, course, student in events:
        slot = model.setdefault(course, {"students": [], "count": 0})
        if action == "enroll":
            slot["students"].append(student)
            slot["count"] += 1
        elif action == "cancel":
            if student in slot["students"]:
                slot["students"].remove(student)
                slot["count"] -= 1
    return model


def main():
    events = []
    ok1, _ = handle_command({"action": "enroll", "course": "py",
                             "student": "alice"}, events)
    ok2, _ = handle_command({"action": "enroll", "course": "py",
                             "student": "bob"}, events)
    ok3, reason = handle_command({"action": "enroll", "course": "py",
                                  "student": "carol"}, events)
    assert (ok1, ok2) == (True, True) and ok3 is False, reason
    assert reason == "课程已满"
    handle_command({"action": "cancel", "course": "py",
                    "student": "bob"}, events)
    # 写入已落库,但读模型还是上次投影的旧值 —— 最终一致
    stale = {"py": {"students": ["alice", "bob"], "count": 2}}
    fresh = project(events)
    assert fresh == {"py": {"students": ["alice"], "count": 1}}, fresh
    assert stale != fresh
    # 查询只读投影,不碰事件日志:读路径廉价可缓存
    assert fresh["py"]["students"] == ["alice"]
    print("命令侧拒绝:", reason)
    print("事件日志:", events)
    print("投影后读模型:", fresh, "(bob 已取消,carol 未占座)")


if __name__ == "__main__":
    main()
