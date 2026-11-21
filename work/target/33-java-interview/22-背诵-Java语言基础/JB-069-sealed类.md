---
title: "[JB-069] 语言杂项·sealed类（版本）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 语言杂项 · sealed类（版本）

- **事实**：JDK17 转正 sealed 类：用 permits 显式限定继承层级，配合 switch 模式匹配做穷尽检查。
- **原理**：编译器检查 switch 是否覆盖所有允许的子类型，漏分支直接编译错。
- **常见误区**：
  1. sealed 类允许任何类继承它。（错）
  2. sealed 与模式匹配无关。（错）
  3. sealed 的子类也不能再被继承是强制规则。（错）
- **工程用法**：状态机/权限模型/AST 节点设计是典型场景。
- **版本锚点**：JDK17+
