---
title: [V3-497] Vue3 动画体系编排：列表过渡与 FLIP 原理
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 面试题, 动画]
type: 面试题
---

## V3-497：Vue3 动画体系编排：列表过渡与 FLIP 原理

**答**：
- TransitionGroup 原理：v-move 类 + FLIP（First-Invert-Play）——更新前记录位置（First），DOM 重排后用 transform 反向位移（Invert），再过渡到 0（Play）——位置移动动画零 layout 成本（transform 合成）
- FLIP 的实现关键：TransitionGroup 在更新前后测量 children 位置，leave 元素保持在流内（position absolute 化时机）——「移动的元素和 leave 的元素同时动画」的编排
- 交错的实现：CSS 变量 + transition-delay 按索引递增（v-move 内联 --i）——stagger 动画纯 CSS 完成
- 与虚拟列表冲突：虚拟列表项频繁卸载/重建，FLIP 测量会错乱——虚拟列表内禁用 move 过渡或只对「同 key 更新」做过渡
- 性能红线：TransitionGroup 只动 transform/opacity；列表项内 margin/height 过渡会破坏 FLIP 测量并触发 layout——大列表动画只允许「位置类」属性

```vue
<TransitionGroup name="list" tag="ul">
  <li v-for="i in items" :key="i.id" :style="{ '--i': i }">{{ i.text }}</li>
</TransitionGroup>
```

```css
.list-move { transition: transform .3s; }
.list-enter-active { transition: all .3s; transition-delay: calc(var(--i) * 30ms); }
.list-leave-active { position: absolute; }  /* leave 脱流, 让 move 测量正确 */
```
