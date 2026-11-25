---
title: [TST-682] 笔试：实现前端故障注入器框架（API / DOM / 网络 / 存储）
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-682：笔试：实现前端故障注入器框架（API / DOM / 网络 / 存储）

**题目**：实现 ChaosKit：register(type,inject,restore) 注册故障；enable(type,opts) 在 window.__CHAOS_ON__ 为真时执行注入并记录回滚函数；disableAll() 逆序回滚所有激活故障。

**答**：
- 用注册表把故障类型映射到注入函数，统一 enable/disable 接口。
- 每个注入器必须支持回滚，框架在实验结束后自动恢复。
- 注入点的开关用全局标记，便于紧急熔断。

```javascript
class ChaosKit {
  constructor() { this.injectors = new Map(); this.active = []; }
  register(type, inject, restore) {
    this.injectors.set(type, { inject, restore });
  }
  enable(type, opts) {
    if (!window.__CHAOS_ON__) return false;
    const mod = this.injectors.get(type);
    if (!mod) throw new Error(`未知故障类型 ${type}`);
    const undo = mod.inject(opts);
    this.active.push({ type, undo, restore: mod.restore });
    return true;
  }
  disableAll() {
    this.active.forEach(a => (a.undo ? a.undo() : a.restore()));
    this.active = [];
  }
}
const kit = new ChaosKit();
kit.register('api', (o) => { const old = fetch;
  window.fetch = () => Promise.reject(new Error(o.msg));
  return () => { window.fetch = old; }; });
```

**评分点**：
- 注入器注册与查找正确
- 回滚机制完整且逆序执行
- 全局熔断开关生效
- 未知类型有明确错误
