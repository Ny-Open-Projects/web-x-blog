---
title: "[MY-041] 锁·Next-Key（分类）"
date: 2026-11-18
categories: [Java面试, MySQL]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 锁 · Next-Key（分类）

- **事实**：InnoDB 行锁三种：Record Lock 锁记录、Gap Lock 锁间隙、Next-Key=Record+Gap
- **原理**：RR 下可重复读与防幻读靠 Next-Key（左开右闭区间），RC 下禁用 Gap Lock 只锁记录（并发更好）
- **常见误区**：
  1. Next-Key 是右开左闭（错）
  2. RC 下有间隙锁（错）
  3. Gap Lock 锁住具体行（错）
- **工程用法**：加锁分析的基本单位
- **版本锚点**：InnoDB 文档
