import threading
import time

sem = threading.BoundedSemaphore(3)  # 最多 3 个并发


def access(i: int) -> None:
    with sem:
        print(f"任务 {i} 获得名额, 当前并发上限内")
        time.sleep(0.2)
    print(f"任务 {i} 释放名额")


if __name__ == "__main__":
    threads = [threading.Thread(target=access, args=(i,)) for i in range(8)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("全部任务完成")
