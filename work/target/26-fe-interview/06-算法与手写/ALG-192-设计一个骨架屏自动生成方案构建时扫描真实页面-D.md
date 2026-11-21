---
title: [ALG-192] 设计一个骨架屏自动生成方案：构建时扫描真实页面 DOM，按元素类型生成同布局的灰色占位块，避免手写每个页面的骨架屏？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-192：设计一个骨架屏自动生成方案：构建时扫描真实页面 DOM，按元素类型生成同布局的灰色占位块，避免手写每个页面的骨架屏？
**答**：两步算法：① 遍历——`createTreeWalker` 只遍历元素节点，`getBoundingClientRect` 拿每个候选元素（文本类画细灰条、图片/按钮/视频画灰块）的位置尺寸；② 生成——按"fixed 定位 + 灰底 + 圆角"输出骨架层 HTML/JSON，配呼吸动画。要点：① 只取首屏（viewport 内）元素；② 容器命中子元素时跳过（去重），防文本与其父容器叠块；③ 构建时跑一次并缓存，运行时直接注入。遍历 O(节点数)。

```javascript
function generateSkeleton(root, viewportH = innerHeight) {
  const walker = document.createTreeWalker(root, NodeFilter.SHOW_ELEMENT);
  const blocks = [];
  while (walker.nextNode()) {
    const el = walker.currentNode;
    const rect = el.getBoundingClientRect();
    if (rect.top > viewportH) break;          // 只取首屏
    if (rect.width === 0 || rect.height === 0) continue;
    if (el.matches('p, span, h1, h2, h3')) {
      // 文本类：画细灰条（高度取行高，宽度取实际占宽）
      blocks.push({ type: 'line', x: rect.x, y: rect.y, w: rect.width, h: 16 });
    } else if (el.matches('img, video, button')) {
      // 媒体与按钮：画灰块
      blocks.push({ type: 'block', x: rect.x, y: rect.y, w: rect.width, h: rect.height });
    } // 容器自身跳过：其子块已表达布局，防叠块
  }
  // 生成同布局骨架层：fixed 定位灰块 + 呼吸动画
  return blocks.map(b => `<div style="position:fixed;left:${b.x}px;top:${b.y}px;
    width:${b.w}px;height:${b.h}px;background:#eee;border-radius:4px;
    animation:pulse 1.5s ease-in-out infinite"></div>`).join('');
}
```
