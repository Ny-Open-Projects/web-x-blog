"""Q2871 有界重排的批处理:数量上限与时限上限双触发。

下游按批处理最高效,但上游不能无限等:攒够 max_size 立刻发,攒不够
但最老一条等满 max_wait 也要发——两个条件谁先到谁触发,尾事件永远
不会被无限拖延,吞吐与时延各有一道上限。
"""


def run_batcher(arrivals, max_size, max_wait):
    """arrivals: [(tick, item)],返回 [(tick, items, reason)]。"""
    buffer = []
    first_tick = None
    flushes = []
    for tick, item in arrivals:
        if not buffer:
            first_tick = tick
        buffer.append(item)
        if len(buffer) >= max_size:
            flushes.append((tick, buffer[:], "size"))
            buffer, first_tick = [], None
        elif tick - first_tick >= max_wait:
            flushes.append((tick, buffer[:], "time"))
            buffer, first_tick = [], None
    if buffer:
        flushes.append((arrivals[-1][0], buffer[:], "drain"))
    return flushes


def main():
    # 场景一:量不够,时限先到
    arrivals1 = [(1, "a"), (2, "b"), (3, "c"), (20, "d")]
    out1 = run_batcher(arrivals1, max_size=5, max_wait=2)
    assert out1 == [(3, ["a", "b", "c"], "time"),
                    (20, ["d"], "drain")], out1
    # 场景二:时限没到,数量先满
    arrivals2 = [(1, "a"), (1, "b"), (2, "c"), (2, "d"), (2, "e")]
    out2 = run_batcher(arrivals2, max_size=5, max_wait=10)
    assert out2 == [(2, ["a", "b", "c", "d", "e"], "size")], out2
    # 场景三:混合,两种触发加收尾冲刷交替出现
    arrivals3 = [(1, "a"), (2, "b"), (3, "c"), (4, "d"), (6, "e"),
                 (30, "g")]
    out3 = run_batcher(arrivals3, max_size=3, max_wait=2)
    reasons = [r for _, _, r in out3]
    assert reasons == ["size", "time", "drain"], reasons
    print("时限触发:", out1[0])
    print("数量触发:", out2[0])
    print("混合场景触发序列:", reasons)


if __name__ == "__main__":
    main()
