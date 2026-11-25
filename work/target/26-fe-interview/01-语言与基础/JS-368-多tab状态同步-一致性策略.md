---
title: [JS-368] 多 tab 状态同步：一致性策略
date: 2026-11-21
categories: [JavaScript]
tags: [前端面试, 面试题, 并发]
type: 面试题
---

## JS-368：多 tab 状态同步：一致性策略

**答**：
- 同步通道选型：BroadcastChannel（现代首选，同源实时）、storage 事件（兼容兜底）、SharedWorker（需要中心协调者时）、Web Locks（互斥操作）——按拓扑选，中心化场景 SharedWorker 最干净
- 一致性模型：多 tab 场景多数是「最终一致」（设置/登录态广播），少数需要「互斥写」（同一份草稿编辑权）——先用 Web Locks 抢「编辑权」，别的 tab 变只读
- 冲突处理：tab A 与 B 同时改同一设置——LWW（时间戳新者胜）适合简单设置；带版本号拒绝旧写适合关键数据；提示用户手动合并是最后手段
- 状态源设计：持久层（IndexedDB）为唯一真源，tab 内存态只是缓存——任何 tab 写入先落库再广播，其他 tab 以库为准刷新（避免广播丢失导致漂移）
- 登录态专项：token 刷新单飞（Web Locks + 广播新 token）、登出全 tab 踢回登录——这是多 tab 最常见的业务一致性需求

```javascript
// 编辑权互斥
async function acquireEditLock(docId) {
  return navigator.locks.request(`doc-${docId}`, { ifAvailable: true }, (lock) => {
    if (!lock) return false;
    readOnly = false;                        // 我获得编辑权
    return new Promise(res => lock.addEventListener('release', () => { readOnly = true; res(true); }));
  });
}
// 广播: 任何 tab 保存 → 落库 → 广播 → 其他 tab 刷新
const bc = new BroadcastChannel('docs');
bc.onmessage = ({ data }) => data.type === 'saved' && reloadIfOpen(data.docId);
```
