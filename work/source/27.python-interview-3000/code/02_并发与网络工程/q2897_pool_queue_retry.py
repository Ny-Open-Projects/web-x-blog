# -*- coding: utf-8 -*-
"""线程池 + 队列 + 重试的组合模板。

- 入口队列: 生产者只管投递, 有界队列天然形成背压;
- 工作池: N 个线程从队列取任务, 单个任务失败不拖垮别的任务;
- 重试: 按异常分类决定重试或直接死信, 退避用指数序列;
- 收尾: 哨兵值关门, 对账成功/重试/死信三本账。
"""
import queue
import threading
import time

SENTINEL = None            # 关门哨兵: 每个工作线程一个
N_WORKERS = 4
MAX_RETRY = 3
BASE_DELAY = 0.02          # 指数退避基数, 演示用小值

# 确定性失败计划: (任务号, 第几次尝试) -> 必失败
FAIL_PLAN = {(3, 1), (7, 1), (7, 2)}

intake = queue.Queue(maxsize=64)   # 有界队列 = 背压
dead = queue.Queue()               # 死信队列 DLQ
stats = {"ok": 0, "retried": 0, "dead": 0}
slock = threading.Lock()


def flaky(task_id, attempt):
    """模拟不稳定任务: 按计划表失败, 11 号是永远修不好的毒任务。"""
    if (task_id, attempt) in FAIL_PLAN:
        raise IOError("transient failure")
    if task_id == 11:
        raise ValueError("poison task")
    return True


def worker(wid):
    while True:
        item = intake.get()
        if item is SENTINEL:
            intake.task_done()
            break
        task_id, payload = item
        attempt, done = 0, False
        while attempt < MAX_RETRY:
            attempt += 1
            try:
                flaky(task_id, attempt)
                with slock:
                    stats["ok"] += 1
                    if attempt > 1:
                        stats["retried"] += 1
                done = True
                break
            except (IOError, OSError) as exc:      # 可重试类: 指数退避
                if attempt == MAX_RETRY:
                    dead.put((task_id, repr(exc)))
                    break
                time.sleep(BASE_DELAY * (2 ** (attempt - 1)))
            except ValueError as exc:              # 致命类: 不重试直接死信
                dead.put((task_id, repr(exc)))
                break
        if not done:
            with slock:
                stats["dead"] += 1
        intake.task_done()


if __name__ == "__main__":
    workers = [threading.Thread(target=worker, args=(i,), daemon=True)
               for i in range(N_WORKERS)]
    for t in workers:
        t.start()
    for i in range(1, 13):                 # 12 个任务, 11 号是毒任务
        intake.put((i, "payload-%d" % i))
    for _ in workers:
        intake.put(SENTINEL)
    intake.join()                          # 等全部条目(含哨兵)处理完
    for t in workers:
        t.join(timeout=2)

    ok, retried, n_dead = stats["ok"], stats["retried"], stats["dead"]
    print("对账: 成功 %d (重试后成功 %d), 死信 %d" % (ok, retried, n_dead))
    print("死信明细:", sorted(dead.queue))
    # 3 号失败一次后成功; 7 号失败两次第三次成功; 11 号进死信
    assert (ok, retried, n_dead) == (11, 2, 1), stats
    assert sorted(k for k, _ in dead.queue) == [11]
    print("要点: 队列解耦投递与执行, 重试按异常分类, 次数用尽进 DLQ")
