---
title: "[JB-015] 包装类·Long比较（误用）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 包装类 · Long比较（误用）

- **事实**：Long 类型用 == 比较，超出缓存范围（-128~127）时即使值相等也返回 false。
- **原理**：== 比较引用，超缓存范围的 Long 是不同对象。
- **常见误区**：
  1. Long 用 == 比较值相等就一定 true。（错）
  2. Long 缓存范围是 -128~255。（错）
  3. Long 的 == 与 equals 语义相同。（错）
- **工程用法**：电商订单号等大数值 Long 比较必须用 equals——经典线上事故源。
- **版本锚点**：JLS 5.1.7（缓存 -128~127）
