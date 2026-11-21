---
title: [HW-130] 手写首屏图片加载编排——LCP 候选高优先、次屏懒加载、失败降级与整体完成回调
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

**答**：首屏图片编排器：三档优先级（hero 立即+fetchpriority、首屏内容图并行限 2、次屏 IO 触发），hero 失败降级（原图 → 压缩版 → 占位色），整体完成回调供埋点（首屏图片完成时间 = 业务首屏指标，PER-231）。

```javascript
function orchestrateFirstScreen({ hero, contentImgs, belowFold }) {
  const done = new Promise((resolveAll) => {
    let remaining = 1 + contentImgs.length;
    const oneDone = () => { if (--remaining === 0) resolveAll(performance.now()); };
    // 1. hero：立即 + 高优先 + 失败降级链
    loadWithFallback(hero, [
      { src: hero.src, fetchpriority: 'high' },
      { src: hero.src.replace('.avif', '.webp'), fetchpriority: 'high' },   // 降级格式
      { src: null, placeholder: true },                                     // 最终降级：占位色
    ]).then(oneDone);
    // 2. 内容图：并发限 2
    let active = 0, next = 0;
    const drain = () => {
      while (active < 2 && next < contentImgs.length) {
        const img = contentImgs[next++];
        active++;
        loadImg(img).catch(() => img.style.background = 'var(--img-fallback)').finally(() => {
          active--; oneDone(); drain();
        });
      }
    };
    drain();
    // 3. 次屏：IO 触发（不属于首屏完成回调的一部分）
    belowFold.forEach((img) => lazyObserve(img));
  });
  return done;    // 首屏图片完成时间 → 上报业务首屏指标
}
// hero 降级链：avif → webp → 占位色（LCP 永远有内容，不因单图失败白屏）
// 内容图限并发 2（与 hero 抢带宽时让路）；次屏走 IO 不占首屏预算
```

**评分点**：
- 三档编排（hero 高优/内容图限并发/次屏 IO）与首屏完成回调的业务指标价值。
- hero 降级链（格式降级 → 占位色）保证 LCP 元素永不空缺。
- 并发限制让路语义；次屏不占首屏预算。
- 完成回调返回时间戳可直接作为业务首屏指标上报。
