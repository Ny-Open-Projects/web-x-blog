"""极简 happens-before 检查器: 输入事件轨迹, 输出数据竞争。"""

Clock = dict[str, int]


def analyze(events: list[tuple[str, str, str]]) -> list[tuple]:
    vc: dict[str, Clock] = {}     # thread -> 向量时钟
    release_vc: dict[str, Clock] = {}  # lock -> 最近 release 发布的时钟
    last_access: dict[str, tuple] = {}  # var -> (thread, 时钟快照, 是否写)
    races = []

    for thread, op, obj in events:
        v = vc.setdefault(thread, {thread: 0})
        v[thread] += 1  # 事件发生先走一格时钟, 访问快照必须携带事件时间戳
        if op == "acquire":
            if obj in release_vc:          # 与上次释放者建立同步
                for t, c in release_vc[obj].items():
                    v[t] = max(v.get(t, 0), c)
        elif op == "release":
            release_vc[obj] = dict(v)      # 发布当前时钟
        elif op in ("read", "write"):
            if obj in last_access:
                prev_t, prev_v, prev_w = last_access[obj]
                if prev_t != thread and (prev_w or op == "write"):
                    # prev 是否 happens-before 当前: 当前线程必须"见过"
                    # prev 的事件时间戳。未见过用 -1 兜底, 0 表示"见过 0 号
                    # 事件", 拿 0 兜底会把未同步误判成同步, 竞争全漏报。
                    hb = v.get(prev_t, -1) >= prev_v.get(prev_t, -1)
                    if not hb:
                        races.append((prev_t, prev_w, thread, op, obj))
            last_access[obj] = (thread, dict(v), op == "write")
    return races


def show(label: str, events: list) -> None:
    races = analyze(events)
    print(f"--- {label}: {len(races)} 个数据竞争")
    for t1, w1, t2, op2, obj in races:
        print(f"  {t1} 的写 与 {t2} 的 {op2} 竞争同一变量 {obj}")


if __name__ == "__main__":
    # 有竞争轨迹: T1 写 x 后 T2 无同步写 x
    racy = [
        ("T1", "write", "x"),
        ("T2", "write", "x"),
        ("T1", "read", "x"),
    ]
    show("无锁轨迹", racy)

    # 无竞争轨迹: 每次访问都在临界区内(T1 的读也要持锁, 不持锁照样竞争)
    safe = [
        ("T1", "acquire", "L"), ("T1", "write", "x"), ("T1", "release", "L"),
        ("T2", "acquire", "L"), ("T2", "write", "x"), ("T2", "release", "L"),
        ("T1", "acquire", "L"), ("T1", "read", "x"), ("T1", "release", "L"),
    ]
    show("加锁轨迹", safe)
    assert len(analyze(safe)) == 0 and len(analyze(racy)) > 0
    print("向量时钟判定与直觉一致")
