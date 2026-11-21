import queue
import threading


class TaskQueue:
    def __init__(self, workers: int = 2):
        self.q: queue.Queue = queue.Queue(maxsize=100)
        self.workers: list[threading.Thread] = []
        for i in range(workers):
            t = threading.Thread(target=self._run, name=f"worker-{i}")
            t.start()
            self.workers.append(t)

    def submit(self, fn, *args, **kwargs) -> None:
        self.q.put((fn, args, kwargs))  # 队列满时自动阻塞,形成背压

    def _run(self) -> None:
        while True:
            item = self.q.get()
            if item is None:      # 哨兵:退出信号
                self.q.task_done()
                break
            fn, args, kwargs = item
            try:
                fn(*args, **kwargs)
            except Exception as exc:
                print(f"[error] task failed: {exc}")
            finally:
                self.q.task_done()

    def shutdown(self) -> None:
        for _ in self.workers:
            self.q.put(None)
        for t in self.workers:
            t.join()


if __name__ == "__main__":
    tq = TaskQueue(workers=2)
    tq.submit(print, "send email")
    tq.submit(print, "generate report")
    tq.q.join()
    tq.shutdown()
