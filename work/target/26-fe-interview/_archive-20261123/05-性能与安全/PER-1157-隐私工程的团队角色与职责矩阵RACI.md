---
title: [PER-1157] 隐私工程的团队角色与职责矩阵（RACI）
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1157：隐私工程的团队角色与职责矩阵（RACI）

**答**：
- 角色：DPO/合规（决策）、平台工程（SDK/工具）、业务工程（执行采集规范）、安全（防护）、法务（文本）。
- RACI 表：采集新增（业务 R、合规 A）、SDK 变更（平台 R、合规 C）、事件响应（安全 R、DPO A）。
- 例会：月度隐私例会过变更清单与事件；季度合规评审过审计结果。
- 赋能：业务工程自助工具（字段注册 UI、预检 CLI），减少对平台的阻塞。

```javascript
// 隐私 RACI 矩阵
const RACI = {
  'new-collection': { business: 'R', dpo: 'A', platform: 'C', security: 'I' },
  'sdk-change':     { platform: 'R', dpo: 'A', business: 'C', security: 'C' },
  'breach-response':{ security: 'R', dpo: 'A', business: 'I', platform: 'C' },
  'dsar-execution': { platform: 'R', dpo: 'A', business: 'C', security: 'I' },
};
function whoDoes(what) { return RACI[what] ?? { note: '未定义，先补矩阵' }; }
```
