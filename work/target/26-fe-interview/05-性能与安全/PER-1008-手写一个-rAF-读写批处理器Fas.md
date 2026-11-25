---
title: [PER-1008] 手写一个 rAF 读写批处理器（FastDom 简化版）
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-1008：手写一个 rAF 读写批处理器（FastDom 简化版）

**答**：
- 需求：实现 fastdom 对象：read(fn)/write(fn) 排队，微任务边界统一执行——一次 flush 中先执行全部 read 再全部 write，同一帧多次调用只 flush 一次；measure(fn) 立即返回 Promise（在下一批 read 中执行并返回结果）；clear(id) 取消。
- 边界：read 中不得再调 write（违规记录告警但继续）；flush 顺序按加入序；返回的 handle 可取消未执行任务。
- 评分点：读写分批；rAF 合帧；measure Promise 化；clear 取消

```javascript
const fastdom = (() => {
  const reads = [], writes = []; let scheduled = false; let id = 0;
  function flush() {
    scheduled = false;
    const rs = reads.splice(0), ws = writes.splice(0);
    rs.forEach(r => r.fn());            // 先批量读
    ws.forEach(w => w.fn());            // 再批量写
  }
  function schedule() {
    if (!scheduled) { scheduled = true;
      requestAnimationFrame(flush); }
  }
  return {
    read(fn) { const h = { id: ++id, fn, kind: 'r' }; reads.push(h); schedule(); return h; },
    write(fn) { const h = { id: ++id, fn, kind: 'w' }; writes.push(h); schedule(); return h; },
    measure(fn) {
      return new Promise(res => {
        this.read(() => res(fn()));     // 在 read 批中执行并回传
      });
    },
    clear(h) {
      const q = h.kind === 'r' ? reads : writes;
      const i = q.indexOf(h); if (i >= 0) q.splice(i, 1);
    },
  };
})();
```
