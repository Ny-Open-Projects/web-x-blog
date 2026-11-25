---
title: [1137] Agent 定义该配置化还是代码化，边界在哪
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 工程化]
type: 面试题
---

## 1137：Agent 定义该配置化还是代码化，边界在哪

**答**：
- 配置化（YAML/JSON 声明）：prompt 模板、工具白名单、预算、降级链——「数据和策略」类变更高频且无需发版。
- 代码化：编排逻辑（条件分支、并行结构）、自定义工具实现、复杂状态机——逻辑变更需要测试与评审，配置承载不了。
- 边界判断：变更是否需要「逻辑正确性验证」？需要就代码化（进 Git + 测试 + 门禁），只是参数调整就配置化（配置中心 + 灰度）。
- 追问钩子：配置里写逻辑（if/else 塞进 YAML）是常见腐化——怎么办？——配置表达力设上限（只允许简单映射与阈值），复杂逻辑必须下沉到代码；定期审计配置里的「逻辑气味」。

```yaml
# 配置化：策略与参数
agent: coder-1
prompt: prompts/coder.v12.md
tools: [fs.read, fs.write, test.run]
budget: { rounds: 15, tokens: 60000 }
degrade: { on_fail: retry_then_handoff }
```

```ts
// 代码化：编排逻辑
if (task.risk === 'high') await pipeline(['plan', 'exec', 'review']);
else await route(task);
```

