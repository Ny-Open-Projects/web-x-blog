---
title: [PER-671] 手写一个小程序 setData 合并节流器：高频更新（滚动/进度）按帧合并为一次路径级 setData
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-671：手写一个小程序 setData 合并节流器：高频更新（滚动/进度）按帧合并为一次路径级 setData

**答**：
- 在 670 基础上实现高频场景：滚动进度、倒计时等每帧变化的值，不能每帧 setData——收集器在 rAF（小程序用定时器模拟）周期内合并所有路径更新，一次 setData。
- 要点：路径合并时数组项更新要保留索引（`list[3].x` 与 `list[4].x` 合并不冲突）；同一路径多次更新取最后值；flush 时机用 `wx.nextTick` 或 50ms 定时器。
- 边界：新字段与路径更新混用时以路径优先（范围小）；列表插入（shift/unshift）不能路径化，要整段更新并重算索引——区分可路径化与结构变化两类更新。
- 评分点：结构变化与路径更新的区分。

```javascript

class FrameBatcher {
  constructor(page, intervalMs = 50) {
    this.page = page; this.map = new Map(); this.timer = null;
  }
  set(path, value) {
    this.map.set(path, value);                                  // 同路径取最后值
    if (!this.timer) this.timer = setTimeout(() => this.flush(), 50);
  }
  spliceList(listPath, insertFn) {                              // 结构变化：整段更新
    this.map.set(listPath, { __structural: true, apply: insertFn });
    this.flush();
  }
  flush() {
    clearTimeout(this.timer); this.timer = null;
    const payload = {}; const structs = [];
    for (const [path, v] of this.map) {
      if (v && v.__structural) structs.push(v);                 // 结构变化最后处理
      else payload[path] = v;
    }
    for (const s of structs) {
      const list = s.apply(this.page.data[s.listPath ?? 'list']);
      payload[s.path ?? 'list'] = list;                         // 重算索引整段更新
    }
    this.map.clear();
    this.page.setData(payload);                                 // 一次跨线程通信
  }
}
// 用法：batcher.set('progress', 0.73); batcher.set('progress', 0.81); -> 一次 setData progress=0.81
```
