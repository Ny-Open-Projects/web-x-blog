---
title: [1001] Agent 应用的攻击面有哪些，威胁模型怎么画
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 安全, 威胁模型]
type: 面试题
---

## 1001：Agent 应用的攻击面有哪些，威胁模型怎么画

**答**：
- 五大攻击面：输入侧（用户 prompt、外部内容注入——网页/文档/工单里的隐藏指令）、工具侧（工具返回内容被投毒、越权调用）、模型侧（提示注入、越狱）、输出侧（答案泄露敏感信息、产出恶意代码被下游执行）、基础设施侧（凭证泄露、日志含敏感数据）。
- Agent 比聊天机器人多了「执行能力」，威胁等级跃迁：注入不再只是「让模型说错话」，而是「让模型做错事」（删库、外发、转账），威胁模型必须以「可执行动作」为中心。
- 建模方法：按「数据流」画——外部数据从哪进、经过哪些 Agent、触达哪些工具、副作用落在哪；每个跨界点就是一个防线位置。
- 追问钩子：哪条路径最危险？——「外部内容 → 检索 Agent → 执行工具」这条链：输入不可信 + 终点有副作用，是注入攻击的黄金通道。

```ts
// 威胁模型表：路径 × 风险 × 防线
const threatModel = [
  { path: 'user -> agent', risk: 'jailbreak', defense: '输入过滤 + 拒答训练' },
  { path: 'web -> rag -> agent', risk: 'indirect_injection', defense: '内容消毒 + 来源信任分级' },
  { path: 'agent -> tool.exec', risk: 'dangerous_action', defense: '权限白名单 + 人工审批门' },
  { path: 'agent -> output', risk: 'sensitive_leak', defense: '输出审查 + DLP 扫描' },
];
```
