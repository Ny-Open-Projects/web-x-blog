"""反熵对账:默克尔树逐层比对,根相同零传输,根不同下钻到差集最小同步。"""
import hashlib


def h(s):
    return hashlib.md5(s.encode()).hexdigest()


class MerkleTree:
    """叶子为 键加值 的哈希,两两向上聚合;奇数个叶子复制末位补齐。"""

    def __init__(self, items):
        self.keys = sorted(items)
        leaves = [h(k + "|" + items[k]) for k in self.keys]
        self.levels = [leaves]
        cur = leaves
        while len(cur) > 1:
            if len(cur) % 2 == 1:
                cur = cur + [cur[-1]]
            cur = [h(cur[i] + cur[i + 1]) for i in range(0, len(cur), 2)]
            self.levels.append(cur)

    def root(self):
        return self.levels[-1][0]

    def differing(self, other):
        """从根向下找叶子差异:每层只下钻哈希不同的子树。"""
        diffs = []
        self._walk(other, len(self.levels) - 1, 0, diffs)
        return sorted(diffs)

    def _walk(self, other, level, idx, diffs):
        if self.levels[level][idx] == other.levels[level][idx]:
            return                               # 子树一致:整棵跳过
        if level == 0:
            if idx < len(self.keys):
                diffs.append(self.keys[idx])
            return
        for child in (2 * idx, 2 * idx + 1):
            self._walk(other, level - 1, child, diffs)


if __name__ == "__main__":
    va = {"k%d" % i: "v%d" % i for i in range(1, 9)}
    vb = dict(va)
    vb["k3"], vb["k6"] = "stale3", "stale6"      # 两键取值分叉

    ta, tb = MerkleTree(va), MerkleTree(vb)
    assert ta.root() != tb.root(), "取值不同根必不同"
    assert ta.differing(tb) == ["k3", "k6"], "只下钻差异子树,精确到最小差集"

    transferred = 0
    for k in ta.differing(tb):
        vb[k] = va[k]
        transferred += 1
    tb2 = MerkleTree(vb)
    assert tb2.root() == ta.root(), "同步后根一致"
    assert ta.differing(tb2) == [], "二次对账零差异零传输"
    assert transferred == 2, "8 键对账只需传 2 个差异键"

    assert ta.differing(MerkleTree(dict(va))) == [], "同根子树整棵跳过"
    print("反熵对账通过:根不同下钻差集,仅同步 2 键,同步后根一致零传输")
