import concurrent.futures
import time


def make_task(n: int) -> float:
    return 0.01 if n % 5 else 0.03  # 少量慢任务


def drain_all(jobs: int) -> int:
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        futs = [pool.submit(time.sleep, make_task(i)) for i in range(jobs)]
        concurrent.futures.wait(futs)
        return sum(1 for f in futs if f.done() and not f.cancelled())


def cancel_queued(jobs: int) -> tuple:
    pool = concurrent.futures.ThreadPoolExecutor(max_workers=4)
    futs = [pool.submit(time.sleep, make_task(i)) for i in range(jobs)]
    time.sleep(0.02)                   # 先让 4 个任务跑起来
    pool.shutdown(wait=True, cancel_futures=True)
    done = sum(1 for f in futs if f.done() and not f.cancelled())
    cancelled = sum(1 for f in futs if f.cancelled())
    return done, cancelled


if __name__ == "__main__":
    jobs = 40
    full = drain_all(jobs)
    print(f"排空式关闭: 完成 {full}/{jobs}, 一个不丢")
    done, cancelled = cancel_queued(jobs)
    print(f"取消式关闭: 完成 {done} 个(含在跑的), 排队取消 {cancelled} 个")
    assert done + cancelled == jobs, "每个 Future 必有终态"
    print("排空/取消语义验证通过")
