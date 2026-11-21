import contextvars
import time

current_deadline = contextvars.ContextVar("deadline", default=None)


def remaining_ms() -> float:
    dl = current_deadline.get()
    return (dl - time.monotonic()) * 1000 if dl is not None else float("inf")


def enter_budget(own_ms: float):
    """子级预算 = min(父级剩余, 本级声明), 返回可恢复的 token。"""
    parent = remaining_ms()
    child = min(parent, own_ms)
    token = current_deadline.set(time.monotonic() + child / 1000)
    return token, parent, child


class DeadlineExceeded(Exception):
    pass


def stage(name: str, work_s: float, own_ms: float) -> str:
    token, parent, child = enter_budget(own_ms)
    try:
        rem = remaining_ms()
        need = work_s * 1000
        if rem < need:
            raise DeadlineExceeded(
                f"{name}: 剩余 {rem:.0f}ms < 需要 {need:.0f}ms, 快速放弃")
        time.sleep(work_s)
        return f"{name}: 耗时 {need:.0f}ms, 链上剩余 {remaining_ms():.0f}ms"
    finally:
        current_deadline.reset(token)


def main() -> None:
    token = current_deadline.set(time.monotonic() + 0.300)   # 入口: 总预算 300ms
    try:
        print("入口预算 300ms")
        print(stage("网关鉴权", 0.02, 100))
        print(stage("查用户服务", 0.08, 200))
        try:
            stage("查推荐服务", 0.25, 250)      # 剩余约 200ms < 需要 250ms
            print("推荐服务: 完成")
        except DeadlineExceeded as exc:
            print(f"第三级快速失败: {exc}")
            print("上游拿到部分结果 + 明确降级, 而不是 300ms 整体超时")
    finally:
        current_deadline.reset(token)

    start = time.monotonic()
    time.sleep(0.25)
    print(f"无预算传递对照: 白等 {(time.monotonic()-start)*1000:.0f}ms 才得到同样的失败")


if __name__ == "__main__":
    main()
