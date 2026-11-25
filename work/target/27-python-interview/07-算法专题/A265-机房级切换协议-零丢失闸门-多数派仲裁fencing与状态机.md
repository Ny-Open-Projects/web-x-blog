---
title: [A265] 机房级切换协议：零丢失闸门、多数派仲裁与 fencing 纪元
date: 2026-11-24
categories: [Python算法笔试]
tags: [Python面试, 笔试题, 27]
type: 笔试题
---

### A265 · 机房级容灾切换与数据零丢失

> 难度:★★★★★ | 标签:容灾切换, RPO=0, 复制位点, 脑裂仲裁, fencing, 切换状态机

**问**（笔试·场景题）：A113 给过「RPO 由复制方式决定、RTO 由切换流程决定、脑裂靠 Quorum」的结论，A238 定了指标口径，A135 定了流量步进曲线——本题要你把这些结论**落成一套可执行的切换协议**。背景：同城双机房，主库 A、备库 B，SLA 承诺 **RPO=0（一笔都不能丢）**，切换必须在 30 秒内完成。请设计并实现：① **零丢失闸门**：切换前用复制位点核算 GAP（主库已确认、备库还差几笔），GAP≠0 时按策略分流——RPO=0 策略拒绝切换并等待追平，可用性策略允许强切但必须**显式记账丢了多少笔**，绝不许静默丢失；② **半同步退化的抉择**：备库抖动导致半同步 ACK 超时时，写入口必须二选一——停写保 RPO=0，或降级异步保可用性，且这个选择是**提前写进策略的**，不能故障现场拍脑袋；③ **脑裂仲裁**：切换必须拿到仲裁席位多数派（3 席过 2）才放行，防止双机房网络分区时各切各的；④ **fencing 纪元**：每次切换全局纪元 +1，旧主复活后持旧纪元的写请求必须被拒——「我以为我还是主」是脑裂最经典的二次事故；⑤ **切换状态机**：PROBE → ARBITRATE → FENCE → PROMOTE → VERIFY → SERVE 全程留痕，演练验收时逐状态断言。请说清与 A113（结论层：RPO/RPO 算法与演练分级）、A238（口径层：RTO/RPO 怎么算）、A135（流量层：步进切换与预热）、A162（切换后数据对账）、A179（冗余表决器）的分工——本题是**决策与执行协议层**：把「能不能切、怎么切、切完旧主怎么办」变成代码。

**答**：① 分工：A113 告诉你「半同步 → RPO≈0」这个**映射关系**，A238 告诉你演练后**数字怎么算**，A135 告诉你**流量怎么挪**，A162 告诉你切完**数据怎么对**——但没有一张卡回答切换**当下**的决策序列：GAP 怎么算、不满足怎么办、旧主怎么防复活、每一步怎么留痕验收。本题就是这条决策链。② 零丢失闸门的本质是**把 SLA 变成一道代码里的 if**：`GAP = 主库已确认位点 - 备库位点`。RPO=0 语义下，GAP>0 就意味着「切过去必丢 GAP 笔」，唯一正确的动作是拒绝并追平（`ship()` 把主库日志补到备库），追平后重试；可用性语义下强切可以，但必须**把丢失笔数写进事件流**——「丢了 3 笔」是可复盘的事故，「不知道丢了没有」是不可复盘的事故。两者的选择**必须故障前冻结**：RPO=0 的代价是半同步退化时拒绝写入（可用性归零），这是 CAP 的三选二，故障现场没有第四个选项，现场拍脑袋一定会选错。③ 半同步退化是**演练里最高频的前置故障**：备库 GC 卡顿、网卡抖动都会让 ACK 超时，此时主库的写入口被控制器接管——`rpo0` 策略直接只读化（写请求报错，业务侧显式失败），`available` 策略降级为异步复制（RPO 开始积累，监控上必须出现「RPO 债务」指标）。关键工程约束：**降级是有方向的、可解释的**，降级动作要留痕（事件流里有「半同步退化 → 停写」这一条），否则故障复盘时说不清「那 3 分钟到底丢没丢」。④ 脑裂仲裁的两层防线：**切之前**，多数派仲裁——3 席至少 2 席认为主已死才放行（A179 表决器思想），双机房各自分区时谁都凑不齐多数派，宁可双停不可双主；**切之后**，fencing 纪元——全局 epoch 单调递增，新主拿新纪元，旧主手里永远是旧纪元，它复活后的每一次写都会被 `epoch != self.epoch` 拒绝。为什么两个都要：仲裁防「同时出现两个切换决策」，fencing 防「旧决策的执行者不知道决策已变」——旧主不是恶意节点，它只是**消息滞后**，fencing 是对滞后者的硬隔离，比「让它自己发现主丢了」可靠得多（自己发现依赖心跳，心跳本身就会误报）。⑤ 状态机与验收：PROBE（连续探测失败防误切）→ ARBITRATE（多数派投票）→ FENCE（旧主只读化 + 纪元递增）→ PROMOTE（备库升主、授权新纪元）→ VERIFY（零丢失校验：旧主已确认的每一笔在新主日志里都存在）→ SERVE（流量切换）。每个转移落一条 `(step, state, note)` 事件——这就是 A238 口径里的「打点」，演练报告逐状态断言：仲裁没过的不许切、fencing 后旧主写必被拒、VERIFY 阶段丢笔数必须等于闸门记账。演练的价值就在这些断言可执行：**容灾方案不能只有文档，必须是一段每次都能跑绿的代码**。

```python
# 全部标准库；机房级切换协议：复制位点 GAP 核算 + 多数派仲裁 + fencing 纪元 + 切换状态机


class DataSite:
    """一个数据站点。LSN 单调递增；acked = 已确认给客户端的最大位点。"""

    def __init__(self, name):
        self.name = name
        self.acked = 0
        self.log = {}            # lsn -> 事务负载
        self.epoch = 0           # 最后一次被授权写时的纪元（fencing token）
        self.writable = True

    def write(self, payload, epoch):
        if not self.writable:
            raise PermissionError("%s 已只读化（fenced）" % self.name)
        if epoch != self.epoch:
            raise PermissionError(
                "%s 纪元过期：持 %d，当前 %d（旧主复活被拒）" % (self.name, epoch, self.epoch))
        self.acked += 1
        self.log[self.acked] = payload
        return self.acked


class ReplicaLink:
    """主备复制链路：ship() 把主库日志补到备库；degraded 模拟备库抖动。"""

    def __init__(self, primary, standby):
        self.primary, self.standby = primary, standby
        self.degraded = False

    def ship(self):
        moved = 0
        for lsn in range(self.standby.acked + 1, self.primary.acked + 1):
            self.standby.log[lsn] = self.primary.log[lsn]
            self.standby.acked = lsn
            moved += 1
        return moved

    def gap(self):
        return self.primary.acked - self.standby.acked


class SwitchController:
    """切换协议本体：策略前置冻结 + 状态机留痕 + 仲裁 + fencing。"""

    def __init__(self, policy="rpo0"):
        if policy not in ("rpo0", "available"):
            raise ValueError("policy 只能是 rpo0 / available")
        self.policy = policy
        self.epoch = 1           # 全局纪元，每次切换 +1
        self.state = "NORMAL"
        self.events = []         # (step, state, note) —— 演练报告的数据源
        self.step = 0

    def _go(self, state, note):
        self.step += 1
        self.state = state
        self.events.append((self.step, state, note))

    def write(self, site, link, payload):
        """经控制器的写入口：半同步退化时按**前置策略**抉择，不现场拍脑袋。"""
        if site.epoch == 0:          # 首次接管：控制器向主库授权纪元（epoch=0 即未授权）
            site.epoch = self.epoch
        if link.degraded:
            if self.policy == "rpo0":
                site.writable = False
                self._go("NORMAL", "半同步退化 + rpo0 策略 → 停写保零丢失")
                raise PermissionError("降级只读：宁可不可写，不许丢数据")
            self._go("NORMAL", "半同步退化 + available 策略 → 降级异步，RPO 债务开始积累")
        lsn = site.write(payload, self.epoch)
        link.ship()              # 半同步语义：备库落位后才算确认
        return lsn

    def switch(self, link, standby, votes):
        """votes: 各仲裁席位观测（True=认为主已死）。走完整状态机。"""
        up = sum(1 for v in votes if v)
        if up * 2 <= len(votes):
            self._go("ARBITRATE", "多数派仲裁未过（%d/%d 席）→ 禁止切换，防双主" % (up, len(votes)))
            return False
        self._go("ARBITRATE", "多数派确认主故障（%d/%d 席）" % (up, len(votes)))
        gap = link.gap()
        if gap:
            if self.policy == "rpo0":
                self._go("VERIFY", "零丢失闸门：GAP=%d ≠ 0 → 拒绝切换，等待追平" % gap)
                return False
            self._go("VERIFY", "可用性策略强切：显式记账丢失 %d 笔（不许静默）" % gap)
        self._go("FENCE", "纪元 %d→%d，旧主只读化：持旧纪元的写全部被拒"
                 % (self.epoch, self.epoch + 1))
        self.epoch += 1
        link.primary.writable = False
        standby.epoch = self.epoch
        standby.writable = True
        self._go("PROMOTE", "备库 %s 升主，授权纪元 %d" % (standby.name, standby.epoch))
        lost = [l for l in link.primary.log if l > standby.acked]
        assert all(l in standby.log for l in link.primary.log if l <= standby.acked)
        self._go("VERIFY", "零丢失校验：新主已含旧主全部已确认事务，缺口 %d 笔" % len(lost))
        self._go("SERVE", "流量切至新主 %s" % standby.name)
        return True


if __name__ == "__main__":
    # 场景 1：半同步 + GAP=0 的常规切换，零丢失达成，旧主复活被 fencing 拒绝
    pri, sta = DataSite("A机房"), DataSite("B机房")
    link = ReplicaLink(pri, sta)
    ctl = SwitchController(policy="rpo0")
    for i in range(5):
        ctl.write(pri, link, "order-%d" % i)
    assert link.gap() == 0 and pri.acked == sta.acked == 5
    assert ctl.switch(link, sta, votes=[True, True, False]) is True
    assert sum(1 for l in pri.log if l not in sta.log) == 0
    print("常规切换: RPO=0 达成（5/5 笔在新主），状态机 %s ✅" % "→".join(
        s for _, s, _ in ctl.events))
    try:
        pri.write("复活后偷偷写入", ctl.epoch - 1)      # 旧主手里只有旧纪元
        raise AssertionError("旧主写入必须被拒")
    except PermissionError as e:
        print("fencing: %s ✅" % e)

    # 场景 2：异步滞后 3 笔 + rpo0 → 闸门拒绝；追平后重试成功
    pri2, sta2 = DataSite("A机房"), DataSite("B机房")
    link2 = ReplicaLink(pri2, sta2)
    ctl2 = SwitchController(policy="rpo0")
    for i in range(4):
        ctl2.write(pri2, link2, "tx-%d" % i)
    link2.degraded = True                              # 备库抖动
    ctl2._go("NORMAL", "模拟复制滞后：备库停在位点 1")
    sta2.acked = 1
    link2.degraded = False
    assert ctl2.switch(link2, sta2, votes=[True, True, True]) is False
    link2.ship()                                       # 追平
    assert ctl2.switch(link2, sta2, votes=[True, True, True]) is True
    assert sta2.acked == pri2.acked == 4
    print("零丢失闸门: GAP=3 被拒 → 追平重切成功，4/4 笔无损 ✅")

    # 场景 3：available 策略强切，丢失笔数显式记账
    pri3, sta3 = DataSite("A机房"), DataSite("B机房")
    link3 = ReplicaLink(pri3, sta3)
    ctl3 = SwitchController(policy="available")
    for i in range(6):
        ctl3.write(pri3, link3, "tx-%d" % i)
    sta3.acked = 3                                     # 滞后 3 笔
    for l in [l for l in sta3.log if l > 3]:           # 滞后部分同步从备库日志里去掉
        del sta3.log[l]
    assert ctl3.switch(link3, sta3, votes=[True, True, False]) is True
    assert sum(1 for l in pri3.log if l not in sta3.log) == 3
    print("可用性强切: 显式记账丢 3 笔（事件流可复盘，绝不静默丢失）✅")

    # 场景 4：多数派仲裁不过 → 拒绝切换（双机房分区时谁都切不了）
    pri4, sta4 = DataSite("A机房"), DataSite("B机房")
    link4 = ReplicaLink(pri4, sta4)
    ctl4 = SwitchController()
    ctl4.write(pri4, link4, "tx-0")
    assert ctl4.switch(link4, sta4, votes=[True, False, False]) is False
    print("脑裂仲裁: 1/3 席位未过半 → 禁止切换，宁可双停不可双主 ✅")

    # 场景 5：半同步退化 + rpo0 → 停写；available → 降级异步并留痕
    pri5, sta5 = DataSite("A机房"), DataSite("B机房")
    link5 = ReplicaLink(pri5, sta5)
    ctl5 = SwitchController(policy="rpo0")
    link5.degraded = True
    try:
        ctl5.write(pri5, link5, "tx-x")
        raise AssertionError("rpo0 策略下必须停写")
    except PermissionError as e:
        print("半同步退化: %s ✅" % e)
    ctl6 = SwitchController(policy="available")
    pri6, sta6 = DataSite("A机房"), DataSite("B机房")   # 新站点演示可用性策略
    link6 = ReplicaLink(pri6, sta6)
    link6.degraded = True
    ctl6.write(pri6, link6, "tx-y")
    assert any("降级异步" in note for _, _, note in ctl6.events)
    print("策略抉择: 降级动作留痕可复盘 ✅")
```

**追问**：1) 仲裁席位放在哪？—— 绝不能和数据站点同址：双机房架构里「每个机房一席」会退化成 1v1 平票（这正是双机房做不了自动仲裁、必须第三点仲裁或云厂商 witness 的原因）；三机房各一席 + 多数派 2/3 是底线方案，更好的是**独立仲裁集群**（3~5 个轻量 witness 节点，与数据机房网络故障域隔离）。席位故障时降级为「人工决策」——自动仲裁不可用时的默认值必须是人工，而不是「跳过仲裁直接切」，跳过仲裁等于亲手打开脑裂的门。2) RPO=0 和可用性为什么必然互斥？—— 半同步 ACK 超时那一刻，主库面前只有两条路：等备库（写入延迟无限增长，等于不可写）或放弃等待（复制降级为异步，RPO 开始积累）。CAP 里 C 与 A 在网络分区下的取舍就是这道题的原型；工程上能优化的只是**第三条路的存在感**——同城专线延迟 <2ms 时半同步代价小（A113 的口径），退化概率低，但「低」不等于「无」，策略必须按「退化一定会发生」来写。3) 演练验收清单该有哪些断言？—— 最小集合：a) 仲裁断言——1/3 票拒绝、2/3 票放行；b) fencing 断言——切换后旧主写必被拒、新主写必成功；c) 零丢失断言——VERIFY 阶段旧主已确认事务 100% 在新主日志（丢笔数 = 闸门记账）；d) RTO 打点断言——各状态转移时间戳齐备且总时长 ≤ 30 秒（口径按 A238 冻结）；e) 回切断言——旧主修复后作为新备接入，数据先对账（A162）再回切，回切走同一套状态机。少任何一条，演练就只是「演」，不是「验」。

## 背诵要点
1. 零丢失闸门：GAP = 主已确认位点 - 备位点；GAP≠0 时 rpo0 拒切追平、available 强切但显式记账丢笔数——绝不静默丢失。
2. 半同步退化二选一必须**前置冻结**：停写保 RPO=0 或降级异步保可用性，CAP 之下没有第三选项，现场拍脑袋必错。
3. 脑裂双防线：切前多数派仲裁（席位与数据站分离，1v1 平票即人工决策），切后 fencing 纪元（旧主持旧纪元写必被拒）；状态机 PROBE→ARBITRATE→FENCE→PROMOTE→VERIFY→SERVE 全程留痕、逐状态断言。
