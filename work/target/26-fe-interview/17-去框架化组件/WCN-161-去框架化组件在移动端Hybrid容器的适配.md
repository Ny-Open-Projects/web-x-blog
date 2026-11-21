---
title: [WCN-161] 去框架化组件在移动端 Hybrid / WebView 容器的适配：性能与桥接怎么处理？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 选型与工程落地]
type: 面试题
---

## WCN-161：去框架化组件在移动端 Hybrid/WebView 容器的适配怎么处理？

**答**：
- 兼容面：老 WebView（Android 5~7 级 Chromium）可能缺 DSD/adoptedStyleSheets/delegatesFocus——构建时用 browserslist 双产物（modern 走原生，legacy 走 polyfill + style 注入降级）。
- 性能差异：移动端 GC 与解析更慢——组件产物压缩 + 更激进的视口懒加载；避免影子树内大列表（配合原生 scroll 复用）。
- 原生桥接：组件事件 → JSBridge 调用原生能力（相机/支付）。设计上组件只派发 `wc-native-request` 事件，容器层适配器（App 内注入）监听并调用 bridge，组件保持容器无关。
- 数据注入：App 初始数据（登录态/主题）由容器通过 property 注入根组件（`app-root.user = {...}`），向下经 context/signal 分发。
- 调试：WebView 远程调试（Chrome inspect / Safari Web Inspector）配合 __wcDebug 助手；灰度用容器版本号 + 组件版本号二维上报。

```javascript
// 容器无关的原生请求模式
class ScanButton extends HTMLElement {
  connectedCallback() {
    this.shadowRoot.querySelector('button').onclick = () => {
      this.dispatchEvent(new CustomEvent('wc-native-request', {
        bubbles: true, composed: true,
        detail: { action: 'scan', fallback: 'input' },   // 声明式请求原生能力
      }));
    };
  }
}
// App 容器层适配器（注入的胶水）
window.addEventListener('wc-native-request', (e) => {
  const { action } = e.detail;
  window.NativeBridge?.call(action)   // JSBridge
    .then((r) => e.target.dispatchEvent(new CustomEvent('wc-native-result', { detail: r, composed: true })));
});
```
