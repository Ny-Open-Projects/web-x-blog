---
title: [A159] API 废弃通知的宽限期管理
date: 2026-11-20
categories: [Python算法笔试]
tags: [Python面试, 笔试题, 27]
type: 笔试题
---

### A159 · API 废弃宽限期

> 难度:★★☆ | 标签:API 治理, 废弃, 版本

**问**（笔试·场景题）：要废弃一个旧 API（`GET /v1/user-info`），调用方 30 个——废弃流程五步（标记/通知/迁移期/只读/下线）各自做什么，「没人响应通知」怎么办（默认弃权与强制切换），宽限期多长合理（按调用方类型分级），下线当天「漏网调用方」怎么兜底（不是直接 500）？

**答**：① 五步流程（Q6012 Sunset 退役的细化）：**标记**（响应头 `Deprecation`+`Sunset`+`Link: rel="deprecation"` 新端点）→ **通知**（邮件+控制台横幅+webhook 三渠道，30/15/7/1 天四次节奏）→ **迁移期**（新旧并行，迁移指南+联调支持）→ **只读期**（返回缓存快照+明确警告头，不再维护）→ **下线**（410 Gone + 指向新 API 的 body）。② 默认弃权：通知渠道全覆盖后仍无响应的调用方，宽限期结束时**强制切新 API**（网关重写路由到 v2——多数调用方无感，不兼容的会失败但已尽力通知）——「沉默不是同意继续用旧版」。③ 宽限期分级：内部团队 30 天 / 关键合作伙伴 90 天（合同约定）/ 公开 API 180 天——按「迁移成本与商务关系」定，不是拍一个数。④ 漏网兜底：410 响应体带新端点指引 + 网关层「软下线」观察（410 返回后一周内调用方若暴增申诉，可临时重开白名单）——下线的目标是「可追溯的关闭」不是「一刀切断」。

```python
# 全部标准库；demo 实现「废弃五步状态机 + 默认弃权 + 软下线兜底」
import time

DEPRECATION_HEADERS = {
    "Deprecation": "true",
    "Sunset": "Wed, 31 Dec 2026 23:59:59 GMT",
    "Link": '</v2/user-info>; rel="deprecation"; type="text/html"',
}

class DeprecationFlow:
    def __init__(self, deadline_ts: float, grace_by_type: dict[str, int]):
        self.deadline, self.grace = deadline_ts, grace_by_type
        self.acknowledged: set[str] = set()
        self.notified_at: list[float] = []
    def notify_round(self) -> list[float]:
        self.notified_at.append(time.time())
        return self.notified_at                       # 30/15/7/1 天节奏（演示记时刻）
    def deadline_for(self, caller_type: str) -> float:
        return self.deadline + self.grace.get(caller_type, 0)
    def on_deadline(self, caller: dict) -> str:
        if caller["id"] in self.acknowledged and not caller["migrated"]:
            return f"强制切换：网关重写 {caller['id']} → v2（已确认知悉未迁移）"
        if caller["id"] not in self.acknowledged:
            return f"默认弃权：{caller['id']} 未响应通知 → 网关重写尝试 v2"
        return "migrated"
    def soft_offline(self, path: str) -> tuple[int, str]:
        return 410, json_body(path)

def json_body(path: str) -> str:
    return f'{{"error": "gone", "message": "API 已下线", "successor": "/v2/{path}"}}'

if __name__ == "__main__":
    flow = DeprecationFlow(deadline_ts=time.time() + 90 * 86400,
                           grace_by_type={"partner": 90 * 86400})
    for _ in range(4):
        flow.notify_round()
    callers = [{"id": "team-a", "type": "internal", "migrated": True},
               {"id": "team-b", "type": "internal", "migrated": False},
               {"id": "partner-x", "type": "partner", "migrated": False}]
    for c in callers:
        print(f"{c['id']}:", flow.on_deadline(c))
    code, body = DeprecationFlow.soft_offline("user-info")
    assert code == 410 and "/v2/user-info" in body
    print("软下线 410:", body)
    # 口径：五步（标记/通知/迁移/只读/下线）+ Sunset 头；沉默=默认弃权强制切；
    # 宽限期按调用方分级；410 带新端点指引+申诉白名单兜底。
```

**追问**：1) 为什么「网关重写强制切 v2」而不是直接 410？——多数旧调用只是路径不同（v1/v2 语义相同），重写后无感继续（不破坏业务）；真正不兼容的才 410——下线的执行原则是「尽力保持可用，只关闭该关的」。2) Sunset 头给了日期但客户端 SDK 不读自定义头怎么办？（提示：Deprecation/Sunset 是标准头（RFC 8594），主流 SDK/网关支持采集；再加主动通知（邮件/webhook）双保险——被动头+主动通知缺一不可）3) 「只读期返回缓存快照」对写型 API 怎么办？（提示：写型 API 只读期直接 405（方法不允许）+ 指引新端点——读可快照、写不可快照，两类分开处理）

## 背诵要点
1. 废弃五步：标记（Deprecation+Sunset 头）→ 通知（30/15/7/1 天节奏）→ 迁移期并行 → 只读期 → 410 下线带新端点指引。
2. 默认弃权：通知全覆盖后无响应 = 网关强制重写切新 API；宽限期按调用方分级（内部 30 天/伙伴 90 天/公开 180 天）。
3. 下线兜底：软下线（410+申诉白名单临时重开）——「可追溯的关闭」而非一刀切。

## 复盘追问
1. 下线后一周，一个没在调用方清单里的「隐藏调用方」410 报错炸了——防线上缺了什么？（提示：调用方清单靠流量基线（Q123 trace）而非登记——下线前 1 周的「实际流量来源」扫描能抓到未登记调用方（比如脚本直连）；清单永远要和流量对账）
2. 合作伙伴以合同没写 API 变更条款为由拒绝迁移，怎么破？（提示：合同补「API 生命周期条款」（通知即生效）——当下方案：白名单宽限+商务跟进；长期：所有新合同带生命周期条款，这是平台化必修课）
