---
title: "[Q7719] Agent 计划缓存：工具升级后旧计划还在跑"
date: 2026-11-23
categories: [PythonAgent与LLM]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7719 · Agent 计划缓存：工具升级后旧计划还在跑

难度：P6 ｜ 标签：Agent、计划缓存、缓存失效、工具版本

基线：Python 3.12；纯 Python 模拟计划缓存 key 与工具 schema 变更。

**问**：为了省 token，Agent 把"查天气→查航班→汇总"这类计划缓存起来，同样的用户意图直接复用。后来天气工具把参数 `city` 改名 `location`，缓存计划仍然用旧参数调用，连续报错；更糟的是权限收紧后，旧计划还在调用已被禁用的工具。计划缓存到底该缓存什么、什么时候必须失效？

**答**：
- **结论**：计划是**对工具契约和权限的依赖**，不是纯文本。缓存 key 必须包含：用户意图/目标、**工具集版本与 schema 哈希**、权限/策略版本、关键上下文约束（地区、时间、租户）、模型版本。任一变化都必须 miss 并重新规划。只按"意图文本"做 key，工具改名、参数变更、权限收紧都会命中过期计划。
- **取舍**：计划缓存能省规划 token 与首步延迟，但失效逻辑复杂；缓存粒度越粗（整个计划）收益越大、风险越高。折中：缓存"计划骨架"（步骤类型）而不是具体参数，执行前用当前 schema 重新绑定参数；或只缓存只读、低风险的计划，写操作/高权限操作每次重规划。计划缓存 ≠ 工具结果缓存，前者缓存决策，后者缓存数据，失效条件不同。
- **实战**：① key 里放 `tools_version`/`schema_hash`/`policy_version`，工具注册表变更时统一 bump 版本；② 计划带 TTL 与最大复用次数；③ 执行前做**前置条件校验**（工具存在、参数 schema 通过、权限允许），失败即重规划；④ 监控计划命中率与"命中后失败率"，后者升高说明失效策略有漏。

```python
def make_plan(goal: str, tools: dict[str, list[str]]) -> list[dict]:
    if goal == "出差":
        city_key = "location" if "location" in tools["weather"] else "city"
        return [{"tool": "weather", "args": {city_key: "$city"}},
                {"tool": "flight", "args": {"from": "$from", "to": "$to"}}]
    return []


def cache_key(goal: str, version: str, policy: str) -> str:
    return f"{goal}|{version}|{policy}"


def run(goal: str, cache: dict[str, list[dict]], version: str,
        policy: str, tools: dict[str, list[str]]) -> str:
    key = cache_key(goal, version, policy)
    plan = cache.get(key)
    if plan is None:
        plan = make_plan(goal, tools)
        cache[key] = plan
        source = "replanned"
    else:
        source = "cached"
    for step in plan:
        params = tools.get(step["tool"], [])
        if any(k not in params for k in step["args"]):
            return f"{source} -> schema mismatch on {step['tool']}"
    return f"{source} -> ok"


if __name__ == "__main__":
    tools_v1 = {"weather": ["city"], "flight": ["from", "to"]}
    tools_v2 = {"weather": ["location"], "flight": ["from", "to"]}
    cache: dict[str, list[dict]] = {}
    print(run("出差", cache, "v1", "allow", tools_v1))
    print("工具升级但仍用旧 key:", run("出差", cache, "v1", "allow", tools_v2))
    print("版本进 key:", run("出差", cache, "v2", "allow", tools_v2))
    print("结论：计划缓存必须绑定工具版本/schema/权限，执行前还要再校验")
```

**追问一**：为什么"计划骨架"缓存比"完整计划"缓存更安全？
→ 解析：骨架只记录"先查天气再查航班"这类步骤类型，具体参数在执行前按当前 schema 重新绑定，工具改名/加参数不会直接失效；完整计划把旧参数一起缓存，契约一变就报错。代价是骨架复用时仍要一次参数填充，省不了这部分 token。

**追问二**：计划缓存和工具结果缓存可以共用一套失效机制吗？
→ 解析：不能。计划依赖工具契约/权限/模型版本，结果依赖数据本身与时间（天气 10 分钟就过期）；共用 key 会导致"计划还新、结果已旧"或反之。两者要分别定义 TTL、版本因子与失效事件。
