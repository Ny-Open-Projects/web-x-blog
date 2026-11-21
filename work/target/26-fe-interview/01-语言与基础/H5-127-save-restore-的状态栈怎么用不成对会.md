---
title: [H5-127] save/restore 的状态栈怎么用？不成对会出什么问题？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-127：save/restore 的状态栈怎么用？不成对会出什么问题？
**答**：
- `save()` 把 fillStyle/strokeStyle/变换矩阵/裁剪区/阴影/字体等状态压栈，`restore()` 弹栈恢复；栈是 LIFO，保存顺序和恢复顺序必须严格配对。
- 不成对的后果：变换跨帧/跨分支累积（图形越转越歪）、`clip()` 裁剪区越缩越小、样式"泄漏"到后面的绘制。
- 配对原则：进入绘制分支先 save，离开前必 restore（try/finally 思维）；深层递归绘制里可用 `setTransform` 直接重置兜底。
- 注意：restore 只恢复"状态"，不恢复画布像素——清像素用 clearRect；`clip()` 属于状态的一部分，在 save/restore 之间使用。

```javascript
const ctx = canvas.getContext('2d');

// 反模式：不成对 —— rotate 会跨调用累积，图形越画越歪
function drawBad(angle) {
  ctx.rotate(angle);          // 没有 save，状态泄漏到下一次调用
  ctx.fillRect(0, 0, 50, 50);
}

// 正解 1：进入分支即 save，退出前 restore（try/finally 思维）
function drawSafe(angle) {
  ctx.save();                 // 快照当前状态
  try {
    ctx.translate(100, 100);
    ctx.rotate(angle);
    ctx.fillStyle = '#2563eb';
    ctx.fillRect(-25, -25, 50, 50);
  } finally {
    ctx.restore();            // 提前 return / 异常都不会泄漏状态
  }
}

// 正解 2：深层递归（树形结构绘制）里，用 setTransform 直接重置兜底
function resetToBase(dpr) {
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);  // 不依赖栈深度，强制回到基准
}

// 裁剪也属于状态：save 里 clip、restore 释放，否则裁剪区会叠加收紧
ctx.save();
ctx.beginPath();
ctx.arc(60, 60, 50, 0, Math.PI * 2);
ctx.clip();                    // 只能画进圆内
ctx.fillStyle = '#f59e0b';
ctx.fillRect(0, 0, 120, 120);
ctx.restore();                 // 释放裁剪

// 记住两点：
// 1) restore 不恢复像素 —— 清像素用 clearRect
// 2) save/restore 数量不匹配时浏览器不报错，靠"进分支必配对"的纪律保证
```
