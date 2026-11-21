---
title: [PER-637] 隐私合规在前端的技术落实：Cookie 同意管理（CMP）与埋点分级门控怎么做？
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-637：隐私合规在前端的技术落实：Cookie 同意管理（CMP）与埋点分级门控怎么做？

**答**：
- 合规要求落成技术机制：**同意前不加载非必要追踪类脚本**（统计/广告 SDK 必须等用户同意后才 init，这是 GDPR/个保法的硬要求，先加载再撤回违规）、**同意状态可撤回**（撤回后停采集并按需清理已存数据）、**分级记录**（同意时间、版本、范围留证据，监管检查要能出示）。
- 技术实现：CMP SDK 管理同意状态（categories: necessary/ analytics/ marketing），提供 `gate(category, fn)` 门控——未同意时 fn 不执行；TMS（标签管理器）按状态决定加载哪些第三方。
- 埋点分级：necessary（登录态必需）、analytics（需同意）、marketing（需明确授权）；埋点上报 SDK 统一读取分级，未达级别直接丢弃，从机制上杜绝忘记判断。
- 中国法增量：个人信息单独同意（人脸/身份证）、最小必要原则（埋点字段审批制）、出境评估——审批清单与字段分级要落进埋点平台。

```javascript

class CMP {
  constructor() {
    this.state = this.load() ?? { version: 'v1', granted: [], ts: null };
  }
  grant(categories) {
    this.state = { version: this.state.version, granted: categories, ts: Date.now() };
    localStorage.setItem('cmp', JSON.stringify(this.state));  // 留证据
    emit('cmp-change', this.state);
  }
  withdraw(categories) {
    this.state.granted = this.state.granted.filter(c => !categories.includes(c));
    localStorage.setItem('cmp', JSON.stringify(this.state));
    emit('cmp-withdraw', categories);                          // SDK 监听后停采集
  }
  has(category) { return this.state.granted.includes(category); }
  gate(category, fn) {                                         // 埋点统一门控
    if (category === 'necessary' || this.has(category)) return fn();
    return null;                                               // 未同意直接丢弃
  }
}
// 埋点 SDK：track(category, event) { return cmp.gate(category, () => send(event)); }
// TMS：analytics 类脚本仅在 cmp.has('analytics') 为真时才插入 <script>
```
