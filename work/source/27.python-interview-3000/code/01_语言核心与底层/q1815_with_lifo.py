"""with 多项嵌套的清理顺序:LIFO 与抑制边界。"""


class Tracer:
    def __init__(self, name, fail_enter=False):
        self.name = name
        self.fail_enter = fail_enter

    def __enter__(self):
        if self.fail_enter:
            raise RuntimeError(self.name + " 进入失败")
        print("enter " + self.name)
        return self

    def __exit__(self, exc_type, exc, tb):
        seen = exc_type.__name__ if exc_type else "无"
        print("exit  " + self.name + " | 顺带看到异常: " + seen)
        return False                     # 不抑制


def order_demo():
    with Tracer("外层"), Tracer("内层"):
        print("body 执行")


def body_error_order():
    try:
        with Tracer("外层"), Tracer("内层"):
            raise ValueError("业务异常")
    except ValueError as e:
        print("捕获:", e)


def enter_fail_still_cleans():
    # 第二个 CM 的 __enter__ 失败:第一个已进入,仍会收到清理机会
    try:
        with Tracer("外层"), Tracer("内层", fail_enter=True):
            print("body 不会执行")
    except RuntimeError as e:
        print("捕获:", e)


if __name__ == "__main__":
    print("--- 正常路径:进入顺序 A-B,退出顺序 B-A ---")
    order_demo()
    print("--- 体异常:先出内层再出外层,异常最后交给外层 ---")
    body_error_order()
    print("--- 第二个 enter 失败:第一个仍被清理 ---")
    enter_fail_still_cleans()
