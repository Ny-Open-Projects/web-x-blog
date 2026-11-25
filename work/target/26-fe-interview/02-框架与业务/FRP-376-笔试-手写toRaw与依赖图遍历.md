---
title: [FRP-376] 笔试：手写 toRaw 与依赖图遍历（调试 dump）
date: 2026-11-21
categories: [框架原理]
tags: [前端面试, 笔试题, 架构]
type: 笔试题
---

## FRP-376：笔试：手写 toRaw 与依赖图 dump

**答**：在响应式内核上实现调试工具：① `toRaw(obj)`：从 Proxy 找回原始对象（WeakMap 反查 + 深层递归 toRaw）；② `dumpDeps()`：导出依赖图（哪个 effect 订阅哪些 key、哪些 key 被哪些 effect 订阅——双向视图）；③ `whoTriggers(key)`：给定 key 找会触发的 effect；④ `effectCount()`：活跃 effect 数（泄漏探针——只增不减告警）；⑤ dump 输出结构设计（便于人读与 diff）。写出实现。

```javascript
const rawToProxy = new WeakMap();
const proxyToRaw = new WeakMap();

function toRaw(obj) {
  const raw = proxyToRaw.get(obj);
  if (!raw) return obj;
  // 深层: 遍历原始对象属性, 嵌套 Proxy 继续反查
  const out = Array.isArray(raw) ? raw.slice() : { ...raw };
  for (const k of Object.keys(out)) {
    const v = out[k];
    if (typeof v === 'object' && v !== null) out[k] = toRaw(proxyToRaw.get(v) ?? v);
  }
  return out;
}

function dumpDeps() {
  const byEffect = [], byKey = [];
  for (const [target, keys] of depMap) {
    for (const [key, effects] of keys) {
      byKey.push({ key: `${targetName(target)}.${String(key)}`, effects: [...effects].map((e) => e.name ?? 'anonymous') });
      for (const e of effects) {
        let entry = byEffect.find((x) => x.effect === (e.name ?? 'anonymous'));
        entry ? entry.keys.push(key) : byEffect.push({ effect: e.name ?? 'anonymous', keys: [key] });
      }
    }
  }
  return { byEffect, byKey };      // 双向视图: 人读 byEffect, diff byKey
}
function whoTriggers(target, key) {
  return [...depMap.get(target)?.get(key) ?? []].map((e) => e.name ?? 'anonymous');
}
function effectCount() { return effectRegistry.size; }   // 只增不减 → 泄漏
```

**评分点**：
- toRaw 的 WeakMap 双向映射与深层递归
- 双向依赖图视图（effect 视角/key 视角）
- whoTriggers 的归因用途（改这个 key 会炸谁）
- effectCount 泄漏探针语义

## 变体与延伸（补充）

**变体与延伸**：

1. toRaw 的深层递归为什么不能直接返回原对象引用？ → 嵌套属性可能仍是 Proxy，直接返回外层 raw 会让内层继续响应式；要么原地替换（有副作用），要么克隆新对象，面试要讲清这个取舍。
2. dumpDeps 里用 targetName 当 key 有什么风险？ → 同名对象会撞 key 让 diff 混淆，而且 WeakMap 本身不可遍历；应给每个 target 分配自增 id，名字只作附加标签。
3. effectCount 为什么能当泄漏探针？ → 正常卸载时 cleanup 会从 registry 注销，计数应回落；持续单调上升说明 effect 没被 stop，常见于组件销毁未清理或在 effect 里又创建 effect。
