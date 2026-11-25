---
title: [TST-228] 「布局崩了」（重叠/溢出/错位）用传统 diff 难判定，AI 如何辅助？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-228：「布局崩了」（重叠/溢出/错位）用传统 diff 难判定，AI 如何辅助？
**答**：
- 规则层：DOM 几何检查（元素重叠率/溢出视口/零尺寸）用 Playwright evaluate 检测——确定性高。
- AI 层：截图喂视觉模型识别「明显视觉异常」（错位/截断/空块），补充规则盲区。
- 两层结果合并：规则命中直接 block，AI 疑似进人工队列。
- 布局崩检测进 CI 门禁后，视觉回归从「像素对比」升级为「体验质量检查」。

```javascript
const overflow = await page.evaluate(() => {
  const bad = [];
  for (const el of document.querySelectorAll('*')) {
    const r = el.getBoundingClientRect();
    if (r.width > 0 && (r.right > innerWidth + 2 || r.left < -2))
      bad.push(el.className || el.tagName);   // 溢出检测
  }
  return bad.slice(0, 10);
});
r
```
