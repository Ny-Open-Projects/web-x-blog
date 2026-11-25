---
title: [MP-376] 笔试：手写 globalData 响应式 store
date: 2026-11-21
categories: [小程序]
tags: [前端面试, 笔试题, 架构]
type: 笔试题
---

## MP-376：笔试：手写响应式 store

**答**：实现小程序全局 store：① 基于 getApp().globalData——Proxy 代理（写时通知订阅者）；② 页面订阅：`useStore(page, key, mapper)`——onShow 同步 + 订阅推送双通道（订阅兜底跨页、onShow 兜底热启动）；③ 卸载清理（onUnload 取消订阅）；④ 选择器（只订阅关心的 key——减少 setData）；⑤ 与「纯 onShow 拉取」方案的对比。写出实现。

```javascript
export function createStore(globalData) {
  const subs = new Map();        // key -> Set<fn>
  return new Proxy(globalData, {
    set(t, key, v) {
      const old = t[key];
      t[key] = v;
      if (!Object.is(old, v)) subs.get(key)?.forEach((fn) => fn(v, old));
      return true;
    },
  });
}
App({ onLaunch() { this.store = createStore(this.globalData); } });

// 页面绑定
export function useStore(page, key, mapper = (v) => v) {
  const sync = () => { const v = getApp().store[key]; page.setData({ [key]: mapper(v) }); };
  const unsub = getApp().storeSubscribe?.(key, sync);
  // 简化: 用 wx 事件桥
  const handler = () => sync();
  getApp().event.on(`store:${key}`, handler);
  sync();                                            // 订阅即同步
  const origUnload = page.onUnload;
  page.onUnload = function () {
    getApp().event.off(`store:${key}`, handler);
    origUnload?.call(this);
  };
}
// 对比: 纯 onShow 拉取 — 简单可靠但「同栈页面打开时不刷新」(目标页不是栈顶);
//        订阅推送 — 实时但需管理清理. 组合: 订阅为主 + onShow 兜底(热启动).
```

**评分点**：
- Proxy 通知语义（写时触发订阅者）
- 双通道设计（订阅实时 + onShow 兜底热启动）
- 卸载清理（订阅泄漏防护）
- selector 映射（减少 setData 范围）与两方案取舍

## 变体与延伸（补充）

**变体与延伸**：

1. 页面绕过 store 直接改 globalData 会怎样？ → Proxy 根本不会收到通知，订阅者全都不更新；必须约定只经 store 写入，或把 globalData 整体替换成代理并封掉原始引用。
2. 已经有订阅推送了，为什么还要 onShow 兜底？ → 冷启动或从后台恢复时订阅链已断，onShow 拉一次可纠正；同栈非栈顶页面本就收不到实时更新，回到栈顶也靠 onShow 对齐。
3. 直接给 page.onUnload 赋值有什么隐患？ → 会顶掉业务已有的 onUnload，导致别的清理或埋点静默失效；必须先保存原函数再链式调用，这也是所有页面生命周期劫持的通则。
