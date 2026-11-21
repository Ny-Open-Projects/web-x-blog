"""幂等消费的去重窗口:TTL 去重表在窗口内挡重复,过期放行并 LRU 限容。"""
from collections import OrderedDict


class DedupWindow:
    def __init__(self, ttl, capacity=1000):
        self.ttl = ttl
        self.capacity = capacity
        self.table = OrderedDict()      # msg_id -> expire_at
        self.dropped = 0

    def _evict(self, now):
        while self.table:
            msg_id, expire_at = next(iter(self.table.items()))
            if expire_at <= now:
                self.table.popitem(last=False)
            else:
                break
        while len(self.table) > self.capacity:
            self.table.popitem(last=False)

    def seen(self, msg_id, now):
        """True 表示窗口内见过该消息应跳过,False 表示首次应处理。"""
        self._evict(now)
        if msg_id in self.table:
            self.dropped += 1
            self.table.move_to_end(msg_id)
            self.table[msg_id] = now + self.ttl     # 重复投递也刷新窗口
            return True
        self.table[msg_id] = now + self.ttl
        self.table.move_to_end(msg_id)
        while len(self.table) > self.capacity:      # 插入后立即收敛到容量内
            self.table.popitem(last=False)
        return False


if __name__ == "__main__":
    dw = DedupWindow(ttl=60)
    assert dw.seen("m1", now=100) is False, "首次投递应处理"
    assert dw.seen("m1", now=130) is True, "窗口内重复投递应跳过"
    assert dw.dropped == 1

    # 窗口过期后放行:这是 at-least-once 的边界,下游要能容忍重放
    assert dw.seen("m1", now=200) is False, "过期后按新消息处理"

    # LRU 限容:容量 2,塞第三个挤掉最老的
    small = DedupWindow(ttl=1000, capacity=2)
    small.seen("a", 0)
    small.seen("b", 1)
    assert small.seen("a", 2) is True, "重复命中并刷新 LRU 位次"
    assert small.seen("c", 3) is False, "新消息正常入库"
    assert small.seen("b", 4) is False, "b 被挤出窗口,重复投递会被再处理"
    assert small.seen("b", 4) is True, "再处理后的 b 重新进入窗口去重"
    assert len(small.table) == 2, "容量约束始终成立"

    # 过期清理让表不会无限膨胀
    long = DedupWindow(ttl=10)
    for i in range(500):
        long.seen("m%d" % i, now=i)
    assert len(long.table) <= 11, "滚动时间窗下存量受 TTL 约束"
    print("去重窗口通过:窗口内挡重 复投刷窗,过期放行,LRU 与 TTL 双重限容")
