import multiprocessing
import os
import time


def worker(seconds: float) -> None:
    time.sleep(seconds)
    print(f"子进程 pid={os.getpid()} 完成耗时 {seconds}s 任务")


if __name__ == "__main__":
    print("主进程 pid =", os.getpid())
    procs = [multiprocessing.Process(target=worker, args=(0.3 + i * 0.1,)) for i in range(3)]
    for p in procs:
        p.start()
    for p in procs:
        p.join()
    print("所有子进程退出, exitcode:", [p.exitcode for p in procs])
