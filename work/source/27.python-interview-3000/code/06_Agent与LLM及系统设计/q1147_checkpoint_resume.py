"""长任务检查点:两阶段状态 begin/done,断点续跑跳过已完成步骤。"""
import json, random


class TaskRunner:
    def __init__(self, steps, journal=None):
        self.steps = steps
        self.journal = journal or {}      # step_id -> "begin" | {"done": result}

    def run(self):
        for step_id, fn in self.steps:
            state = self.journal.get(step_id)
            if isinstance(state, dict) and "done" in state:
                print(f"  跳过 {step_id} 已完成")
                continue
            self.journal[step_id] = "begin"
            result = fn()                  # 崩溃模拟点:此行抛异常则停在 begin
            self.journal[step_id] = {"done": result}
            print(f"  完成 {step_id} -> {result}")
        return self.journal


def persist(journal):
    return json.dumps(journal, ensure_ascii=False)


def restore(s):
    return json.loads(s)


if __name__ == "__main__":
    random.seed(7)
    steps = [
        ("fetch", lambda: "100 条数据"),
        ("clean", lambda: "92 条有效"),
        ("analyze", lambda: "报告 v1"),
        ("notify", lambda: "已通知"),
    ]

    def crash():
        raise RuntimeError("模拟进程在 analyze 阶段被 kill")

    r1 = TaskRunner(steps[:2] + [("analyze", crash)])
    try:
        r1.run()
    except RuntimeError as e:
        snapshot = persist(r1.journal)
        print("崩溃:", e, "已持久化检查点")

    # 断点续跑:从快照恢复
    runner2 = TaskRunner(steps, journal=restore(snapshot))
    print("续跑:")
    final = runner2.run()
    assert all(isinstance(v, dict) for v in final.values())
    assert final["analyze"]["done"] == "报告 v1"
    print("全部步骤完成,幂等续跑成立")
