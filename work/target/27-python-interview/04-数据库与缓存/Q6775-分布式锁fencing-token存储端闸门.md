---
title: "[Q6775] 锁过期后旧进程还在写：fencing token 的存储端互斥闸门"
date: 2026-11-24
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6775 · 锁过期后旧进程还在写：fencing token 的存储端互斥闸门

难度：P7 ｜ 标签：分布式锁、fencing token、互斥窗口、租约、单调闸门

基线：Python 3.12；模拟锁服务的单调 token 授予与存储端的写闸门校验，复现"锁过期后旧持有者恢复写入"被拒绝的完整链路，全标准库实跑。

**问**：Redis 分布式锁有租约（TTL），任务卡顿超过 TTL 后锁被释放、第二个客户端拿到锁开始写——但第一个客户端恢复后**不知道锁已经易主**，继续写就造成双写互斥破坏。看门狗续期（Q972）能缓解，但续期失败/进程假死时呢？fencing token 是怎么把互斥从"锁服务建议"升级成"存储端强制"的？

**答**：
- **结论**：锁服务（Redis/etcd/ZooKeeper）本质是**协调者，不是存储互斥的执行者**——它发锁，但拦不住拿着过期锁的客户端直接写存储。fencing token 的做法：**锁服务每次授予锁时发一个单调递增的编号**（etcd 的 revision、ZK 的 zxid 都天然满足）；客户端写存储时**必须携带 token**；存储端维护"已接受的最大 token"，**只接受大于它的写入，旧 token 一律拒绝**。于是 GC 停顿/网络分区导致锁过期的场景里：客户端 A 恢复后仍以为自己持锁，带着旧 token 写入，被存储端闸门挡下——互斥从"希望客户端守约"变成"存储端物理强制"。与看门狗（Q972）的关系：看门狗降低过期概率，fencing token 保证过期后果可控——前者是概率防御，后者是结构性防御，生产锁方案两者都要。
- **取舍**：① token 校验必须放**存储端**且单调判断要原子：客户端自查等于没查（客户端无法感知自己已过期，这正是问题的起点）；② 不是所有存储都支持：Redis SET NX 不带 token 语义，要用 Lua 脚本里比较 token 或改用支持条件写的存储（DB 条件更新、etcd 事务）；③ 单调 token 的来源要全局唯一递增：多实例锁服务（Redlock 类）下编号可能重复/回退，Redlock 本身没有 token 机制，需自建（如 DB 号段）——这也是 Redlock 争议（Q971）里"多数派锁仍会失效"的实际落地对策；④ 兼容成本：所有写路径都要带 token，遗留代码路径是漏闸风险，用统一 DAO/网关层收口。
- **实战**：① 锁方案评审时问一句"锁过期后的双写怎么办"——答不出 fencing 或等价机制的设计不合格；② token 用数据库号段表或 etcd revision，别用进程内计数器（重启回退）；③ 拒绝事件要留痕：存储端每次 REJECT 记录（谁、token 几、已见最大几），它是互斥破坏的实时证据，直接告警；④ 幂等重放（Q1205/Q1481）与 fencing 互补：fencing 防旧持有者，幂等防网络重试的重复写，两条防线各自独立。

```python
"""Q6775 fencing token: 锁过期后旧持有者的写入必须被单调 token 闸门拒绝。"""
import itertools


class LockService:
    """每次授予锁 token 单调递增(如 etcd revision / 号段)."""
    def __init__(self):
        self._counter = itertools.count(1)
        self._holder: str | None = None

    def acquire(self, client: str) -> int:
        self._holder = client
        return next(self._counter)


class Storage:
    """fencing 闸门: 只接受大于已见最大 token 的写入."""
    def __init__(self):
        self.max_token = 0
        self.log: list[tuple[str, int]] = []

    def write(self, client: str, token: int, value: str) -> str:
        if token <= self.max_token:
            return f"REJECT {client} stale token={token}"
        self.max_token = token
        self.log.append((value, token))
        return f"ACCEPT {client} token={token}"


if __name__ == "__main__":
    s = Storage()
    ls = LockService()
    t1 = ls.acquire("A")                 # A 拿锁
    print(f"A 获锁 token={t1}, 写入: {s.write('A', t1, 'A-1')}")

    # A 遇 GC 停顿, 锁过期, B 获锁并写入
    t2 = ls.acquire("B")
    print(f"B 获锁 token={t2}, 写入: {s.write('B', t2, 'B-1')}")

    # A 恢复, 以为仍持锁继续写 -> 被闸门拒绝
    r = s.write("A", t1, "A-2")
    print(f"A 恢复后用旧 token 再写: {r}")
    ok = r.startswith("REJECT") and [v for v, _ in s.log] == ["A-1", "B-1"]
    print(f"校验: 互斥窗口外写入被拒, 日志顺序 {s.log} -> {'通过' if ok else '异常'}")
    print("结论：锁服务只能给'建议', fencing token 才把互斥落到存储端;")
    print("      token 必须存储侧单调校验, 客户端自查过期等于没查")
```

**追问一**：存储端比较 token 有并发竞态吗？两个请求同时到达怎么保证闸门本身不乱序？

→ 解析：闸门的"读 max_token → 比较 → 写 max_token"必须是原子的，否则两个并发写可能都读到旧值双双通过。落地上：① 关系型存储用条件更新 `UPDATE ... SET max_token=:t WHERE max_token < :t`（行锁保证原子），受影响行数为 0 即拒绝；② Redis 用 Lua 脚本（单线程执行天然原子）；③ etcd 用事务（compare-and-put）。真正的坑在"原子但非因果"：token 单调由锁服务保证，但存储端只见 token 数值——只要锁服务的授予顺序全局一致（单点计数或共识序号），闸门就是正确的。这也是为什么 Redlock 类多实例方案自建 token 时要用 DB 号段而不是各实例自增：**token 的单调性来自锁服务的一致性，闸门只能信任不能重建**。

**追问二**：fencing token 挡住了旧持有者，但挡不住"新持有者还没获锁完成、存储还没有任何 token"的初始窗口，怎么办？

→ 解析：初始窗口的问题其实是"存储端尚未见过任何 token"时，旧 token（如果是首次使用）也可能被接受——这是正常的：第一个 token 通过闸门后 max_token 就有下界了。真正的风险是**混合模式**：系统里一部分写路径带 token、一部分遗留路径不带（裸写）。裸写绕过闸门，fencing 全部失效。对策是收口而不是修补：① 写路径统一走 DAO/网关层，层内强制要求 token（缺 token 直接抛异常，测试环境就拦截）；② 灰度期给遗留路径加"无 token 写入"的审计日志，清零后才允许开启强制模式；③ 数据面校验兜底：关键表加乐观锁版本列（version check-and-set），即使闸门被绕过，版本冲突也能拦——fencing 是入口闸门，CAS 版本列是数据面防线，纵深防御。
