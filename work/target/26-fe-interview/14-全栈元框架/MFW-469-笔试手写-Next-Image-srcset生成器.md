---
title: [MFW-469] 笔试：手写 Next Image srcset 生成器
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-469：Next Image srcset 生成器
**答**：实现 `buildSrcset(src, { width, sizes, deviceSizes, imageSizes, quality })`：1) 按 sizes 描述符（如 `(max-width: 640px) 100vw, 50vw`）结合 deviceSizes [640,750,828,...,3840] 计算每档需要的实际像素宽；2) 只保留 ≤ 原图 width 的档位（放大无意义白耗流量），去重排序；3) 输出 `url Widthw` 逗号串，URL 参数含 w 与 q（Next 图像优化器格式 `/api/image?url=..&w=..&q=..`）；4) quality 超 [0,100] 抛错（防误配）。

```javascript
export function buildSrcset(src, { width, sizes, deviceSizes, imageSizes = [], quality = 75 }) {
  if (quality <= 0 || quality > 100) throw new Error('quality out of range')
  const breakpoints = [...deviceSizes, ...imageSizes].sort((a, b) => a - b)
  // 从 sizes 描述符近似取最大视口占比（演示：解析最后一个百分比/vw）
  const vw = Math.max(100, ...[...sizes.matchAll(/(\d+)v[wh]/g)].map(m => +m[1]))
  const need = new Set(
    breakpoints.filter(b => b <= width)          // 不放大
      .map(b => Math.min(b, Math.ceil(b * vw / 100)))
  )
  need.add(Math.min(width, Math.max(...breakpoints)))
  return [...need].sort((a, b) => a - b)
    .map(w => `${imgUrl(src, w, quality)} ${w}w`).join(', ')
}

function imgUrl(src, w, q) {
  const u = new URL('/api/image', 'https://site.example')
  u.searchParams.set('url', src)
  u.searchParams.set('w', String(w))
  u.searchParams.set('q', String(q))
  return u.pathname + '?' + u.searchParams.toString()
}
```

**评分点**：
- 断点过滤 ≤ 原图宽（放大是纯浪费——常见失分点）
- 档位去重 + 升序（浏览器 srcset 匹配依赖有序性）
- URL 参数规范化走 URLSearchParams（手拼字符串会漏 encode）
- quality 边界校验（0/101 这类误配要构造期炸）
