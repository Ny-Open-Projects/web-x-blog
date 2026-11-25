---
title: [DP-515] 笔试：手写乐观列表对账
date: 2026-11-21
categories: [设计模式]
tags: [前端面试, 笔试题, 设计模式]
type: 笔试题
---

## DP-515：笔试：手写乐观列表

**答**：实现乐观列表的对账逻辑：① 乐观插入：tempId 消息立即入列（pending 标记）；② 服务端确认：tempId → 真实 id 替换（保持位置）；③ 去重：服务端推送与乐观项重叠（同 content 且 pending——去重合并）；④ 失败移除：乐观项失败 → 移除 + 通知；⑤ 排序恢复：插入时按时间排序（乱序到达的消息按 ts 插入正确位置）。写出实现。

```javascript
class OptimisticList {
  #items = []; #subs = new Set();
  optimisticAdd(item) {
    const temp = { ...item, id: `temp-${crypto.randomUUID()}`, pending: true };
    this.#insertSorted(temp);                          // 按时间排序插入
    this.#notify();
    return temp.id;
  }
  confirm(tempId, real) {
    const i = this.#items.findIndex((x) => x.id === tempId);
    if (i < 0) return;
    // 去重: 真实消息已由推送到达
    const dup = this.#items.findIndex((x) => x.id === real.id);
    if (dup >= 0) { this.#items.splice(i, 1); return; }   // 乐观项删除, 保留真实项
    this.#items[i] = { ...real, pending: false };      // id 替换保位置
    this.#notify();
  }
  fail(tempId) {
    this.#items = this.#items.filter((x) => x.id !== tempId);
    this.#notify();
  }
  receivePush(msg) {                                   // 推送到达: 去重乐观项
    const dupIdx = this.#items.findIndex((x) => x.pending && x.content === msg.content);
    if (dupIdx >= 0) this.#items[dupIdx] = msg;
    else this.#insertSorted(msg);
    this.#notify();
  }
  #insertSorted(item) {
    const i = this.#items.findIndex((x) => x.ts > item.ts);
    i < 0 ? this.#items.push(item) : this.#items.splice(i, 0, item);
  }
}
```

**评分点**：
- tempId → 真实 id 的替换保位置（乐观确认）
- 推送与乐观项的去重（双通道重叠）
- 失败移除 + 排序插入（乱序到达按 ts）
- pending 标记驱动 UI（视觉区分乐观态）
