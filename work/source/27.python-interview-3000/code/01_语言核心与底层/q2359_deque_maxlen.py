"""deque 的 maxlen:自动淘汰的滚动窗口与滑动平均。"""
from collections import deque

if __name__ == "__main__":
    window = deque(maxlen=5)
    for i in range(8):
        window.append(i)
    print("只留最后 5 个:", list(window))

    w2 = deque([1, 2, 3], maxlen=3)
    w2.appendleft(0)
    print("appendleft 淘汰右端:", list(w2))

    w3 = deque(maxlen=3)
    w3.extend([10, 20, 30, 40, 50])
    print("extend 超量保留尾部:", list(w3))

    prices = [10, 11, 12, 13, 14, 15]
    ma = deque(maxlen=3)
    for p in prices:
        ma.append(p)
        print(f"price={p} window={list(ma)} avg={sum(ma) / len(ma):.2f}")
