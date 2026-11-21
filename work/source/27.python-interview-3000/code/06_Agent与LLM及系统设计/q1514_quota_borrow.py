"""配额分配与回收:组织-团队-个人三层配额树,个人不足向团队借,周期结束归还并再平衡。"""


class QuotaNode:
    def __init__(self, name, quota):
        self.name, self.quota = name, quota
        self.used = 0
        self.borrowed = 0                  # 向父节点借来的额度
        self.children = {}
        self.parent = None

    def free(self):
        return self.quota + self.borrowed - self.used


class QuotaTree:
    """三层配额树:个人配额是份额 团队配额是硬上限;用量沿树回滚 父池实时可见。"""

    def __init__(self):
        self.root = QuotaNode("org", 1000)

    def add_team(self, name, quota):
        t = QuotaNode(name, quota)
        t.parent = self.root
        self.root.children[name] = t
        return t

    def add_user(self, team, name, quota):
        u = QuotaNode(name, quota)
        u.parent = self.root.children[team]
        self.root.children[team].children[name] = u
        return u

    def _borrow(self, node, need):
        """向直接父节点借:父池空闲足够才借,只登记在借方 由用量回滚扣父池。"""
        parent = node.parent
        if parent is None or parent.free() < need:
            return False
        node.borrowed += need
        return True

    def _add_usage(self, node, amount):
        """用量回滚:自身与全部祖先的 used 同步增加 父池空闲实时下降。"""
        while node is not None:
            node.used += amount
            node = node.parent

    def consume(self, path, amount):
        """path 形如 team/user:个人额度不够先借,借不到整体拒绝,不做半笔。"""
        team = self.root.children[path[0]]
        node = team.children[path[1]] if len(path) > 1 else team
        short = amount - node.free()
        if short > 0 and not self._borrow(node, short):
            return {"ok": False, "need_borrow": short}
        node.borrowed = max(0, node.borrowed)
        self._add_usage(node, amount)
        return {"ok": True, "borrowed_total": node.borrowed}

    def settle(self):
        """周期结算:借来的额度被豁免 用量沿树等额回落 完成一次软回收。"""
        for team in self.root.children.values():
            for user in team.children.values():
                if user.borrowed > 0:
                    amt = user.borrowed
                    user.borrowed = 0
                    node = user
                    while node is not None:
                        node.used -= amt
                        node = node.parent
        return {"root_free": self.root.free()}


if __name__ == "__main__":
    tree = QuotaTree()
    tree.add_team("teamA", 400)
    tree.add_user("teamA", "u1", 100)
    tree.add_user("teamA", "u2", 100)
    tree.add_team("teamB", 500)
    tree.add_user("teamB", "u3", 50)

    r = tree.consume(("teamA", "u1"), 100)             # 用满自身份额
    assert r["ok"] is True and r["borrowed_total"] == 0
    assert tree.root.children["teamA"].free() == 300, "用量回滚后团队池实时下降"

    r2 = tree.consume(("teamA", "u1"), 80)             # 自身已满 向团队借 80
    assert r2["ok"] is True and r2["borrowed_total"] == 80
    assert tree.root.children["teamA"].free() == 220

    r3 = tree.consume(("teamA", "u2"), 380)            # 缺 280 团队池只有 220 借不到
    assert r3["ok"] is False and r3["need_borrow"] == 280

    r4 = tree.consume(("teamB", "u3"), 60)             # u3 超 10 → 团队B 借
    assert r4["ok"] is True and r4["borrowed_total"] == 10
    assert tree.root.free() == 1000 - 240, "根池反映全树用量"

    settled = tree.settle()
    assert tree.root.children["teamA"].children["u1"].borrowed == 0, "周期末归还在借"
    assert tree.root.children["teamA"].children["u1"].free() == 0, "自身份额已用完 借用部分被豁免"
    assert tree.root.children["teamA"].free() == 300, "团队池回收 220→300"
    assert settled["root_free"] == 1000 - 150
    assert tree.root.children["teamA"].children["u2"].free() == 100
    print("配额树通过:u1 借 80 u3 借 10 u2 大额被拒 结算后根池余量", settled["root_free"])
