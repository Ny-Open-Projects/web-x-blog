import multiprocessing as mp

N = 300  # Manager 每次操作都是一次 IPC 往返, 且 macOS spawn 子进程很慢,
         # 进程数与规模都要小, 保证 25s 内跑完


def race_worker(d) -> None:
    """复合操作不加锁: 演示丢失更新。"""
    for _ in range(N):
        d["count"] = d.get("count", 0) + 1


def safe_worker(d, lock) -> None:
    for _ in range(N):
        with lock:
            d["count"] = d.get("count", 0) + 1


def nested_worker(d) -> None:
    inner = d["inner"]        # 反 pickle 出来的本地副本(普通 dict)!
    inner["hit"] = inner.get("hit", 0) + 1  # 改的是副本, 不回传


if __name__ == "__main__":
    with mp.Manager() as mgr:
        d1 = mgr.dict()
        ps = [mp.Process(target=race_worker, args=(d1,)) for _ in range(2)]
        for p in ps:
            p.start()
        for p in ps:
            p.join()
        print(f"无锁复合操作: {d1['count']} / 期望 {2 * N}")

        d2 = mgr.dict()
        lk = mgr.Lock()
        ps = [mp.Process(target=safe_worker, args=(d2, lk)) for _ in range(2)]
        for p in ps:
            p.start()
        for p in ps:
            p.join()
        print(f"加锁复合操作: {d2['count']} / 期望 {2 * N}")
        assert d2["count"] == 2 * N, "加锁复合操作不允许丢失更新"

        d3 = mgr.dict()
        d3["inner"] = {}  # 普通嵌套 dict
        # 注意: 传给子进程的只能是 Proxy/可 pickle 对象, Manager 本体
        # 持有 weakref 与进程句柄, 传 mgr 会 TypeError: cannot pickle 'weakref'
        p = mp.Process(target=nested_worker, args=(d3,))
        p.start()
        p.join()
        print("嵌套普通 dict 修改丢失:", d3["inner"] == {})

        d4 = mgr.dict()
        d4["inner"] = mgr.dict()  # 嵌套也要用代理
        p = mp.Process(target=nested_worker, args=(d4,))
        p.start()
        p.join()
        print("嵌套 Manager dict 生效:", d4["inner"].get("hit"))
        assert d4["inner"].get("hit") == 1
