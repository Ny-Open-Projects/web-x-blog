# 714 GORM 回调式事务与嵌套控制

> 分类：数据库 / GORM | 难度：L3 | 题型：用法题 | 频率：中 | 关键词：**Transaction(func)** / **return error 回滚** / **嵌套事务** / **用内层 tx**
> 原文锚点：第 21~31,43~45 段「transaction 方法传回调函数(入参是 ORMDB 指针)；return error 回滚(含嵌套内层)，return nil 提交；嵌套内层必须用回调内的 tx」

## 一句话总述
GORM 回调式事务 `db.Transaction(func(tx *gorm.DB) error)`：函数体**返回 error 即整体回滚、返回 nil 即提交**，且天然支持**嵌套**——内层 `tx.Transaction(...)` 的 error 只会回滚内层、外层 return nil 仍提交其他成功部分。关键是**每一层都用自己回调入参的 tx**，绝不用外层 db。

## 面试官视角
- 考察意图：是否理解回调式的自动提交/回滚契约与嵌套粒度
- P5 知 return error 回滚；P6 能讲嵌套事务的独立回滚；P7 能讲清"内层 error 不连坐外层、外层用什么对象"
- 红旗：外层 return nil 却期望内层 error 也提交；嵌套里误用外层 db
- 惊艳点：用"user1 提交、user2 因内层 error 回滚、user3 随外层 nil 提交"的最小例子讲清嵌套粒度 [源码]

## 主问答
**Q（面试官原话）：** 回调式事务里 return error 和嵌套事务是怎么表现的？
**A：**
1. **error/nil 即回滚/提交**：回调返回 **error → 该事务内所有语句回滚**；返回 **nil → 提交**。不需手写 Commit/Rollback [源码]。
2. **嵌套独立回滚**：外层 `tx.Transaction` 内再起内层 `tx.Transaction`，内层 return error 只回滚**内层**那部分；外层最终 return nil 仍提交其余成功部分（如 user1、user3 提交，user2 回滚）[源码]。
3. **对象铁律**：嵌套内层必须用**内层回调入参的 tx**，外层也用**外层回调入参的 tx**——任何一层用外层 `db` 都会脱离当前事务上下文，这是高频翻车点 [经验]。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | return error? | 语义 | 回滚 | P5 |
| L2 | 嵌套回滚范围 | 粒度 | 仅内层 | P6 |
| L3 | 外层 nil 影响? | 边界 | 提交其余 | P6+ |
| L4 | 用哪个对象 | 实战 | 各自 tx | P7 |
| L5 | 与 Savepoint 比 | 选型 | 粗粒度 vs 细粒度 | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| GORM v2 | 嵌套事务语义 | 回调 error/nil 契约长期成立 |

## 关键代码
```go
err := db.Transaction(func(tx *gorm.DB) error {
    tx.Create(&user1)                      // 提交
    tx.Transaction(func(itx *gorm.DB) error { // 内层用 itx
        tx.Create(&user2)                  // 假设此处 return error
        return errors.New("fail")
    }) // 仅 user2 回滚
    tx.Create(&user3)                      // 随外层 nil 提交
    return nil
})
```

## ⚠️ 原文纠错
源码将若干术语音译为崩坏词，本卡统一为规范术语（goRM→GORM、事物→事务、签到事务→嵌套事务、TS→tx、ORMDB→gorm.DB 等）；技术结论未做事实性更正 [经验]。

## 总结与追问预判
- 回调式：error 回滚、nil 提交、嵌套独立粒度、每层用各自 tx。
- 总览与关预编译见 714-gorm-transaction-overview；部分回滚见 714-gorm-transaction-savepoint。
