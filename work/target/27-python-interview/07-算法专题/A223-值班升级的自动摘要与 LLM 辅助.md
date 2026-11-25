---
title: [A223] 值班升级的 LLM 辅助：摘要与处置建议
date: 2026-11-20
categories: [Python算法笔试]
tags: [Python面试, 笔试题, 27]
type: 笔试题
---

### A223 · 值班 LLM 辅助

> 难度:★★★ | 标签:LLM, 值班, 可靠性

**问**（笔试·场景题）：值班拿到告警，LLM 自动摘要「历史相似故障与处置」——LLM 辅助值班的价值点（摘要压缩/相似故障检索/处置建议草稿），**幻觉风险**在值班场景的特殊严重性（错误处置建议被值班执行=二次事故），LLM 建议的「信任分级」（建议仅供参考 vs 可直接执行的分界），值班场景的 LLM 数据源（内部 runbook+历史工单 vs 公网知识）怎么选择？

**答**：① 价值三档：**摘要压缩**（历史 10 次相似故障的处置摘要——值班不用翻 10 篇 runbook）、**相似检索**（RAG 检索历史工单，Q176）、**处置建议草稿**（按历史处置生成建议清单——值班复核后执行）；三档的风险递增（摘要≈事实压缩最安全，建议草稿=生成内容有幻觉风险）。② 值班幻觉的特殊严重性：值班在压力下**信任机器建议**（没精力交叉验证）——错误建议被直接执行（如「重启主库」）= 二次事故；防线：建议必须带**依据链接**（哪次历史故障/哪条 runbook——可追溯验证）、高风险动作（重启/删除）**永不自动建议**（只列人工确认项）。③ 数据源：**内部 runbook+历史工单优先**（与本环境强相关、已验证），公网知识（Stack Overflow 等）仅作参考且标注来源（内部环境与公网假设可能完全不同）——值班 LLM 的价值在「组织内部经验的检索与压缩」，不是「通用知识问答」。

```python
# 全部标准库；demo 实现「值班 LLM 辅助的安全护栏」
import time

HIGH_RISK_ACTIONS = {"restart_master", "drop_table", "rm_rf", "scale_down_prod"}

def llm_advice_guard(advice: list[dict]) -> dict:
    """LLM 处置建议的安全护栏：分级 + 依据链接 + 高风险永不自动。"""
    safe, need_confirm, blocked = [], [], []
    for a in advice:
        action = a["action"]
        if action in HIGH_RISK_ACTIONS:
            blocked.append({**a, "why": "高风险动作 LLM 不给建议，仅列入人工确认项"})
        elif a.get("source_link"):            # 有依据链接（runbook/历史工单）
            safe.append(a)
        else:
            need_confirm.append({**a, "why": "无依据链接，需值班复核后执行"})
    return {"safe": safe, "need_confirm": need_confirm, "blocked": blocked}

def summarize_history(incidents: list[dict]) -> str:
    """摘要压缩（最安全档）：历史相似故障处置摘要。"""
    lines = [f"- {i['date']}: {i['cause']} → {i['fix']}（耗时 {i['mttr']}min）"
             for i in incidents]
    return "历史相似故障:\n" + "\n".join(lines)

if __name__ == "__main__":
    advice = [
        {"action": "switch_readonly", "source_link": "runbook/db-readonly"},
        {"action": "increase_pool", "source_link": None},          # 无依据
        {"action": "restart_master", "source_link": "somewhere"},  # 高风险
    ]
    g = llm_advice_guard(advice)
    assert len(g["safe"]) == 1 and g["safe"][0]["action"] == "switch_readonly"
    assert len(g["need_confirm"]) == 1 and len(g["blocked"]) == 1
    print("护栏分级: safe", [a["action"] for a in g["safe"]],
          "| 需复核", [a["action"] for a in g["need_confirm"]],
          "| 拦截", [a["action"] for a in g["blocked"]])
    hist = [{"date": "11-01", "cause": "索引失效", "fix": "重建索引", "mttr": 25},
            {"date": "10-15", "cause": "锁等待", "fix": "kill 长事务", "mttr": 12}]
    print(summarize_history(hist))
    # 口径：三档价值风险递增；建议必须带依据链接；高风险动作永不自动建议；
    # 数据源内部优先（组织经验检索>通用知识问答）。
```

**追问**：1) 为什么值班场景的幻觉比聊天场景严重？——聊天场景幻觉被用户辨识（人有余裕判断），值班场景在高压+信任机器的环境（值班没精力验证 + 信任自动化惯例）——幻觉建议可能被直接执行为破坏性操作——场景的风险等级决定 LLM 的护栏等级。2) 「依据链接」怎么保证有效？（提示：链接指向的内容也要验证存在与相关（链接到不存在的 runbook = 假依据）——RAG 管道的链接是检索命中的真实文档（Q7503 引用溯源同构）——依据链接是「可追溯验证」的设计）3) 值班 LLM 的评估怎么 做？（提示：历史事故回放测试（喂历史告警，LLM 建议与实际有效处置对比，Q7501 judge）+ 上线前固定集回归（错误建议率 =0 才上）——值班 LLM 上线的门槛是「零错误建议」，不是「大部分正确」）

## 背诵要点
1. 价值三档风险递增：摘要压缩（最安全）→ 相似检索 → 处置建议草稿（幻觉风险最高）。
2. 护栏分级：有依据链接=可直接参考、无依据=需值班复核、高风险动作**永不自动建议**。
3. 数据源内部优先：组织经验的检索与压缩是价值核心；值班 LLM 上线门槛 = 历史回放零错误建议。

## 复盘追问
1. 值班 LLM 上线后值班「越来越依赖建议」（自己不看 runbook），能力退化风险？（提示：LLM 建议带依据链接（引导读 runbook 原文）+ 定期「无 LLM 演练」（保持人的处置能力）——LLM 是副驾驶不是自动驾驶（值班能力不能外包给模型））
2. LLM 摘要说「本次故障与 3 个月前相似」，但相似度其实是表面匹配（真因不同），值班被误导——怎么防？（提示：相似度检索的「相关 ≠ 相因」问题——摘要同时呈现「差异提示」（与历史故障的不同点，如「本次涉及新版本」）+ 相似度阈值保守 + 摘要定位为「线索」而非「结论」（值班自行验证相似性））
