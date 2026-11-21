import time
from concurrent.futures import ThreadPoolExecutor


def slow_task(n: int) -> int:
    time.sleep(0.2)
    if n == 2:
        raise ValueError("任务 2 故意失败")
    return n * 10


def on_done(fut) -> None:
    if fut.exception() is not None:
        print(f"回调: 任务失败 {fut.exception()!r}")
    else:
        print(f"回调: 任务成功, 结果 {fut.result()}")


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=3) as pool:
        futures = [pool.submit(slow_task, i) for i in range(4)]
        for fut in futures:
            fut.add_done_callback(on_done)
        # 阻塞等待全部结束
        results = [fut.result() if fut.exception() is None else None for fut in futures]
        print("收集结果:", results)
