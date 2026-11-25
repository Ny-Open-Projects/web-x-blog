---
title: [AGT-130] KV 缓存友好的 prompt 帐布局是什么？前缀稳定性为什么能省钱提速？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-130：KV 缓存友好的 prompt 帐布局是什么？前缀稳定性为什么能省钱提速？
**答**：
- 原理：推理服务对 prompt 前缀做 KV 缓存——前缀完全相同的请求可以复用已计算的注意力缓存，TTFT 显著下降，很多云厂商按缓存命中降价（可省 50%~90% 的输入费用）。
- 布局铁律：把**变化最少的内容放最前，变化最多的放最后**——静态系统提示 → 工具定义 → 长期记忆摘要 → RAG 片段 → 历史摘要 → 最近消息 → 本轮输入。
- 两大杀手：其一，任何前缀字节变化（时间戳、随机 ID、动态菜单）都会使缓存失效；其二，多轮对话时 history 追加在尾部是安全的，但「每轮重排消息」会把缓存全废。
- 实践：给静态段打 cache 标记（如 Anthropic 的 cache_control），上线前 diff 检查两次请求的前缀是否字节级一致。

```typescript
// KV 缓存友好的消息组装：稳定前缀 + 只在尾部追加
export function buildMessages(opts: {
  systemPrompt: string;           // 静态：版本化，永不内嵌时间戳/随机数
  toolDefs: unknown[];            // 静态：工具定义放前缀内，顺序固定（JSON 序列化前排序）
  longTermSummary: string;        // 半静态：仅在摘要更新时变化
  compactedHistory: string;       // 半静态：滚动摘要
  recentTurns: Msg[];             // 追加式：只增不改
  currentInput: string;           // 每轮变化：放最后
}) {
  // 关键检查：recentTurns 只允许 append，若发生中间修改则视为缓存全失效并告警
  const staticPrefix = [
    { role: 'system', content: opts.systemPrompt },                     // ← cache_control 标记点
    { role: 'system', content: `工具协议说明：\n${JSON.stringify(opts.toolDefs)}` },
    { role: 'system', content: `[长期记忆]\n${opts.longTermSummary}` },
  ];
  const mutableSuffix = [
    { role: 'system', content: `[历史摘要]\n${opts.compactedHistory}` },
    ...opts.recentTurns,
    { role: 'user', content: opts.currentInput },
  ];
  return [...staticPrefix, ...mutableSuffix];
}

// 上线前的缓存命中率守护测试：同一会话连续两轮，静态前缀必须字节级一致
export function assertPrefixStable(a: string, b: string, minPrefixRatio = 0.6) {
  let i = 0;
  while (i < Math.min(a.length, b.length) && a[i] === b[i]) i++;
  const ratio = i / Math.min(a.length, b.length);
  if (ratio < minPrefixRatio) throw new Error(`前缀稳定性不达标：${(ratio * 100).toFixed(1)}%`);
}
```
