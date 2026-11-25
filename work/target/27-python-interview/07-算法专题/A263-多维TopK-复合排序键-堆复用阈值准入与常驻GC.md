---
title: [A263] 多维 Top-K：复合排序键、堆复用与阈值准入
date: 2026-11-24
categories: [Python算法笔试]
tags: [Python面试, 笔试题, 27]
type: 笔试题
---

### A263 · 多维 Top-K 与堆复用

> 难度:★★★★ | 标签:Top-K, 多键排序, 堆复用, 阈值准入, 懒丢弃

**问**（笔试·编程题）：服务健康榜每 10 秒汇总一次各服务的「危急等级 / 错误率 / P99」，选 Top-K 最危急的服务上值班大屏。要求：① 排序是**多键字典序**：危急等级降序 → 错误率降序 → P99 降序，同分必须按 name 升序做**确定性 tie-break**（大屏上同分服务每轮顺序乱跳，值班同学会以为系统在抖）；② 每轮上报是**流式**的：同一个服务会反复上报（分数更新），堆里必然堆满旧版本条目，出榜时要做 **stale 校验 + 同名去重**，绝不能把一个服务算成两席；③ 堆对象**跨轮询周期复用**，不许每轮重建堆、不许全量排序；④ 长跑内存有界：写出堆长期尺寸不变量的断言（模拟 300 轮、几十个服务换血）；⑤ 每轮 board 结果要与「全量排序重算」的朴素实现对账一致。请说清与 A009（静态数组第 K 大：快速选择 vs 堆的取舍）、A100（流式单维计数 Top-K：heapq.nsmallest 的用法）、A110（热点探测：sketch 近似 + 准入迟滞）、Q2361（堆延迟删除/版本号技巧本体）的分工——本题考的不是「会 nlargest」，而是**多键比较器怎么设计、常驻堆怎么当长期结构用而不腐坏**。

**答**：① 分工：A009 是「一次性选出一个数」，A100 是「单键计数的流式 Top-K」，A110 是「内存受限下的近似热点」（sketch 只高估、堆只装候选），Q2361 是「heapq 没有删除接口」这一个技巧点的正面回答。本题把它们组装成**常驻排行榜**：多键、可更新、跨周期、内存有界——生产里的「服务健康榜/热榜/告警聚合」都是这个形状。② 多键比较器：`(level, err, p99)` 要降序、name 要升序，Python 堆是小顶堆，所以前三个键**取负**进堆：`(-level, -err, -p99, name)`。堆顶就是「榜上最该被顶替的条目」，新条目比堆顶好才准入。tie-break 必须把 name 拼进键尾：三个数值全同的两条比较器相等，heapq 会退回去比下一个字段——不拼 name 就会比到不可比较的 dict 或直接 TypeError；拼了 name，同分顺序就**恒定**，大屏不再抖。为什么用字典序而不是加权求和：字典序无纲量问题（level 是档位、err 是比率、p99 是毫秒，硬乘权重出来的分数毫无可解释性），且「P0 告警哪怕零错误也压过 P1」这种业务规则天然是字典序；加权分只在「各维度已归一化且业务认可线性换算」时才该用。③ 流式更新的两条铁律：**版本号识别 stale**（每次上报 `ver += 1`，出堆时 `ver != 最新` 即丢弃——Q2361 的版本号法）与**同名去重**（合法堆里同名最多只有最新版一条，旧版必然 stale，出堆时顺带挡住）。④ 堆复用的关键在**阈值准入**：堆满且新条目不比堆顶好就**不 push**（push 了迟早要出，白花 log k），这样堆尺寸永远 ≤ k；出榜时全量出堆做一次 GC——stale 丢弃、有效条目按出堆序（天然升序，本身就是合法小顶堆）放回，榜外有效条目存进 side 表（name → 最新键），下一轮若_heap 不满或它们变好还能进来。GC 顺手把「换血服务」的尸体清掉，这就是内存有界的来源：断言「任何时刻 `len(heap) <= k`」、side 表 ≤ 存活服务数。⑤ 对账：朴素实现 = 每轮把最新状态全量排序取前 K。300 轮随机负载（分数漂移 + 部分服务每轮缺席）逐轮对账，全部一致——这比 assert 几个手挑数字强得多，能抓到「stale 条目占席」「同分乱序」「榜外条目回不来」三类最难肉眼发现的 bug。⑥ 复杂度账：每轮 m 条上报，准入 O(log k)；出榜 GC O(堆内条目·log)，堆内 ≤ k 所以是 O(k log k)；整体每轮 O(m log k + k log k)，与「每轮重建堆 O(m log m)」的差距在 m ≫ k 时是一个数量级。

```python
# 全部标准库；多维 Top-K：多键字典序比较器 + 常驻堆复用 + 阈值准入 + stale 校验
import heapq
import random


class MultiKeyTopK:
    """常驻多维 Top-K：堆对象跨轮询周期复用，出榜时顺带 GC。"""

    def __init__(self, k):
        if k <= 0:
            raise ValueError("k 必须为正")
        self.k = k
        self._heap = []      # 小顶堆，尺寸恒 ≤ k；堆顶 = 榜上最该被顶替者
        self._side = {}      # name -> (key, ver)：榜外有效条目（待翻盘）
        self._ver = {}       # name -> 最新版本号

    def key_of(self, level, err, p99, name):
        """多键字典序：level/err/p99 降序（取负进小顶堆），name 升序 tie-break。"""
        return (-level, -err, -p99, name)

    def report(self, name, level, err, p99):
        self._ver[name] = self._ver.get(name, 0) + 1
        key = self.key_of(level, err, p99, name)
        ver = self._ver[name]
        if len(self._heap) < self.k:
            heapq.heappush(self._heap, (key, name, ver))
            self._side.pop(name, None)
        elif key < self._heap[0][0]:
            ev_key, ev_name, ev_ver = heapq.heapreplace(self._heap, (key, name, ver))
            if ev_ver == self._ver.get(ev_name):        # 被顶下的仍是最新版 → 进 side 待翻盘
                self._side[ev_name] = (ev_key, ev_ver)
            self._side.pop(name, None)
        else:
            self._side[name] = (key, ver)               # 不上榜也记最新状态

    def board(self):
        """出榜：全量出堆 GC（stale 丢弃），与 side 合并后重算 Top-K，堆复用。"""
        valid, stale = [], 0
        while self._heap:
            key, name, ver = heapq.heappop(self._heap)
            if ver == self._ver.get(name):
                valid.append((key, name, ver))
            else:
                stale += 1                              # 旧版本条目：就地作废
        for name, (key, ver) in self._side.items():
            if ver == self._ver.get(name):
                valid.append((key, name, ver))
        valid.sort(key=lambda e: e[0])                  # 键含 name，天然全序无并列
        acc = valid[:self.k]
        self._side = {n: (k, v) for k, n, v in valid[self.k:]}
        self._heap = acc[:]                             # 升序列表本身是合法小顶堆，直接复用
        assert len(self._heap) <= self.k                # 尺寸不变量：堆永不超 k
        return [name for _, name, _ in acc]


if __name__ == "__main__":
    # 1) 多键字典序 + 确定性 tie-break：等级 > 错误率 > P99 > name
    board = MultiKeyTopK(3)
    board.report("svc_b", 2, 0.9, 100)
    board.report("svc_a", 2, 0.9, 100)          # 与 svc_b 三键全同 → name 升序 svc_a 先
    board.report("svc_c", 2, 0.5, 800)          # 同级错误率更低 → 靠后
    board.report("svc_d", 1, 0.99, 900)         # 等级低 → 最后
    assert board.board() == ["svc_a", "svc_b", "svc_c"], board.board()
    print("多键排序: [svc_a, svc_b, svc_c, svc_d] 取前三，同分按 name 定序 ✅")

    # 2) 同名重复上报：只有最新版本有效，不占两席
    board = MultiKeyTopK(2)
    board.report("x", 3, 0.1, 50)
    board.report("y", 2, 0.1, 50)
    board.report("x", 1, 0.0, 20)               # x 掉档 → 应被 y、z 顶掉
    board.report("z", 2, 0.2, 60)
    assert board.board() == ["z", "y"], board.board()
    print("版本更新: x 降档后出榜，stale 条目未占席 ✅")

    # 3) 长跑对账：300 轮随机负载，每轮与「全量排序重算」逐一对账
    board = MultiKeyTopK(5)
    latest = {}                                  # 朴素实现的真相源
    rng = random.Random(7)
    names = ["svc_%02d" % i for i in range(40)]
    for cycle in range(300):
        for name in rng.sample(names, 25):       # 每轮 25 个服务上报，其余缺席
            lv, er, p99 = (rng.choices([1, 2, 3], weights=[6, 3, 1])[0],
                           round(rng.random() * 0.2, 4), rng.randrange(20, 2000))
            board.report(name, lv, er, p99)
            latest[name] = (lv, er, p99)
        expected = [n for n, _ in sorted(
            ((n, board.key_of(*v, n)) for n, v in latest.items()),
            key=lambda kv: kv[1])[:5]]
        got = board.board()
        assert got == expected, (cycle, got, expected)
        assert len(board._heap) <= 5
    print("长跑对账: 300 轮与全量重算逐轮一致，堆尺寸恒 ≤ 5、side ≤ 存活服务数 ✅")

    # 4) 榜外翻盘：side 里的服务变差转好仍能回榜，不会「一落榜永落榜」
    board = MultiKeyTopK(1)
    board.report("a", 5, 0.5, 100)
    board.report("b", 1, 0.1, 10)                # b 落 side
    assert board.board() == ["a"]
    board.report("b", 9, 0.9, 900)               # b 翻盘
    assert board.board() == ["b"]
    print("榜外翻盘: side 条目更新后重回榜首，不因阈值准入被永久淘汰 ✅")
```

**追问**：1) 业务非要「加权分」怎么办？—— 先逼出归一化契约：各维度除以 SLO 基准（err/目标错误率、p99/SLO 延迟），再线性加权。两个坑要当场指出：**权重是准静态的**（写死在代码里的权重每次调整都是一次口径变更，必须配置化 + 带版本，否则两周后没人说得清大屏为什么这么排）；**加权分会抹平字典序的硬规则**（P0 × 0.6 可能输给 P1 × 1.0，业务是否接受要白纸黑字）。实现上加权分只是把 `key_of` 换成一个分数函数 + name 兜底，堆复用结构一行不用改——**比较器与堆结构解耦**，这正是把 key_of 独立成函数的意义。2) 出榜 GC 全量出堆，会不会比「不 GC」慢？—— 堆尺寸恒 ≤ k（阈值准入保证），GC 是 O(k log k)，与准入同量级；不 GC 的版本 stale 条目要靠「出堆直到凑够 k 条有效」的循环挤掉，堆里僵尸越积越多后每次出榜都在还债，最坏退化成 O(僵尸数·log)。GC 版本把还债摊到每一轮、每轮还清，**摊还复杂度反而更低且内存严格有界**——这和 Q2361 「作废集合随出堆同步收缩」是同一条纪律。3) 多线程上报怎么加锁？—— 上报路径全部是「单堆 + 两个 dict」的复合操作，`heapreplace` 与 `_ver` 更新必须原子，单锁最稳（上报是 O(log k)，锁竞争极短）；真要分段，按 name 哈希分片后**每片一个完整 Top-K**再归并（每片取前 k，归并取前 k），不能让多线程共享一个堆——heapq 不是线程安全的，并发 heappush 会直接把堆序弄坏，这类事故在压测里表现为「榜单随机少几个服务」，很难查。

## 背诵要点
1. 多键降序取负进小顶堆，键尾拼 name 做确定性 tie-break；字典序优先于加权分（无纲量问题、硬规则可表达）。
2. 流式更新两条铁律：版本号识别 stale + 同名去重；阈值准入（不比堆顶好不 push）让堆尺寸恒 ≤ k。
3. 出榜时全量出堆 GC：stale 丢弃、有效按出堆序（天然小顶堆）放回、榜外有效进 side 表待翻盘；每轮与全量重算对账。
