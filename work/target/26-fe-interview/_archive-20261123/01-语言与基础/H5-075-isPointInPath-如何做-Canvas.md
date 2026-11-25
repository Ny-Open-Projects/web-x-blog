---
title: [H5-075] isPointInPath 如何做 Canvas 内的精确事件拾取？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-075：isPointInPath 如何做 Canvas 内的精确事件拾取？
**答**：
- Canvas 是"一块位图"，没有子元素事件；拾取思路 = 把事件坐标转成画布坐标，再用几何判断点落在哪个图形里。
- `ctx.isPointInPath(path2D, x, y)` 判定点是否在**当前路径或指定 Path2D** 内；配合 `Path2D` 存每对象的路径即可批量判定。
- 坐标转换必须考虑 CSS 缩放与 transform：先按 `canvas.width / rect.width` 归一，再乘相机的逆矩阵。
- 优化：对象多时先做包围盒粗筛，再用 isPointInPath 精筛；或维护空间索引（四叉树/网格）。
- `isPointInStroke(path2D, x, y)` 是线类图形（折线、曲线）的对应版本。

```html
<canvas id="hit" width="600" height="400" style="width:600px"></canvas>
<script>
  const cv = document.getElementById('hit');
  const ctx = cv.getContext('2d');

  // 每个对象持有自己的 Path2D
  const items = [
    { id: 'a', path: new Path2D('M 100 60 L 260 60 L 180 200 Z'), color: '#6cf' },
    { id: 'b', path: new Path2D(), color: '#fc6' },
  ];
  items[1].path.arc(420, 200, 80, 0, Math.PI * 2);

  for (const it of items) {
    ctx.fillStyle = it.color;
    ctx.fill(it.path);
  }

  cv.addEventListener('pointermove', (e) => {
    const rect = cv.getBoundingClientRect();
    // CSS 尺寸 -> 画布物理坐标（本例 1:1，若有 DPR/CSS 缩放需按比例换算）
    const x = (e.clientX - rect.left) * (cv.width / rect.width);
    const y = (e.clientY - rect.top) * (cv.height / rect.height);

    // 倒序遍历：后画的在上层，命中即停
    for (let i = items.length - 1; i >= 0; i--) {
      if (ctx.isPointInPath(items[i].path, x, y)) {
        cv.style.cursor = 'pointer';
        cv.title = `命中元素 ${items[i].id}`;
        return;
      }
    }
    cv.style.cursor = 'default';
  });

  cv.addEventListener('click', (e) => {
    const rect = cv.getBoundingClientRect();
    const x = e.clientX - rect.left, y = e.clientY - rect.top;
    const hitItem = items.find(it => ctx.isPointInPath(it.path, x, y));
    if (hitItem) console.log('点击了', hitItem.id);
  });
</script>
```
