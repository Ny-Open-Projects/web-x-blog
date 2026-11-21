import logging
import logging.handlers
import multiprocessing as mp

def worker(q, n):
    logger = logging.getLogger(f"worker{n}")
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.handlers.QueueHandler(q))
    for i in range(3):
        logger.info("来自 worker %s 的第 %s 条日志", n, i)

def start_listener(q):
    logging.basicConfig(level=logging.INFO, format="[统一写出] %(message)s")
    root = logging.getLogger()
    ql = logging.handlers.QueueListener(q, root.handlers[0])
    ql.start()
    return ql

if __name__ == "__main__":
    mp.set_start_method("spawn")
    q = mp.Queue()
    ql = start_listener(q)
    ps = [mp.Process(target=worker, args=(q, i)) for i in range(2)]
    for p in ps:
        p.start()
    for p in ps:
        p.join()
    q.put(None)      # 哨兵结束 listener
    ql.stop()        # stop 会排空剩余队列,保证不丢尾日志
    print("子进程只入队,主进程单点写盘")
