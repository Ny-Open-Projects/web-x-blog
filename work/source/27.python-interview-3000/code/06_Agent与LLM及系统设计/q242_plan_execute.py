"""演示 Plan-and-Execute:规划器产出计划,执行器逐步执行并支持 replan。"""


class FakePlanner:
    def plan(self, goal: str) -> list[str]:
        return [f"1. 检索与「{goal}」相关的资料", "2. 提取关键数据", "3. 撰写摘要"]

    def replan(self, goal: str, done: list[str], failed: str) -> list[str]:
        return [f"重试: {failed}", "4. 汇总输出"]


class Executor:
    def execute(self, step: str) -> str:
        if step.startswith("2"):
            return "失败:资料为空"  # 模拟某一步失败
        return f"完成[{step[:8]}...]"


def plan_and_execute(planner, executor, goal: str) -> str:
    plan = planner.plan(goal)
    done, failed = [], None
    for step in plan:
        print(f"执行:{step}")
        result = executor.execute(step)
        if result.startswith("失败"):
            failed = step
            break
        done.append(step)
    if failed:
        print("触发 replan")
        for step in planner.replan(goal, done, failed):
            print(f"重新执行:{step} -> {executor.execute(step)}")
    return "任务结束"


if __name__ == "__main__":
    plan_and_execute(FakePlanner(), Executor(), "行业报告")
