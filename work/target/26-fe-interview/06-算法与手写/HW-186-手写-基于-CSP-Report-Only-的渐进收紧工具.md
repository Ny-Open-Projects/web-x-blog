---
title: [HW-186] 手写 CSP 渐进收紧工具——违规聚类 → 白名单建议生成 → 策略 diff 输出
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---
## HW-186：手写 CSP 渐进收紧工具——违规聚类 → 白名单建议生成 → 策略 diff 输出
**答**：从 Report-Only 违规数据到"下一版策略"的自动化：读 CSP 收集端数据（PER-307）→ 按 directive 聚类违规源 → 高频源生成白名单建议（可配置的信任评级：需人工确认）→ 与当前策略 diff 输出新策略文本（JSON→header 格式化）→ 每轮只新增"已确认安全"的白名单（收紧节奏控制）。

```javascript
function suggestPolicy(current, violations, { minCount = 5, trusted = new Set() } = {}) {
  // violations: PER-307 聚合输出 [{ key: [directive, host], count, samples }]
  const additions = {};
  for (const { key, count } of violations) {
    const [directive, host] = key;
    if (count < minCount) continue;                       // 低频违规：多为噪音/爬虫，不进白名单
    if (trusted.has(host)) {
      (additions[directive] ??= []).push(host);           // 信任评级通过：建议加入
    }
  }
  const next = { ...parse(current) };
  for (const [d, hosts] of Object.entries(additions)) {
    next[d] = [...new Set([...(next[d] ?? []), ...hosts])];
  }
  return {
    additions,                                            // 本轮新增（透明化：每次收紧加了什么）
    policy: serialize(next),                              // header 格式文本
    remaining: violations.filter((v) => !trusted.has(v.key[1])),   // 未信任源：待人工评级清单
  };
}
function parse(header) {                                  // 'script-src a b; img-src c' → 对象
  const out = {};
  for (const part of header.split(';')) {
    const [d, ...srcs] = part.trim().split(/\s+/);
    if (d) out[d] = srcs;
  }
  return out;
}
function serialize(policy) {
  return Object.entries(policy).map(([d, srcs]) => `${d} ${srcs.join(' ')}`).join('; ');
}
// 收紧节奏纪律：每轮只加"trusted 已确认"的源（minCount 过滤噪音）；
// remaining 清单是人工评级的输入（评级后进 trusted 集合，下一轮生效）—— 收紧是循环不是一步到位
```

**评分点**：
- 违规聚类 → 信任评级 → 白名单建议的自动化链路。
- minCount 噪音过滤 + trusted 人工确认的两道闸。
- 策略 parse/serialize 往返正确（header 格式）。
- remaining 清单作为人工评级输入的循环收紧节奏——本题核心。
