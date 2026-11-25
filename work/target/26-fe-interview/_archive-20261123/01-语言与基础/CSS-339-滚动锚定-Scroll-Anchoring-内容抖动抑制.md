---
title: [CSS-339] 滚动锚定（Scroll Anchoring）：内容抖动抑制机制
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 面试题, 渲染管线]
type: 面试题
---

## CSS-339：滚动锚定（Scroll Anchoring）：内容抖动抑制机制

**答**：
- 机制：用户滚动中，若视口上方内容高度变化（图片加载/广告插入），浏览器自动补偿 scrollTop 保持视觉内容不跳——Chrome/Firefox 默认开启，这解释了「图片加载不抖」的现状
- 失效场景：scrollTop 被脚本修改、元素设置了 scroll anchoring 排除（overflow-anchor: none）、滚动容器为 body 且结构复杂时偶发失效
- 主动控制：`overflow-anchor: none` 禁用（自己管理滚动的聊天流/无限列表要禁，避免与手动补偿冲突）；`overflow-anchor: auto` 指定锚点元素
- 与无限加载配合：顶部插入内容的列表（如插入到上方的新消息）会触发锚定补偿，如果自己做了「scrollTop += 插入高度」手动补偿会双重补偿抖动——二选一
- 调试：布局抖动排查时先确认是否锚定失效（上方 DOM 变动 + 无补偿），Performance 面板看 Layout Shift 来源

```css
/* 聊天流: 自己补偿滚动, 禁用引擎锚定防双重补偿 */
.chat-list { overflow-anchor: none; }
/* 普通内容页: 保持默认(锚定开启), 图片加载不跳 */
.article { overflow-anchor: auto; }
```
