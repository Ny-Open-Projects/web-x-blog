import resource
import select
import socket
import time


def raise_limit() -> None:
    soft, hard = resource.getrlimit(resource.RLIMIT_NOFILE)
    if soft < hard:
        try:
            resource.setrlimit(resource.RLIMIT_NOFILE, (hard, hard))
        except (ValueError, PermissionError):
            pass


def bench(n_pairs: int) -> float:
    """n 个 fd 只有 1 个就绪, 测 select 单轮耗时。"""
    pairs = [socket.socketpair() for _ in range(n_pairs)]
    readers = [a for a, _ in pairs]
    writers = [b for _, b in pairs]
    writers[-1].send(b"x")  # 只唤醒最后一个

    rounds = 50
    t0 = time.perf_counter()
    for _ in range(rounds):
        r, _, _ = select.select(readers, [], [], 0)
        assert r
        r[0].recv(1)          # 消费数据
        writers[-1].send(b"x")  # 补上, 保持每轮都有就绪
    dt = (time.perf_counter() - t0) / rounds
    for a, b in pairs:
        a.close()
        b.close()
    return dt


if __name__ == "__main__":
    raise_limit()
    soft, _hard = resource.getrlimit(resource.RLIMIT_NOFILE)
    print(f"当前 fd 软限: {soft}")
    for n in (10, 50, 100, 200):
        max_pairs = min(n, soft // 2 - 16)
        if max_pairs < n:
            print(f"  n={n}: 受 fd 限制仅测 {max_pairs}")
            n = max_pairs
        dt = bench(n)
        print(f"  {n:>4} 个 fd, 1 个就绪: select 单轮 {dt * 1e6:7.1f} µs")
    print("扫描成本随 fd 数线性增长 — 这就是 select 的 O(n)")
