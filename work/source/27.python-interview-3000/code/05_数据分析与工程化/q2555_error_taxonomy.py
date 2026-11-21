"""错误分类统计: 一批运行的错误画像"""

from collections import Counter

ENTRIES = [
    ("orders_sync", "upstream", "源库连接拒绝"),
    ("orders_sync", "data", "金额字段出现非数字"),
    ("orders_sync", "data", "日期格式非法"),
    ("payments_sync", "data", "金额字段出现非数字"),
    ("payments_sync", "infra", "磁盘写满"),
    ("users_sync", "code", "KeyError: city"),
    ("users_sync", "upstream", "接口 503"),
    ("users_sync", "data", "手机号位数异常"),
    ("report_build", "infra", "对象存储超时"),
    ("report_build", "code", "TypeError 拼接"),
    ("report_build", "data", "空文件输入"),
    ("report_build", "upstream", "源库连接拒绝"),
]


def classify(entries):
    counts = Counter(cat for _, cat, _ in entries)
    total = sum(counts.values())
    return counts, total


if __name__ == "__main__":
    counts, total = classify(ENTRIES)
    print(f"运行错误 {total} 条, 分类画像:")
    for cat, n in counts.most_common():
        bar = "#" * n
        print(f"  {cat:<9} {n:2d} {n / total:5.0%} {bar}")
    top = counts.most_common(1)[0]
    print(f"头号问题: {top[0]} 类占 {top[1] / total:.0%}, 优先排班处理")
    assert top[0] == "data", "本批头号应是数据类错误"
    detail = Counter(msg for _, cat, msg in ENTRIES if cat == top[0])
    print("头号类内部: " + ", ".join(f"{m} x{n}" for m, n in detail.most_common()))
    print("要点: 先分类再统计, 治理顺序看占比; 同类内再聚重复消息, 一类错往往就是一个根因")
