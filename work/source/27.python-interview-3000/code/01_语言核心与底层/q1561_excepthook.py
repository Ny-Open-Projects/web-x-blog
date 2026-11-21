import sys
import threading

caught = []


def thread_hook(args):
    """threading.excepthook:参数是 exc_type 等组成的命名元组。"""
    caught.append((args.thread.name, args.exc_type.__name__, str(args.exc_value)))


def broken_worker():
    raise ValueError("worker 内部炸了, 线程将静默死亡")


if __name__ == "__main__":
    threading.excepthook = thread_hook          # 3.8+

    t = threading.Thread(target=broken_worker, name="poller")
    t.start()
    t.join()
    print("main thread still alive:", True)
    print("hook caught:", caught)

    # sys.excepthook:主线程未捕获异常的最后一站,签名 (type, value, tb)
    def main_hook(etype, evalue, tb):
        print("main hook would log:", etype.__name__, "-", evalue)

    original = sys.excepthook
    sys.excepthook = main_hook
    try:
        raise RuntimeError("simulate uncaught in main")
    except RuntimeError:
        etype, evalue, tb = sys.exc_info()
        sys.excepthook(etype, evalue, tb)   # 演示性调用;真实场景由解释器触发
    finally:
        sys.excepthook = original
