"""zoneinfo:标准库时区的构造、换算与比较规则。"""
from datetime import datetime
from zoneinfo import ZoneInfo

SH = ZoneInfo("Asia/Shanghai")
NY = ZoneInfo("America/New_York")

if __name__ == "__main__":
    naive = datetime(2026, 1, 15, 9, 0)
    sh = naive.replace(tzinfo=SH)
    ny = sh.astimezone(NY)
    print("上海:", sh, "offset", sh.utcoffset())
    print("纽约:", ny, "offset", ny.utcoffset())

    print("aware 比较按绝对时刻:", sh < datetime(2026, 1, 15, 23, 0, tzinfo=SH))

    try:
        sh < naive
    except TypeError as exc:
        print("naive 与 aware 不可比较:", exc)

    utc = sh.astimezone(ZoneInfo("UTC"))
    print("统一到 UTC 再运算:", utc)
