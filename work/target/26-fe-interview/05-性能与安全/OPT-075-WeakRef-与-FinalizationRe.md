---
title: [OPT-075] WeakRef 与 FinalizationRegistry 是什么？为什么慎用？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-075：WeakRef 与 FinalizationRegistry 是什么？为什么慎用？

**答**：
- `WeakRef` 创建不阻止 GC 的弱引用：缓存/伴生数据挂在对象上，宿主回收后引用自动变 undefined；`WeakMap/WeakSet` 能满足的场景优先用它们（更简单且有确定语义）。
- `FinalizationRegistry` 在对象被回收后收到回调，理论可用于清理外部资源（句柄/日志），但**回调时机不可控**，绝不放业务逻辑。
- 慎用三个理由：回调可能永不执行（页面关闭/GC 策略）、时机不确定导致调试困难、误用反而延长对象生命周期（注册表本身持有引用）。
- 合法用途有限：级联缓存失效、调试泄漏的观测探针，且必须配合显式清理主路径。

```javascript
// 一一对应：WeakRef 缓存 + FinalizationRegistry 观测（附显式主路径）
// 用途一：大资源的软缓存——内存压力下允许自动失效
const cache = new Map();          // key -> WeakRef
const registry = new FinalizationRegistry((key) => {
  // 对象被回收后清掉失效的 ref，防止 Map 无限膨胀
  // 注意：这只是辅助清理，不能依赖它做正确性
  cache.delete(key);
});
function setCached(key, bigObj) {
  cache.set(key, new WeakRef(bigObj));
  registry.register(bigObj, key);
}
function getCached(key) {
  const ref = cache.get(key);
  const obj = ref?.deref();
  if (!obj) cache.delete(key); // 已被回收，顺手清 ref
  return obj;                  // 可能为 undefined，调用方必须处理 miss
}

// 正确姿势：显式清理才是主路径，WeakRef 只是兜底
class ImageLayer {
  dispose() {
    this.texture = null;       // 显式释放
    registry.unregister?.(this); // 如果注册过就反注册
  }
}

// 慎用示例（反面）：把业务回调整进 FinalizationRegistry
// registry.register(conn, () => conn.close())  <- 错误！回调可能永不执行，
// 连接可能一直不关。外部资源必须在 try/finally 或 dispose 里显式关闭。
```
