---
title: [TST-626] 测试环境即服务（TEaaS）的核心能力有哪些？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-626：测试环境即服务（TEaaS）的核心能力有哪些？

**答**：
- 结论：把环境从「人肉申请」变成「按需申领、自动回收」的服务——租约、快照、隔离是三要素。
- 能力清单：环境模板、快照克隆、租约与续期、租户隔离、成本归属。
- 关键指标：环境就绪时长与复用率；_ready 探活失败自动重建。
- 追问钩子：两个团队同时改同一个共享环境导致串扰，你如何从架构上根除？

```javascript
class EnvPool {
  constructor(templates) { this.free = [...templates]; this.leases = new Map(); }
  acquire(team, ttl = 30) {
    const t = this.free.pop();
    if (!t) throw new Error('无可用环境');
    const lease = { team, tpl: t, expire: Date.now() + ttl * 60000 };
    this.leases.set(team, lease); return lease;
  }
  renew(team, ttl) {
    const l = this.leases.get(team);
    if (!l) throw new Error('租约不存在');
    l.expire = Date.now() + ttl * 60000; return l;
  }
  sweep() {
    [...this.leases].forEach(([k, l]) => {
      if (l.expire < Date.now()) { this.free.push(l.tpl); this.leases.delete(k); }
    });
  }
}
```
