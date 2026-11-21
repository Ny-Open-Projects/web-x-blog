---
title: "[MY-095] SQL·SQL 注入（安全）"
date: 2026-11-18
categories: [Java面试, MySQL]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## SQL · SQL 注入（安全）

- **事实**：SQL 注入防御：预编译（PreparedStatement 占位符）而非拼接，ORM 参数绑定天然防注入
- **原理**：预编译把 SQL 结构与数据分离，注入字符成为纯数据，动态拼接（order by/表名白名单校验）是残余风险点
- **常见误区**：
  1. 拼接参数自动防注入（错）
  2. ORM 完全免疫注入（错）
  3. 注入只影响查询（错）
- **工程用法**：安全编码底线
- **版本锚点**：实战共识
