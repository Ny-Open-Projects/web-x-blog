---
title: [Q249] Reflection 自我反思与自我修正
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q249 · Reflection 自我反思与自我修正

> 难度:★★★ | 标签:Agent, 反思

**问**:Reflection(自我反思)模式是什么?它和辩论、ReAct 里的自纠有什么区别?

**答**:Reflection 是"生成 → 批评 → 修订"的单 Agent 循环:同一个(或专职的)LLM 先产出初稿,再以评审者视角对照要求/清单挑毛病,把批评意见回传给生成者修订,循环到评审通过或达到轮数上限。区别:ReAct 的自纠只针对工具报错的即时反应;Reflection 是对产出质量的主动迭代,有明确的评审标准(rubric);辩论是多 Agent 交叉挑错,Reflection 是自我挑错,成本更低。工程要点:1) 评审标准要具体可验证(是否包含 X、是否引用了证据),泛泛的"再想想"几乎无效;2) 通常 1-2 轮收益最大,轮数再多边际递减;3) 评审者和生成者用不同角色/温度,避免"自己夸自己"。这也是 Reflexion、Self-Refine 等论文的核心思想。

```python
# file: code/06_Agent与LLM及系统设计/q249_reflection.py
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
```

**追问**:
- 评审 rubric 怎么写才有效?——可验证条目:「包含 X、引用了证据 E、长度<300 字」,每条独立判;泛泛的「更好一点」无法产生有效修订。
- 轮数上限怎么定?——2-3 轮足够,边际收益快速衰减;还要配 token 预算,防止修订循环烧钱。
- 自我反思会越改越差吗?——会,模型可能过度修订删掉正确内容;保留每版本,评审通过率下降即停,回退最优版本。
