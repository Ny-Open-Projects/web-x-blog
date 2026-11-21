---
title: [SCN-484] 笔试题——实现多标签工作台（KeepAlive/LRU 释放/状态快照恢复）？
date: 2026-11-20
categories: [场景实战]
tags: [前端面试, 笔试题, 场景实战]
type: 笔试题
---

## SCN-484：手写工作台页签：KeepAlive 状态保持、LRU 释放上限、快照恢复

**需求与边界**：
- 输入：页签开合事件；输出：页签栈与组件缓存管理。
- 边界要求：① 页签切换组件状态保持（滚动/表单/筛选）；② 活跃页签上限（>10 LRU 释放最久未用）；③ 释放前状态快照（激活时恢复）；④ 未保存内容关闭提示。

**答**：
```javascript
class TabManager {
  constructor({ maxLive = 10 }) {
    this.tabs = []; this.live = new Map();     // tabId → component 缓存
    this.maxLive = maxLive;
  }
  activate(tabId) {
    touch(tabId);                              // LRU 更新
    const tab = this.tabs.find(t => t.id === tabId);
    if (tab.dirty) warnUnsaved();              // 未保存提示
    if (!this.live.has(tabId) && tab.snapshot)
      restore(tabId, tab.snapshot);            // 快照恢复
  }
  open(route) {
    const id = route.path + JSON.stringify(route.params);
    if (!this.tabs.find(t => t.id === id)) this.tabs.push({ id, ...route });
    this.activate(id);
    if (this.live.size > this.maxLive) {
      const victim = lruOldest(this.live);     // LRU 释放
      this.release(victim);
    }
  }
  release(tabId) {                             // 释放：快照+卸载
    const tab = this.tabs.find(t => t.id === tabId);
    tab.snapshot = serialize(getState(tabId)); // 快照落 idb
    this.live.delete(tabId);                   // 卸载组件释放内存
  }
  close(tabId) {
    const tab = this.tabs.find(t => t.id === tabId);
    if (tab?.dirty && !await confirmClose()) return false;
    this.release(tabId);
    this.tabs = this.tabs.filter(t => t.id !== tabId);
    return true;
  }
}
// dirty 检测：表单/编辑器脏数据标记（离开拦截）。
// 快照：serialize 状态 → idb，激活时 hydrate。
```

**评分点**:
- KeepAlive 状态保持 + LRU 上限释放（内存控制）。
- 释放前快照/激活时恢复（LRU 释放不丢状态）。
- dirty 检测与关闭拦截。
- 页签 id = 路由+参数（同路由多实例）。
