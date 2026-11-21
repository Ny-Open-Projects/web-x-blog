"""Q2600 读租约的批量续期:一次 RPC 续一串,摊薄心跳开销。

租约多、心跳勤,逐个续期的 RPC 量线性爆炸;把临近到期的租约
攒成一批发一次批量请求,一次往返覆盖一串副本,续期次数从 k
降到 1,语义与逐个续期完全等价。
"""


def renew_individually(leases, now, threshold, ttl):
    rpc = 0
    for name in leases:
        if leases[name] - now < threshold:
            rpc += 1
            leases[name] = now + ttl
    return rpc


def renew_batch(leases, now, threshold, ttl):
    due = sorted(n for n in leases if leases[n] - now < threshold)
    if not due:
        return 0, []
    for n in due:
        leases[n] = now + ttl
    return 1, due   # 一次批量调用覆盖所有到期者


def main():
    now = 100.0
    l1 = {"r1": 102.0, "r2": 103.0, "r3": 108.0, "r4": 120.0}
    l2 = dict(l1)
    c1 = renew_individually(l1, now, threshold=5.0, ttl=20.0)
    c2, due = renew_batch(l2, now, threshold=5.0, ttl=20.0)
    assert c1 == 2 and c2 == 1, (c1, c2)
    assert due == ["r1", "r2"], due
    assert l1 == l2, "批量与逐个结果等价"
    c3, due3 = renew_batch(l2, now + 10, threshold=5.0, ttl=20.0)
    assert c3 == 1 and due3 == ["r3"], (c3, due3)   # 上轮没续的 r3 到期被补续
    print("逐个续期 RPC:", c1, "| 批量续期 RPC:", c2, "→ 省", c1 - c2, "次")
    print("本次批量覆盖:", due, "| 下轮补续:", due3, "← 未到期的不碰")


if __name__ == "__main__":
    main()
