"""存储迁移状态机:双写 -> 校验 -> 切读 -> 收尾,每阶段可回滚。"""


class KV:
    """最小存储桩:write 返回固定 ack,便于双写一致性比对。"""

    def __init__(self, name):
        self.name, self.data = name, {}

    def write(self, key, value):
        self.data[key] = value
        return "ok"


class MigrationFSM:
    STAGES = ["dual_write", "verify", "switch_read", "finalize"]
    ROLLBACK = {"dual_write": "stop_new_write",
                "verify": "stop_verify",
                "switch_read": "read_back_to_old",
                "finalize": "resume_dual_write"}

    def __init__(self):
        self.stage = "dual_write"
        self.new_only_write = False
        self.log = []

    def advance(self, condition_ok):
        assert condition_ok, f"进入下一阶段的条件不满足: {self.stage}"
        idx = self.STAGES.index(self.stage)
        self.log.append(f"advance {self.stage} -> {self.STAGES[idx + 1]}")
        self.stage = self.STAGES[idx + 1]
        if self.stage == "finalize":
            self.new_only_write = True

    def rollback(self):
        action = self.ROLLBACK[self.stage]
        if self.stage == "finalize":
            self.new_only_write = False
            self.stage = "switch_read"
        elif self.stage == "switch_read":
            self.stage = "verify"
        self.log.append(f"rollback via {action} -> {self.stage}")
        return action


class DualWriteProxy:
    def __init__(self, old_db, new_db, fsm):
        self.old, self.new, self.fsm = old_db, new_db, fsm
        self.divergence = []

    def write(self, key, value):
        if self.fsm.new_only_write:
            self.new.write(key, value)
            return "new_only"
        r_old = self.old.write(key, value)          # 旧库权威:以它为提交标准
        r_new = self.new.write(key, value)
        if r_new != r_old:
            self.divergence.append(key)
        return "dual"


if __name__ == "__main__":
    old_db, new_db = KV("mysql-old"), KV("newstore")
    fsm = MigrationFSM()
    proxy = DualWriteProxy(old_db, new_db, fsm)

    proxy.write("o1", 100)
    assert old_db.data["o1"] == 100 and new_db.data["o1"] == 100
    print("双写期: 两库一致,旧库权威")

    fsm.advance(condition_ok=len(proxy.divergence) == 0)     # 校验期
    proxy.write("o2", 200)
    fsm.advance(condition_ok=all(old_db.data[k] == new_db.data[k] for k in old_db.data))
    print("切读期: 读流量灰度走新库,状态:", fsm.stage)

    # 切读后发现新库异常 -> 秒级回滚
    action = fsm.rollback()
    print("回滚动作:", action, "回到:", fsm.stage)
    assert action == "read_back_to_old" and fsm.stage == "verify"

    fsm.advance(True)                                   # verify -> switch_read
    fsm.advance(condition_ok=True)                      # switch_read -> finalize
    proxy.write("o3", 300)
    assert new_db.data["o3"] == 300 and "o3" not in old_db.data
    print("收尾期: 只写新库,旧库转只读归档;回滚窗口内可恢复双写")
    print("迁移日志:", fsm.log)
