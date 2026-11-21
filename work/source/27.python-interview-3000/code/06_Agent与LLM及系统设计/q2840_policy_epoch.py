"""Q2840 策略热切换的纪元绑定:步骤开始即钉住策略版本。

运维改了重试上限 超时或工具策略,正在跑的 Agent 怎么办?规则是
步骤边界生效:每一步开始时对策略做快照并钉住纪元号,本步内策略被
热切换也不回头,下一步自然用新版。这样每一步用哪版策略都有据可查。
"""


class PolicyRegistry:
    def __init__(self, policy):
        self._policy = dict(policy)
        self.epoch = 1

    def snapshot(self):
        """步骤开始时调用:钉住当前策略与纪元。"""
        return dict(self._policy), self.epoch

    def hot_swap(self, patch):
        """热切换:只影响之后开始的步骤。"""
        self._policy.update(patch)
        self.epoch += 1


def run_step(registry, name, action):
    """一步的执行:开头钉策略,执行中读的都是钉住的那份。"""
    policy, epoch = registry.snapshot()
    used = action(policy)  # 模拟本步执行期间读到的策略值
    return {"name": name, "epoch": epoch, "retry_max_seen": used}


def main():
    reg = PolicyRegistry({"retry_max": 3})
    # 步骤一开始就钉住 epoch1 的 retry_max=3
    step1 = run_step(reg, "fetch", lambda p: p["retry_max"])
    # 执行中途运维热切换
    reg.hot_swap({"retry_max": 1})
    step2 = run_step(reg, "parse", lambda p: p["retry_max"])
    assert step1 == {"name": "fetch", "epoch": 1, "retry_max_seen": 3}, step1
    assert step2 == {"name": "parse", "epoch": 2, "retry_max_seen": 1}, step2
    assert reg.epoch == 2
    # 纪元可追溯:每个步骤能说清自己用的哪版策略
    trail = [step1["epoch"], step2["epoch"]]
    assert trail == [1, 2], trail
    print("步骤1:", step1, "(中途切换不影响)")
    print("步骤2:", step2, "(已用新策略)")
    print("策略纪元随步骤留痕:", trail)


if __name__ == "__main__":
    main()
