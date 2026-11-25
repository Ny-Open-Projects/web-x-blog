---
title: [PER-354] 骨架屏本身会制造 CLS 吗？骨架屏质量的自动验收怎么做？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-354：骨架屏本身会制造 CLS 吗？骨架屏质量的自动验收怎么做？

**答**：
- 会：骨架屏→真实内容的替换是 CLS 的经典来源——骨架块高度/位置与真内容不一致时，替换瞬间内容大幅位移；甚至"骨架→骨架 B→内容"的多段替换会让 CLS 累加。好的骨架屏应该"占位即真相"。
- 骨架屏质量标准：尺寸一致性（每个骨架块与对应真实元素同高同位，误差 < 4px）；数量一致性（骨架块数量与真实条目一致）；位置一致性（无"先 3 行后 5 行"）；替换一次性（一次替换完成，不要分批跳变）。
- 自动验收：实验室脚本——加载页面截取骨架状态与渲染完成状态的元素矩形（getBoundingClientRect），逐块 diff 高度/位置误差；或者直接跑 Lighthouse 看 CLS + Performance 面板 Layout Shift Regions 截图对照。
- 常见修复：骨架屏用与真内容相同的布局容器与比例（aspect-ratio 占位）；数据分批到达时分批替换但每批保持总数不变（增量填充不位移）；骨架高度用"历史真实高度中位数"初始化。

```javascript
// 骨架屏质量自动验收（实验室）
async function auditSkeleton(page) {
  await page.goto(url, { waitUntil: 'domcontentloaded' });
  const skeleton = await page.evaluate(() => shotRects('.skeleton [data-sk]'));    // 骨架矩形
  await page.waitForSelector('.content-ready');
  const real = await page.evaluate(() => shotRects('.content [data-real]'));
  const diffs = skeleton.map((s, i) => {
    const r = real[i];
    if (!r) return { i, issue: 'count-mismatch' };
    return { i, dH: Math.abs(s.height - r.height), dY: Math.abs(s.y - r.y) };
  }).filter((d) => d.issue || d.dH > 4 || d.dY > 4);
  return { pass: diffs.length === 0, diffs };       // 超差块清单 → 修复占位尺寸
}
```
