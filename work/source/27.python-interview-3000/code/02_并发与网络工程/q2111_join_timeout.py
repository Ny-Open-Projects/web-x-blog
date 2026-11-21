# -*- coding: utf-8 -*-
"""Thread.join 的超时语义: join 只等不杀。

- join(timeout) 超时后正常返回 None, 线程还在跑, is_alive() 为 True;
- join 的返回值永远不携带线程结果, 拿结果要靠共享容器或 Future;
- 超时 join 不释放线程持有的任何资源, 只是把选择权还给调用方。
"""
import threading
import time


def quick_worker(box):
    time.sleep(0.2)
    box.append("quick-done")


def slow_worker(box):
    time.sleep(2.0)
    box.append("slow-done")


def main():
    box = []

    t1 = threading.Thread(target=quick_worker, args=(box,), name="quick")
    t1.start()
    print("join 0.5s:", t1.join(timeout=0.5), "alive:", t1.is_alive(), "box:", box)
    print("join 无限:", t1.join(), "alive:", t1.is_alive(), "box:", box)

    t2 = threading.Thread(target=slow_worker, args=(box,), name="slow")
    t2.start()
    t0 = time.monotonic()
    ret = t2.join(timeout=0.5)
    print("慢任务 join 0.5s: 返回 %r, 耗时 %.2fs, alive=%s" %
          (ret, time.monotonic() - t0, t2.is_alive()))
    # 超时后线程仍在跑: 它持有的时间与资源没有被释放
    t2.join()
    print("补上无限 join 后:", box, "alive:", t2.is_alive())

    # join(0) 相当于一次非阻塞的 is_alive 探测
    t3 = threading.Thread(target=lambda: None)
    t3.start()
    t3.join(timeout=0)
    print("join(0) 后 alive:", t3.is_alive())
    t3.join()


if __name__ == "__main__":
    main()
