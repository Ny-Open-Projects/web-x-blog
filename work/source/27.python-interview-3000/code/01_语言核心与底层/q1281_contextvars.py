import contextvars
import threading

request_id = contextvars.ContextVar("request_id", default="none")


def worker(tag):
    print(tag, "sees:", request_id.get())


def handle(rid):
    token = request_id.set(rid)
    try:
        worker("inside handle")            # 同一线程内可见
    finally:
        request_id.reset(token)            # 精确回滚,不留污染


if __name__ == "__main__":
    handle("req-1")
    worker("main thread after reset")
    t = threading.Thread(target=worker, args=("other thread",))
    t.start()
    t.join()                               # 线程不继承:拿到 default
    ctx = contextvars.copy_context()
    print("explicit copy_context().run:", ctx.run(request_id.get))
