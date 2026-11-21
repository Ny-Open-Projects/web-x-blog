import threading
import time

stop_event = threading.Event()
ready_event = threading.Event()


def worker() -> None:
    print("worker 启动, 等待就绪信号")
    ready_event.wait(timeout=2)
    print("worker 收到就绪信号, 开始干活")
    while not stop_event.is_set():
        time.sleep(0.1)
    print("worker 收到停止信号, 退出")


if __name__ == "__main__":
    t = threading.Thread(target=worker)
    t.start()
    time.sleep(0.2)
    ready_event.set()
    time.sleep(0.5)
    stop_event.set()
    t.join()
