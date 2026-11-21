import threading
import time

store = {"snapshot": tuple()}  # 只做原子引用替换
writer_lock = threading.Lock()  # 仅写者互斥
inconsistencies = [0]


def writer() -> None:
    for i in range(200):
        new_snapshot = tuple(range(i % 64))  # 构建完整新版本
        with writer_lock:
            store["snapshot"] = new_snapshot  # 原子发布
        time.sleep(0.001)


def reader(idx: int) -> None:
    for _ in range(2000):
        snap = store["snapshot"]  # 无锁读引用
        # 不可变快照: 一致性由构造完整性保证
        if len(snap) > 1 and list(snap) != list(range(len(snap))):
            inconsistencies[0] += 1  # 理论上不可能
        time.sleep(0)


if __name__ == "__main__":
    ts = [threading.Thread(target=writer)]
    ts += [threading.Thread(target=reader, args=(i,)) for i in range(6)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    print(f"读者读到不一致快照的次数: {inconsistencies[0]} (期望 0)")
    print(f"最终版本大小: {len(store['snapshot'])}")
