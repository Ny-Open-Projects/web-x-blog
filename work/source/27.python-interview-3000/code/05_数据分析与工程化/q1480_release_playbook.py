"""综合案例:一次数据发布的完整剧本,状态机驱动可中断续跑"""

PLAYBOOK = [
    # 阶段, 动作, 失败时的处置
    ("GATE", "跑分级数据测试门禁", "BLOCK 则终止,不进入发布"),
    ("FREEZE", "校验发布窗口与冻结期", "冲突则改期并通知干系人"),
    ("SMOKE", "部署后跑冒烟清单", "任一失败立即回滚"),
    ("CANARY", "小流量金丝雀对比 30 分钟", "STOP 信号则回滚"),
    ("WATCH", "观察期报告逐日巡检", "连续超阈值则回滚并复盘"),
    ("FULL", "全量放量并关闭特性开关旧路径", "问题则按回滚剧本执行"),
]


class Release:
    def __init__(self, version):
        self.version = version
        self.stage_index = 0
        self.history = []

    def run(self, stage_results):
        """stage_results: 每阶段模拟结果, PASS / FAIL"""
        while self.stage_index < len(PLAYBOOK):
            stage, action, failure_plan = PLAYBOOK[self.stage_index]
            result = stage_results.get(stage, "PASS")
            self.history.append((stage, action, result))
            print(f"[{self.version}] {stage}: {action} -> {result}")
            if result == "FAIL":
                print(f"  处置: {failure_plan}")
                print("  执行回滚剧本,发布终止")
                return "ROLLED_BACK"
            self.stage_index += 1
        return "RELEASED"


if __name__ == "__main__":
    print("剧本 A: 顺利发布")
    r1 = Release("v2025.06.2")
    print("结果:", r1.run({}))
    print("\n剧本 B: 金丝雀阶段失败")
    r2 = Release("v2025.06.3")
    print("结果:", r2.run({"CANARY": "FAIL"}))
    print("\n要点:发布是状态机不是清单,每一态的失败路径要和成功路径一样明确")
