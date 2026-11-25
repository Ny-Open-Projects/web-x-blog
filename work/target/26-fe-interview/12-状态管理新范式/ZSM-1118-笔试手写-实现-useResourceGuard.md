---
title: [1118] 笔试手写：实现 useResourceGuard
date: 2026-11-22
categories: [状态管理新范式]
tags: [前端面试, 笔试题, Hook]
type: 笔试题
---

## 1118：笔试手写：实现 useResourceGuard

**答**：未保存状态离开拦截。实现 createResourceGuard()：dirty(fields) 标记脏字段；clean(field) 清除；isDirty() 判定；guard(callback) 返回包装 beforeunload/路由守卫的统一接口——脏时返回拦截回调（callback 收到脏字段清单），干净时直接放行。reset() 全清。

```js
function createResourceGuard() {
  const dirty = new Set();
  return {
    dirty: (...fields) => fields.forEach(f => dirty.add(f)),
    clean: (...fields) => fields.forEach(f => dirty.delete(f)),
    isDirty: () => dirty.size > 0,
    guard(callback) {
      return () => {
        if (!dirty.size) return true; // 干净放行
        callback?.([...dirty]); // 脏：交给 UI 确认（留下/放弃）
        return false;
      };
    },
    reset: () => dirty.clear(),
  };
}
// 用法：window.onbeforeunload = g.guard(fields => confirm(`未保存: ${fields}`))
```

**评分点**：
- 脏字段集合而非单一布尔（可提示具体未保存什么）
- guard 返回统一拦截接口（beforeunload 与路由守卫复用）
- 干净时直接放行不弹框（最小打扰原则）
- 能讨论：与草稿自动保存（useDraftAutosave）的组合——自动保存降低 dirty 窗口
