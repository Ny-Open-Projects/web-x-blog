---
title: [WCN-221] 2026 年还需要 Web Components polyfill 吗？策略是什么？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-221：2026 年还需要 Web Components polyfill 吗？策略是什么？
**答**：
- 三大标准在现代浏览器全量支持——常规业务不再需要 polyfill。
- 仍需的场景：老旧 WebView（企业内嵌设备）、需要 CE v0 特性的历史包袱。
- 策略：特性检测（'customElements' in window）条件加载，且 polyfill 版本冻结在已知稳定版。
- 构建产物双轨：现代 bundle 不含 polyfill，legacy bundle 才含。

```javascript
<script>
if (!('customElements' in window)) {
  document.write('<script src="/polyfills/webcomponents-bundle.js"><\\/script>');
}
</script>
r
```
