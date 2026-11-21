---
title: [ARC-343] 笔试题：实现组件库的 Skeleton 骨架屏占位与文本行数？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 笔试题, 17]
type: 笔试题
---

## ARC-343：笔试题：实现组件库的 Skeleton 骨架屏占位与文本行数？
**题目**：实现 Skeleton：1) 文本骨架按 rows 渲染，最后一行宽度随机 60%~90%（模拟真实文本）；2) 图片/头像/段落预设组合；3) 与真实内容等高（用真实容器渲染后测量再切骨架——或提供 exact 模式）；4) loading 切换无布局抖动。
**评分点**：
- 最后一行宽度随机且 SSR/CSR 一致（种子随机或由 rows 决定，防水合 mismatch）。
- 组合 API 设计合理（avatar+title+rows 默认布局）。
- 等高策略正确（占位结构 mimic 真实结构：行高/间距一致）。
- 切换时动画（淡入淡出）不引起布局跳动。
```tsx
function seedRand(seed: number) {               // SSR 一致的伪随机
  let s = seed;
  return () => (s = (s * 9301 + 49297) % 233280) / 233280;
}
function Skeleton({ loading, rows = 3, avatar = false, children }) {
  if (!loading) return <div className="sk-fade-in">{children}</div>;        // 4) 淡入不跳布局
  const rnd = seedRand(rows * 7919);            // 1) 种子随机：SSR 与客户端同种子同结果
  const widths = Array.from({ length: rows }, (_, i) =>
    i === rows - 1 ? `${60 + Math.floor(rnd() * 30)}%` : '100%');
  return (
    <div className="sk-fade" aria-busy="true" aria-live="polite">
      {avatar && <div className="sk sk-avatar"/>}
      <div className="sk-body" style={{ lineHeight: 1.5, fontSize: 14 }}>    {/* 3) mimic 真实排版参数 */}
        {widths.map((w, i) =>
          <div key={i} className="sk sk-text" style={{ width: w, height: '1.5em', marginBottom: '0.5em' }}/>)}
      </div>
    </div>
  );
}
```
