import threading
import time


def worker(name: str) -> None:
    print(f"线程 {name} 启动, thread_id={threading.get_ident()}")
    time.sleep(0.2)
    print(f"线程 {name} 结束")


class MyThread(threading.Thread):
    def run(self) -> None:
        worker(self.name)


if __name__ == "__main__":
    t1 = threading.Thread(target=worker, args=("t1",), name="worker-1")
    t2 = MyThread(name="worker-2")
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f"活跃线程数: {threading.active_count()}")
