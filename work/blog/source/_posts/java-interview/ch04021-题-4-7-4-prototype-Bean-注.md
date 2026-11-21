---
title: "题 4.7.4：prototype Bean 注入 singleton 有什么问题？如何正确获取？"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 面试题, 33]
type: 面试题
disableNunjucks: true
---

### 题 4.7.4：prototype Bean 注入 singleton 有什么问题？如何正确获取？

**【参考回答（可背）】** 问题：singleton A 注入 prototype B，B 在 A 创建时注入一次，之后 A 的每次使用拿到的是**同一个** B——prototype 语义失效（只"新"了一次）。正确获取三种：① 注入 `ObjectFactory<B>` / `ObjectProvider<B>`，用时 getObject() 每次新建；② @Lookup 抽象方法（CGLIB 覆写返回容器实例）；③ scoped proxy（proxyMode = TARGET_CLASS，代理每次委托容器取新实例）。
**【追问链】** ① request/session 作用域 Bean 注入 singleton 为什么能工作？（就是 scoped proxy 在起作用）② prototype Bean 的销毁回调谁负责？（容器只负责到创建，销毁由客户端自己管理——面试冷知识，答出即证明读过文档）。
**【P10 加分项】** 设计判断："多实例对象优先考虑'工厂模式 + 显式 create'，而不是滥用 prototype 作用域——作用域是容器特性不是对象生命周期管理的万能锤。"
