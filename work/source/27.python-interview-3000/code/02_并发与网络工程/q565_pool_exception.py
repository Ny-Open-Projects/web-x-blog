from concurrent.futures import ThreadPoolExecutor, as_completed
import threading


def bad_task(i: int) -> int:
    if i == 3:
        raise ValueError(f"任务 {i} 失败")
    return i * 10


def safe_submit(pool, fn, *args):
    """包装 submit: worker 内部先记日志, 异常继续存入 Future。"""

    def inner():
        try:
            return fn(*args)
        except Exception as e:
            print(f"[worker {threading.current_thread().name}] 捕获异常: {e!r}")
            raise

    return pool.submit(inner)


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=3) as pool:
        # 姿势一: as_completed 遍历时 result() 重新抛出
        futures = {pool.submit(bad_task, i): i for i in range(5)}
        for fut in as_completed(futures):
            try:
                print("结果:", fut.result())
            except ValueError as e:
                print("as_completed 收割到异常:", e)

    with ThreadPoolExecutor(max_workers=2) as pool:
        # 姿势二: done callback 统一检查
        def on_done(fut):
            exc = fut.exception()
            if exc is not None:
                print("回调发现异常:", repr(exc))

        fut = pool.submit(bad_task, 3)
        fut.add_done_callback(on_done)
        # 注意: result() 会把存入 Future 的异常原地重新抛出, 必须 try/except,
        # 否则演示脚本直接崩; 就算不收割, 回调里也会提前暴露。
        try:
            fut.result()
        except ValueError as e:
            print("主线程收割到异常:", e)
