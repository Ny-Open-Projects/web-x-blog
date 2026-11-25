---
title: [DP-433] 案例：diff 算法的策略分层
date: 2026-11-21
categories: [设计模式]
tags: [前端面试, 面试题, 设计模式]
type: 面试题
---

## DP-433：diff 策略分层

**答**：
- diff 的策略分层：同类型快速路径（type 相同直接 patch——最常见最高效）、keyed diff（key map 复用——乱序场景）、LIS 最小移动（Vue3）/锚点插入（React）——策略按「子节点特征」分派
- patchFlag 的编译期策略：编译器标记动态部分（TEXT/PROPS/CLASS）——patch 只处理标记的部分（靶向更新的策略化）
- 策略分派的实现：无 key → 快速路径、有 key → keyed diff、编译标记 → 靶向 patch——「特征检测 → 策略选择」
- 深水点：diff 策略的「退化场景」——全动态无 key 列表退化到 O(n²)——「策略依赖前提」：编译优化的前提是模板可静态分析

```text
diff 策略分派:
  patchFlag 存在 → 靶向修复 (编译期策略)
  type 相同 → 快速 patch
  有 key → keyed map 复用 + LIS
  无 key → index 对齐 (退化: 状态错位风险)
前提: 编译策略依赖静态可分析 — runtime 模板无此优化
```
