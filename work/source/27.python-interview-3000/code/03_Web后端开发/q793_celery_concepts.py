import queue
import threading
import time

broker: queue.Queue = queue.Queue()
results: dict = {}

def worker(wid: int):
    while True:
        task = broker.get()
        if task is None:
            break
        name, args, task_id = task
        time.sleep(0.01)
        results[task_id] = f"{name} 完成 by worker-{wid} args={args}"
        broker.task_done()

threads = [threading.Thread(target=worker, args=(i,), daemon=True) for i in range(2)]
for t in threads:
    t.start()

def send_task(name: str, *args) -> str:   # producer 视角: 只投递不执行
    tid = f"{name}-1"
    broker.put((name, args, tid))
    return tid

tid = send_task("send_email", "a@b.c")
broker.join()
for _ in threads:
    broker.put(None)
for t in threads:
    t.join()
print(results[tid])
