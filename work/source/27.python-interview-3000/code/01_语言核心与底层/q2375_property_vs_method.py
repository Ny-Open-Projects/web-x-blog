"""property 还是方法:按成本、副作用与失败可能性决定。"""
import time


class Report:
    def __init__(self, rows):
        self.rows = rows

    @property
    def count(self):
        """便宜、无副作用,像字段。"""
        return len(self.rows)

    def stats(self, window):
        """带参数、有计算成本,是动作。"""
        return sum(self.rows[-window:]) / min(window, len(self.rows))

    @property
    def slow_summary(self):
        """反例:property 里做重活。"""
        time.sleep(0.05)
        return sum(self.rows)


class Temperature:
    def __init__(self):
        self._c = 20

    @property
    def celsius(self):
        return self._c

    @celsius.setter
    def celsius(self, v):
        if v < -273.15:
            raise ValueError("低于绝对零度")
        self._c = v


if __name__ == "__main__":
    rep = Report(list(range(100)))
    print("count 像字段:", rep.count)
    print("stats 是动作:", rep.stats(5))

    t0 = time.perf_counter()
    _ = rep.slow_summary
    print(f"property 重活耗时: {time.perf_counter() - t0:.3f}s")

    t = Temperature()
    t.celsius = 25
    print("setter 校验后:", t.celsius)
    try:
        t.celsius = -300
    except ValueError as exc:
        print("setter 拒绝:", exc)
