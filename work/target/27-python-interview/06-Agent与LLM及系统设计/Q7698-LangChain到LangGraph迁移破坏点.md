---
title: [Q7698] LangChain 0.1 到 0.3 与 LangGraph 迁移破坏点
date: 2026-11-21
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7698 · LangChain 0.1 到 0.3 / LangGraph 的迁移破坏点

难度：P6 ｜ 标签：版本演进、LangChain、LangGraph、框架迁移

基线：Python 3.9+；langchain-core 0.1→0.3、langgraph 0.2+；pydantic v2 强制。

**问**：项目 2023 年用 LangChain 0.0.x 写的 agent 链，升级到 0.3 报错一片；同时团队在讨论"要不要干脆迁 LangGraph"。这个迁移的破坏点在哪里？什么信号说明该迁而不是升？

**答**：
- **结论**：0.0.x → 0.3 的破坏点集中在四层：
  1. **包拆分**：单体 `langchain` 拆成 `langchain-core / langchain-community / langchain-openai` 等分装包，import 路径全变，`from langchain.llms import OpenAI` 这类旧路径直接失效（部分有弃用映射但会告警）；
  2. **Pydantic v1 → v2 强制**：0.3 基于 pydantic v2，自定义 Chain/Tool 的字段定义、validator 写法（`@validator` → `@field_validator`）、模型配置全要改；
  3. **Chain → Runnable/LCEL**：`LLMChain/SequentialChain` 被 LCEL（`prompt | llm | parser`）取代，`run()` → `invoke()`，流式/批量/异步接口统一到 Runnable 协议；
  4. **Agent 执行器**：`AgentExecutor` 进入维护模式，官方推荐 LangGraph（显式状态图、可中断恢复、持久化）。
  该迁不迁的信号：agent 有多步状态、需要人工介入（human-in-the-loop）、需要检查点恢复——这些是 Chain 抽象给不了的，LangGraph 的图 + checkpoint 是为它们设计的；反之简单 RAG 链用 LCEL 就够，迁 LangGraph 是过度设计。
- **取舍**：升级路径建议"先做薄适配层再换骨架"：把业务代码与框架调用隔离到自建 wrapper，先升包版本修 import/pydantic，再逐链改写成 LCEL，最后按需上 LangGraph。直接在老 Chain 上堆功能只会加深耦合，下次迁移更痛。
- **实战**：迁移顺序——依赖冻结 + 锁版本 → 分装包 import 批量替换 → pydantic v2 机械迁移（用官方 `bump-pydantic` 类工具）→ 逐链 LCEL 化并配回归评测集 → agent 部分评估 LangGraph 重写。

```python
# 迁移自检：扫描老 import 与 pydantic v1 写法（标准库可运行）。
import re

OLD_IMPORTS = [
    (r"from langchain\.llms import", "langchain-community/langchain-openai 分装包"),
    (r"from langchain\.chains import LLMChain", "LCEL: prompt | llm | parser"),
    (r"from langchain\.agents import .*AgentExecutor", "LangGraph 或 langchain.agents 新 API"),
]
PYDANTIC_V1 = [
    (r"@validator\(", "@field_validator (pydantic v2)"),
    (r"\.run\(", "Runnable 协议: .invoke/.stream"),
]

def scan_migration(files: dict[str, str]) -> list[str]:
    issues = []
    for name, src in files.items():
        for pat, fix in OLD_IMPORTS:
            if re.search(pat, src):
                issues.append(f"{name}: 老导入 {pat} -> {fix}")
        for pat, fix in PYDANTIC_V1:
            for m in re.finditer(pat, src):
                issues.append(f"{name}:{src[:m.start()].count(chr(10)) + 1}: "
                              f"{m.group()} -> {fix}")
    return issues or ["扫描通过"]

if __name__ == "__main__":
    code = {
        "agent.py": "from langchain.chains import LLMChain\n"
                    "chain.run(x)\n",
        "tools.py": "from pydantic import BaseModel\n"
                    "@validator('q')\n",
    }
    for line in scan_migration(code):
        print("-", line)
```

**追问**：
- 一层：为什么 LangChain 生态要强制 pydantic v2？迁移时最常见的坑是什么？→ 提示：v2 校验/序列化语义变化（default 不可变、strict 模式），自定义模型字段里放非 JSON 类型（如 datetime 之外的复杂对象）在 v2 下序列化报错。
- 二层：LangGraph 的 checkpoint 持久化解决什么老痛点？→ 提示：agent 长任务的断点恢复与 human-in-the-loop 中断续跑，Chain 时代只能靠外部自己存状态。

**背诵要点**：
1. 0.3 迁移四层破坏：包拆分 import、pydantic v2 强制、Chain→LCEL（run→invoke）、AgentExecutor 维护模式。
2. 迁不迁 LangGraph 的信号：多步状态/人工介入/检查点恢复；简单 RAG 链用 LCEL 即可。
3. 迁移纪律：先建薄适配层隔离框架，锁版本小步升，每步配回归评测集。

**复盘追问**：
1. 为什么 2023 年的代码升级"报错一片"？提示：0.0.x 时代 import 路径与 API 每周都在变，代码与框架深度耦合；教训是框架调用必须收敛到适配层。
2. 如果团队自研了 80% 的编排逻辑，还需要 LangGraph 吗？提示：评估自研状态图的持久化/中断能力，缺才迁，全自研等价物重复造轮子亦可。
