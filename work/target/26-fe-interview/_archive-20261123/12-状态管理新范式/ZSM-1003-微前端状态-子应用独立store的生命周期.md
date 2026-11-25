---
title: [1003] 微前端子应用 store 的生命周期管理
date: 2026-11-17
categories: [状态管理新范式]
tags: [前端面试, 面试题, 微前端]
type: 面试题
---

## 1003：微前端子应用 store 的生命周期管理

**答**：
- 生命周期规则：子应用 store 随应用创建/销毁（mount 创建实例、unmount 销毁——防内存常驻）；主应用的全局数据（用户态）不进子应用 store（注入引用）。
- 销毁的完整性：store 销毁要连带「订阅清理」（事件总线退订/定时器/Query 缓存——见 QueryClient 生命周期卡）；生命周期测试（mount/unmount 20 次内存不增长——泄漏回归测试）。
- 热切换场景：子应用 A/B 版本切换（灰度）——两版本 store 不共存（切换即销毁重建——状态不迁移，用户回到页面初始态可接受）。
- 追问钩子：为什么子应用 store 不能常驻（unmount 后保留以便快速回访）？——常驻的 store 持有 DOM 引用/定时器/闭包 = 内存泄漏；且回访时数据已过期（用户态变了）——「销毁重建」比「保留复用」更安全。

```ts
export function mount(el, deps) {
  const store = createSubStore(deps);              // 创建
  const unsubs = [bus.subscribe('order.updated', store.onOrderUpdated)];
  // ...渲染
  return () => {                                    // unmount
    unsubs.forEach(u => u());                       // 退订
    store.destroy();                                // 销毁 store
  };
}
```
