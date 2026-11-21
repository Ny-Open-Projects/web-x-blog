import threading
import time


def worker(seconds: float) -> None:
    time.sleep(seconds)
    print(f"耗时 {seconds}s 的任务完成")


if __name__ == "__main__":
    threads = [threading.Thread(target=worker, args=(s,)) for s in (0.3, 0.6)]
    for t in threads:
        t.start()
    for t in threads:
        t.join(timeout=0.5)
        if t.is_alive():
            print(f"{t.name} 超时仍未结束, 不再等待")
    print("主线程收尾")
