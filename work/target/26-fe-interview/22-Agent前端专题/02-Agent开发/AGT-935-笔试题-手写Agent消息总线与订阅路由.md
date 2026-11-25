---
title: [935] 笔试手写：实现带通配符主题的 Agent 消息总线
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 笔试题, 多Agent, 消息总线]
type: 笔试题
---

## 935：笔试手写：实现带通配符主题的 Agent 消息总线

**答**：实现 AgentBus：publish(topic, msg) 与 subscribe(pattern, handler)。pattern 支持 `a.*` 单层通配与 `a.#` 多层通配（类 MQTT）。同一 pattern 多订阅者都收到；handler 异步且互不阻塞；返回 unsubscribe 函数。

```js
class AgentBus {
  constructor() { this.subs = []; this.seq = 0; }
  subscribe(pattern, handler) {
    const s = { pattern: pattern.split('.'), handler, id: ++this.seq };
    this.subs.push(s);
    return () => { this.subs = this.subs.filter(x => x.id !== s.id); };
  }
  match(pat, topic) {
    for (let i = 0; i < pat.length; i++) {
      if (pat[i] === '#') return true;                    // 多层通配吞掉剩余
      if (i >= topic.length) return false;
      if (pat[i] !== '*' && pat[i] !== topic[i]) return false;
    }
    return pat.length === topic.length;                   // 长度必须相等（无 #）
  }
  async publish(topic, msg) {
    const parts = topic.split('.');
    // allSettled：一个 handler 挂了不影响其他订阅者
    await Promise.allSettled(this.subs
      .filter(s => this.match(s.pattern, parts))
      .map(s => s.handler({ topic, ...msg })));
  }
}
const bus = new AgentBus();
bus.subscribe('agent.*.done', m => console.log('A', m.topic));
bus.subscribe('agent.#', m => console.log('B', m.topic));
bus.publish('agent.coder.done', {});  // A、B 都触发
```

**评分点**：
- `*` 与 `#` 语义区分正确：单层 vs 任意多层，`#` 必须放末尾才算规范实现（可加分讨论）
- match 的边界：pattern 比 topic 长、`#` 在中间的处理
- unsubscribe 闭包正确移除订阅
- handler 用 allSettled 隔离故障，说得出为什么不用 all

