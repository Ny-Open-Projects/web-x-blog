"""双写迁移 Redis: 写新读旧 -> 对账 -> 切读 -> 收尾"""
class Cluster:
    def __init__(self):
        self.old, self.new = {}, {}
        self.write_both, self.read_new = False, False

    def write(self, k, v):
        self.old[k] = v
        if self.write_both:
            self.new[k] = v

    def read(self, k):
        return self.new.get(k) if self.read_new else self.old.get(k)

    def reconcile(self):
        missing = {k for k in self.old if self.new.get(k) != self.old[k]}
        for k in missing:                        # 修复后新库才可切读
            self.new[k] = self.old[k]
        return missing

if __name__ == "__main__":
    c = Cluster()
    for i in range(5):
        c.write(f"k{i}", i)
    c.write_both = True
    c.write("k5", 5)
    print("未迁移前差异:", c.reconcile())
    print("对账通过, 切读新库:", (c.__setattr__("read_new", True), c.read("k3"))[1])
    print("收尾: 停旧写 -> 旧实例只读观察 -> 下线")
