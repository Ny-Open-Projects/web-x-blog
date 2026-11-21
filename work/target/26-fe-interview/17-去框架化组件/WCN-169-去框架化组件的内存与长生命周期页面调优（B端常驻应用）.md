---
title: [WCN-169] 去框架化组件在长生命周期页面（B 端常驻应用）的内存调优怎么做的？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 选型与工程落地]
type: 面试题
---

## WCN-169：去框架化组件在长生命周期页面（B 端常驻应用）的内存调优怎么做的？

**答**：
- B 端页面常驻数小时，内存问题累积放大——组件层常见泄漏源：全局 signal 订阅未 dispose（WCN-018）、事件委托绑 document 未清、第三方渲染实例未 destroy、shadowRoot 里缓存大数据。
- 防御机制：组件基类统一 dispose 注册表（基类提供 `onCleanup(fn)`，disconnected 时统一执行）；开发模式检测——元素 detach 后 1 秒仍被引用（WeakRef + 定期检查）则 console.warn 泄漏。
- 常驻页策略：多实例组件池复用（Table 单元格编辑器等重组件池化，避免反复创建影子树）；全局单例组件（modal host）复用同一实例切换内容。
- 观测：Performance Monitor 的 DOM Nodes/JS heap 曲线 + 组件实例计数（registry Map 统计 tag 实例数），长跑测试（8 小时脚本循环操作）验证无增长。
- 大对象隔离：行数据只存 id，详情按需拉取，避免每行持有完整对象闭包。

```javascript
// 基类统一清理 + 泄漏检测
class LongLivedElement extends HTMLElement {
  #cleanups = [];
  onCleanup(fn) { this.#cleanups.push(fn); }
  disconnectedCallback() {
    this.#cleanups.forEach((fn) => fn());
    this.#cleanups = [];
    // 开发模式泄漏探测：1 秒后仍可达则告警
    if (DEV) {
      const ref = new WeakRef(this);
      setTimeout(() => {
        if (ref.deref()) console.warn('疑似泄漏：detach 后仍被引用', this.tagName);
      }, 1000);
    }
  }
}
```
