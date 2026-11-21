"""法定人数写入:N=5 W=3 R=3,分区后少数派两节点凑不齐 W 全部拒绝写,愈合后无脏数据。"""
class QuorumCluster:
    def __init__(self, nodes=5, w=3, r=3):
        self.w, self.r = w, r
        self.alive = set(range(nodes))
        self.data = {}

    def write(self, key, val, ver):
        if len(self.alive) < self.w:
            return {"ok": False, "reason": "存活 %d 不足写法定 %d" % (len(self.alive), self.w)}
        self.data[key] = {"val": val, "ver": ver}
        return {"ok": True, "ver": ver}

    def read(self, key):
        if len(self.alive) < self.r:
            return {"ok": False, "reason": "存活副本不足读法定"}
        rec = self.data.get(key)
        if rec is None:
            return {"ok": False, "reason": "not found"}
        return {"ok": True, "val": rec["val"], "ver": rec["ver"]}

    def partition(self, alive_subset):
        self.alive = set(alive_subset)

    def heal(self, majority_state):
        self.data = dict(majority_state)
        self.alive = set(range(5))


if __name__ == "__main__":
    c = QuorumCluster()
    r0 = c.write("plan", "v1", 1)
    assert r0["ok"], "全员存活写成功"
    c.partition({0, 1})
    rw = c.write("plan", "v1-minor", 2)
    assert not rw["ok"] and "不足写法定" in rw["reason"], "少数派凑不齐 W 拒绝写"
    assert not c.read("plan")["ok"], "少数派连读也不给 防旧值外泄"
    c.partition({2, 3, 4})
    assert c.write("plan", "v2", 2)["ok"], "多数派照常服务"
    majority_state = dict(c.data)
    c.heal(majority_state)
    got = c.read("plan")
    assert got["val"] == "v2" and got["ver"] == 2, "愈合后全网只有多数派的版本"
    assert "v1-minor" not in str(c.data), "少数派从未写成 不存在脏数据"
    print("法定人数通过:少数派拒写拒读 多数派可用 愈合零脏数据")
