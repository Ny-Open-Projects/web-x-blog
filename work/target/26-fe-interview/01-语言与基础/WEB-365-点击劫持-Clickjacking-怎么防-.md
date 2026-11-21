---
title: [WEB-365] 点击劫持（Clickjacking）怎么防？X-Frame-Options 和 frame-ancestors 差在哪？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 安全]
type: 面试题
---

## WEB-365：点击劫持（Clickjacking）怎么防？X-Frame-Options 和 frame-ancestors 差在哪？
**答**：
- 攻击：透明 iframe 叠在你的页面上，诱导用户点击实际点到 iframe 内的"转账/授权"按钮。
- X-Frame-Options: DENY / SAMEORIGIN 是老标准，只管 iframe；CSP frame-ancestors 功能等价但更细（可指定域名列表），且现代浏览器里后者优先。
- JS 兜底：top !== self 时提示用户，但可靠的是响应头；关键操作再加二次确认/手势验证。

```javascript
// 响应头（二选一或都配）
// X-Frame-Options: DENY
// Content-Security-Policy: frame-ancestors 'none'
const antiClickjack = () => {
  if (window.top !== window.self) {           // JS 兜底
    document.body.style.display = 'none';
    alert('检测到被嵌套，请直接访问官网');
  }
};
console.log('支付/授权页必配 frame-ancestors');
```
