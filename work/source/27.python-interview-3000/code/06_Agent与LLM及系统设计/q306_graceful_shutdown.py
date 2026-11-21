import signal
import threading
import time


class Server:
    def __init__(self):
        self.stop_event = threading.Event()
        self.inflight = 0
        self.lock = threading.Lock()

    def handle_signal(self, signum, frame):
        print(f"received signal {signum}, shutting down...")
        self.stop_event.set()  # 只置标志,不在这里做重活

    def serve(self):
        signal.signal(signal.SIGTERM, self.handle_signal)
        signal.signal(signal.SIGINT, self.handle_signal)
        n = 0
        while not self.stop_event.is_set():
            with self.lock:
                self.inflight += 1
            n += 1
            threading.Thread(target=self.handle_request, args=(n,),
                             daemon=True).start()
            time.sleep(0.1)
        self.drain()

    def handle_request(self, idx: int):
        time.sleep(0.3)  # 模拟请求处理
        with self.lock:
            self.inflight -= 1

    def drain(self, timeout: float = 5.0):
        deadline = time.time() + timeout
        while self.inflight > 0 and time.time() < deadline:
            time.sleep(0.05)
        print(f"drained, inflight={self.inflight}, server stopped")


if __name__ == "__main__":
    srv = Server()
    threading.Timer(0.4, lambda: signal.raise_signal(signal.SIGTERM)).start()
    srv.serve()
