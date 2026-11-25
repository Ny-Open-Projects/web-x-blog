---
title: [1186] 给 Agent 建「行为基线」，异常行为怎么检测
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 安全]
type: 面试题
---

## 1186：给 Agent 建「行为基线」，异常行为怎么检测

**答**：
- 基线维度：工具调用序列分布（常用工具与顺序）、参数分布（路径/域名/参数长度）、输出特征（长度/格式/敏感词命中）、成本速率——每 Agent 按历史分布建模（简单分位数即可，不必上重模型）。
- 异常检测分级：硬规则（禁用工具被调用 = 直接熔断告警）、统计偏差（行为分布偏离基线 3 倍标准差 = 降级观察）、组合异常（单条正常但序列模式异常）。
- 基线更新：基线随 prompt/工具变更而重建（旧基线对新版本全是误报），重建窗口内用「影子对比」代替统计告警。
- 追问钩子：为什么用分位数而不是训练异常检测模型？——Agent 行为维度有限且可解释要求高，分位数规则透明可调试；模型方案在维度增长后再引入。

```ts
function baseline(agent, history) {
  return {
    tools: dist(history.map(h => h.toolSeq)),
    params: quantiles(history.map(h => h.paramsLen)),
    costRate: quantiles(history.map(h => h.tokensPerMin)),
  };
}
function detect(b, cur) {
  if (FORBIDDEN.has(cur.tool)) return { level: 'hard', act: 'breaker' };
  if (zScore(cur.paramsLen, b.params) > 3) return { level: 'soft', act: 'observe' };
  if (zScore(cur.tokensPerMin, b.costRate) > 3) return { level: 'soft', act: 'observe' };
  return { level: 'ok' };
}
```

## 追问（补充）

**追问**：

1. 冷启动没有历史数据怎么建基线？→ 先用同类 Agent 的基线做先验，前两周只观察不告警，样本够了再切自建基线，先验基线要标注来源与适用版本，避免误用。
2. 误报太多怎么调？→ 把统计类告警先降为观察级只进看板，硬规则分层，按周校准分位数阈值。
3. 攻击者缓慢偏移绕过基线怎么防？→ 加长周期趋势检测与跨 Agent 横向对比，单点偏离不告警但持续漂移累积升级，阈值调整必须留变更记录。
