---
title: [XP-207] 小程序与 Native 通信：wx API 桥接原理
date: 2026-11-21
categories: [跨端]
tags: [前端面试, 笔试题, 27]
type: 笔试题
---

## XP-207：小程序与 Native 通信：wx API 桥接原理

**答**：
- 题目：wx.xxx API 桥接原理——逻辑层调用 → Native 桥（JS Bridge）→ 原生实现 → 回调返回。实现一个简易 wx 桥。
- 思路：wx 对象 = API 注册表（方法名 → Native 通道）→ 调用时序列化参数 → Native 回调（success/fail/complete）。
- 评分点：桥接流程；回调约定（success/fail/complete）；批量调用优化。

```javascript
class MiniProgramBridge {
  constructor(native) { this.native = native; this.callbacks = new Map(); }
  registerAPI(name, nativeMethod) {                           // API 注册
    this[name] = (options = {}) => {
      const id = genId();
      const { success, fail, complete, ...params } = options;
      this.callbacks.set(id, { success, fail, complete });     // 回调注册
      this.native.call(name, id, params);                      // Native 调用
    };
  }
  onNativeCallback(id, result) {                              // Native 回调
    const { success, fail, complete } = this.callbacks.get(id) ?? {};
    result.errMsg?.includes(':ok') ? success?.(result) : fail?.(result);
    complete?.(result);
    this.callbacks.delete(id);                                 // 清理
  }
}
// 批量优化：wx.setStorage 批量合并（HW-684 JSBridge 批量调用复用）
```
