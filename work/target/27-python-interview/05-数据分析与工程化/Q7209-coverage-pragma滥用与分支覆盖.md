---
title: "[Q7209] coverage pragma 滥用：把没测的分支藏起来"
date: 2026-11-23
categories: [Python数据分析工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7209 · coverage pragma 滥用：把没测的分支藏起来

难度：P6 ｜ 标签：coverage、分支覆盖、pragma、质量门禁

基线：Python 3.12；coverage.py 7.x 分支覆盖语义；纯 Python 模拟覆盖率计算。

**问**：团队把覆盖率门禁定在 85%，有人发现给难测的 `except` 和 `else` 分支加 `# pragma: no cover`，覆盖率立刻从 33% 涨到 50%，CI 全绿。代码一行没多测，指标却上去了。`pragma: no cover` 到底排除了什么？这种"达标"有什么风险？

**答**：
- **结论**：`# pragma: no cover` 告诉 coverage **把该行/该分支从分母里剔除**，既不算覆盖也不算未覆盖。它本意是排除"无法执行"的代码（平台特定分支、`if TYPE_CHECKING`、防御性 `raise`），但被用来排除"难测"的分支时，等于把风险从指标里删掉，而不是消除。更隐蔽的是分支覆盖：排除 `else` 后，`if` 的另一条路径不再计入分母，覆盖率虚高。
- **取舍**：合理使用可以避免为不可达代码写无意义测试；滥用会让门禁失去意义。团队应把 pragma 当成"需要评审的例外"，而不是个人提分工具。替代方案：拆分函数让分支可测、用依赖注入模拟异常、对平台分支用 `sys.platform` 条件跳过并注明原因。
- **实战**：① 统计 pragma 的数量与分布，新增必须 code review 说明"为什么不可达"；② 同时看行覆盖和分支覆盖，防止只堆行覆盖；③ 对 `except` 分支专门做故障注入测试，而不是排除；④ 覆盖率是"下限"不是"目标"，核心模块单独设更高阈值。

```python
def branch_coverage(branches: list[tuple[str, bool, bool]]) -> float:
    """branches: (名称, 是否被执行, 是否加 pragma 排除)。"""
    executable = [(name, hit) for name, hit, excluded in branches if not excluded]
    if not executable:
        return 0.0
    return sum(hit for _, hit in executable) / len(executable)


if __name__ == "__main__":
    raw = [("if-true", True, False), ("if-false", False, False),
           ("except", False, False)]
    hidden = [("if-true", True, False), ("if-false", False, False),
              ("except", False, True)]
    print(f"真实分支覆盖率: {branch_coverage(raw):.0%}")
    print(f"排除 except 后: {branch_coverage(hidden):.0%}")
    print("结论：pragma 把未测分支移出分母，指标上升但风险仍在")
```

**追问一**：为什么行覆盖率 100% 仍可能漏掉严重 bug？
→ 解析：行覆盖只要求该行被执行过，不要求所有分支组合、异常路径、边界值都走到。一个 `if` 的 true 分支跑过就算覆盖，false 分支可能从未执行；循环零次、异常、并发交错都不会体现在行覆盖里。

**追问二**：`# pragma: no branch` 和 `# pragma: no cover` 有什么区别？
→ 解析：`no cover` 把整行/整个分支排除出统计；`no branch` 只告诉 coverage"这个循环/分支不会走另一条路"（比如 `while True` 的退出分支），仍然要求该行被执行。用错会把"没测"伪装成"不可达"。
