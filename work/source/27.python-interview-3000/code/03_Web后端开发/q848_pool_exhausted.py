import queue
import threading
import time

pool: queue.Queue = queue.Queue(maxsize=2)
for _ in range(2):
    pool.put("conn")

def query(i: int, timeout: float = 0.05) -> str:
    try:
        conn = pool.get(timeout=timeout)     # 快速失败, 不无限排队
    except queue.Empty:
        return f"req{i}: 连接等待超时"
    time.sleep(0.08)                         # 慢查询长期占用连接
    pool.put(conn)
    return f"req{i}: ok"

results: list = []
threads = [threading.Thread(target=lambda i=i: results.append(query(i))) for i in range(4)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(sorted(results))
