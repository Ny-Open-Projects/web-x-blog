---
title: [Q274] Agent 应用上生产的检查清单
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q274 · Agent 应用上生产的检查清单

> 难度:★★★★ | 标签:Agent, 部署

**问**:一个 Agent 应用从 demo 到生产,必须补齐哪些工程能力?

**答**:分六块:1) 可靠性——超时/重试/熔断、幂等、降级路径(模型挂了给规则兜底);2) 安全——Prompt 注入防护、工具权限最小化、PII 脱敏、审计日志;3) 可观测——全链路 trace、成本与延迟看板、坏例回流机制;4) 评估——上线前离线评估集回归,上线后 A/B 与抽样人工评估,建立"评估→修复→回归"闭环;5) 成本——缓存、模型分级、预算告警;6) 发布——灰度按流量比例放量、prompt 与工具版本化管理(可回滚)、影子模式(新策略只记录不生效)先跑一段时间再切流。

```python
# file: code/06_Agent与LLM及系统设计/q274_prod_checklist.py
"""生产就绪检查器:逐项检查配置,输出上线前报告。"""

CHECKLIST = {
    "可靠性": ["timeout_configured", "retry_policy", "fallback_path", "idempotent_tools"],
    "安全": ["injection_guard", "tool_whitelist", "pii_redaction", "audit_log"],
    "可观测": ["trace_enabled", "cost_dashboard", "badcase_collection"],
    "评估": ["offline_eval_set", "canary_release", "prompt_versioned"],
}


class ProdReadiness:
    def __init__(self, config: dict):
        self.config = config

    def check(self) -> tuple[bool, list[str]]:
        missing = []
        for category, items in CHECKLIST.items():
            for item in items:
                if not self.config.get(item):
                    missing.append(f"{category}/{item}")
        return not missing, missing

    def report(self) -> str:
        ok, missing = self.check()
        lines = ["== 生产就绪报告 ==", f"结论: {'可上线' if ok else '不可上线'}"]
        lines += [f"  缺失项: {m}" for m in missing] or ["  全部通过"]
        return "\n".join(lines)


if __name__ == "__main__":
    partial = {"timeout_configured": True, "retry_policy": True,
               "injection_guard": True, "trace_enabled": True}
    print(ProdReadiness(partial).report())
    print()
    full = {k: True for items in CHECKLIST.values() for k in items}
    print(ProdReadiness(full).report().splitlines()[1])
```

**追问**:
- 影子模式是什么?——新策略/prompt 只记录输出不返回用户,用线上真实流量对比效果;比离线评估更接近真实分布。
- prompt 怎么版本化?——prompt 当代码:进仓库、走 review、带版本号引用;线上可按版本灰度与回滚。
- 降级路径长什么样?——模型不可用时切规则回答/静态 FAQ/排队;「LLM 挂了全站 500」不是合格的架构。
