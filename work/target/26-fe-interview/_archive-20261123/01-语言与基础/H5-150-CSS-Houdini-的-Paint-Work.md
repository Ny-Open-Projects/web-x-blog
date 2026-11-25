---
title: [H5-150] CSS Houdini 的 Paint Worklet 是什么？有什么用？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-150：CSS Houdini 的 Paint Worklet 是什么？有什么用？
**答**：
- Paint API 允许用 JS 注册自定义"绘制函数"：`CSS.paintWorklet.addModule()` 注册模块，worklet 内 `registerPaint(name, class)`，CSS 里 `background: paint(name)` 直接使用。
- paint 代码运行在**独立线程**、与主线程隔离，随布局/尺寸变化自动重绘——适合复杂背景（圆角虚线框、噪点纹理、聊天气泡）且性能好。
- 类里声明 `inputProperties` 可读取 CSS 自定义属性作为参数，实现"可配置"的绘制。
- 兼容性：仅 Chromium 完整支持，生产必须特性检测 + CSS 降级；模块必须是同源（可用 Blob URL 内联）。

```html
<style>
  .card {
    --dash-color: #2563eb;
    --dash-length: 10px;
    padding: 24px;
    /* 降级：不支持 paint() 时退回普通虚线边框 */
    border: 2px dashed #2563eb;
  }
  @supports (background: paint(dashed-box)) {
    .card { border: none; background: paint(dashed-box); }
  }
</style>
<div class="card">Houdini 虚线边框卡片</div>
<script>
// Paint Worklet 必须是独立模块；这里用 Blob URL 内联演示
const worklet = `
  class DashedBox {
    static get inputProperties() {
      return ['--dash-color', '--dash-length'];   // 可读取的 CSS 变量
    }
    paint(ctx, geom, props) {
      ctx.strokeStyle = props.get('--dash-color').toString();
      ctx.lineWidth = 2;
      const len = parseInt(props.get('--dash-length')) || 8;
      ctx.setLineDash([len, 6]);
      ctx.strokeRect(1, 1, geom.width - 2, geom.height - 2);
    }
  }
  registerPaint('dashed-box', DashedBox);
`;
if ('paintWorklet' in CSS) {
  CSS.paintWorklet.addModule(
    URL.createObjectURL(new Blob([worklet], { type: 'text/javascript' })));
}
// 面试要点：
// 1) paint() 跑在独立线程、随布局自动重绘，适合复杂背景
// 2) 参数通过 CSS 自定义属性传入 —— 样式即可配置
// 3) 仅 Chromium 完整支持，必须 @supports 降级
// 4) Houdini 家族还包括 Properties and Values（注册可动画的自定义属性）、
//    Layout Worklet（自定义布局）、Parser/Typed OM —— Paint 是落地最多的一个
</script>
```
