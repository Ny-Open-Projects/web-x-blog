from multiprocessing import Pool
import os

_CONN = None  # 每个 worker 进程各自的全局"连接"


def init_worker() -> None:
    global _CONN
    _CONN = {"pid": os.getpid(), "opened_at": "startup", "queries": 0}
    print(f"[init] worker {os.getpid()} 建立连接")


def query(sql: str) -> dict:
    _CONN["queries"] += 1  # 同一 worker 的多个任务复用同一连接
    return {"sql": sql, "conn_pid": _CONN["pid"], "queries": _CONN["queries"]}


if __name__ == "__main__":
    with Pool(processes=2, initializer=init_worker) as pool:
        results = pool.map(query, [f"SELECT {i}" for i in range(8)])
    conn_pids = {r["conn_pid"] for r in results}
    print(f"8 个任务只用了 {len(conn_pids)} 个连接 (pid: {conn_pids})")
    for r in results[:4]:
        print(r)
