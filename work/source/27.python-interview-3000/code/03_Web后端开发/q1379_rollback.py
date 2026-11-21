"""发布管理器:版本台账 + 健康门禁 + 回滚(纯标准库演示)。"""


class ReleaseManager:
    def __init__(self):
        self.live = None
        self.log = []

    def deploy(self, version, health):
        if health():
            self.live = version
            self.log.append((version, "live"))
            return True
        self.log.append((version, f"health-check failed, keep {self.live}"))
        return False

    def rollback(self, target, health):
        if health():
            self.live = target
            self.log.append((target, "rollback live"))
            return True
        self.log.append((target, "rollback failed, escalate to human"))
        return False


def healthy_v1():
    return True


def broken_v2():
    return False


rm = ReleaseManager()
print(rm.deploy("v1.4.2", healthy_v1), "live =", rm.live)
print(rm.deploy("v1.5.0", broken_v2), "live =", rm.live)     # 门禁拦住坏版本
print(rm.deploy("v1.4.2", healthy_v1), "live =", rm.live)    # 幂等重发
print(rm.rollback("v1.4.1", healthy_v1), "live =", rm.live)  # 主动回滚
for row in rm.log:
    print(row)
