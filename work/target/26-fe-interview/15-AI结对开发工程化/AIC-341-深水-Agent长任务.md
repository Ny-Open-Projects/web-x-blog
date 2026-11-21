---
title: [AIC-341] Agent 跑 30 分钟以上的长任务（全仓重构），如何设计「过程可视化与可控性」？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-341：Agent 跑 30 分钟以上的长任务（全仓重构），如何设计「过程可视化与可控性」？
**答**：
- 里程碑制：长任务拆成里程碑清单，每个里程碑完成即落盘（commit）+ 通知，人可随时介入。
- 过程日志结构化：每步动作（读/改/测）结构化记录，事后可回放审计。
- 中断恢复：任务状态外置（进度文件），中断后新会话可从里程碑续跑。
- 控制权：暂停/回退到某里程碑/修改指令继续——人始终握方向盘。

```javascript
const longTask = {
  milestones: ['m1: 特征测试', 'm2: 拆分 utils', 'm3: 更新引用', 'm4: 全量验证'],
  protocol: '每里程碑 commit + push branch + notify',
  resume: '进度存 .agent/progress.json → 新会话续跑',
};
r
```
