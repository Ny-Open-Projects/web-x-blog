---
title: [1139] 多 Agent 测试的 fixture（录制/快照）怎么管理
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 测试]
type: 面试题
---

## 1139：多 Agent 测试的 fixture（录制/快照）怎么管理

**答**：
- fixture 三类：模型响应录制（回放测试用）、工具返回快照（mock 数据源）、任务输入样例（真实任务脱敏）；统一目录结构 + 元数据（录制时间、模型版本、来源任务）。
- 失效管理：fixture 绑定模型版本与 prompt 版本，版本不匹配的 fixture 标记过期；过期 fixture 不删除（历史基线），但不再用于门禁。
- 脱敏是硬要求：真实任务录制含业务数据，入库前过 DLP + 假名化——fixture 泄露就是数据泄露。
- 追问钩子：fixture 越积越多怎么治理？——按「被引用次数」治理：门禁引用的核心 fixture 少而精（关键路径覆盖），长尾 fixture 只在夜间全量跑用；零引用半年清理。

```yaml
# fixtures/coder-1/fix-typo/meta.yaml
source_task: T-8821        # 来源任务（脱敏）
model: qwen-coder@2025-09
prompt_ver: v12
recorded: 2026-10-12
pii_scan: pass
refs: [core_set, gate]     # 被哪些测试引用
```

