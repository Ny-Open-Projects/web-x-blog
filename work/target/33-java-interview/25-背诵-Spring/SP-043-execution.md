---
title: "[SP-043] AOP·execution（表达式）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## AOP · execution（表达式）

- **事实**：execution 表达式：修饰符 返回类型 包.类.方法(参数) throws
- **原理**：execution(* com.a.b.service..*.save*(..)) 匹配 service 包下 save 开头方法，.. 是包通配与参数通配
- **常见误区**：
  1. execution 只能匹配 public 方法（错）
  2. (..) 与 (*) 语义相同（错）
  3. 表达式大小写敏感无所谓（错）
- **工程用法**：写切点前先明确匹配范围
- **版本锚点**：AspectJ 语法
