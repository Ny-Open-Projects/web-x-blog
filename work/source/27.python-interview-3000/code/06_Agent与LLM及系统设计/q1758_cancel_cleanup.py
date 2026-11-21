"""任务取消的资源回收:协作式取消令牌 + 资源登记簿,三条退出路径都兜底释放。"""


class CancelToken:
    def __init__(self):
        self._cancelled = False
        self.reason = None

    def cancel(self, reason="user requested"):
        if not self._cancelled:                  # 幂等:首个原因生效
            self._cancelled = True
            self.reason = reason

    @property
    def cancelled(self):
        return self._cancelled


class ResourceRegistry:
    """登记簿:逆序释放,后开先关,符合资源依赖顺序。"""

    def __init__(self):
        self.items = []

    def register(self, name, closer):
        self.items.append((name, closer))

    def close_all(self):
        closed = []
        while self.items:
            name, closer = self.items.pop()
            closer(name)
            closed.append(name)
        return closed


def run_task(token, registry, n_steps, cleanup_log, cancel_at=None, fail_at=None):
    try:
        for i in range(n_steps):
            if token.cancelled:                  # 协作式:每步前检查令牌
                break
            registry.register("res-%d" % i, lambda name: cleanup_log.append(name))
            if i == cancel_at:
                token.cancel("预算耗尽")
            if i == fail_at:
                raise RuntimeError("tool boom")
    finally:
        registry.close_all()
    return "cancelled" if token.cancelled else "done"


if __name__ == "__main__":
    tk, rg, log1 = CancelToken(), ResourceRegistry(), []
    assert run_task(tk, rg, 4, log1, cancel_at=2) == "cancelled"
    assert tk.reason == "预算耗尽"
    assert log1 == ["res-2", "res-1", "res-0"], "取消后已登记资源逆序全释放"
    tk.cancel("重复取消")
    assert tk.reason == "预算耗尽", "取消幂等:首个原因保留"

    tk2, rg2, log2 = CancelToken(), ResourceRegistry(), []
    blew = False
    try:
        run_task(tk2, rg2, 4, log2, fail_at=2)
    except RuntimeError:
        blew = True
    assert blew and log2 == ["res-2", "res-1", "res-0"], "异常路径同样释放全部资源"

    tk3, rg3, log3 = CancelToken(), ResourceRegistry(), []
    assert run_task(tk3, rg3, 3, log3) == "done"
    assert log3 == ["res-2", "res-1", "res-0"], "正常结束也统一释放"
    print("资源回收通过:取消 异常 正常三条路径都触发登记簿逆序释放")
