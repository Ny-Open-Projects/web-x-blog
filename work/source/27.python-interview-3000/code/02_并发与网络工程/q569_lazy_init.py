import threading


class Config:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:  # 第一次检查: 无锁快速路径
            with cls._lock:
                if cls._instance is None:  # 第二次检查: 持锁确认
                    inst = super().__new__(cls)
                    inst.data = {"mode": "prod", "retries": 3}  # 先完成初始化
                    cls._instance = inst  # 最后才发布引用
        return cls._instance


results = []
start_gate = threading.Barrier(8)


def grab() -> None:
    start_gate.wait()
    results.append(Config())


if __name__ == "__main__":
    ts = [threading.Thread(target=grab) for _ in range(8)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    ids = {id(r) for r in results}
    print(f"8 个线程拿到 {len(ids)} 个实例, data 都已初始化:",
          all(r.data for r in results))
    assert len(ids) == 1
