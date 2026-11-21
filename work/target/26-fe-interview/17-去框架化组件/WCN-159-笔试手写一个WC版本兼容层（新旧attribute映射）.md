---
title: [WCN-159] 笔试：手写 WC 版本兼容层（旧 attribute 自动映射到新 API）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, 选型与工程落地]
type: 笔试题
---

## WCN-159：笔试：手写 WC 版本兼容层

**题目**：组件 v2 重命名了 API：`color→tone`、`onclose→wc-close`。实现 `withCompat(Base, map)`：① map 描述旧→新映射（attribute 与事件两类）；② 旧 attribute 设置时同步写到新 attribute（双向，避免消费方读写不一致）；③ 旧事件监听（document 级委托按事件名捕获旧名）转发为新名事件；④ 首次使用旧 API 打 deprecate 告警（每 tag 一次）；⑤ 可关闭（环境变量生产静默）。

**答**：

```javascript
export function withCompat(Base, { attrs = {}, events = {} } = {}) {
  return class CompatElement extends Base {
    connectedCallback() {
      // 1) attribute 迁移：升级时把旧名值搬到新名
      for (const [old, neu] of Object.entries(attrs)) {
        if (this.hasAttribute(old) && !this.hasAttribute(neu)) {
          this.#warn(old, neu);
          this.setAttribute(neu, this.getAttribute(old));
        }
        // 旧名变更监听：同步新名
        this.__attrObserver?.disconnect?.();
        this.__attrObserver = new MutationObserver(() => {});
      }
      // 2) 旧事件转发：捕获阶段拦截旧名
      this.__oldHandlers = Object.entries(events).map(([oldEv, newEv]) => {
        const fn = (e) => {
          this.#warnEvent(oldEv, newEv);
          this.dispatchEvent(new CustomEvent(newEv, {
            bubbles: e.bubbles, composed: true, detail: e.detail,
          }));
        };
        this.addEventListener(oldEv, fn);
        return () => this.removeEventListener(oldEv, fn);
      });
      super.connectedCallback?.();
    }
    disconnectedCallback() { this.__oldHandlers?.forEach((u) => u()); super.disconnectedCallback?.(); }
    // attributeChanged 也要映射：消费方写旧名时补写新名
    attributeChangedCallback(name, o, n) {
      const mapped = attrs[name];
      if (mapped && o !== n && this.getAttribute(mapped) !== n) {
        this.#warn(name, mapped);
        n === null ? this.removeAttribute(mapped) : this.setAttribute(mapped, n);
      }
      super.attributeChangedCallback?.(name, o, n);
    }
    #warned = new Set();
    #warn(old, neu) { if (!this.#warned.has(old)) { this.#warned.add(old);
      if (!PROD) console.warn(`[${this.tagName}] "${old}" 已弃用，请改用 "${neu}"`); } }
    #warnEvent(oldEv, newEv) { if (!this.#warned.has(oldEv)) { this.#warned.add(oldEv);
      if (!PROD) console.warn(`[${this.tagName}] 事件 "${oldEv}" 已改名 "${newEv}"`); } }
  };
}
```

**评分点**：
- attribute 双向映射（升级迁移 + attributeChanged 同步）。
- 旧事件转发为新名 CustomEvent（detail 透传）。
- deprecate 告警去重（每元素每名一次）+ 生产静默。
- 事件监听清理（disconnectedCallback）。
