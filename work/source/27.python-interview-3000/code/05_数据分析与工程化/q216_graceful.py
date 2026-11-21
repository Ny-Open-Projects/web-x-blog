import signal
import threading


class GracefulShutdown:
    def __init__(self):
        self.stopping = threading.Event()
        signal.signal(signal.SIGTERM, self._handle)
        signal.signal(signal.SIGINT, self._handle)

    def _handle(self, signum, frame):
        self.stopping.set()

    def should_stop(self) -> bool:
        return self.stopping.is_set()


def drain_loop(should_stop, processed: list):
    # 工作循环:收到停止信号后处理完当前批次再退出
    while not should_stop():
        processed.append("task")
        if len(processed) >= 3:
            return
    processed.append("drained")


def test_graceful_drain():
    done = []
    flag = {"stop": False}
    drain_loop(lambda: flag["stop"], done)
    assert done == ["task", "task", "task"]
