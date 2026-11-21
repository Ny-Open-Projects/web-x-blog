import queue
import threading


class BatchFlipper:
    """聚合翻页双缓冲: 生产者写活动页, 满页翻给刷写线程。"""

    def __init__(self, threshold: int) -> None:
        self._threshold = threshold
        self._lock = threading.Lock()
        self._active = []            # 活动页
        self._pages = queue.Queue()  # 已翻出的整页
        self._closed = False
        self.flushed = []

    def add(self, item: int) -> None:
        page_out = None
        with self._lock:
            if self._closed:
                raise RuntimeError("已停止接收")
            self._active.append(item)
            if len(self._active) >= self._threshold:
                page_out = self._active   # 翻页: 旧页整体移交
                self._active = []         # 新页立刻接客
        if page_out is not None:
            self._pages.put(page_out)     # IO 队列在锁外

    def close_and_flush(self) -> None:
        with self._lock:
            self._closed = True
            residual = self._active
            self._active = []
        if residual:
            self._pages.put(residual)     # 半页也要翻出去
        self._pages.join()                # 等全部页刷完

    def flusher_loop(self) -> None:
        while True:
            page = self._pages.get()
            time.sleep(0.001)             # 模拟整页一次 IO
            self.flushed.extend(page)
            self._pages.task_done()


if __name__ == "__main__":
    import time
    buf = BatchFlipper(threshold=64)
    t = threading.Thread(target=buf.flusher_loop, daemon=True)
    t.start()
    for i in range(1000):
        buf.add(i)
    buf.close_and_flush()
    assert buf.flushed == list(range(1000)), "必须恰好刷出全部数据且保序"
    full_pages = 1000 // 64
    print(f"整页 {full_pages} 页 + 半页 1 页 = 刷出 {len(buf.flushed)} 条, 每页一次 IO")
