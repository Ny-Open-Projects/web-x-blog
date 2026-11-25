---
title: [H5-080] 路径命令 d 里的 M/L/C/Q/A/Z 分别是什么？如何拼一条贝塞尔曲线？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-080：路径命令 d 里的 M/L/C/Q/A/Z 分别是什么？如何拼一条贝塞尔曲线？
**答**：
- 基础：`M` 移动、`L` 直线、`H/V` 水平垂直线、`Z` 闭合；`d` 中大写=绝对坐标、小写=相对上一终点。
- 曲线：`C` 三次贝塞尔（2 控制点）、`Q` 二次贝塞尔（1 控制点）、`S/T` 是它们的平滑简写（控制点自动镜像）。
- `A rx ry rot large-arc sweep x y` 画椭圆弧：`large-arc` 选大/小弧，`sweep` 选顺/逆时针，是圆环进度条的底层。
- 手写曲线的通用套路：先定锚点序列，再让控制点沿着"切线方向"偏移；数据可视化库（d3-shape）本质就是代码生成 d。
- 实用技巧：用 `getTotalLength()` 与 `getPointAtLength(t)` 把任意路径当"轨道"使用（描边动画、路径跟随运动）。

```html
<svg viewBox="0 0 400 200" width="400">
  <!-- 三次贝塞尔：M 起点，C c1 c2 终点 -->
  <path d="M 20 150 C 80 20, 160 20, 200 150" fill="none" stroke="#36f" stroke-width="3"/>

  <!-- 二次贝塞尔 + S 平滑续接 -->
  <path d="M 20 180 Q 110 60 200 180 T 380 180" fill="none" stroke="#f60" stroke-width="2"/>

  <!-- 圆弧拼圆环进度：两段 A，sweep=1 顺时针 -->
  <path d="M 300 100 A 50 50 0 1 1 300.1 100"
        fill="none" stroke="#eee" stroke-width="10"/>
  <path id="ring" d="M 300 100 A 50 50 0 0 1 350 50"
        fill="none" stroke="#0a0" stroke-width="10" stroke-linecap="round"/>
</svg>

<script>
  // 路径当轨道用： getTotalLength + getPointAtLength
  const ring = document.getElementById('ring');
  const len = ring.getTotalLength();
  console.log('进度弧长：', len.toFixed(1));

  const p = ring.getPointAtLength(len * 0.5);   // 弧中点坐标
  console.log('中点：', p.x.toFixed(1), p.y.toFixed(1));

  // JS 拼贝塞尔：把一组点拟合成平滑曲线（Catmull-Rom 转 Bezier 简版）
  function smoothPath(points) {
    let d = `M ${points[0][0]} ${points[0][1]}`;
    for (let i = 1; i < points.length; i++) {
      const [x0, y0] = points[i - 1], [x1, y1] = points[i];
      d += ` Q ${(x0 + x1) / 2} ${y0} ${x1} ${y1}`; // 中点作控制点的简化平滑
    }
    return d;
  }
  console.log(smoothPath([[0, 100], [50, 40], [100, 90], [150, 30]]));
</script>
```
