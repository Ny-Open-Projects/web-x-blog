---
title: [PER-405] Paint 与合成的预算化：重绘面积、层数与层内存的量化检查清单？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-405：Paint 与合成的预算化：重绘面积、层数与层内存的量化检查清单？

**答**：
- 量化维度：① 重绘面积——单次交互的 Paint 区域（Rendering 面板 Paint Flashing + Performance 面板 Paint 块尺寸），预算：单次交互重绘 < 视口 1/4；② 合成层数量——Layers 面板层数与每层内存（宽×高×4），预算：常规页 < 60 层、层总内存 < 60MB；③ 提升层触发审查——will-change/translateZ/opacity 动画的元素是否真的需要独立层。
- 检查清单流程：打开 Layers 面板 → 找大层（尺寸异常的层通常是"误提升的整页容器"）→ 找重复层（同一样式表克隆的组件实例）→ 触发高频交互录 Paint Flashing → 重绘区域过大的元素定位（通常是阴影/背景图/大面积 hover 态）。
- 优化对照：大层 → 收窄提升范围（提升滚动容器而非整页）；重复层 → constructable stylesheets（PER-392）；大面积重绘 → 阴影改 filter/伪元素缩小绘制区域、背景渐变用 transform 动画。
- 长页专项：长页面用 content-visibility 让屏外子树不产生 paint 成本（PER-346），Paint 预算随之大幅下降。

```text
Paint/合成预算检查清单：
[ ] 单次交互重绘面积 < 25% 视口（Paint Flashing 录制确认）
[ ] 合成层 < 60 层，层内存合计 < 60MB（Layers 面板）
[ ] 无"整页大小"的误提升层（大层定位 → 收窄 will-change 范围）
[ ] 重复组件实例共享样式表（constructable stylesheets）
[ ] 大面积阴影/渐变动画改 filter 或 transform 实现
[ ] 长页开启 content-visibility（屏外零 paint）
量化工具：Layers 面板（层/内存）、Paint Flashing（重绘区域）、Performance Paint 块（时长）
```
