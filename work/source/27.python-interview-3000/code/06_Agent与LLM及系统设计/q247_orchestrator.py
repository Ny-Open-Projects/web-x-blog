"""编排者-执行者实现:拆解任务、分派专职 Agent、失败重试、汇总。"""


class SubAgent:
    def __init__(self, specialty: str, ok_rate: float = 1.0):
        self.specialty, self.ok_rate = specialty, ok_rate

    def run(self, subtask: str) -> str:
        if "不可能" in subtask:  # 模拟失败
            raise RuntimeError(f"{self.specialty} 无法处理该子任务")
        return f"[{self.specialty}] 已完成 {subtask}"


class Orchestrator:
    def __init__(self, agents: dict[str, SubAgent], max_retry: int = 2):
        self.agents, self.max_retry = agents, max_retry

    def run(self, task: str) -> str:
        subtasks = [f"调研{task}", f"分析{task}数据", f"撰写{task}报告"]
        results = []
        for st in subtasks:
            agent = self.agents.get("分析" if "数据" in st else "默认")
            for attempt in range(1, self.max_retry + 1):
                try:
                    results.append(agent.run(st))
                    break
                except RuntimeError as exc:
                    print(f"  子任务失败第{attempt}次:{exc}")
                    if attempt == self.max_retry:
                        results.append(f"[降级] {st} 人工介入")
        return "汇总 -> " + " ; ".join(results)


if __name__ == "__main__":
    orch = Orchestrator({"默认": SubAgent("通用Agent"), "分析": SubAgent("分析Agent")})
    print(orch.run("咖啡市场"))
