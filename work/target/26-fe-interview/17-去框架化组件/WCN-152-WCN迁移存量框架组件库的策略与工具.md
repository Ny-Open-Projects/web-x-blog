---
title: [WCN-152] 把存量框架组件库迁移为 WCN 的策略与工具：怎么控制迁移风险？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 选型与工程落地]
type: 面试题
---

## WCN-152：把存量框架组件库迁移为 WCN 的策略与工具：怎么控制迁移风险？

**答**：
- 策略选择：① 重写（core 用 Lit/纯 WC）——适合简单组件；② 封装（Vue 的 defineCustomElement 直接导出现有 SFC）——快速但带 Vue runtime；③ 适配层共存（adapters 复用旧实现，外部 API 对齐 WC 契约）——过渡期方案。
- 迁移顺序：按"依赖复杂度"排序——叶子组件（Icon/Tag）→ 布局 → 表单控件（最复杂，form-associated）→ 容器/弹层（最后，涉及 top layer 与 slot）。
- 行为对齐工具：契约测试脚本（props/events 矩阵）同时跑旧实现与新实现，diff 输出；视觉回归双跑。
- 兼容层：旧框架包改为转发到 WC + adapters（`import { Button } from '@old/lib'` 内部渲染 `<acme-button>`），业务代码零改动，风险后移。
- 度量与止损：迁移看板（组件级状态），单组件迁移超过预算人日即回退为适配层方案。

```javascript
// 兼容层示意：旧 React 组件库入口转发到 WC
export const Button = React.forwardRef((props, ref) => (
  <acme-button ref={ref} {...normalizeProps(props)} />   // 归一化 prop 名（variant → acme-variant）
));
// 业务侧 import { Button } from '@old/lib' 不变；内部已替换为 WC 实现
```
