import threading
import time


class TaskManager:
    def __init__(self):
        self._tasks: dict[str, dict] = {}
        self._lock = threading.Lock()

    def submit(self, task_id: str, total: int, fn) -> None:
        self._tasks[task_id] = {"status": "running", "done": 0,
                                "total": total, "error": None}

        def runner():
            try:
                for i in range(total):
                    fn(i)
                    with self._lock:  # 进度写入线程安全
                        self._tasks[task_id]["done"] = i + 1
                self._tasks[task_id]["status"] = "done"
            except Exception as exc:
                self._tasks[task_id]["status"] = "failed"
                self._tasks[task_id]["error"] = str(exc)

        threading.Thread(target=runner, daemon=True).start()

    def query(self, task_id: str) -> dict:
        t = self._tasks[task_id]
        pct = round(t["done"] / t["total"] * 100) if t["total"] else 0
        return {**t, "percent": pct}


def work(step: int) -> None:
    time.sleep(0.05)  # 模拟处理一行数据


if __name__ == "__main__":
    tm = TaskManager()
    tm.submit("t1", 10, work)
    for _ in range(12):
        info = tm.query("t1")
        if info["status"] in ("done", "failed"):
            break
        time.sleep(0.1)
    print(tm.query("t1"))
