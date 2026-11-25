---
title: "[Q6730] pipeline 响应错位：EXEC 的嵌套数组与错误占位"
date: 2026-11-23
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6730 · pipeline 响应错位：EXEC 的嵌套数组与错误占位

难度：P7 ｜ 标签：Redis、pipeline、MULTI/EXEC、协议解析

基线：Python 3.12；redis-py 4.x/5.x `pipeline(transaction=False)`；纯 Python 模拟 RESP 回复配对。

**问**：为了省 RTT，把"读 A、写 B、读 C"三条命令塞进一个 pipeline。上线后发现偶发拿到别人的结果：读 A 返回了 C 的值，写 B 的返回被当成读 A。更奇怪的是，加了 `MULTI/EXEC` 之后错位更频繁。pipeline 不是严格按发送顺序返回吗？为什么会串？

**答**：
- **结论**：Redis 单连接上的回复确实是**严格 FIFO**，但"按位置取第 i 个回复"这个假设只在**每条命令恰好一个顶层回复**时成立。两个破坏点：① `MULTI/EXEC` 事务里，`MULTI` 回 `+OK`、入队命令回 `+QUEUED`、`EXEC` 回一个**数组**（每个命令一个元素），嵌套结构让按位置取值的代码整体错一位；② 某条命令返回错误（`-WRONGTYPE`）时，错误本身仍占一个回复槽位，如果上层"跳过错误继续读"却没有推进对应关系，后续全部错位。连接复用/重连时如果没清空残留缓冲，还会读到上一条请求的回复。
- **取舍**：pipeline 的收益是 RTT 摊薄，代价是**错误处理与结果配对复杂**。`transaction=True` 会把命令包进 MULTI/EXEC，获得原子性但多两个回复且失败语义不同（运行时错误不回滚）；`raise_on_error=False` 能把错误当值返回，便于逐条对账，但要求调用方自己检查每条结果。高可靠场景宁可多一次 RTT，也不要在一个 pipeline 里混事务与非事务命令。
- **实战**：① pipeline 里不要混 `MULTI/EXEC` 与普通命令，事务单独一次；② 用 `raise_on_error=False` 拿到逐条结果，按**命令下标**校验类型（错误对象 vs 值）；③ 连接归还池前必须把未读回复读干净，异常路径也要 drain，否则下个请求读到脏回复；④ 对关键写操作，pipeline 后跟一次 `EXISTS`/读回校验，别假设"发出去了就是成功"。

```python
"""pipeline 结果配对：按槽位 vs 按结构，演示两种错位。"""

ERROR = object()


def flatten_naive(replies: list[object]) -> list[object]:
    """错误做法：把 EXEC 的数组展开，假设一条命令一个标量。"""
    out: list[object] = []
    for r in replies:
        if isinstance(r, list):
            out.extend(r)          # 嵌套数组被摊平，位置全乱
        else:
            out.append(r)
    return out


def pair_by_index(cmds: list[str], replies: list[object]) -> list[tuple[str, object]]:
    """正确做法：一条命令对应一个顶层回复，不展开、不跳过。"""
    assert len(cmds) == len(replies), "回复数与命令数不一致，连接已错位"
    return list(zip(cmds, replies))


if __name__ == "__main__":
    cmds = ["MULTI", "INCR counter", "EXEC"]
    replies: list[object] = ["OK", "QUEUED", [1]]
    naive = flatten_naive(replies)
    print("摊平后:", naive)
    print("按位置取 INCR 的结果:", naive[1], "(实际是 QUEUED，真值在数组里)")

    paired = pair_by_index(cmds, replies)
    print("正确配对:", paired[-1], "-> EXEC 的结果是 [1]")

    # 错误占位：错误也占一个槽位，不能跳过
    cmds2 = ["GET a", "LPUSH b", "GET c"]
    replies2: list[object] = ["v1", ERROR, "v3"]
    paired2 = pair_by_index(cmds2, replies2)
    for cmd, rep in paired2:
        print(f"{cmd:<10} -> {'ERROR' if rep is ERROR else rep}")
    print("结论：错误必须占位返回；跳过它会让后续结果整体前移一位")
```

**追问一**：`MULTI/EXEC` 里某条命令运行时失败（如对字符串执行 `LPUSH`），其他命令会回滚吗？
→ 解析：不会。Redis 事务没有回滚，`EXEC` 会执行所有入队命令，失败的返回错误对象，成功的照常生效。只有**入队时**的语法/未知命令错误会让 `EXEC` 整体拒绝（EXECABORT）。所以事务不能当关系库的原子回滚用，业务要自己补偿。

**追问二**：为什么连接池归还连接前必须 drain 未读回复？
→ 解析：pipeline 的回复是延迟读取的，异常发生时可能只读了一部分。若直接把连接放回池，下一个请求会从缓冲区里读到上一条请求的剩余回复，表现为"结果串号"。正确做法是异常时关闭连接（不归还），或循环读到预期条数/超时后再决定丢弃。
