import multiprocessing as mp
import os


def child(name: str) -> None:
    ctx = mp.get_start_method()
    print(f"[{name}] pid={os.getpid()} 启动方式={ctx}")


def run_with(ctx_name: str) -> None:
    ctx = mp.get_context(ctx_name)  # 显式选择启动方式
    p = ctx.Process(target=child, args=(ctx_name,))
    p.start()
    p.join()


def fork_demo_with_thread() -> None:
    """演示 fork 只复制当前线程: 子进程看到的线程数是 1。"""
    ctx = mp.get_context("fork")

    def background() -> None:
        pass

    t = threading.Thread(target=background, name="phantom")
    t.start()
    # fork 发生时 phantom 线程存在, 但子进程里它不存在
    p = ctx.Process(target=lambda: print("子进程 threading.active_count =",
                                         threading.active_count()))
    p.start()
    p.join()
    t.join()


if __name__ == "__main__":
    import threading  # 放在模块层避免 spawn 重复执行时缺名字

    available = mp.get_all_start_methods()
    print("平台支持:", available, "当前默认:", mp.get_start_method())
    for m in available:
        run_with(m)
    if "fork" in available:
        fork_demo_with_thread()
