---
title: [V3-484] Vue 应用的内存面：组件实例与 effect 泄漏排查
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 面试题, 性能]
type: 面试题
---

## V3-484：Vue 应用的内存面：组件实例与 effect 泄漏排查

**答**：
- 泄漏面清单：全局注册的 watch/computed 未 stop、事件总线订阅未解绑、定时器闭包持有组件实例、Provide 大对象被深层组件闭包持有、keep-alive 缓存无 max
- Vue 特有的 retain 链：effect 持有组件 instance（渲染 effect 不手动停则实例不回收）——卸载时框架自动停渲染 effect，但「自建 effectScope 外的手动 effect」要自己管
- 排查路径：Heap Snapshot 搜组件名 → Retainers 看 effect/Dep 链 → 定位未 stop 的副作用源头；Detached DOM + VueComponent 构造器堆积是经典指纹
- effectScope：把组件内自建副作用装进 scope，onScopeDispose 统一清理——比逐个 onUnmounted 少出错；跨组件共享副作用用独立 scope 显式 stop
- keep-alive 治理：max 上限必设；大缓存组件（图表类）activated 时重建数据、deactivated 释放（数据大但状态不需要保留的场景）

```javascript
// effectScope 统一管理
const scope = effectScope();
scope.run(() => {
  watch(source, cb);
  const c = computed(() => heavy());
});
onUnmounted(() => scope.stop());   // 一键清理 scope 内所有副作用
```
