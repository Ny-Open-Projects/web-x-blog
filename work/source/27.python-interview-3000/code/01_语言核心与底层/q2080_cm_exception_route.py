"""@contextmanager 的异常路由:yield 处是被注入异常的入口。"""
import contextlib


@contextlib.contextmanager
def checked(tag):
    print(f"[{tag}] 进入")
    try:
        yield "resource"           # with 体的异常从这里注入生成器
    except ValueError:
        print(f"[{tag}] 捕获 ValueError,选择吞掉")
        # 不重新抛出 == __exit__ 返回 True,异常被抑制
    finally:
        print(f"[{tag}] 清理:无论路由结果如何都执行")


@contextlib.contextmanager
def passing(tag):
    try:
        yield "resource"
    finally:
        print(f"[{tag}] 清理后放行异常")
    # 生成器不吞:异常在 yield 处穿出,继续向外传播


if __name__ == "__main__":
    with checked("吞异常型") as r:
        print("拿到资源:", r)
        raise ValueError("坏值")
    print("with 体之后继续执行,异常没有穿出\n")

    try:
        with passing("放行型"):
            raise KeyError("缺失键")
    except KeyError as e:
        print("异常穿出 with:", e)
