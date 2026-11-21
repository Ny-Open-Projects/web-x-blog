"""向量时钟对比版本向量:前者判任意事件间的因果,后者只管同一对象的副本版本。"""


def vc_tick(clock, node):
    clock[node] = clock.get(node, 0) + 1
    return dict(clock)


def vc_merge(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = max(out.get(k, 0), v)
    return out


def vc_compare(a, b):
    """2 相等  -1 a 先于 b  1 b 先于 a  0 并发。"""
    if a == b:
        return 2
    keys = set(a) | set(b)
    a_le = all(a.get(k, 0) <= b.get(k, 0) for k in keys)
    b_le = all(b.get(k, 0) <= a.get(k, 0) for k in keys)
    if a_le:
        return -1
    if b_le:
        return 1
    return 0


class VersionVector:
    """同一对象在副本上的版本向量:本副本 put 自增,同步取 max。"""

    def __init__(self):
        self.vv = {}

    def local_put(self, replica):
        self.vv[replica] = self.vv.get(replica, 0) + 1

    def sync(self, other_vv):
        for k, v in other_vv.items():
            self.vv[k] = max(self.vv.get(k, 0), v)

    def compare(self, other_vv):
        return vc_compare(self.vv, dict(other_vv))


if __name__ == "__main__":
    # 向量时钟:B 收到 A 的事件后,B 的一切都后于 A 的那个事件
    ea = vc_tick({}, "A")
    eb = vc_merge(vc_tick({}, "B"), ea)      # B 观察到 A 的事件
    assert vc_compare(ea, eb) == -1, "B 见过 A 的事件,B 后于 A"

    # 两个副本互不知情地各自前跳:并发,谁也不比谁新
    ca = vc_tick({}, "A")
    cb = vc_tick({}, "B")
    assert vc_compare(ca, cb) == 0, "互不知情的事件是并发"
    merged = vc_merge(ca, cb)
    assert vc_compare(merged, ca) == 1 and vc_compare(merged, cb) == 1

    # 版本向量:同一对象的两个副本,谁领先一目了然
    va = VersionVector()
    va.local_put("r1")
    va.local_put("r1")
    vb = VersionVector()
    vb.sync(va.vv)
    assert vb.compare(va.vv) == 2, "同步后版本一致"
    va.local_put("r1")
    assert vb.compare(va.vv) == -1, "r1 多写一次,r2 的副本已落后"
    vb.sync(va.vv)
    assert vb.compare(va.vv) == 2

    # 版本向量视角的写冲突:r1 与 r2 各写各的,互为并发
    vc1 = VersionVector()
    vc1.local_put("r1")
    vc2 = VersionVector()
    vc2.local_put("r2")
    assert vc2.compare(vc1.vv) == 0, "分叉写必须判并发交给冲突处理"
    print("双时钟通过:因果判先后 独立判并发,版本向量同步取 max 分叉判冲突")
