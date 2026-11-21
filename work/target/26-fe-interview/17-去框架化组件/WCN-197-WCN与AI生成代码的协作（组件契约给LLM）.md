---
title: [WCN-197] WCN 与 AI 生成代码的协作：为什么 WC 契约对 AI Coding 更友好？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 选型与工程落地]
type: 面试题
---

## WCN-197：WCN 与 AI 生成代码的协作：为什么 WC 契约对 AI Coding 更友好？

**答**：
- 契约清晰：custom-elements.json 是机器可读的单一事实源——AI（Cursor/Copilot）读 manifest 即知道可用组件、attribute 类型、事件结构，生成代码幻觉率显著低于"从源码猜 API"。
- 宿主无关：AI 生成的消费代码只需 HTML/属性/事件三种语法，跨框架不踩桥接坑（React 19 之前的序列化问题等）。
- prompt 工程实践：把 manifest 喂给 AI（规则文件/上下文），要求"只使用 registry.json 中的组件"；生成的代码用契约测试自动验证（WCN-171）——AI 产出 → CI 契约断言，闭环。
- 组件实现本身也可 AI 辅助：规范（WCN-177 反模式清单 + 开发规范）作为 prompt 上下文，AI 生成的 WC 组件先过 ESLint 规则集（WCN-178）再人工 review。
- 风险：AI 可能 invent 不存在的 part/token——契约 lint 与视觉回归兜底。

```text
AI 协作闭环
manifest/规范 → prompt 上下文
AI 生成消费代码/组件实现
→ ESLint（WCN-178 规则）
→ 契约冒烟测试（WCN-171）
→ 视觉回归
→ 人工 review 合入
```
