---
title: [ALG-172] 企业内部系统给页面加了带用户 ID 的水印，防止截图泄密。有人会删 DOM 或改透明度。如何用 MutationObserver 做防篡改？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-172：企业内部系统给页面加了带用户 ID 的水印，防止截图泄密。有人会删 DOM 或改透明度。如何用 MutationObserver 做防篡改？
**答**：`MutationObserver` 监听 body 的 childList（防删除）与水印 style 属性（防改透明度/位置），触发即重建水印并上报安全事件（带路径与时间，便于溯源定位到人）。要点：① observer 回调里再改 DOM 会再次触发自己，注意别死循环（重建前先 disconnect 或做状态判断）；② 防篡改只是提高门槛，权威溯源靠水印内容 + 服务端审计。

```javascript
function protectWatermark(wm) {
  const observer = new MutationObserver(() => {
    const gone = !document.body.contains(wm);
    const faded = parseFloat(getComputedStyle(wm).opacity) < 0.1;
    if (gone || faded) {
      observer.disconnect();               // 先断开，防止重建动作再次触发自己
      wm.style.opacity = '0.08';
      if (gone) document.body.appendChild(wm); // 重建水印
      observer.observe(document.body, {
        childList: true, subtree: true,
        attributes: true, attributeFilter: ['style'],
      });
      reportSecurityEvent('watermark_tamper', { // 上报溯源
        uid: wm.dataset.uid, path: location.pathname, ts: Date.now(),
      });
    }
  });
  observer.observe(document.body, {
    childList: true, subtree: true,
    attributes: true, attributeFilter: ['style'],
  });
  return () => observer.disconnect();
}
```
