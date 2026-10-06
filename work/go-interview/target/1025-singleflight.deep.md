# 1025 Singleflight 与并发原语（深挖）

> 分类：Go 并发 | 难度：中高 | 题型：原理深挖 | 频率：高 | 关键词：**singleflight、请求合并、CyclicBarrier、WaitGroup、缓存击穿**

> 原文锚点：第 1~94 段「singleflight 原理与场景、CyclicBarrier 扩展」

## 思路与架构
singleflight 解决「相同 key 并发只回源一次」，架构三层：
- 接入层：缓存未命中处调用 `g.Do(key, fn)`。
- 合并层：Group 用 `map[key]*call` 去重，锁保护并发读写。
- 等待层：call 内 WaitGroup 让后续请求阻塞共享首个结果；channel 用于中断/通知。
CyclicBarrier 是并列的同步原语，强调「多对等 goroutine 到齐放行 + 可循环」，与 singleflight 的「合并回源」语义不同，不可混用。

## 方案取舍
- 用 singleflight 而非限流：限流是「削峰控速率」，singleflight 是「同 key 并发合并为一次」，目标不同。
- 用 singleflight 而非批处理：批处理主动攒一批再发，singleflight 被动合并同时刻请求，透明无感。
- key 设计：key 必须能唯一标识回源目标（如缓存名+参数），过粗会误合并、过细则失去合并效果。
- Forget 的取舍：结果有时效时 Forget 让同 key 重新回源；滥用会导致每次都回源，失去合并意义。

## 答题技巧
1. 开口先给场景：「缓存击穿——大量并发同时回源压垮 DB」。
2. 讲清三步走：声明 Group → 缓存未命中调 Do(key, fn) → 同 key 并发只一次回源。
3. 源码一句话：map[key]*call 去重 + WaitGroup 等待，首个跑 fn 写 val，其余共享。
4. 对比收尾：singleflight 合并回源 ≠ 限流 ≠ 批处理；CyclicBarrier 是另类「多对等到齐」同步原语。
5. 实战话术：「用 singleflight 包住回源函数，key 用缓存名，20 个并发最终只打 1 次 DB。」
