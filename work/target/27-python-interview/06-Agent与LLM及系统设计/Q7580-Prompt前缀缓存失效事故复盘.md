---
title: "[Q7580] Prompt 前缀缓存失效成本暴涨事故复盘"
date: 2026-11-20
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7580 · Prompt 前缀缓存失效成本暴涨事故复盘

难度：P6 ｜ 标签：事故复盘 / prompt cache / 成本 / 前缀稳定性

**问**：某次发版后 LLM 账单暴涨 3 倍，排查发现 prompt cache 命中率从 65% 掉到 0。复盘：什么改动会"静默"杀死前缀缓存？怎么从架构上保证前缀稳定性？

**答**：

**结论**：前缀缓存按"从开头逐 token 精确匹配"工作，任何前缀头部字节变化都使整条缓存作废。这次事故的元凶是版本管理把"构建日期+git commit hash"注入 system prompt 开头——每次发版（甚至每次构建）所有请求的前缀全变，命中率清零。同类杀手清单：动态时间戳在头部、每请求随机 UUID、按用户个性化内容排在前部、SDK 升级改变了消息序列化细节（空格/字段顺序）。修复原则一句话：**prompt 按"从不变到易变"排序**——system（钉死）→ few-shot/工具 schema（随版本变，但同版本内稳定）→ 会话历史 → 用户当轮输入 → 易变元数据（时间戳等放最尾）。

**取舍**：前缀稳定性与其他诉求的冲突：① 内容版本化 vs 缓存——prompt 改版后缓存本来就该失效，问题不在"变"而在"无意义地变"（构建 hash 对模型无信息量，纯损失）；要变的内容（真正的新指令）留在头部付一次失效成本，纯噪声移到尾部。② 个性化 vs 缓存——用户名等个性化内容如果必须在前部，可拆成"公共前缀 + 用户消息"，牺牲部分命中；或评估把个性化挪到尾部是否改变行为（大部分不会）。③ 多租户缓存隔离与命中率——租户前缀分开缓存保隔离，公共 system 部分设计成共享前缀提高命中。

**实战**：防复发三层：① 上线前缓存命中率回归：CI 里对代表性会话跑两次相同前缀请求，断言第二次命中（API 返回 cached_tokens / usage 字段核对）；② prompt 组装器固化排序规则（lint 检查易变字段位置）；③ 监控命中率按 prompt 模板版本分维度——命中率按版本掉零即告警，事故当天就能发现而不是月底看账单。

```python
# Prompt 组装器：前缀稳定性排序 + 缓存命中回归校验（仅标准库，Python 3.9+）
from __future__ import annotations

import hashlib


def assemble_prompt(system: str, few_shot: str, history: str,
                    user_msg: str, metadata: dict) -> str:
    """铁律：从不变到易变。metadata（时间戳等）必须在最尾。"""
    tail = "\n".join(f"{k}: {v}" for k, v in sorted(metadata.items()))
    return "\n".join([system, few_shot, history, user_msg, tail])


def stable_prefix_hash(prompt: str, marker: str = "Q?") -> str:
    """对用户消息之前的稳定前缀取 hash（缓存按前缀匹配）。"""
    return hashlib.sha1(prompt[:prompt.index(marker)].encode()).hexdigest()


def cache_regression(assemble: callable, meta_a: dict, meta_b: dict) -> bool:
    """回归：两次请求仅尾部元数据不同 → 稳定前缀 hash 必须相同（可命中）。"""
    p1 = assemble(meta_a)
    p2 = assemble(meta_b)
    return stable_prefix_hash(p1) == stable_prefix_hash(p2)


def main() -> None:
    system = "You are a helpful assistant."
    few_shot = "Example: ..."
    history = "user: hi\nassistant: hello"
    meta1 = {"build": "a1b2c3", "ts": "2026-11-20T10:00:00"}
    meta2 = {"build": "d4e5f6", "ts": "2026-11-20T10:01:00"}

    # 修复版：易变元数据在尾部 → 前缀稳定
    assert cache_regression(
        lambda m: assemble_prompt(system, few_shot, history, "Q?", m),
        meta1, meta2)
    print("修复版：build/ts 在尾部 → 前缀 hash 稳定，缓存可命中")

    # 事故版：build hash 注入头部 → 每次构建缓存全失效
    def buggy_assemble(m: dict) -> str:
        return f"build={m['build']}\n{system}\n{few_shot}\n{history}\nQ?"
    assert not cache_regression(buggy_assemble, meta1, meta2)
    print("事故版：build 在头部 → 前缀 hash 变化，命中率归零")

    # 账：65% 命中 → 0，单 token 成本差
    input_tokens, price = 1_000_000, 0.15  # $/1M
    hit_price = price * 0.10  # cached token 通常是原价的 1/10
    cost_good = input_tokens * (0.65 * hit_price + 0.35 * price) / 1e6
    cost_bad = input_tokens * price / 1e6
    print(f"月成本: 命中 65% ${cost_good:.0f} vs 命中 0 ${cost_bad:.0f} "
          f"(+{cost_bad / cost_good - 1:.0%})")
    assert cost_bad > cost_good * 2
    print("结论：排序铁律 + CI 缓存回归 + 按模板版本监控命中率")


if __name__ == "__main__":
    main()
```

**追问链**：

- 追问 1：为什么构建 hash 这类"对模型无信息量"的内容危害特别大？——它每次构建必变且必在前缀头部（人们习惯把版本信息放开头），对生成质量零贡献，却每次发版杀掉全量缓存；是纯成本泄漏。要版本化的真正指令变化，应随指令内容本身进 prompt 并接受合理失效。
- 追问 1.1：怎么从 API 响应确认缓存真的命中了？——usage 里 cached_tokens（OpenAI）/ cache_read_input_tokens（Anthropic）字段；按请求记录并聚合命中率，而不是凭"感觉变快"。注意供应商缓存 TTL（几分钟到小时级）与最小前缀长度门槛（如 1024 token 以下不缓存）。
- 追问 2：如果业务必须把"用户个性化上下文"放前面（比如用户画像），缓存与个性化怎么兼得？——分层：画像压缩成短 token 且放尾部；或接受"每用户一个前缀簇"的命中率模型（命中只在同用户连续请求间发生，命中率上限下降但仍有收益）；极端场景评估放弃 prompt cache 换语义缓存（结果级），账要重算。

**背诵要点**：

1. 前缀缓存逐 token 精确匹配，头部任何字节变化（构建 hash/时间戳/UUID/SDK 序列化差异）即全量失效。
2. 排序铁律：system（钉死）→ few-shot/工具 schema → 会话历史 → 用户输入 → 易变元数据放最尾。
3. 防复发：CI 缓存命中回归（两次同前缀断言命中）、usage 的 cached_tokens 落监控、命中率按 prompt 模板版本分维度告警；65%→0 命中率意味着成本 +150% 以上。

**复盘追问**：

1. 事故靠月底账单才发现，你设计的"当天发现"监控指标是什么？阈值多少？
2. 如果元数据必须进前部（合规要求），你如何重算命中率模型并向团队说明成本预期？
