---
title: [PER-081] 第三方脚本权限如何收敛？沙箱 iframe 方案怎么落地？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-081：第三方脚本权限如何收敛？沙箱 iframe 方案怎么落地？

**答**：
- 默认在主页面 `<script>` 引入的第三方脚本拥有**同源全权**：可读 Cookie、DOM、发请求冒充用户；应默认视为不可信。
- 收敛手段按强度递进：CSP 限制其能连的域 → 沙箱 iframe（`sandbox` 属性裁剪权限）→ 自托管代理脚本（拿不到原始第三方更新权）。
- 沙箱 iframe 落地：第三方功能（客服、地图、统计）装进 `sandbox="allow-scripts"` 的 iframe，无 `allow-same-origin` 时它拿不到父页面 DOM 与 Cookie，跨窗通信只走 postMessage。
- 需要跳出 iframe 的交互（弹全屏层）用 postMessage 请求父页面代为执行，能力面最小化。

```html
<!-- 客服组件装进沙箱 iframe：只有脚本执行权，无同源权无表单无弹窗 -->
<iframe
  src="https://support-widget.example.com/embed?site=mysite"
  sandbox="allow-scripts"
  referrerpolicy="no-referrer"
  style="width:360px;height:560px;border:0"
  title="客服"></iframe>
```

```javascript
// 父页面：只暴露最小能力给 iframe，走白名单消息
window.addEventListener('message', (e) => {
  if (e.origin !== 'https://support-widget.example.com') return; // 来源白名单
  const actions = {
    'widget:open-fullscreen': () => document.body.classList.add('widget-expanded'),
    'widget:close': () => document.body.classList.remove('widget-expanded'),
    'widget:track': () => {}, // 需要埋点时也由父页面统一发，iframe 不直接上报
  };
  const data = e.data ?? {};
  if (typeof data.type === 'string' && actions[data.type]) actions[data.type]();
});
// 注意：iframe 内第三方脚本拿不到 document.cookie、localStorage 与父页面 DOM
```
