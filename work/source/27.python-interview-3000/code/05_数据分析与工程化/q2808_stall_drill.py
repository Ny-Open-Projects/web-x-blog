"""假死注入与看门狗恢复演练: 确定性时间线上的处置验证"""

WARN_AGE = 2   # 连续 2 拍无心跳 -> 告警
KICK_AGE = 3   # 连续 3 拍 -> 戳一下
KILL_AGE = 4   # 连续 4 拍 -> 判死重拉
STALL_FROM, STALL_TO = 4, 6  # 注入假死: 第 4 到 6 拍不写心跳, 第 7 拍被戳醒


def drill(ticks=9):
    last_hb, events = 0, []
    for t in range(1, ticks + 1):
        active = t <= STALL_FROM - 1 or t > STALL_TO
        if active:
            last_hb = t
        age = t - last_hb
        if age == 0:
            level = "OK"
        elif age < WARN_AGE:
            level = "OK"
        elif age < KICK_AGE:
            level = "WARN"
        elif age < KILL_AGE:
            level = "KICK"
        else:
            level = "KILL"
        events.append((t, age, level, active))
    return events


if __name__ == "__main__":
    print(" tick  心跳年龄  判定      worker")
    for t, age, level, active in drill():
        state = "写心跳" if active else "假死中"
        print(f"  {t:<4} {age:<7} {level:<9} {state}")
    events = drill()
    levels = {t: level for t, _, level, _ in events}
    first_warn = next(t for t, _, lv, _ in events if lv == "WARN")
    first_kick = next(t for t, _, lv, _ in events if lv == "KICK")
    recovered = levels.get(first_kick + 1)
    assert first_warn == 5, "假死始于第 4 拍, WARN 应出现在第 5 拍"
    assert first_kick == 6, "第 6 拍年龄到 3 应触发 KICK"
    assert recovered == "OK", "被戳后 worker 应在下一拍恢复心跳"
    assert not any(lv == "KILL" for _, _, lv, _ in events), "及时 KICK 后不应走到判死"
    assert levels[STALL_FROM - 1] == "OK", "假死前一切正常"
    print("要点: 演练把处置阈值走一遍, WARN 给观察窗, KICK 给自愈机会, KILL 永远是最后一步")
