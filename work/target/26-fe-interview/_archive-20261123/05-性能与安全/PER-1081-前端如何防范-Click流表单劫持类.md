---
title: [PER-1081] 前端如何防范 Click流/表单劫持类攻击（表单自动填充与浏览器扩展）
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1081：前端如何防范 Click流/表单劫持类攻击（表单自动填充与浏览器扩展）

**答**：
- 恶意扩展与页面注入可监听表单输入窃取数据（密码/卡号）。
- 防御：敏感输入用 autocomplete 隔离（new-password/one-time-code）、考虑自定义安全键盘（虚拟键盘 + canvas 绘制，适用于金融）、避免敏感数据进 localStorage。
- 检测：MutationObserver 监听输入框被替换/覆盖的异常（透明层覆盖攻击）；CSP 限制注入脚本能力有限，关键还是最小权限容器。
- 合规：金融场景的安全键盘还要防截屏（部分平台 API）与模拟点击。

```javascript
// 覆盖攻击检测
function overlayGuard(input) {
  const check = () => {
    const r = input.getBoundingClientRect();
    const topEl = document.elementFromPoint(r.left + r.width / 2, r.top + r.height / 2);
    if (topEl && !input.contains(topEl) && topEl !== input &&
        !input.parentElement.contains(topEl))
      report({ type: 'overlay-suspect', covering: topEl.tagName });
  };
  const io = new IntersectionObserver(check);
  io.observe(input);
  return () => io.disconnect();
}
// elementFromPoint 命中非 input 的透明元素 -> 疑似劫持
```
