---
title: [A165] 客户端版本强制的灰度升级策略
date: 2026-11-20
categories: [Python算法笔试]
tags: [Python面试, 笔试题, 27]
type: 笔试题
---

### A165 · 客户端版本强制升级

> 难度:★★☆ | 标签:客户端, 版本管理, 强制升级

**问**（笔试·场景题）：App 旧版本调用已下线的 API——「客户端版本碎片化」（用户不升级，版本从 1.0 到 5.0 并存）怎么服务（服务端兼容旧版的成本曲线），「强制升级」的策略矩阵（硬强制/软提示/禁止降级），「强制升级」什么时候能开（未升级用户比例与新功能依赖的权衡），升级失败（应用商店审核慢）的兜底（服务端开关能力）？

**答**：① 版本碎片化现实：移动端用户升级滞后数月（强制更新会掉用户）——服务端策略：**兼容窗口**（旧 API 维护 N 个月，Q150 废弃流程）+ 旧版本「最简可用」（不新增功能但保基本可用）——兼容成本随版本数线性涨，版本压缩策略（强制升级消灭 1.0/2.0）。② 强制升级矩阵：**硬强制**（不可用，只有弹升级框——用于：安全漏洞/数据结构破坏性变更）、**软提示**（可用+提示条）、**禁止降级**（应用商店防降级攻击——旧版本有已知漏洞时禁止从 5.0 降到 2.0）——分级依据：影响面（安全 > 数据 > 功能）。③ 时机判断：硬强制开的前提 =「未升级用户的存量行为已兼容」（服务端不再破坏旧版）+「升级通道可用」（商店审核已过/热更通道就绪）——先保通道再强制，否则用户被卡死在升级页。④ 服务端开关兜底：升级失败（商店审核 3 天/用户不升）时，服务端 feature flag 兜住新功能（旧版本客户端拿到「功能未开放」而非崩溃）——「服务端永远比客户端多一层开关」。

```python
# 全部标准库；demo 实现「版本策略矩阵 + 硬强制时机判定」
import time

class VersionPolicy:
    def __init__(self, min_hard_version: str, supported: set[str]):
        self.min_hard, self.supported = min_hard_version, supported
    def version_tuple(self, v: str) -> tuple:
        return tuple(int(x) for x in v.split("."))
    def check(self, client_version: str) -> dict:
        vt = self.version_tuple(client_version)
        if client_version not in self.supported:
            hard = vt >= self.version_tuple(self.min_hard)
            return {"allowed": hard or False, "mode": "hard-upgrade"
                    if hard else "unsupported-killed",
                    "reason": "版本过旧且不满足硬强制条件（通道未就绪）"}
        if vt < self.version_tuple(self.min_hard):
            return {"allowed": True, "mode": "soft-prompt",
                    "reason": "软提示升级（功能可用）"}
        return {"allowed": True, "mode": "ok"}
    def can_enable_hard(self, upgrade_ratio: float, store_review_done: bool,
                        flag_for_old: bool) -> tuple[bool, str]:
        """硬强制时机：升级通道就绪 + 旧版本有服务端兜底。"""
        if not store_review_done:
            return False, "商店审核未过：用户被卡升级页 → 先保通道"
        if not flag_for_old:
            return False, "旧版本无服务端开关兜底：强制升级=旧版崩"
        if upgrade_ratio < 0.9:
            return False, f"升级率 {upgrade_ratio:.0%}：软提示阶段观察"
        return True, "通道就绪+兜底就绪+软提示已充分 → 可硬强制"

if __name__ == "__main__":
    pol = VersionPolicy(min_hard_version="4.0", supported={"4.0", "4.1", "5.0"})
    print(pol.check("5.0"))                      # ok
    print(pol.check("3.5"))                      # unsupported-killed（不在白名单）
    print(pol.check("4.0"))                      # soft-prompt
    assert pol.check("3.5")["mode"] == "unsupported-killed"
    ok, why = pol.can_enable_hard(upgrade_ratio=0.7, store_review_done=False, flag_for_old=False)
    print("硬强制时机:", ok, why)
    assert not ok
    ok2, why2 = pol.can_enable_hard(0.95, True, True)
    print("时机成熟:", ok2, why2)
    assert ok2
    # 口径：硬强制三前提（通道就绪/旧版兜底/软提示充分）；服务端永远比客户端多一层开关。
```

**追问**：1) 为什么「服务端永远比客户端多一层开关」？——客户端发出去就改不了（用户不升级=旧代码常驻），服务端随时可改——新功能上线时服务端 flag 控制（旧版本拿「未开放」响应），客户端代码只做「响应缺失时的兜底显示」——服务端开关是客户端碎片的唯一解药。2) 「禁止降级」的合理场景与误用？（提示：合理：旧版本有已知安全漏洞（降级=把漏洞装回去）；误用：为了「逼用户用新功能」禁降级——降级自由被剥夺会引发用户强烈反弹；界限是「安全」不是「产品意愿」）3) 版本碎片化的长期治理？（提示：热更能力（不进商店的修复通道，需合规审查）+ 强制升级的常态化节奏（每季度压一次最低版本）+ 服务端兼容成本预算（旧版本维护占研发容量 10% 上限——超了就推强制升级）——三管齐下压碎片）

## 背诵要点
1. 版本碎片化服务策略：兼容窗口 + 旧版最简可用 + 版本压缩（强制升级消灭老版本）。
2. 强制升级矩阵：硬强制（安全/数据破坏）/软提示/禁降级（安全）——硬强制三前提：通道就绪+旧版兜底+软提示充分。
3. 服务端永远比客户端多一层开关——flag 是客户端碎片的唯一解药；升级失败时旧版拿「未开放」而非崩溃。

## 复盘追问
1. 硬强制升级导致 2% 用户流失（卸载），业务方问责——怎么平衡？（提示：流失 2% vs 安全漏洞风险敞口——分级决策：安全类强制（流失可接受）、功能类不强制（用兼容兜底）；且强制前评估「不升级用户的活跃度」（僵尸用户强制升级反而「洗」掉沉默用户——有时是正收益））
2. 应用商店审核卡了 5 天（硬强制已开），用户卡在升级页——这事故怎么复盘？（提示：根因 = 「先开强制后等审核」的顺序错误；防复发 = 硬强制开关与「商店版本上线」事件绑定（自动开启而非手动）+ 灰度逐步收紧而非一键全量）
