"""finally 里的 return/break/continue:会覆盖 try 的既定走向。"""


def with_break_in_finally():
    for i in range(3):
        try:
            if i == 1:
                continue
            print("  body:", i)
        finally:
            if i == 2:
                print("  finally 决定 break")
                break
    return "循环结束"


def with_return_in_finally():
    try:
        return "try 的返回"
    finally:
        return "finally 的返回"       # 覆盖前者


if __name__ == "__main__":
    print(with_break_in_finally())
    print(with_return_in_finally())

    log = []

    def clean_version():
        try:
            log.append("工作")
            return "结果"
        finally:
            log.append("清理")        # 只清理,不改控制流

    print(clean_version(), log)
