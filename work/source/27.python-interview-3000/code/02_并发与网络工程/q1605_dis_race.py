"""竞态的微观镜头: dis 看自增的字节码窗口。

counter[0] += 1 不是一条指令, 而是一串字节码:
LOAD_FAST -> LOAD_CONST(0) -> BINARY_SUBSCR -> LOAD_CONST(1)
-> INPLACE_ADD -> STORE_SUBSCR。
GIL 保证"单条字节码"原子, 但这六步之间任何一次切换都会丢更新。
限流计数器差一次就是放过一个超限请求, 所以计数必须加锁或换原子结构。
"""
import dis
import threading


def incr_plain(cell):
    cell[0] += 1


def show_bytecode():
    print("incr_plain 的字节码:")
    for ins in dis.get_instructions(incr_plain):
        print("  %-16s %s" % (ins.opname, ins.argrepr))


OPS = 50000
TRIALS = 5


def race_once(with_lock):
    cell = [0]
    lock = threading.Lock() if with_lock else None

    def worker():
        for _ in range(OPS):
            if lock:
                with lock:
                    cell[0] += 1
            else:
                cell[0] += 1            # 六步字节码之间存在切换窗口

    ts = [threading.Thread(target=worker) for _ in range(2)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    return cell[0]


def main():
    show_bytecode()
    expected = 2 * OPS
    lost_rounds = []
    for i in range(TRIALS):
        got = race_once(False)
        if got != expected:
            lost_rounds.append((got, expected - got))
            print("无锁第 %d 轮: 期望 %d 实得 %d, 丢失 %d 次更新"
                  % (i + 1, expected, got, expected - got))
    locked = race_once(True)
    print("加锁一轮: 期望 %d 实得 %d" % (expected, locked))
    assert locked == expected, "加锁后的计数必须分毫不差"
    if lost_rounds:
        print("结论: %d/5 轮出现丢失——字节码间隙就是竞态窗口" % len(lost_rounds))
    else:
        print("本轮未复现丢失(切换未落在窗口内), 但窗口客观存在, 加锁是唯一保证")


if __name__ == "__main__":
    main()
