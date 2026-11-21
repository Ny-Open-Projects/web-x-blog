"""Reflection 循环:初稿 -> 自我批评(对照 rubric)-> 修订,直到评审通过或达上限。"""


class FakeWorkerLLM:
    """生成者:第一版有缺陷,收到具体批评后修订。"""

    def generate(self, task: str, feedback: str = "") -> str:
        if not feedback:
            return f"《{task}》初稿(遗漏了成本分析)"
        return f"《{task}》修订稿(已针对批评修订:补充成本分析)"


class FakeReflector:
    """评审者:对照 rubric 检查,返回具体可执行的批评或通过。"""

    RUBRIC = ("成本分析",)

    def critique(self, draft: str) -> str:
        missing = [r for r in self.RUBRIC if r not in draft]
        if missing:
            return f"不合格:缺少 {missing},请补充后再交"
        return "通过"


def reflect_loop(worker, reflector, task: str, max_iters: int = 3) -> str:
    draft, feedback = worker.generate(task), ""
    for i in range(1, max_iters + 1):
        verdict = reflector.critique(draft)
        print(f"  第{i}轮 评审:{verdict}")
        if verdict == "通过":
            return draft
        draft = worker.generate(task, verdict)  # 把具体批评回传修订
    return draft + "(达到最大反思轮数,带已知风险输出)"


if __name__ == "__main__":
    final = reflect_loop(FakeWorkerLLM(), FakeReflector(), "Agent 工程化方案")
    print("最终产出:", final)
