from __future__ import annotations

import threading
from concurrent.futures import ThreadPoolExecutor
from typing import Optional

_shared_pool: Optional[ThreadPoolExecutor] = None
_lock = threading.Lock()


def get_pool(max_workers: int = 8) -> ThreadPoolExecutor:
    # 错误做法:每次请求 with ThreadPoolExecutor 会让线程反复创建销毁
    # 正确做法:进程内共享一个池
    global _shared_pool
    with _lock:
        if _shared_pool is None:
            _shared_pool = ThreadPoolExecutor(
                max_workers=max_workers, thread_name_prefix="worker"
            )
    return _shared_pool


def test_pool_is_shared():
    p1 = get_pool()
    p2 = get_pool()
    assert p1 is p2
    names = [t.name for t in threading.enumerate()]
    assert all(not n.startswith("leak") for n in names)
