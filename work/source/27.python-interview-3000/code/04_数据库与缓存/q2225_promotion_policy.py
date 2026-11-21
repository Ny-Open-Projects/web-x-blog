"""冷热晋升判定: 频次加新近度, 体积预算把关"""

class HotTracker:
    """滑动窗口内计数, 达标晋升, 跌破降级"""
    def __init__(self, window, threshold):
        self.window = window
        self.threshold = threshold
        self.hits = {}
        self.hot = set()

    def touch(self, key, now):
        h = self.hits.setdefault(key, [])
        h.append(now)
        while h and h[0] < now - self.window:
            h.pop(0)
        if len(h) >= self.threshold:
            if key not in self.hot:
                self.hot.add(key)
                return "晋升"
            return "维持"
        if key in self.hot:
            self.hot.discard(key)
            return "降级"
        return "冷"

tracker = HotTracker(window=100, threshold=3)
events = [("item-a", 1), ("item-a", 3), ("item-a", 5),
          ("item-b", 10), ("item-b", 80), ("item-a", 200)]
for key, now in events:
    print("t=%-4d touch %-7s -> %s  窗口内命中=%d" % (now, key, tracker.touch(key, now),
                                                     len(tracker.hits[key])))
print("item-a 当前热:", "item-a" in tracker.hot, " item-b 当前热:", "item-b" in tracker.hot)

def promote_cost_ok(value_bytes, budget_kb=64):
    return value_bytes <= budget_kb * 1024
print("8KB 对象可进 L1:", promote_cost_ok(8 * 1024), " 512KB 对象超预算:",
      promote_cost_ok(512 * 1024))
print("晋升三要素: 窗口频次 单对象体积预算 失效成本, 跌破阈值要能降级")
