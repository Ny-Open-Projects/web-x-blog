## 思路与架构
"GORM 事务操作"本质是**ORM 层对 MySQL 事务的封装选择**：把"自动提交回滚的回调式"与"精细部分回滚的显式式"两种封装，映射到"整段成否 / 长事务细粒度"两类业务，并叠加"关预编译 + 用 tx 对象"两个工程前提。它把 714- 三张主卡收敛成一张选型表。

```text
GORM 事务选型树
  业务形态 ──► 选哪条 ──► 关键 API
  整段成或不成      回调式        db.Transaction(func(tx) error)
                                     return error→回滚 / nil→提交
  长事务要保前半段  显式式        db.Begin + Savepoint + RollbackTo + Commit
  任意事务          前提          DisablePreparedStmt=true + 用回调内 tx
```

## 方案取舍
| 写法 | 回滚粒度 | 适合 | 注意 |
| --- | --- | --- | --- |
| 回调 Transaction | 整段 | 简单成否 | 用回调内 tx |
| 显式 Begin/Savepoint | 定点 | 长事务细粒度 | 记得 Commit |
| 原生 SQL 事务 | 语句级 | 非 ORM 场景 | 见 1229 |

**取舍结论**：简单业务用回调式最省心；需要保留前半段用显式式+Savepoint。两条路共同前提是"事务客户端关预编译、操作走 tx 对象"——预编译语句与事务争连接资源，故常初始化双客户端隔离。

**分层边界**：原生 MySQL 事务（ACID/autocommit）在 1229-transaction-basics；Go MySQL 初始化与预编译在 1246（只引不重述）；本卡只讲 GORM ORM 层封装 [边界]。

## 答题技巧
1. **先报两路**：回调式（自动）/显式式（Savepoint 部分回滚）。
2. **点两个前提**：关预编译 + 用 tx 对象——这是 GORM 事务最容易翻车的两点。
3. **嵌套用内层 tx**：回调嵌套每层用各自入参 tx，不碰外层 db。
4. **粒度对比收尾**：整段成否用回调，长事务细粒度用显式。
5. **避坑**：不在事务里用外层 db；不忘 Commit 致连接悬挂；不以为回滚只能全有全无。

## 细节与核心 API

```go
// 事务：db.Transaction 自动 commit/rollback
err := db.Transaction(func(tx *gorm.DB) error {
    if err := tx.Create(&order).Error; err != nil { return err }   // 返回 err 自动 rollback
    if err := tx.Model(&user).Where("id=?", uid).Update("bal", gorm.Expr("bal - ?", amt)).Error; err != nil {
        return err
    }
    return nil // 返回 nil 自动 commit
})
// 手动事务
tx := db.Begin()
defer func() { if r := recover(); r != nil { tx.Rollback() } }()
// 关键：必须用 tx 而非 db 执行后续语句，否则脱离事务
// 隔离级别：db.Session(&gorm.Session{SkipDefaultTransaction: true}) 可关自动事务提升性能
```
