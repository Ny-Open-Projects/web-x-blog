---
title: [PER-784] WebView 池与页面预渲染的协同与冲突：什么时候用池、什么时候用预渲染、能否叠加
date: 2026-11-21
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-784：WebView 池与页面预渲染的协同与冲突：什么时候用池、什么时候用预渲染、能否叠加

**答**：
- 本质差异：池预热的是"空白容器"（不知道下一个页面是谁，收益是容器启动段）；预渲染预热的是"具体页面"（知道意图，收益是容器+网络+渲染全链路）。
- 选型：导航目的地确定的入口（首页 banner、tab 切换）用预渲染；目的地不确定的通用跳转用池。
- 冲突点：叠加使用时预渲染页也要占池实例，池容量调度必须区分"池化实例"与"预渲染占用"，否则预热互相挤掉对方。
- 工程建议：意图强（点击概率 > 60%）才预渲染；其余场景池兜底。两者命中数据分开统计，避免收益归因混乱。

```javascript
// 决策表：意图强度 × 资源预算
function chooseWarmStrategy(intentProb, lowEnd) {
  if (lowEnd) return 'pool';                  // 低端机只保留池（预渲染内存代价高）
  if (intentProb > 0.6) return 'prerender';   // 高意图：预渲染具体页面
  return 'pool';                              // 低意图：池兜底
}
// 协同约束：预渲染实例计入池占用，避免互相挤兑
class WarmBudget {
  constructor(cap) { this.cap = cap; this.used = { pool: 0, prerender: 0 }; }
  tryOccupy(kind) {
    const total = this.used.pool + this.used.prerender;
    if (total >= this.cap) return false;      // 预算满了：按 kind 淘汰对方最旧实例
    this.used[kind]++; return true;
  }
}
```
