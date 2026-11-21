from itertools import takewhile, dropwhile

LOG = [
    "09:00 boot ok",
    "09:05 deploy start",
    "09:10 deploy done",
    "09:15 alarm cpu",
    "09:20 alarm mem",
]


def logs_before(deadline):
    """有序流前缀截断:deadline 之前的行。"""
    return list(takewhile(lambda line: line[:5] < deadline, LOG))


def strip_comments(lines):
    """dropwhile 剥离开头连续注释,之后的行全部保留。"""
    return list(dropwhile(lambda line: line.startswith("#"), lines))


if __name__ == "__main__":
    print("before 09:12:")
    for line in logs_before("09:12"):
        print("  ", line)

    src = ["# config", "# generated", "host=db", "# comment inside", "port=5432"]
    print("after dropwhile:", strip_comments(src))

    # 与 filter 的差异:filter 跳过不合格项继续,takewhile 一旦停机就结束
    alarms = [line for line in LOG if "alarm" in line]
    print("filter finds alarms:", alarms)
    print("takewhile stops early:",
          list(takewhile(lambda l: "alarm" not in l, LOG)))

    # 迭代器不可回卷:takewhile 消费过的部分拿不回来
    it = iter(LOG)
    prefix = list(takewhile(lambda l: l < "09:16", it))
    print("prefix size:", len(prefix), "| remaining:", list(it))
