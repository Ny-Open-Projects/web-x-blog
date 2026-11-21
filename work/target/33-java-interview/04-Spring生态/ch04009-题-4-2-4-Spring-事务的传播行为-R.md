---
title: "题 4.2.4：Spring 事务的传播行为？REQUIRES_NEW 和 NESTED 的区别？"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 面试题, 基础题, 33]
type: 面试题
disableNunjucks: true
---

### 题 4.2.4：Spring 事务的传播行为？REQUIRES_NEW 和 NESTED 的区别？

**【参考回答（可背）】**
7 种传播行为，重点背 3+1：
- REQUIRED（默认）：有事务加入，没有新建；
- REQUIRES_NEW：**挂起当前事务**，新建独立事务（内层回滚不影响外层已提交；外层回滚不影响内层已提交）；
- NESTED：在当前事务内设置**保存点（savepoint）**，内层回滚回滚到保存点，外层可继续；外层回滚内层必回滚（同一物理事务）；
- SUPPORTS/NOT_SUPPORTED/MANDATORY/NEVER：边界语义。
选择经验：**发短信/写日志等"必须独立成败"用 REQUIRES_NEW；主流程内的可补偿子步骤用 NESTED**。
底层：事务状态由 PlatformTransactionManager 管理，挂起 = 把当前 ThreadLocal 连接保存、清空、新建连接（注意 REQUIRES_NEW 占用**两个数据库连接**，嵌套过深会耗尽连接池——真实事故点）。

**【追问链】**
1. Spring 事务和数据库事务的关系？→ Spring 事务是**编程模型抽象**，真事务由 JDBC 连接的 autocommit/commit/rollback 完成；Spring 做的是把"连接绑定 ThreadLocal、传播、回滚规则"这套胶水管好。
2. 长事务危害？→ 连接占用（池耗尽）、undo 增长、间隙锁范围扩大（死锁概率↑）、主从延迟放大。治理：事务内不 RPC/不发 MQ（先落库后异步）、@Transactional 只包必要代码、大事务拆分。

**【P10 加分项】**
讲"大事务治理"专项：APM 按 RT 维度找 Top 事务 → 规则扫描（事务内 RPC/IO）→ 拆分为"本地事务 + 事务外副作用 + 补偿" → 落地 TransactionSynchronization 的 afterCommit 发消息（保证**先提交再通知**，避免消费方读不到数据）。

---
