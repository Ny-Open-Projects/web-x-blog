"""生成器流水线:读-解析-过滤-聚合全链路惰性求值,内存与输入规模无关"""

from io import StringIO

RAW = StringIO("city,amount\n华东,120\n华南,80\n华东,60\n华北,90\n华东,300\n华南,20\n")


def read_lines(fh):
    """跳过表头后逐行吐出"""
    for i, line in enumerate(fh):
        if i == 0:
            continue
        yield line.rstrip("\n")


def parse(rows):
    for line in rows:
        city, amount = line.split(",")
        yield city, int(amount)


def filter_big(rows, threshold=50):
    for city, amount in rows:
        if amount >= threshold:
            yield city, amount


def sum_by_city(rows):
    acc = {}
    for city, amount in rows:
        acc[city] = acc.get(city, 0) + amount
    return acc


if __name__ == "__main__":
    pipeline = filter_big(parse(read_lines(RAW)), 50)
    result = sum_by_city(pipeline)
    print("过滤后按城市求和:", dict(sorted(result.items())))
    print("要点:各段用 yield 串联,数据逐条流过不落地中间集合,到聚合器才收敛;内存 O(分组数) 而不是 O(行数),百 GB 文件也跑得动")
