---
title: [DP-478] 案例：RTL 布局的策略
date: 2026-11-21
categories: [设计模式]
tags: [前端面试, 面试题, 设计模式]
type: 面试题
---

## DP-478：RTL 策略

**答**：
- RTL 的模式组合：策略（布局策略：物理属性 → 逻辑属性 margin-inline——源头上 RTL 无感）、适配器（图标/箭头的镜像适配——SVG scaleX(-1)）、观察者（locale 变更 → dir 属性切换 + 重算）
- 逻辑属性迁移的清单：left/right → inset-inline-start/end、text-align → text-align:start、transform 不镜像（物理坐标）——迁移清单驱动
- 不可镜像的判定：logo 不镜像、视频进度条镜像、数字与代码段 bdi 包裹——「镜像白名单/黑名单」
- 深水点：RTL 的「渐进迁移」——存量样式物理属性 + [dir='rtl'] 覆盖（旧）vs 构建期 postcss-rtlcss 自动转换（中）vs 逻辑属性重写（新）——三代方案共存

```css
/* 逻辑属性: RTL 自动镜像 */
.card { margin-inline-start: 12px; text-align: start; }
[dir='rtl'] .arrow { transform: scaleX(-1); }       /* 图标镜像白名单 */
.url-field { unicode-bidi: plaintext; }              /* 混排自适应 */
```
