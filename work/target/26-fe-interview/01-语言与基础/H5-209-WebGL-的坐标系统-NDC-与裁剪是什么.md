---
title: [H5-209] WebGL 的坐标系统：NDC 与裁剪是什么
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, WebGL]
type: 面试题
---

## H5-209：WebGL 的坐标系统：NDC 与裁剪是什么

**答**：
- WebGL 最终坐标是 NDC（归一化设备坐标）：x/y/z 都在 -1~1 之间，超出即被裁剪，不绘制
- 流水线：局部坐标 → MVP 矩阵变换 → 裁剪坐标（除以 w 得 NDC）→ 视口变换映射到屏幕像素
- 除以 w 就是「透视除法」：w=z 距离时，远处的东西自动变小——透视效果由此而来
- 两个易错点：z 轴朝向（WebGL 右手系看进屏幕是 -z）；canvas 尺寸与 gl.viewport 要同步（否则画面比例错）
- 面试钩子：问「为什么三角形翻转了」多半是 y 轴方向或视口尺寸问题

```javascript
function resize() {
  const dpr = devicePixelRatio;
  canvas.width = clientWidth * dpr;
  canvas.height = clientHeight * dpr;
  gl.viewport(0, 0, canvas.width, canvas.height); // 必须同步，否则拉伸变形
}
```
