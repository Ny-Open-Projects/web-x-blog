"""读修复:读多副本对版本,取最新回写落后副本,修复计数可观测。"""


class Replica:
    def __init__(self, name):
        self.name = name
        self.data = {}                           # key -> (version, value)

    def put(self, key, version, value):
        cur = self.data.get(key)
        if cur is None or version > cur[0]:      # 旧版本写不覆盖新
            self.data[key] = (version, value)

    def get(self, key):
        return self.data.get(key)


class RepairableStore:
    """读 R 个副本,以最高版本为准,顺手把落后副本补齐。"""

    def __init__(self, replicas, read_quorum=2):
        self.replicas = replicas
        self.read_quorum = read_quorum
        self.repairs = 0

    def read(self, key):
        votes = []
        for r in self.replicas[:self.read_quorum]:
            v = r.get(key)
            if v is not None:
                votes.append((v[0], v[1], r))
        if not votes:
            return None
        best_version, value, _ = max(votes, key=lambda x: x[0])
        for r in self.replicas:                  # 全量回写:落后副本被修复
            cur = r.get(key)
            if cur is None or cur[0] < best_version:
                r.put(key, best_version, value)
                self.repairs += 1
        return {"value": value, "version": best_version}


if __name__ == "__main__":
    r0, r1, r2 = Replica("r0"), Replica("r1"), Replica("r2")
    r0.put("k", 3, "v3")                         # 写请求只落到部分副本
    r1.put("k", 2, "v2")
    r2.put("k", 1, "v1")
    store = RepairableStore([r0, r1, r2], read_quorum=2)

    got = store.read("k")
    assert got == {"value": "v3", "version": 3}, "读时以最高版本为准"
    assert store.repairs == 2, "两个落后副本被读路径顺手修复"
    assert r1.get("k") == (3, "v3") and r2.get("k") == (3, "v3")

    before = store.repairs
    store.read("k")
    assert store.repairs == before, "收敛后读不再产生修复,修复幂等"

    r1.put("k", 1, "ancient")                    # 旧版本写无法覆盖新版本
    assert r1.get("k") == (3, "v3")
    assert RepairableStore([Replica("r9")]).read("nope") is None
    print("读修复通过:读法定版本取新,落后副本回写收敛,旧写入不回退")
