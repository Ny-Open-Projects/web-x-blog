---
title: "[SP-084] 测试·@Transactional 回滚（事务）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 测试 · @Transactional 回滚（事务）

- **事实**：测试类 @Transactional 默认每测试方法后回滚不污染库
- **原理**：由测试框架管理（非生产代理语义），需要真实提交的集成步骤用 @Commit 或编程式事务
- **常见误区**：
  1. 测试事务会真实提交（错）
  2. 回滚机制影响被测代码语义（错）
  3. 所有集成测试都应加 @Transactional（错）
- **工程用法**：集成测试的标准姿势
- **版本锚点**：Spring Test 文档
