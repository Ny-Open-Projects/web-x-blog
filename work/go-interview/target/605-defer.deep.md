# 605 defer 执行顺序与使用场景深挖

> 分类：Go 错误处理 / defer | 难度：L3 | 题型：深挖 | 频率：高 | 关键词：**LIFO** / **链表栈** / **收尾场景** / **recover** / **context cancel**
> 原文锚点：第 1~47 段「defer链表栈LIFO;场景:关文件/HTTP body/DB/释放锁/recover/context cancel/计时;申请即defer」

## 思路与架构
defer 由两个维度构成——**顺序维度**（LIFO，链表栈挂 goroutine，最后声明插头部、退出从头部取）与**场景维度**（函数退出前收尾：关资源/释放锁/recover/cancel/计时）。回答时先讲清"为什么 LIFO"（结构根因），再枚举"在哪用"（场景清单），最后落"两个关键坑"（recover 直接调用、cancel 防泄漏）。

## 方案取舍
```text
defer 矩阵：
──────────────────────────────────────────────────────────────
维度          结论                      易错/边界
顺序          LIFO(链表栈)              最后声明最先执行
结构          实例挂 goroutine 单链表   退出统一弹出
时机          return 求值后、返回前      见 607
场景-资源     关文件/HTTP body/DB       申请即 defer
场景-锁       释放锁                    防忘解锁/死锁
场景-恢复     recover 捕获 panic        必须直接调用、仅当前协程
场景-取消     cancel() context         主退通知子退、忘写则泄漏
场景-计时     defer 记耗时             含后续耗时

设计法则：
- 申请资源立即 defer 释放（提前 return/panic 也不漏）
- recover 直接写在 defer 函数体；跨协程各自 recover
- context 必 defer cancel，防子协程泄漏
- LIFO 顺序靠链表栈，非数组栈
```

## 答题技巧
```text
面试话术（先顺序后场景，再两个坑）：
1. 顺序：LIFO，链表栈挂 goroutine，最后声明插头部、退出从头部取
2. 时机：return 求值后、真正返回前（见 607）
3. 场景：关资源/释放锁/recover/cancel/计时，申请即 defer
4. 坑1：recover 必须直接调用、仅当前协程
5. 坑2：defer cancel 主退通知子退，忘写泄漏
```

> 边界：return 时机见 607-defer-exec-order；循环变量坑见 607-defer-loop-var；命名返回值见 607-defer-named-return；context 见 602-withvalue-timeout；协程泄漏见 1022-goroutine-leak；优雅退出见 713-graceful-shutdown。本卡只深挖"defer 顺序与场景"不重述 defer 底层字段。
