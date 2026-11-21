"""用 concurrent.futures 并发执行多个 tool_call,结果按 id 顺序回填。"""
import time
from concurrent.futures import ThreadPoolExecutor


def fetch_price(item: str) -> str:
    time.sleep(0.1)  # 模拟网络 IO
    return f"{item}=99元"


def run_concurrent(calls: list[dict], max_workers: int = 3) -> list[dict]:
    results = [None] * len(calls)
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        future_map = {pool.submit(fetch_price, c["args"]["item"]): i
                      for i, c in enumerate(calls)}
        for fut in future_map:
            idx = future_map[fut]
            try:
                results[idx] = {"id": calls[idx]["id"],
                                "content": fut.result(timeout=2)}
            except Exception as exc:
                results[idx] = {"id": calls[idx]["id"],
                                "content": f"工具失败: {exc}"}
    return results


if __name__ == "__main__":
    calls = [{"id": f"call_{i}", "args": {"item": f"商品{i}"}} for i in range(6)]
    start = time.time()
    for r in run_concurrent(calls):
        print(r)
    print(f"串行需 0.6s,实际耗时 {time.time() - start:.2f}s")
