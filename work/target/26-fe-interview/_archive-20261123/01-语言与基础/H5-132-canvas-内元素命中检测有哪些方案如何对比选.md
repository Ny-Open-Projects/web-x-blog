---
title: [H5-132] canvas 内元素命中检测有哪些方案？如何对比选型？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-132：canvas 内元素命中检测有哪些方案？如何对比选型？
**答**：
- **isPointInPath**：保留矢量路径语义、精确，但每元素一次调用 O(n)，路径需要重建一遍；适合元素少、形状复杂（不规则多边形）。
- **几何计算**：自己写圆/矩形相交，最快；配合"包围盒粗筛 + 精确判定"两级可撑到海量元素；缺点是每种图形都要写逻辑。
- **像素拾取缓冲（picking buffer）**：把每个元素用"id 编码成的颜色"画到离屏 canvas，命中时读 1 像素反查 id——O(1) 查询且形状任意，代价是场景变化时重画缓冲。
- 选型口诀：少量复杂路径 isPointInPath；大量规则图形几何 + 空间索引；元素极多或形状任意用拾取缓冲；实际项目常见"包围盒粗筛 + 上述精判"组合。

```javascript
const dpr = devicePixelRatio || 1;
const shapes = [
  { type: 'rect', x: 10, y: 10, w: 80, h: 50 },
  { type: 'circle', cx: 180, cy: 60, r: 40 },
];

function buildPath(c, s) {
  if (s.type === 'rect') c.rect(s.x, s.y, s.w, s.h);
  if (s.type === 'circle') c.arc(s.cx, s.cy, s.r, 0, Math.PI * 2);
}

// 方案 A：isPointInPath —— 保留矢量路径，精确，元素少时用
function hitByPath(ctx, x, y) {
  for (let i = shapes.length - 1; i >= 0; i--) {   // 倒序：先命中最上层
    ctx.beginPath();
    buildPath(ctx, shapes[i]);
    if (ctx.isPointInPath(x, y)) return shapes[i];
  }
  return null;
}

// 方案 B：几何计算 —— 最快；先包围盒粗筛再精确判定
function hitByGeometry(x, y) {
  for (let i = shapes.length - 1; i >= 0; i--) {
    const s = shapes[i];
    if (s.type === 'rect' &&
        x >= s.x && x <= s.x + s.w && y >= s.y && y <= s.y + s.h) return s;
    if (s.type === 'circle') {
      if ((x - s.cx) ** 2 + (y - s.cy) ** 2 > (s.r + 6) ** 2) continue; // 粗筛+容差
      return s;
    }
  }
  return null;
}

// 方案 C：像素拾取缓冲 —— 每个元素用唯一颜色画到离屏，读点反查 id
function buildPickBuffer() {
  const pick = document.createElement('canvas');
  pick.width = canvas.width; pick.height = canvas.height;
  const c = pick.getContext('2d', { willReadFrequently: true });
  shapes.forEach((s, i) => {
    c.fillStyle = '#' + (i + 1).toString(16).padStart(6, '0');  // id 编码成颜色
    c.beginPath(); buildPath(c, s); c.fill();
  });
  return (x, y) => {
    const d = c.getImageData(x * dpr, y * dpr, 1, 1).data;
    if (d[3] === 0) return null;                       // 透明 = 没命中
    const idx = (d[0] << 16 | d[1] << 8 | d[2]) - 1;
    return shapes[idx] ?? null;
  };
}

const ctx = canvas.getContext('2d');
console.log(hitByPath(ctx, 40, 30));   // rect
console.log(hitByGeometry(180, 60));   // circle
const pickHit = buildPickBuffer();
console.log(pickHit(40, 30));          // rect
```

## 二十二、Canvas 工程化
