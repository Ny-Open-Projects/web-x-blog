---
title: [H5-164] SVG 路径 morphing（d 属性插值）怎么做？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-164：SVG 路径 morphing（d 属性插值）怎么做？
**答**：
- 前提：两条 path 的**命令序列结构一致**（同数量、同类型命令与点数）——不一致时先归一化（统一采样为等点数折线，或用 flubber/GSAP MorphSVG 自动处理）。
- CSS 路线：`d: path()` 支持插值动画（Chromium/新版 Firefox），但同样要求结构兼容。
- JS 路线（通用）：把 d 字符串解析成数字数组，逐位 lerp 插值后拼回；这是理解 morph 的本质——"把形状归一化成等长参数序列"。
- 归一化思路：flatten 全部曲线为折线（采样 N 点）→ 逐点插值 → 可选拟合回曲线；起点对齐（从最近点开始重排）可减少"翻转"。

```javascript
// d 属性 morphing：核心是"两条路径的命令序列结构一致"后逐点插值
function lerp(a, b, t) { return a + (b - a) * t; }

// 两个同结构路径（M + C + S，点数相同）
const from = 'M10,50 C40,10 80,90 110,50 S180,10 210,50';
const to   = 'M10,50 C40,90 80,10 110,50 S180,90 210,50';

// CSS 路线（Chromium/Firefox 新版）：d 支持插值，要求结构完全兼容
const style = document.createElement('style');
style.textContent = `
  #morph { animation: morph 2s infinite alternate ease-in-out; }
  @keyframes morph {
    from { d: path('${from}'); }
    to   { d: path('${to}'); }
  }
`;
document.head.append(style);

// JS 路线（通用）：解析成数字数组后按位插值 —— 生产用 flubber/GSAP MorphSVG
function parseNumbers(d) {
  return d.match(/-?\d+(\.\d+)?/g).map(Number);
}
function groupSize(cmd) {
  return { M: 2, L: 2, C: 6, S: 4, Q: 4, T: 2, H: 1, V: 1, Z: 0 }[cmd] ?? 0;
}
function morphD(fromD, toD, t) {
  const a = parseNumbers(fromD), b = parseNumbers(toD);
  if (a.length !== b.length) throw new Error('结构不一致：先归一化采样点数');
  const letters = fromD.match(/[A-Za-z]/g);
  let i = 0;
  return letters.map((L) => {
    let s = L;
    for (let k = 0; k < groupSize(L); k++) {
      s += ' ' + lerp(a[i], b[i], t).toFixed(2);
      i++;
    }
    return s;
  }).join(' ');
}
console.log(morphD(from, to, 0.5));   // 中间态

// 结构不一致时的归一化思路（面试讲清即可）：
// 1) 全部转成折线（flatten 采样 N 点）→ 点数一致 → 逐点 lerp → 可选拟合回曲线
// 2) 起点对齐：从"距离最近点"开始重排采样序，减少交叉翻转
// 3) flubber / GSAP MorphSVG 内部做的就是这套归一化 + 插值
```
