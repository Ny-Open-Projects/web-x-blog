---
title: [Q1691] pipeline 与 MULTI/EXEC: 省往返与原子是两件事
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1691 · pipeline 与 MULTI/EXEC: 省往返与原子是两件事

> 难度:★★★★ | 标签:Redis, 原子性

**问**:pipeline 和 Redis 事务 MULTI/EXEC 有什么区别?什么时候必须用后者?

**答**:pipeline 只解决网络问题:客户端把一批命令打包发送省去逐条 RTT,但服务器仍可能穿插执行其他客户端的命令,块内没有原子性。MULTI/EXEC 解决原子问题:命令先入队,EXEC 时整块连续执行,期间其他客户端无法插入。语义差异还有:pipeline 里某条失败不影响其他条,MULTI 队列阶段语法错误让整块不入队,EXEC 后的运行时错误只跳过出错那条继续。需要原子性(计数对、锁释放校验、扣减组合)时用 MULTI/EXEC 或 Lua,pipeline 里再包 MULTI 两者兼得;还要记得 EXEC 前用 WATCH 可实现 CAS 重试。

```python
# file: code/04_数据库与缓存/q1691_pipeline_vs_multi.py
"""pipeline 与 MULTI/EXEC: 省往返与保证原子是两件事"""

class Server:
    """单线程命令执行器: 按到达顺序逐条执行"""

    def __init__(self):
        self.kv = {}
        self.log = []

    def exec_cmd(self, client, cmd):
        op, key, val = cmd
        if op == "SET":
            self.kv[key] = val
        elif op == "INCR":
            self.kv[key] = self.kv.get(key, 0) + 1
        self.log.append((client, op, key))
        return self.kv[key]

def run_pipeline(server, a_cmds, b_cmd):
    """pipeline 只是打包发送, 服务器仍可能穿插其他客户端的命令"""
    for i, cmd in enumerate(a_cmds):
        server.exec_cmd("A", cmd)
        if i == 1:                        # A 的第二条之后, B 插队
            server.exec_cmd("B", b_cmd)

def run_multi(server, a_cmds, b_cmd):
    """MULTI/EXEC: 命令先入队, EXEC 时整块连续执行, 其他客户端无法穿插"""
    queued = list(a_cmds)                 # MULTI 后命令进入队列
    server.exec_cmd("B", b_cmd)           # B 的命令在 EXEC 之前执行
    for cmd in queued:                    # EXEC 原子块
        server.exec_cmd("A", cmd)

a_cmds = [("SET", "lock", "A"), ("INCR", "hits", None), ("SET", "lock", "A-again")]
b_cmd = ("SET", "lock", "B")

s1 = Server()
run_pipeline(s1, a_cmds, b_cmd)
print("pipeline 场景执行序:", [op + ":" + key for _, op, key in s1.log])
print("  最终 lock =", s1.kv["lock"], "-> B 插在中间, A 的第二次 SET 又覆盖了 B")

s2 = Server()
run_multi(s2, a_cmds, b_cmd)
print("MULTI/EXEC 场景执行序:", [op + ":" + key for _, op, key in s2.log])
print("  最终 lock =", s2.kv["lock"], "-> B 先执行完, A 的块内三条连续完成")
print("结论: pipeline 只省 RTT 不保证原子; 需要原子用 MULTI/EXEC 或 Lua; WATCH 提供 CAS 重试")
print("另注: pipeline 内某条失败不影响其他条; MULTI 块内语法错误整块不入队, 运行时错误跳过该条继续")
```

**追问**:
- pipeline 一次塞十万条会怎样?——客户端内存与服务器输入缓冲都被打大,分批几百上千条最稳,响应逐批回收。
- Lua 和 MULTI 怎么选?——需要中间计算与条件分支用 Lua,MULTI 只是命令打包;但 Lua 会阻塞,脚本要短,集群下注意 KEYS 约束。

---
