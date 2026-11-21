"""accumulate:运行聚合、自定义 func 与 initial 初值。"""
import operator
from itertools import accumulate

if __name__ == "__main__":
    data = [3, 1, 4, 1, 5]

    print("前缀和:  ", list(accumulate(data)))
    print("前缀最大: ", list(accumulate(data, max)))
    print("前缀最小: ", list(accumulate(data, min)))
    print("累积乘:   ", list(accumulate(data, operator.mul)))
    print("带期初余额:", list(accumulate([-100, 50, -20], initial=1000)))

    # 惰性:可与生成器组合处理流
    stream = (x * 2 for x in data)
    print("流式前缀和首项:", next(accumulate(stream)))
