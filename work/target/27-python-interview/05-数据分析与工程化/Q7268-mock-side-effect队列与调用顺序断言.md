---
title: "[Q7268] 用例过了流程还是错的：mock 的 side_effect 队列与调用顺序断言"
date: 2026-11-24
categories: [Python数据分析工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7268 · 用例过了流程还是错的：mock 的 side_effect 队列与调用顺序断言

难度：P5 ｜ 标签：mock、side_effect、调用顺序断言、call_args_list、资损测试

基线：Python 3.12；实现最小 mock（调用记录 + side_effect 按次序出牌），注入"前几步成功最后一步炸"组合，用调用序列断言拦截资损路径，全标准库实跑。

**问**：测试只断言"返回值对"，但支付流程"扣款成功、发通知失败"和"先发通知再扣款"这两种错序根本测不出来。mock 的 side_effect 除了返回值还能干什么？多步流程的正确断言姿势是什么？怎么注入"第 N 步才失败"的现实故障组合？

**答**：
- **结论**：mock 的价值分三层，只断返回值是用了第一层：① **返回值**（`return_value`）：够测纯函数式调用，测不了状态与顺序；② **side_effect**：按调用次序依次出牌的**队列**——元素可以是返回值（每次不同）、异常（第 N 次调用抛错）、或可调用对象（参数校验逻辑）；这让"前两步成功、第三步网关超时"这类真实故障组合可以精确复现；③ **调用记录**（`call_args_list`/`mock_calls`）：被测对象到底按什么顺序、什么参数调了 mock——**多步流程的核心断言就是调用序列**：锁库存必须先于扣款、失败路径必须出现补偿调用且**不得出现**通知调用（资损红线）。顺序错了即使每一步返回值都对，流程也是错的——返回值断言对顺序完全失明。
- **取舍**：① 顺序断言的粒度：全序列精确匹配（`assert mock.mock_calls == [...]`）脆（重构加一行日志就挂）vs 关键子序列断言（`assert_has_calls`/先搜前缀）：核心业务不变量用全序列，辅助调用用子序列；② side_effect 队列长度要和调用次数对齐：次数多了 IndexError，这个"意外失败"本身是断言信号（mock 比预期多调了）；③ 部分真实 mock（autospec，Q7215）防接口漂移：纯 MagicMock 会接受任何方法名，接口改名后测试还在测一个不存在的 API；④ mock 什么不 mock 什么：外部网络/第三方 mock，本地确定性逻辑别 mock（mock 掉的字典操作测不出真实语义，Q1080 边界）。
- **实战**：① 资损类流程（支付/库存/退款）测试规范固定：正向序列断言 + 每一步失败的补偿序列断言 + 红线断言（失败后禁止出现的调用）；② side_effect 注入"第 N 步失败"用参数化覆盖每一步（N=1..总步数），这是流程测试的最小完备集；③ 断言失败信息要可读：把实际调用序列格式化进 assert 消息，不然排查 mock 测试全靠脑补。

```python
"""Q7268 mock 调用顺序断言: side_effect 队列 + 调用序列复盘, 拦截资损路径。"""


class Recorder:
    """最小 mock: 记录调用序列, side_effect 按 pop 次序给出(值/异常两用)."""

    def __init__(self, side_effect=None):
        self.side_effect = list(side_effect) if side_effect else None
        self.calls: list[tuple[str, tuple]] = []

    def __getattr__(self, name):
        def method(*args, **kw):
            self.calls.append((name, args or tuple(kw.items())))
            if self.side_effect is None:
                return None
            item = self.side_effect.pop(0)
            if isinstance(item, Exception):
                raise item
            return item
        return method


def run_payment(gw: Recorder) -> str:
    """支付流程: 锁库存 -> 扣款 -> 发通知, 任何一步失败要补偿前序动作."""
    gw.lock(sku="sku-1", qty=1)
    try:
        gw.charge(order_id="o1", cents=9900)
    except RuntimeError:
        gw.unlock(sku="sku-1")           # 补偿: 释放库存
        return "补偿完成, 未扣款未通知"
    gw.notify(order_id="o1")
    return "done"


if __name__ == "__main__":
    # side_effect 按调用次序出牌: 轮1 三步全过, 轮2 扣款时网关超时, 补偿 unlock 正常
    gw = Recorder(side_effect=[None, None, None, None, RuntimeError("网关超时"), None])

    r1 = run_payment(gw)
    print(f"轮1: {r1}, 序列 {[c[0] for c in gw.calls]}")

    r2 = run_payment(gw)
    print(f"轮2: {r2}, 序列追加 {[c[0] for c in gw.calls[3:]]}")

    seq = [c[0] for c in gw.calls]
    # 顺序断言: 超时后不允许出现 notify, 且必须出现 unlock 补偿
    ok = ("补偿" in r2 and "notify" not in seq[5:] and "unlock" in seq[5:]
          and gw.side_effect == [] and len(gw.calls) == 6)
    print(f"累计序列: {seq}")
    print(f"校验: side_effect 异常注入 + 顺序断言拦截资损 -> {'通过' if ok else '异常'}")
    print("结论：多步流程测试的核心断言是调用序列而非返回值;")
    print("      side_effect 队列按次序出牌, 可精确注入'前几步成功最后一步炸'的现实组合")
```

**追问一**：side_effect 传一个函数和传一个列表有什么区别？什么场景必须用函数？

→ 解析：传列表 = 按**调用次序**出牌（与参数无关，第几次调用就给第几个元素）；传函数 = 每次调用都执行它，**以实参为输入**决定返回值/异常——前者适合"脚本化的时序剧本"，后者适合"参数敏感的仿真"。必须用函数的场景：① 参数相关行为：`charge(cents=...)` 金额超过风控阈值才抛错——列表写不出这种条件逻辑；② 调用次数不确定：重试循环里"同一调用第二次成功"，用函数查内部计数器比精确数队列出牌位可靠；③ 多 mock 联动：工具调用的返回值取决于另一个 mock 的状态（库存查了才知道扣多少）。混合形态也合法：`side_effect=[f1, f2]` 每个元素都可以是可调用对象。选择原则：**剧本用列表，规则用函数**——把"第几次"写进剧本、把"什么参数什么结果"写进规则，测试的可读性完全不同。

**追问二**：调用顺序断言怎么应对"合法的顺序变化"？把测试写死顺序是不是过度约束？

→ 解析：要先区分"业务不变量"和"实现细节"。`unlock 必须在 charge 失败后出现`、`notify 不允许出现在失败路径`——这是资损不变量，写死是对的，任何顺序变化都该测试报警。`charge 内部先调风控还是先调计价`——这是实现细节，写死会把重构误报为失败。工程做法：① **不变量断言用谓词而非全序列**：`assert calls.index("unlock") > calls.index("charge")`、`assert "notify" not in failed_calls`——表达"相对顺序约束"而不是"完整剧本"；② 或在 mock 层加状态机检查：定义合法转移表（locked→charged→notified），Recorder 每次调用核对转移合法性，非法转移即失败——比逐调用断言更接近业务语义；③ 实现细节类顺序不进测试，进代码 review。判据一句话：**如果顺序变化会引发资损/数据错乱，就值得断言；只影响性能或日志，就别写死**。过度约束的测试和没有测试一样危险——前者教会团队"测试挂了不用看"。
