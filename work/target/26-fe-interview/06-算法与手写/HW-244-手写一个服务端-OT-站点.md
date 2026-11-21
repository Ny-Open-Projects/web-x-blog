---
title: [HW-244] 手写一个服务端 OT 站点：操作日志与版本号仲裁
date: 2026-11-21
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-244：手写一个服务端 OT 站点：操作日志与版本号仲裁

**答**：
- 需求：实现 OTServer：ops 日志（按版本号存储）；receive(clientRev, op)——clientRev == lastRev 直接应用广播；落后则先对 op 依次变换日志中 rev 之后的 op（log 侧变换），应用后版本++ 并广播；历史查询：给定版本区间返回 ops。
- 边界：clientRev > lastRev 拒绝（非法）；变换需保留日志原 op 不变（用变换结果新对象）；并发同版本 op 按到达顺序仲裁。
- 评分点：服务端侧变换方向；日志不可变性；版本仲裁。

```javascript
class OTServer {
  constructor() { this.ops = []; this.doc = ''; }         // ops[i] 产生版本 i+1
  get lastRev() { return this.ops.length; }
  receive(clientRev, op) {
    if (clientRev > this.lastRev) return { err: 'rev-too-new' };
    let o = { ...op };
    for (let i = clientRev; i < this.lastRev; i++) {      // 对已提交 op 逐个变换
      const { a1, b1 } = transform(o, this.ops[i]);
      o = a1;
    }
    this.ops.push(o);
    this.doc = applyOp(this.doc, o);
    return { rev: this.lastRev, op: o };                  // 广播给其他客户端
  }
  history(fromRev, toRev) { return this.ops.slice(fromRev, toRev); }   // 回放/追赶用
}
function applyOp(text, op) {
  return op.type === 'insert'
    ? text.slice(0, op.pos) + op.text + text.slice(op.pos)
    : text.slice(0, op.pos) + text.slice(op.pos + op.text.length);
}
```
