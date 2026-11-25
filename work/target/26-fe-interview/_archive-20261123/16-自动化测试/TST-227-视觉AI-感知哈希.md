---
title: [TST-227] 除了像素 diff，感知哈希（pHash）在视觉测试里怎么用？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-227：除了像素 diff，感知哈希（pHash）在视觉测试里怎么用？
**答**：
- pHash 把图哈希成短指纹，汉明距离衡量相似度——快，适合海量粗筛。
- 用法：先 pHash 粗筛（距离 > 阈值才进入像素 diff 精查），省算力。
- pHash 对布局大变化敏感、对局部小改动不敏感——不能替代像素 diff。
- 适合场景：监控线上页面截图的异常漂移（RUM + pHash 异常检测）。

```javascript
import { imageHash } from 'image-hash';
const d = hamming(await imageHash(a), await imageHash(b));
if (d > 6) await pixelDiff(a, b);   // 粗筛命中才精查
r
```
