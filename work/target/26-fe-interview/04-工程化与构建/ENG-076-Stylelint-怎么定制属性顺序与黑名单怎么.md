---
title: [ENG-076] Stylelint 怎么定制？属性顺序与黑名单怎么配？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-076：Stylelint 怎么定制？属性顺序与黑名单怎么配？
**答**：
- 继承 stylelint-config-standard 打底，再用 rules 覆盖团队特有约束。
- 属性顺序用 stylelint-order 插件的 properties-order：布局属性在前、视觉属性在后，review 可读性明显提升。
- 黑名单用 declaration-property-value-disallowed-list：禁 border:none（该用 0）、禁万能选择器等。
- 与 Prettier 的边界同前：Stylelint 管写法质量与架构约束，缩进分号等交给 Prettier。

```json
{
  "extends": ["stylelint-config-standard"],
  "plugins": ["stylelint-order"],
  "rules": {
    "order/properties-order": [
      "position", "z-index", "top", "left",
      "display", "flex", "grid",
      "width", "height", "margin", "padding",
      "color", "background", "border"
    ],
    "declaration-property-value-disallowed-list": {
      "/^border/": ["none"],
      "/^font/": ["system-ui"]
    },
    "max-nesting-depth": 3
  }
}
```
