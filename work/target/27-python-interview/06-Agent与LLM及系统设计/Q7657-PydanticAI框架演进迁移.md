---
title: [Q7657] PydanticAI 框架演进与迁移
date: 2026-11-21
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7657 · PydanticAI 框架演进与版本迁移

难度：P6 | 标签：PydanticAI、Agent 框架、版本演进

**问**：团队在裸调 SDK 和 LangChain 之间，考虑引入 PydanticAI。它的定位是什么？核心抽象（Agent/依赖注入/结构化输出）如何映射到工程收益？引入与升级要注意什么？

**答**：结论：PydanticAI 的定位是**类型安全的轻量 Agent 层**——把 Pydantic v2 的校验与序列化复用到 LLM 交互：工具签名即 schema、结构化输出直接得到验证过的模型实例、依赖注入（`deps_type`）解决"测试时替换服务"的问题。相比 LangChain 的价值是少抽象（不隐藏 prompt 与消息流），相比裸 SDK 的价值是补齐"工具注册/结构化输出/重试"三件工程件。它是 Pydantic 团队出品，演进节奏跟随 Pydantic v2 生态，升级风险点集中在 output 类型语义与模型 provider 抽象的版本变化。

实战要点：
1. 三个核心抽象的映射：`Agent(model, tools, deps_type, output_type)`——工具用函数签名自动生成 schema；`output_type=Model` 时返回 pydantic 校验后实例（失败触发自动重试喂错误）；deps 通过 RunContext 注入，生产换配置、测试换桩。
2. 版本基线：PydanticAI 要求 Pydantic v2（不要混 v1 环境）；早期版本 API 变动较快，锁定次版本并关注 changelog，封装一层自己的 Agent 包装类隔离升级（Q7550 同款纪律）。
3. 引入判据：工具多、结构化输出多、需要可测试性 → 值得；单次对话+一次调用 → 裸 SDK 更省。

```python
"""PydanticAI 核心抽象的降级模拟（无第三方时用标准库演示语义）
基线：pydantic>=2.7, pydantic-ai>=0.2"""
from dataclasses import dataclass, field
from typing import Protocol


class CityInfo(Protocol):
    name: str
    population: int


@dataclass
class Deps:
    """依赖注入：生产连真实服务，测试换桩"""
    geo_api: object


@dataclass
class FakeGeo:
    cache: dict = field(default_factory=dict)

    def lookup(self, city: str) -> dict:
        return {"name": city, "population": 1_000_000}


@dataclass
class AgentRunner:
    """模拟 output_type 结构化输出 + 校验失败自动重试"""
    max_retries: int = 2

    def run(self, raw_output: dict, schema_fields: set[str]) -> object:
        for attempt in range(self.max_retries + 1):
            missing = schema_fields - raw_output.keys()
            if not missing:
                return raw_output
            err = f"missing fields {missing}"  # 错误喂回模型重试
            print(f"retry {attempt + 1}: {err}")
            raw_output = {**raw_output, **{k: "..." for k in missing}}
        raise ValueError("structured output failed after retries")


runner = AgentRunner()
try:
    print(runner.run({"name": "Hangzhou"}, {"name", "population"}))
except ValueError as e:
    print("final:", e)
print(runner.run({"name": "Hangzhou", "population": 12_000_000},
                 {"name", "population"}))

# deps 注入语义：测试用 FakeGeo，生产换真实 API
deps = Deps(geo_api=FakeGeo())
print(deps.geo_api.lookup("Suzhou"))
```

**追问 1**：为什么"工具签名自动生成 schema"比手写 JSON schema 强？
**提示**：签名即真源——类型错了 import/静态检查期就报，schema 不会与代码漂移（Q7629 schema 不一致事故的结构化解法）。

**追问 2**：PydanticAI 的结构化输出自动重试消耗什么？
**提示**：每次校验失败=一次额外模型调用，token 成本翻倍风险；对高失败率输出先修 prompt/换模型而不是依赖重试兜底。

## 背诵要点
- PydanticAI=类型安全轻量层：工具签名即 schema、output_type 返回校验实例、deps_type 依赖注入。
- 基线 Pydantic v2 + 锁次版本，自建包装类隔离升级；判据=工具多/结构化多/要可测试。
- 结构化输出自动重试是"额外模型调用"，失败率高先修 prompt。

## 复盘追问
- 从裸 SDK 迁到 PydanticAI，哪些调用点不值得迁（单轮对话）？
- deps 注入在集成测试里怎么与真依赖（DB/HTTP）分层？
