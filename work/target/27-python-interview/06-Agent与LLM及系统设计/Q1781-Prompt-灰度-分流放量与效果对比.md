---
title: [Q1781] Prompt 灰度:分流放量与效果对比
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1781 · Prompt 灰度:分流放量与效果对比

> 难度:★★★☆ | 标签:LLM 运维, Prompt 灰度, 实验

**问**:改了一版 prompt,怎么安全地验证它更好并逐步放量?

**答**:灰度三件套:稳定分桶、离线评估、放量门禁。分桶按用户标识确定性映射,同一用户永远同桶,保证实验可复现可回放,放量比例就是桶阈值;候选版先过离线评估集,主指标不回退、增量指标有提升才获得放量资格;放量后继续盯线上指标,达标进入下一档比例。所有对比基于同一评估集同一打分口径,否则"提升"可能只是打分口径漂移。灰度的本质是把不确定性切小份逐步承担,任何一档不合格都能退回基线而不伤存量用户。

```python
# file: code/06_Agent与LLM及系统设计/q1781_prompt_canary.py
"""Prompt 灰度:按用户标识稳定分桶到候选提示词,评估集对比达标才放量。"""

PROMPTS = {
    "baseline": "你是客服助手,回答保持简短",
    "candidate": "你是客服助手,回答保持简短并附一个跟进建议",
}

EVAL_SET = [
    {"q": "怎么改地址", "expect_key": "地址"},
    {"q": "怎么退款", "expect_key": "退款"},
]


def bucket(user_id, rollout_pct):
    """稳定分桶:同一用户永远同桶,可复现可回放。"""
    return int(user_id) % 100 < rollout_pct


def fake_generate(prompt, q):
    """生成桩:candidate 版本多附一句跟进建议,命中期望词。"""
    key = next(e["expect_key"] for e in EVAL_SET if e["expect_key"] in q)
    base = "已处理%s诉求" % key
    if "跟进建议" in prompt:
        base += " 需要跟进建议可再次咨询"
    return base


def eval_prompt(name):
    prompt = PROMPTS[name]
    hits = sum(1.0 for e in EVAL_SET
               if e["expect_key"] in fake_generate(prompt, e["q"]))
    aux = sum(1.0 for e in EVAL_SET
              if "跟进建议" in fake_generate(prompt, e["q"]))
    return {"hit_rate": hits / len(EVAL_SET), "aux_rate": aux / len(EVAL_SET)}


if __name__ == "__main__":
    users = [105, 115, 125, 135, 145, 155, 165, 175, 185, 195]
    canary_ids = [u for u in users if bucket(u, 20)]
    assert canary_ids == [105, 115], "放量 20% 精确命中 2 个用户"
    assert all(bucket(u, 20) == bucket(u, 20) for u in users), "分桶稳定可复现"

    base, cand = eval_prompt("baseline"), eval_prompt("candidate")
    assert base["hit_rate"] == 1.0 and cand["hit_rate"] == 1.0, "主指标不回退"
    assert cand["aux_rate"] == 1.0 > base["aux_rate"] == 0.0, "候选版带来增量收益"
    gate = cand["hit_rate"] >= base["hit_rate"] and cand["aux_rate"] > base["aux_rate"]
    assert gate, "达标才继续放量"
    print("Prompt 灰度通过:稳定分桶 20 命中 2 人,评估达标获准放量")
```

**追问**:
- 为什么不用随机分流? 答:随机分流同一用户每轮可能换桶,实验期用户体验来回跳,且无法按用户做前后对比。
- 灰度期间怎么归因指标? 答:按桶打标进日志,指标按桶聚合对比,与成本归因同一套租户标签机制。
