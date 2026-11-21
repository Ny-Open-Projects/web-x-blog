"""多机房容灾:同城同步复制 RPO=0 vs 异地异步复制 RPO>0,演练切换。"""


class DataCenter:
    def __init__(self, name, mode):
        self.name, self.mode = name, mode
        self.data, self.replica_targets = {}, []
        self.pending = []

    def link(self, other):
        self.replica_targets.append(other)

    def write(self, k, v):
        self.data[k] = v
        for t in self.replica_targets:
            if self.mode == "sync":
                t.data[k] = v                    # 同城:复制成功才算写完成
            else:
                self.pending.append((t, k, v))   # 异地:异步
        return True

    def flush_replication(self):
        while self.pending:
            t, k, v = self.pending.pop(0)
            t.data[k] = v


if __name__ == "__main__":
    hz, hz_bj = DataCenter("杭州主", "sync"), DataCenter("杭州备", "sync")
    hz.link(hz_bj)
    hz.write("pay-1", 99)
    print("同城双活:主写后备立即可见 ->", hz_bj.data)
    assert hz_bj.data["pay-1"] == 99, "同步复制 RPO=0"

    # 机房级故障:备机房接管
    primary_down = True
    print("杭州主故障,备机房接管读:", hz_bj.data["pay-1"])

    sh, bj = DataCenter("上海", "async"), DataCenter("北京", "async")
    sh.link(bj)
    sh.write("pay-2", 100)
    print("异地多活:主写后北京复制进度 ->", bj.data, "(可能滞后)")
    assert "pay-2" not in bj.data, "异步复制未 flush 前存在 RPO 窗口"
    sh.flush_replication()
    assert bj.data["pay-2"] == 100
    print("复制完成后收敛;RPO = 未 flush 期间的数据量")

    # 演练切换检查单(代码化)
    checklist = {"RPO 验证": "模拟断链后比对两侧数据差",
                 "RTO 验证": "从故障注入到备端接管读写的耗时",
                 "防脑裂": "切换需仲裁方确认旧主不可达"}
    for k, v in checklist.items():
        print(f"  {k}: {v}")
