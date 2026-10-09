# 714 GORM 事务操作总览（两种 API + 关预编译）

> 分类：数据库 / GORM | 难度：L3 | 题型：用法题 | 频率：中 | 关键词：**Transaction 回调** / **Begin/Savepoint** / **关预编译** / **用回调内 tx**
> 原文锚点：第 3~50 段「GORM 事务两种写法：回调 transaction 方法 / 常规 begin+commit+rollback；事务必须关闭 SQL 预编译；用回调内的 tx 对象」

## 一句话总述
GORM 事务有两条路：**① 回调式** `db.Transaction(func(tx *gorm.DB) error)`——函数内 return error 自动回滚、return nil 自动提交，且支持嵌套；**② 显式式** `tx := db.Begin()` + `Savepoint` + `RollbackTo` + `Commit` 做部分回滚。前提是**事务客户端必须关闭 SQL 预编译**（`DisablePreparedStmt=true`），且操作必须用**回调内/Begin 出来的 tx 对象**，而非外层 db。

## 面试官视角
- 考察意图：是否真写过 GORM 事务、知不知道预编译开关与 tx 对象陷阱
- P5 知 GORM 有事务；P6 能讲清回调式的 error/nil 语义与嵌套；P7 能讲"为何关预编译"和"必须用 tx 对象"
- 红旗：事务里继续用外层 `db` 而非 `tx`；不知道事务要关预编译会报错
- 惊艳点：点出"预编译语句占用连接资源、与事务冲突，故事务客户端要单独关预编译，可初始化两个 GORM 客户端隔离" [源码]

## 主问答
**Q（面试官原话）：** 用 GORM 怎么写事务？
**A：**
1. **两条 API**：回调式 `db.Transaction(func(tx *gorm.DB) error{...})` 最简洁；显式式 `tx := db.Begin()` 后 `tx.Commit()/tx.Rollback()` 或更细的 `Savepoint`+`RollbackTo` 做部分回滚 [源码]。
2. **前提·关预编译**：执行事务的 GORM 客户端须设 `DisablePreparedStmt=true`——预编译语句会占用连接资源、与事务机制冲突，不关会报错；实践中可初始化**两个客户端**（一个带预编译跑普通查询、一个关预编译跑事务）[源码]。
3. **铁律·用 tx 对象**：回调里必须用入参 `tx`（嵌套内层也要用回调内的 `tx`），不能用外层 `db`——外层 db 不在当前事务上下文里，用了等于脱离事务 [经验]。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 几种写法 | 广度 | 回调/显式 | P5 |
| L2 | 回调语义 | 机制 | error回滚/nil提交 | P6 |
| L3 | 为何关预编译 | 边界 | 资源冲突 | P6+ |
| L4 | 用哪个对象 | 实战 | 必须用 tx | P7 |
| L5 | 部分回滚 | 进阶 | Savepoint | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| GORM v2 | DisablePreparedStmt 选项 | 事务客户端关预编译长期成立 |

## 关键代码
```go
// 回调式：return error→回滚，return nil→提交（支持嵌套）
err := db.Transaction(func(tx *gorm.DB) error {
    if err := tx.Create(&user1).Error; err != nil { return err } // 用 tx，不是 db
    return nil // 提交
})
// 显式式 + 部分回滚
tx := db.Begin()
tx.Create(&u4); tx.SavePoint("step1"); tx.Create(&u5)
tx.RollbackTo("step1") // 仅回滚 u5（step1 之后）
tx.Commit()
```

## ⚠️ 原文纠错
源码将若干术语音译为崩坏词，本卡统一为规范术语（goRM/goline→GORM/Go、事物→事务、circle→SQL、boss→false、高德OYM→GORM、隐射→映射、浪值→零值/false、签到事务→嵌套事务、TS→tx、测刻→savepoint 等）；技术结论未做事实性更正 [经验]。

## 总结与追问预判
- GORM 事务两路：回调（嵌套/自动提交回滚）与显式（Savepoint 部分回滚）；前提关预编译、用 tx 对象。
- 原生 MySQL 事务概念见 1229；Go MySQL 初始化/预编译见 1246（只引不重述）。
