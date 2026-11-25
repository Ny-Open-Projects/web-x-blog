---
title: [CSS-359] 主题系统分层设计：从 token 到组件到页面
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## CSS-359：主题系统分层设计：从 token 到组件到页面

**答**：
- 三层 token：primitive（原始色板 --blue-500）→ semantic（语义 --color-primary/--color-bg）→ component（组件级 --btn-radius）；上层引用下层，页面只消费语义层
- 切换机制：data-theme 属性挂在 html，semantic 层变量按主题重映射——切换成本 = 一层变量重算（比全量 class 切换便宜）
- 与引擎失效结合：语义变量尽量挂在「就近子树根」（暗色卡片区域局部变量）而不是全改 :root——失效范围收敛到子树
- 暗色模式细节：颜色不是简单反转（阴影变发光、透明度层级反转），要出暗色 token 映射表；图片/插图资产双套或降亮度处理
- 工程约束：token 变更走设计系统流程（设计侧 Figma token 同步脚本生成 CSS），禁止业务侧私用 primitive 层——保证主题完整性

```css
:root {
  /* primitive */
  --gray-0: #fff; --gray-9: #111;
  /* semantic */
  --color-bg: var(--gray-0); --color-fg: var(--gray-9);
}
[data-theme='dark'] {
  --color-bg: var(--gray-9); --color-fg: var(--gray-0);
}
.card { color: var(--color-fg); }   /* 组件只消费语义层 */
```
