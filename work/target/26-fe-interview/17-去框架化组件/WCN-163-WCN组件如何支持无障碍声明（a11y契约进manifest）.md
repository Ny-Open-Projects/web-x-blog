---
title: [WCN-163] WCN 组件如何把无障碍声明做成契约？manifest 里的 a11y 字段与宿主责任怎么划分？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 选型与工程落地]
type: 面试题
---

## WCN-163：WCN 组件如何把无障碍声明做成契约？

**答**：
- 契约化思路：custom-elements.json 扩展 a11y 字段——`requiredRoles`（宿主必须提供）、`defaultRole`、`keyboard`（支持的按键列表）、`requiredLabels`（宿主须传 aria-label/可读文本）；发布时 CI 校验文档与实现一致。
- 宿主责任划分：组件负责内部语义（影子树 role/aria 状态/键盘行为/焦点管理）；宿主负责外部语义（业务含义 aria-label、可见文本、禁用原因说明）。
- 状态同步：组件状态（loading/open）通过 `internals.states`（:--loading）与 aria reflection 双通道暴露，宿主据此联动外部提示（aria-live 区）。
- 键盘契约文档化：如 `x-dialog`: Enter/Space 触发、Esc 关闭、Tab 圈内循环——写进组件 README 与 Storybook 交互说明。
- 回归保障：a11y 断言进 E2E（键盘序列脚本 + axe 扫描），任何 aria 属性变更触发 a11y 基线更新评审。

```json
{ "tagName": "acme-dialog",
  "a11y": {
    "defaultRole": "dialog",
    "requiredFromHost": ["aria-label 或可见标题（slot=title）"],
    "keyboard": ["Tab 循环", "Escape 关闭", "Enter 确认"],
    "states": ["open", "loading"]
  } }
```

```html
<!-- 宿主按契约使用 -->
<acme-dialog aria-label="确认退款">
  <span slot="title">确认退款</span>
</acme-dialog>
```
