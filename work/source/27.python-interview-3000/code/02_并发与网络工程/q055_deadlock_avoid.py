import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()
locks = {1: lock1, 2: lock2}


def acquire_sorted(ids: list[int]):
    # 统一按编号排序加锁, 破坏循环等待
    ordered = sorted(ids)
    for i in ordered:
        locks[i].acquire()
    return ordered


def release_all(ordered: list[int]) -> None:
    for i in reversed(ordered):
        locks[i].release()


def transfer(from_id: int, to_id: int) -> None:
    ordered = acquire_sorted([from_id, to_id])
    try:
        print(f"从账户 {from_id} 转到 {to_id}, 持锁顺序 {ordered}")
        time.sleep(0.05)
    finally:
        release_all(ordered)


if __name__ == "__main__":
    threads = [
        threading.Thread(target=transfer, args=(1, 2)),
        threading.Thread(target=transfer, args=(2, 1)),  # 反向转账也安全
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("无死锁完成")
