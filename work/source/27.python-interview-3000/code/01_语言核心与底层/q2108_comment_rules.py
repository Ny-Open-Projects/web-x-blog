"""注释规范:注释写为什么,代码写是什么。"""


def bad(total):
    # total 加一              # 复述代码:零信息量
    return total + 1


def good(total):
    # +1 兼容旧账单的闭区间计数口径(2023 年前含首含尾统计)
    return total + 1


RETRY_LIMIT = 3               # 命名即文档:常量取代裸写 3
SECONDS_PER_DAY = 86400


if __name__ == "__main__":
    print("两个函数行为相同:", bad(10) == good(10))
    print("坏注释复述语法,好注释交代业务口径与历史约束")
    print("TODO 要可追踪:TODO(wang) 下线旧计费分支 - PAY-1024")
    print("分工:docstring 写接口契约,行内注释写实现取舍")
