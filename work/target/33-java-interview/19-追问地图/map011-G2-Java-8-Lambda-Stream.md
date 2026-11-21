---
title: "G2. Java 8 Lambda/Stream 核心机制？（一面高频）"
date: 2026-11-18
categories: [Java面试, 追问地图]
tags: [Java面试, 补漏卡, 33]
type: 补漏卡
disableNunjucks: true
---

### G2. Java 8 Lambda/Stream 核心机制？（一面高频）

**【参考回答（可背）】** 四点：① Lambda 本质是**函数式接口实例**（单抽象方法），编译为 invokedynamic + LambdaMetafactory 生成实现类（非匿名内部类，延迟到首次调用才生成）；② Stream 三段式：源 → 中间操作（惰性，只记录不执行）→ 终端操作触发；③ 中间操作分无状态（filter/map）与有状态（sorted/distinct），有状态操作会打断"一次遍历"优化；④ **parallelStream 底层就是 commonPool**——IO 任务禁用（呼应第 2 章 2.4a.2 的全局故障域坑），数据量小或操作轻时并行反而慢（拆分/合并开销）。
**【追问链】** Optional 解决什么？→ 显式表达"可能缺失"，消灭 `if (obj != null)` 防御式代码；map/flatMap 链式判空。Stream 关闭吗？→ 文件 IO 的 Stream 要 try-with-resources。
**【P10 加分项】** 团队规范视角："我们规定 Stream 只用于集合内的声明式转换，业务逻辑复杂的用 for——可读性优先；parallelStream 一律需压测证明有收益才允许。"
