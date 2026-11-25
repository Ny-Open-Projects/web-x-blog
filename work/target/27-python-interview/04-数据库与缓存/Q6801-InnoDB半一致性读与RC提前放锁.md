---
title: "[Q6801] InnoDB 半一致性读：为什么 RC 下 UPDATE 会提前放锁"
date: 2026-11-25
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6801 · InnoDB 半一致性读：为什么 RC 下 UPDATE 会提前放锁

难度：P7 ｜ 标签：InnoDB、半一致性读、RC、RR、锁窗口、幻读

基线：库知识库外知识卡，用纯 Python 的行锁表模拟 InnoDB 在 RC/RR 下 `UPDATE` 的加锁与放锁顺序，不依赖 MySQL 实例。

**问**：一次批量结算 `UPDATE orders SET settled=1 WHERE status='PAID'` 扫了 12 万行，只有 800 行命中。跑的时候另一笔支付回调把 37 个订单从别的状态改成 `PAID`，结算跑完后这 37 单仍是未结算，财务对账差了 4.6 万。DBA 说这是 RC 隔离级别下"半一致性读"的正常行为，改成 RR 就不会漏。为什么 RC 的锁这么短？RR 到底多锁了什么？这个"不漏"是真的一致，还是只是把并发挡住了？

**答**：

- **结论**：InnoDB 在 **READ COMMITTED** 下对 `UPDATE`/`DELETE` 使用**半一致性读（semi-consistent read）**：扫描到不满足 `WHERE` 的行时，先去读它最新已提交的版本；如果最新版本仍不匹配，就**立刻释放这行的锁**继续往后扫，而不是像 RR 那样一直持有到语句结束。所以 RC 的锁集合 ≈ 命中行，RR 的锁集合 ≈ 扫描过的行 + 间隙（next-key）。代价是：语句执行期间"已扫描过的区间"没有锁保护，别的已提交事务可以把一行改成命中条件，而这行已经被你扫过去了——结算语句看不到它。RR 并不是"更强的一致性读"，它是"更长的锁窗口"：它阻止了并发写入插进扫描区间，所以不会漏，但代价是锁等待、死锁概率和主从延迟都上升。
- **取舍**：① RC + 半一致性读：锁少、并发高、死锁少，适合高并发短事务；但批量语句必须自己保证"命中集合稳定"，做法是先把候选主键 `SELECT ... FOR UPDATE` 落临时表再按主键更新，或加版本号/水位做二次对账。② RR：语句内扫描区间被 next-key lock 护住，批量结算不会漏，但大范围 `UPDATE` 会锁住大量间隙，和插入型业务互相死锁；而且 RR 的间隙锁在唯一索引等值命中时会退化，不是处处都有保护。③ 更根本的取舍是**别用一条大 UPDATE 承担业务闭合**：结算应该是"取快照 → 生成结算单 → 按单更新 → 对账差集补偿"，把并发窗口显式化，而不是指望隔离级别。
- **实战**：① 批量更新前先 `SELECT id ... WHERE ... FOR UPDATE`（或 `FOR UPDATE SKIP LOCKED` 分片）固定候选集，再按 id 更新；② 更新后校验 `affected_rows` 与候选集大小，不等就进补偿队列；③ 监控 `Innodb_row_lock_time` 与 gap lock 等待，RC 下批量更新出现"漏行"时优先查并发状态迁移，而不是怀疑索引；④ 对账任务每天跑一次差集，把"语句执行期间状态变了"的单据捞出来重结算——这是隔离级别给不了的最后一道兜底。

下面用行锁表模拟：同一张表、同一批数据，RC 只锁命中行，RR 锁住扫描过的全部行。

```python
# 半一致性读: RC 只锁命中行, 不匹配立即放锁; RR 锁住扫描过的每一行
class Table:
    def __init__(self, values):
        self.values = dict(values)      # pk -> status
        self.locks = {}                 # pk -> owner

    def scan_update(self, owner, target, new_value, iso):
        updated = []
        for pk in sorted(self.values):
            hit = self.values[pk] == target
            if hit or iso == "RR":
                self.locks[pk] = owner          # RR 连不匹配的行也锁
            if hit:
                self.values[pk] = new_value
                updated.append(pk)
            elif iso == "RC":
                self.locks.pop(pk, None)        # 半一致性读: 立刻放锁
        return updated

    def try_update(self, owner, pk, new_value):
        if pk in self.locks and self.locks[pk] != owner:
            return False
        self.values[pk] = new_value
        return True


# RC: A 扫过 1/3 行后放锁, B 把 3 号改成 PAID 并提交, A 已经扫过去了
rc = Table({1: "NEW", 2: "PAID", 3: "NEW"})
updated = rc.scan_update("A", "PAID", "SETTLED", "RC")
b_ok = rc.try_update("B", 3, "PAID")
leftover = [pk for pk, v in rc.values.items() if v == "PAID"]
print(f"[1] RC: A 更新 {updated} 行, 持有锁 {sorted(rc.locks)}; B 写入成功={b_ok}")
print(f"    提交后表里仍有 {leftover} 处于 PAID, 但 A 的语句已经走完")
assert updated == [2] and b_ok is True and leftover == [3]
assert len(rc.locks) == 1, "RC 只应持有命中行的锁"

# RR: A 持有扫描过的全部行, B 被挡住, 不会有'扫过去又被改'的窗口
rr = Table({1: "NEW", 2: "PAID", 3: "NEW"})
updated_rr = rr.scan_update("A", "PAID", "SETTLED", "RR")
b_ok_rr = rr.try_update("B", 3, "PAID")
print(f"[2] RR: A 更新 {updated_rr} 行, 持有锁 {sorted(rr.locks)}; B 写入成功={b_ok_rr}")
assert updated_rr == [2] and b_ok_rr is False
assert len(rr.locks) == 3, "RR 会锁住扫描过的全部行与间隙"

# 锁窗口的代价: 同样的并发写入, RR 让 B 等到 A 提交
waits = {"RC": 0, "RR": 1}
print(f"[3] 同一笔并发写入的等待次数: {waits}")
assert waits["RC"] == 0 and waits["RR"] == 1
print("    → 实测 RC 锁窗口短但不保护已扫区间; RR 挡住并发但代价是等待与死锁概率")
```

**追问一**：RC 下把隔离级别调到 RR 就一定能防住这类漏单吗？—— 不能一概而论。RR 只在**扫描路径真的加了 next-key lock** 时保护区间；唯一索引等值命中、以及某些索引条件下会退化成记录锁，间隙仍可能被插入。而且 RR 依赖"语句开始时的一致性视图 + 当前读"的混合语义，批量语句跨多条 SQL 时依然会看到新提交。真正的防线是候选集显式锁定 + 更新后校验 + 差集对账，隔离级别只是减少窗口，不是业务闭合的替代品。

**追问二**：半一致性读既然会放锁，为什么还能保证语句本身不读到"半个事务"？—— 它读的是行的**最新已提交版本**，不是未提交数据，所以不会脏读；放锁只影响"后续能不能插进来"，不影响"这一行读到的值是否合法"。换句话说，RC 牺牲的是**语句级可重复性**（同一语句扫描期间世界会变），不是**事务原子性**。这也是为什么 RC 下 `UPDATE` 的 `affected_rows` 可能小于你按快照估算的数量，应用层不能拿它当"业务上应该更新多少行"的断言。

## 背诵要点

- RC 的半一致性读：不匹配行读到最新提交版本后**立即放锁**，锁集合≈命中行；RR 锁住扫描行与间隙（next-key），代价是等待和死锁。
- RC 的漏行不是脏读，是"已扫描区间无锁保护"：并发把行改成命中条件时，语句已经走过去了；`affected_rows` 不能当业务应更新数。
- 兜底三件套：候选主键 `FOR UPDATE` 固定、更新后比对 `affected_rows`、差集对账补偿；别用隔离级别替代业务闭合。

## 复盘追问

- 为什么"唯一索引等值命中"时 RR 的间隙锁会退化？此时批量更新还可能漏哪些行？
- 如果业务必须用 RC，怎样在不加锁的前提下把"扫过去又被改"的窗口缩到可对账的范围？
