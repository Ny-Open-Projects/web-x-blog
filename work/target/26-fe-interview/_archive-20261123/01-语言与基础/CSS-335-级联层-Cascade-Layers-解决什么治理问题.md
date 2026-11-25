---
title: [CSS-335] 级联层（Cascade Layers）：解决什么治理问题
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 面试题, 渲染管线]
type: 面试题
---

## CSS-335：级联层（Cascade Layers）：解决什么治理问题

**答**：
- 核心机制：@layer 把规则分层，层间顺序在「specificity 之前」决定——后声明的层整体覆盖先声明的层，无论选择器权重；未分层规则的优先级高于所有层
- 解决的治理问题：三方样式覆盖（Reset/Base/Components/Utilities 各占一层）不再靠 !important 和超长选择器互殴——权重内战变成显式层次声明
- 顺序规则：@layer a, b; 先声明顺序即优先级顺序（后者高）；同一层内仍按 specificity/source order 正常级联；@import 可指定进层（`@import url() layer(base)`）
- 与 !important 反转：!important 在层间是「反序」生效（早层 important 赢），这是规范设计——用于「重要基线不可覆盖」语义
- 迁移策略：老项目渐进接入——先声明空层占位顺序，再逐层迁移规则；未被分层的存量规则天然压过新层，保证迁移安全

```css
@layer reset, base, components, utilities;   /* 优先级: utilities 最高 */

@layer reset { * { margin: 0; } }
@layer base { h1 { font-size: 2rem; } }
@layer components { .btn { padding: 8px 16px; } }
@layer utilities { .mt-0 { margin-top: 0 !important; } }

/* utilities 层的 .mt-0 覆盖 components 层, 无论选择器权重 */
```
