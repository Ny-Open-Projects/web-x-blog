---
title: [SCN-1231] AI 对话的打字机效果与性能平衡
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1231：AI 对话的打字机效果与性能平衡

**答**：
- 效果：打字机逐字渲染——整 token 渲染（非逐字符）+ 节流（rAF 批量）。
- 关闭：动画敏感用户关闭（prefers-reduced-motion 直出全文）。
- 长文：长回复渲染分批（每帧最多 500 字），防主线程长任务。

```javascript
// 打字机节流
function typewriter(container, fullText, { reduced = false } = {}) {
  if (reduced || matchMedia('(prefers-reduced-motion: reduce)').matches)
    return container.textContent = fullText;           // 直出
  let i = 0;
  return new Promise(resolve => {
    function step() {
      const chunk = fullText.slice(i, i + 30);         // 每 rAF 30 字符
      i += chunk.length;
      container.textContent = fullText.slice(0, i);
      if (i < fullText.length) requestAnimationFrame(step);
      else resolve();
    }
    requestAnimationFrame(step);
  });
}
```
