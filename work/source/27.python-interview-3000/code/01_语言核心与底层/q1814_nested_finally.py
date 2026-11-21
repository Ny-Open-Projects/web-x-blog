"""嵌套 finally 的 return:异常在哪一层静默消失。"""


def inner_swallows():
    try:
        try:
            raise ValueError("原始异常")
        finally:
            return "内层 finally 的 return 终止传播"   # 异常在这里被丢弃
    except ValueError:
        return "外层 except 还能接到吗?"                # 永远接不到


def cleanup_only():
    log = []
    try:
        try:
            raise ValueError("原始异常")
        finally:
            log.append("内层清理完成")                  # finally 不 return
    except ValueError as e:
        log.append("外层捕获:" + str(e))
    return log


def outer_finally_wins():
    log = []
    try:
        try:
            raise ValueError("原始异常")
        finally:
            log.append("内层 finally 执行")
    finally:
        log.append("外层 finally 也执行")
        return log + ["外层 finally 的 return 覆盖一切"]


if __name__ == "__main__":
    print(inner_swallows())
    print(cleanup_only())
    print(outer_finally_wins())
