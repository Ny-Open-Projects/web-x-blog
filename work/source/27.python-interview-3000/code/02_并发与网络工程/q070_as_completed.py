import random
import time
from concurrent.futures import ThreadPoolExecutor, as_completed


def task(i: int) -> int:
    delay = random.uniform(0.1, 0.5)
    time.sleep(delay)
    return i


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=5) as pool:
        futures = {pool.submit(task, i): i for i in range(5)}
        for fut in as_completed(futures):
            print(f"任务 {futures[fut]} 先完成, 结果 {fut.result()}")
    print("注意完成顺序与提交顺序无关")
