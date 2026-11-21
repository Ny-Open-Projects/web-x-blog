---
title: [H5-171] 微前端场景下 Web Components 如何做集成层？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-171：微前端场景下 Web Components 如何做集成层？
**答**：
- 契约：子应用把入口封装成自定义元素（内部完成挂载/路由/卸载），主应用只认 `<micro-app-xxx>` 标签——**与框架无关**，主应用不需要知道子应用是 Vue 还是 React。
- 输入输出协议：attribute 传可序列化输入，CustomEvent 输出（必须 `composed: true` 才能穿出 Shadow DOM），复杂共享状态走全局 context。
- 样式隔离靠 Shadow DOM 或子应用 scoped；坑：Shadow DOM 内的 portal/modal 要挂到宿主文档、全局对象（window/router）需要包装。
- 与 qiankun 等 JS 沙箱方案对比：WC 自带样式边界但**没有 JS 沙箱**，复杂场景两者结合；共享依赖用 externals 避免每个子应用带一份框架。

```javascript
// 子应用出口：把整个子应用包成一个自定义元素 —— 与主框架解耦的契约
class MicroApp extends HTMLElement {
  static observedAttributes = ['user-id'];
  connectedCallback() {
    if (this.mounted) return;          // 防重复挂载（微前端常见坑）
    this.mounted = true;
    this.host = document.createElement('div');
    this.append(this.host);
    // 子应用内部完成 createApp/mount（以 Vue 为例）
    // this.app = createApp(UserModule).mount(this.host);
    this.dispatchEvent(new CustomEvent('app:ready', { bubbles: true, composed: true }));
  }
  disconnectedCallback() {
    this.app?.unmount();               // 卸载必须彻底：定时器/全局事件/路由副作用
    this.mounted = false;
  }
  attributeChangedCallback(name, _, val) {
    // attribute 输入：主应用改属性 → 子应用响应
    if (name === 'user-id' && this.app) this.app.updateProps({ userId: val });
  }
}
customElements.define('micro-app-user', MicroApp);

// 输出协议：CustomEvent 必须 composed: true 才能穿出 Shadow DOM
function emit(name, detail) {
  this.dispatchEvent(new CustomEvent(name, {
    bubbles: true, composed: true, detail,
  }));
}
// emit.call(this, 'app:navigate', { path: '/orders' });

// 主应用侧：像用普通标签一样集成，完全不知道子应用用什么框架
document.body.insertAdjacentHTML('beforeend',
  '<micro-app-user user-id="42"></micro-app-user>');
document.addEventListener('app:navigate', (e) => {
  console.log('主应用路由接管', e.detail.path);
});

// 面试口径：
// 1) WC 做微前端壳的优势：浏览器原生契约（define 即隔离边界）、框架无关
// 2) 样式隔离靠 Shadow DOM 或构建期 scoped；Shadow 内 portal/modal 要挂宿主文档
// 3) 共享依赖用 externals，避免每个子应用带一份 Vue/React
// 4) 与 qiankun 对比：WC 有样式边界但没有 JS 沙箱，复杂场景两者结合
```
