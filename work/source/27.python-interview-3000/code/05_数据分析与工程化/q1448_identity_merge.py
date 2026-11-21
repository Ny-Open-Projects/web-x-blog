"""同人多账号合并:并查集做实体消解,按共享手机号/设备/邮箱连通"""

ACCOUNTS = [
    # account_id, 手机号, 设备, 邮箱
    ("a1", "13800000001", "devA", None),
    ("a2", None, "devA", "x@mail.com"),
    ("a3", "13800000002", "devB", "x@mail.com"),
    ("a4", "13800000003", "devC", None),
    ("a5", None, "devC", None),
]


class UnionFind:
    def __init__(self, items):
        self.parent = {x: x for x in items}

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]  # 路径压缩
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.parent[rb] = ra


def merge_accounts(accounts):
    uf = UnionFind([a[0] for a in accounts])
    key_index = {}  # 共享键 -> 任一账号
    for aid, phone, device, email in accounts:
        for key in ("phone:" + str(phone), "dev:" + str(device), "mail:" + str(email)):
            if key.endswith("None"):
                continue
            if key in key_index:
                uf.union(key_index[key], aid)
            else:
                key_index[key] = aid
    groups = {}
    for aid, *_ in accounts:
        groups.setdefault(uf.find(aid), []).append(aid)
    return sorted(sorted(g) for g in groups.values())


if __name__ == "__main__":
    for group in merge_accounts(ACCOUNTS):
        print("同一自然人:", group)
    print("线上还要解决合并后的指标口径:按'人'聚合时用组内代表键或维护映射表")
