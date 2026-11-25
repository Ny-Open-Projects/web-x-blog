---
title: [ENG-272] ADR（架构决策记录）流程怎么运转才不是形式主义？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## ENG-272：ADR 怎么运转？
**答**：
- 触发标准：决策满足「难逆转 + 跨团队影响 + 有真实权衡」三条才写 ADR——否则是文档洪水（换 lint 规则不配 ADR）。
- 轻量模板：背景/选项/取舍/后果/状态（proposed→accepted→superseded），一页以内；ADR 编号 + 检索（ENG-220 知识库）。
- 生命周期：superseded 机制让旧决策显式失效（新 ADR 链接旧 ADR）——ADR 只增不删会变成误导信息库。
- 落地检验：ADR 被引用进评审/新成员 onboarding（「先读这 5 篇 ADR」）才说明有真实消费。
- 追问钩子：为什么「superseded 状态」比「删除旧 ADR」重要——删除让历史决策失去上下文（为什么当时这么做）；superseded 链保留演进轨迹，新读者能看到决策如何被推翻与迭代，这是组织记忆的完整性。

```markdown
<!-- ADR-0012 模板（一页内） -->
状态: superseded by ADR-0020
背景: 构建全量 40min
选项: A Turborepo / B Nx / C 自研
取舍: B 插件重，C 维护成本高 → A
后果: 引入缓存治理责任（ENG-205）
```
