import threading
import time


def heartbeat() -> None:
    while True:
        print("心跳...")
        time.sleep(0.1)


def task() -> None:
    time.sleep(0.5)
    print("task 完成")


if __name__ == "__main__":
    d = threading.Thread(target=heartbeat, daemon=True)
    t = threading.Thread(target=task, daemon=False)
    d.start()
    t.start()
    time.sleep(0.2)
    print("主线程即将退出, 守护线程被丢弃, 非守护线程会被 join")
    # 主线程结束时: task 线程会跑完, heartbeat 循环被直接终止
