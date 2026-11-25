---
title: [A164] API 废弃：迁移窗口与回收节奏
date: 2026-11-20
categories: [Python算法笔试]
tags: [Python面试, 笔试题, 27]
type: 笔试题
---

### A164 · API 废弃回收

> 难度:★★☆ | 标签:API 治理, 废弃, 版本

**问**（笔试·场景题）：废弃一个内部 API（3 个团队在用）——废弃的生命周期（标记 deprecated→宽限期→强断）各阶段的技术动作，宽限期怎么定（固定 90 天 vs 按调用方迁移进度），「强断」前的最后验证（流量真的归零了吗），僵尸调用方（清单外偷偷调用的）怎么发现？

**答**：① 生命周期四阶段：**deprecated 标记**（响应头 `Deprecation+Sunset`（RFC 8594，Q6012）+ 文档标注替代方案）、**迁移窗口**（宽限期内新旧并存，调用方按自己的节奏迁）、**流量验证**（Sunset 日期前确认调用量归零——有残留调用则延期或点对点强推）、**强断**（返回 410 Gone + 替代方案指引——410 语义「永久消失」优于 404）。② 宽限期按迁移进度而非固定天数：默认 90 天，但「3 个调用方都迁完」可提前强断、「有调用方未动」则延期+升级催办（宽限期是策略不是倒计时）。③ 强断前验证：**流量监控三重**（网关计数归零、日志无调用、调用方代码库 grep 无引用）——三重全零才断，防止「监控漏了某个角落的调用」。④ 僵尸调用方发现：强断后突然冒出来的调用 = 清单外调用方——**410 响应里的联系方式**（`Contact: api-owners@`）让它自己找上门；长期口径：所有 API 调用走网关（Q165），网关视角无死角。

```python
# 全部标准库；demo 实现「废弃生命周期管理器」
import time

class Deprecation:
    def __init__(self, api: str, default_grace_days: int = 90):
        self.api, self.default = api, default_grace_days
        self.callers: dict[str, dict] = {}       # caller -> {"migrated": bool}
        self.sunset = None
    def register_caller(self, name: str):
        self.callers[name] = {"migrated": False, "last_seen": time.time()}
    def mark_migrated(self, caller: str):
        self.callers[caller]["migrated"] = True
    def can_force_cut(self) -> tuple[bool, str]:
        """强断验证：全部迁移 + 流量归零双重确认。"""
        pending = [c for c, m in self.callers.items() if not m["migrated"]]
        if pending:
            return False, f"未迁移调用方: {pending} → 延期或点对点强推"
        return True, "全部迁移完成 + 流量三重验证归零 → 410 Gone"
    def grace_deadline(self) -> int:
        """宽限期按迁移进度调整：全迁完可提前，钉子户延期。"""
        pending = sum(1 for m in self.callers.values() if not m["migrated"])
        return self.default if pending else 0     # 全迁完=立即

if __name__ == "__main__":
    dep = Deprecation("GET /v1/user-profile")
    for c in ("mobile-app", "bi-job", "partner-x"):
        dep.register_caller(c)
    ok, why = dep.can_force_cut()
    assert not ok and "bi-job" in why            # 有钉子户不能断
    print("强断校验:", why)
    dep.mark_migrated("mobile-app"); dep.mark_migrated("bi-job")
    ok, why = dep.can_force_cut()
    assert not ok and "partner-x" in why         # 只剩 partner-x
    dep.mark_migrated("partner-x")
    ok, why = dep.can_force_cut()
    assert ok
    print("全部迁移:", why, "| 宽限期调整:", dep.grace_deadline(), "天（全迁完立即）")
    # 强断响应：410 Gone + Contact 头——清单外僵尸调用方自己找上门（Q165 网关视角无死角）。
```

**追问**：1) 为什么强断用 410 而不是 404？——404「不存在」语义模糊（可能是 typo）；410 Gone「永久消失+曾有」让调用方明确知道「这个 API 被刻意废弃了」——配合 `Link` 头指替代方案，调试体验完全不同。2) 调用方「说迁移了但实际没切干净」（灰度切了一半）怎么发现？（提示：流量监控按调用方维度拆分（网关按身份计数）——总量归零但某调用方的旧路径仍有残留——按调用方的流量视图比总量视图细，是强断验证的必要粒度）3) 「对方不迁移我等不起」的死局怎么破？（提示：升级路径：点对点强推（催办+高层对齐）→ 定最终强断日（公布）→ 强断（410 有指引）——「等待迁移」是过程不是结论，无限等待=API 永远删不掉；Q6012 退役五步的完整执行）

## 背诵要点
1. 废弃四阶段：deprecated 标记（RFC 8594 头）→ 迁移窗口 → 流量三重验证归零 → 强断 410 Gone。
2. 宽限期按迁移进度调整（全迁完立即强断、钉子户延期+催办）——是策略不是固定倒计时。
3. 强断前双重确认：调用方全部迁移 + 网关/日志/代码三重流量归零；410+Contact 让僵尸调用方现身。

## 复盘追问
1. 强断后某调用方「突然」打爆了值班电话（清单外调用），复盘责任怎么分？（提示：调用方未在服务目录登记（Q166 目录驱动路由的缺口）+ 废弃流程未做「网关视角全量调用方扫描」——行动项：API 调用必须过网关（登记自动化），废弃前用网关数据校对清单）
2. 内部 API 废弃和外部门 API（第三方开发者）废弃的差别？（提示：外部用户不可控——宽限期更长（6-12 月）+ 响应带迁移指引 + 不能强断（只能「停止维护」软废弃）——对外废弃的本质是「持续多年的兼容承诺」）
