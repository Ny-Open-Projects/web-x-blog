---
title: [A203] 内部 API 平台：服务目录与自助接入
date: 2026-11-20
categories: [Python算法笔试]
tags: [Python面试, 笔试题, 27]
type: 笔试题
---

### A203 · 内部 API 平台

> 难度:★★☆ | 标签:API 平台, 服务目录, 自助化

**问**（笔试·场景题）：内部 40 个服务，新人想用「用户查询接口」却不知道谁提供、怎么调——服务目录（API marketplace）要包含什么（服务清单/文档/沙箱/SLA/owner），「自助接入」流程（申请→审批→凭证→沙箱试调）怎么设计才不让平台团队成为瓶颈，「服务目录的新鲜度」（服务下线了目录还挂着）怎么治理？

**答**：① 服务目录五要素：**服务清单**（谁提供/什么功能/状态 live-deprecated）、**文档**（契约 schema+示例，Q7038 数据契约同构）、**沙箱**（自助试调环境——不申请凭证也能体验）、**SLA**（可用性/延迟承诺，Q144）、**owner**（负责人与支持渠道）——缺 owner 的服务 = 不可信服务（Q202 owner 治理同构）。② 自助接入：申请自动化（表单→自动审批（低风险服务）/owner 审批（敏感数据服务）→ 自动发凭证 → 沙箱可试调）——平台团队的参与点在「审批敏感服务」与「疑难支持」，标准接入零人工（自助是平台规模化唯一路径）。③ 目录新鲜度：目录状态与服务存活自动联动（服务下线自动标 deprecated，Q150 联动；服务自动发现（服务注册表）作为目录的事实源——手工维护的目录必然过期（Q202 同构）。

```python
# 全部标准库；demo 实现「服务目录 + 自助接入状态机」
from enum import Enum

class SvcState(Enum):
    LIVE = "live"; DEPRECATED = "deprecated"; RETIRED = "retired"

class ServiceCatalog:
    def __init__(self):
        self.services: dict[str, dict] = {}
        self.requests: list[dict] = []
    def register(self, name: str, owner: str, sla: float, contract: dict):
        self.services[name] = {"owner": owner, "sla": sla, "contract": contract,
                               "state": SvcState.LIVE, "consumers": set()}
    def request_access(self, requester: str, service: str, scope: str) -> str:
        svc = self.services[service]
        assert svc["state"] == SvcState.LIVE, "已下线服务拒绝接入（目录新鲜度）"
        sensitive = "pii" in json.dumps(svc["contract"])
        approved = not sensitive or scope == "read"   # 敏感写服务需 owner 审批
        self.requests.append({"requester": requester, "service": service,
                              "approved": approved, "scope": scope})
        return "auto-approved + 沙箱凭证" if approved else "pending owner 审批"

    def auto_sync(self, registry: set[str]):
        """服务注册表自动同步：下线服务标 deprecated（新鲜度自动联动）。"""
        for name in self.services:
            if name not in registry and self.services[name]["state"] == SvcState.LIVE:
                self.services[name]["state"] = SvcState.DEPRECATED

import json
if __name__ == "__main__":
    cat = ServiceCatalog()
    cat.register("user-query", "user-team", sla=99.9,
                 contract={"fields": ["id", "name"], "pii": False})
    cat.register("credit-score", "risk-team", sla=99.95,
                 contract={"fields": ["score"], "pii": True})
    print(cat.request_access("newdev", "user-query", "read"))
    print(cat.request_access("newdev", "credit-score", "write"))   # 敏感写 → owner 审批
    cat.auto_sync(registry={"credit-score"})                       # user-query 服务已下线
    assert cat.services["user-query"]["state"] == SvcState.DEPRECATED
    try:
        cat.request_access("newdev2", "user-query", "read")
    except AssertionError as e:
        print("目录新鲜度拦截:", e, "✅")
    # 口径：目录五要素（清单/文档/沙箱/SLA/owner）；自助接入（低风险自动/敏感 owner 审批）；
    # 目录与服务注册表自动同步（新鲜度靠自动联动非人工维护）。
```

**追问**：1) 为什么「缺 owner 的服务不可信」？——owner 缺失 = 出问题没人修、变更没人通知、SLA 无人兜底——消费方用它的风险不可控；目录把 owner 作为服务卡片必填字段（缺失自动降级为「不可信」标识）——owner 治理（Q202）是目录可信度的基础。2) 「自助接入」的审批自动化边界？（提示：低风险（读/无 PII）自动批，敏感（PII 写/资金）owner 审批——审批分级不是「全自动 vs 全人工」，是「按风险路由」；自动审批的凭证也要有 TTL 与权限范围（最小权限，Q6145 联动））3) 服务注册表与目录的「事实源」怎么分工？（提示：注册表管「服务是否存活」（运行时事实），目录管「业务信息」（文档/SLA/owner——设计时事实）——目录从注册表同步存活状态，避免两处手工维护漂移（Q130 配置漂移同构））

## 背诵要点
1. 目录五要素：服务清单/契约文档/沙箱/SLA/owner——缺 owner 的服务不可信。
2. 自助接入：低风险自动批（沙箱凭证），敏感（PII 写/资金）owner 审批——按风险路由不是全自动。
3. 目录新鲜度：与服务注册表自动联动（下线自动标 deprecated）——事实源同步非手工维护。

## 复盘追问
1. 服务目录建好后没人用（大家都直接问同事），冷启动怎么破？（提示：目录的高频刚需先做（沙箱试调——新人自己就能调通最有吸引力）+ 搜索入口嵌进聊天工具（问「用户查询接口」时自动返回目录卡片）+ 强制点（新服务上线必须登记目录才发凭证）——冷启动靠「刚需入口+强制登记」双轮）
2. 两个服务功能重复（两个用户查询接口），目录怎么处理重复？（提示：标记「重复能力」+ 推荐主服务（流量/SLA/owner 响应数据支撑）+ 重复服务进迁移清单（Q150 废弃流程）——目录的价值不只是「找到服务」更是「发现重复、推动收敛」）
