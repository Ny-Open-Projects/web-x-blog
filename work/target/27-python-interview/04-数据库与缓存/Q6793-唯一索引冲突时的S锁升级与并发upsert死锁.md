---
title: "[Q6793] 唯一索引冲突时的 S 锁升级：三个并发 upsert 为什么互相等死"
date: 2026-11-25
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6793 · 唯一索引冲突时的 S 锁升级：三个并发 upsert 为什么互相等死

难度：P7 ｜ 标签：InnoDB、唯一索引、插入意向锁、S 锁升级、upsert、死锁、wait-for graph

基线：MySQL 5.7 与 8.0 的 ODKU 加锁差异；Python 3.12 用锁表 + 等待图模拟 S→X 升级与环检测，全标准库实跑。

**问**：库存表用 `INSERT ... ON DUPLICATE KEY UPDATE stock=stock-1` 做扣减，压测时三条并发同键请求偶发死锁，`SHOW ENGINE INNODB STATUS` 里三个事务都显示 `HOLDS S lock on PRIMARY`、同时 `WAITING FOR X lock`。插入意向锁不是"互相兼容"的吗，为什么会死？"锁升级"升的到底是什么？MySQL 8.0 之后这个死锁为什么变了，但没消失？

**答**：

- **结论**：先纠正一个常见混淆：**插入意向锁（insert intention lock）是间隙锁的一种，纯插入之间互不冲突**——它只和"别人在这个间隙上持有的间隙锁"冲突。真正的死锁不在插入意向锁，而在**唯一键冲突检查**：RR 隔离级别下，`INSERT` 撞到已存在的唯一键时，要对那条已存在的记录加 **S 锁**做重复性确认；`ON DUPLICATE KEY UPDATE` 接着要把这条记录改成新值，于是对同一记录发起 **S→X 的原地升级**。三个事务各自持有 S、又都想升 X，S 与 X 互斥，等待图形成一个三元环——完整的死锁。这不是"锁数量升级"，是**同一资源上的锁模式升级**，而模式升级无法靠"再加一把锁"解决。
- **取舍**：绕过升级路径有三条，各有代价。① `INSERT IGNORE`：冲突检查只拿 S、不升 X，三向死锁消失，但它把**所有**错误都吞成 warning（数据截断、类型不匹配也静默），只适合纯幂等标记位；② MySQL 8.0 的 ODKU 改为**直接取 X**，不再有 S→X 升级，三向死锁消失，但热点行被完全串行化、冲突也消耗自增 ID，高并发下吞吐被单行锁限制；③ 显式 `SELECT ... FOR UPDATE` 先拿 X 再写，等于把升级路径提前成"一次 X 申请"，语义最清晰，代价是多一次往返、且要自己处理"记录不存在"的场景。工程上还要加**死锁重试**（按 error 1213 分类退避），因为再好的写法也挡不住多唯一键、二级索引顺序不一致带来的两向死锁。
- **实战**：某秒杀接口的 upsert 在 QPS 峰值出现每分钟数次死锁，重试后成功率仍掉到 97%。死锁日志显示三个事务对同一 `PRIMARY` 记录各持 S、各等 X，与压测复现一致。短期把 SQL 改成"先 `SELECT ... FOR UPDATE` 拿 X，再 insert/update"，死锁归零，代价是 P99 多了 0.4ms；中期把热点库存拆成 16 个桶（`sku_id + bucket`）分散单行竞争，upsert 落到不同行；长期把预扣移到 Redis，DB 只做异步落账。三层做完，同一 SKU 的写吞吐从 1.2 万/s 提到 8 万/s。

下面用锁表 + wait-for 图把三种写法的加锁路径跑一遍。

```python
# 唯一键冲突的 S→X 升级 vs 直接 X: 等待图环检测
class LockMgr:
    def __init__(self):
        self.holders, self.waits = {}, {}

    def acquire(self, txn, res, mode):
        held = {t: m for t, m in self.holders.get(res, {}).items() if t != txn}
        if all(mode == "S" and m == "S" for m in held.values()):
            self.holders.setdefault(res, {})[txn] = mode
            self.waits.pop(txn, None)
            return True
        self.waits[txn] = set(held)          # 记录等待边
        return False

    def release_all(self, txn):
        for res in self.holders:
            self.holders[res].pop(txn, None)
        self.waits.pop(txn, None)

    def cycle(self):
        def dfs(n, path):
            for b in self.waits.get(n, ()):
                if b == path[0]:
                    return path + [b]
                if b in self.waits and b not in path:
                    r = dfs(b, path + [b])
                    if r:
                        return r
        for n in self.waits:
            r = dfs(n, [n])
            if r:
                return r
        return None


def scenario(mode):
    m, ts = LockMgr(), ["T1", "T2", "T3"]
    if mode == "upgrade":                    # 5.7: 先做重复键检查拿 S
        for t in ts:
            m.acquire(t, "uk:sku42", "S")
        print(f"   [{mode}] 各持 S 的事务数: "
              f"{sum(m.holders['uk:sku42'].get(t) == 'S' for t in ts)}")
    for t in ts:                             # 再写: 升 X / 直接 X
        if not m.acquire(t, "uk:sku42", "X"):
            print(f"   [{mode}] {t} 申请 X 被阻塞")
    ring = m.cycle()
    print(f"   [{mode}] waits={ {k: sorted(v) for k, v in m.waits.items()} } ring={ring}")
    return ring, m


ring_up, m_up = scenario("upgrade")
assert ring_up and ring_up[0] == ring_up[-1], "三向 S→X 升级必成环"
assert all(len(m_up.waits[t]) == 2 for t in ("T1", "T2", "T3"))
ring_dx, m_dx = scenario("direct_x")
assert ring_dx is None and m_dx.holders["uk:sku42"] == {"T1": "X"}, "直接 X 只排队"
print("    → 实测 5.7 的 S→X 升级成环; 8.0 直接 X 只有一个持有者, 其余排队")

# 死锁处置: 每轮回滚环里编号最大的事务, 数需要几个 victim
m, alive, victims = LockMgr(), ["T1", "T2", "T3"], 0
for t in alive:
    m.acquire(t, "uk:sku42", "S")
while True:
    for t in alive:
        m.acquire(t, "uk:sku42", "X")
    ring = m.cycle()
    if not ring:
        break
    victim = max(ring[:-1])
    print(f"   [3] 环 {ring} → 回滚 {victim}")
    m.release_all(victim)
    alive.remove(victim)
    victims += 1
print(f"    → 实测 三向死锁至少要回滚 {victims} 个事务, 剩 {alive} 存活")
assert victims >= 2
```

**追问一**：为什么插入意向锁"互不冲突"，但并发插入同一个唯一键还是会互相等？—— 插入意向锁描述的是"我要在某间隙里插一条记录"的意图，多个插入意图可以同时存在，所以纯插入不互斥。但唯一键要求**全局唯一**：当目标键已存在，插入方必须对那条已存在记录加 S 锁确认"它确实存在且值没变"，这一步是记录锁不是间隙锁；随后 ODKU 要改它，就变成 S→X。换句话说，冲突来自"对已存在记录的读写"，不是"插入意向"本身。如果没有重复键（每条都插新键），就只能看到插入意向锁，不会出现这个环。

**追问二**：有了死锁重试，还需要改 SQL 吗？—— 需要，重试只是**兜底**不是**解法**。死锁频率随并发度平方上升，重试会把失败放大成延迟尖刺，并在重试风暴里二次打满连接池。判断标准：如果死锁日志里同一形态反复出现（同表、同索引、同顺序），说明加锁顺序/升级路径有结构性问题，必须改；如果只是低频、随机分布，重试 + 退避就够了。改的方向按代价排序：统一加锁顺序（多唯一键场景）→ 把升级提前成显式 X → 拆热点行 → 把竞争移出 DB。

## 背诵要点

- 插入意向锁是间隙锁的一种，插入意图之间兼容；唯一键冲突检查对**已存在记录**加 S 锁，ODKU 再升 X，S 与 X 互斥。
- 三并发同键 upsert 在 5.7 形成 S→X 的三元等待环；8.0 改为直接 X，变成串行等待而不是成环。
- 处置顺序：统一加锁顺序 → `SELECT ... FOR UPDATE` 提前拿 X → 拆热点行 → 移出 DB；死锁重试只做兜底，error 1213 分类退避。

## 复盘追问

- 死锁日志里三个事务都 `HOLDS S`、都 `WAITING FOR X`，说明走的是哪条加锁路径？（唯一键重复检查的 S + ODKU 的 S→X 升级；纯插入意向锁不会出现这个形态）
- 为什么把 `INSERT ... ON DUPLICATE KEY UPDATE` 改成 `SELECT ... FOR UPDATE` 再写能消除死锁？（把"先 S 后升 X"的两步合成一次 X 申请，消灭升级窗口；代价是多一次往返）
