---
title: [944] 笔试手写：实现对话上下文按 token 预算的裁剪策略
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 笔试题, 多Agent, 上下文管理]
type: 笔试题
---

## 944：笔试手写：实现对话上下文按 token 预算的裁剪策略

**答**：实现 trimContext(messages, budget, est)：消息分 system / history / 最近 turns 必保（最后 4 条）；裁剪顺序：先丢最老的 history，再压缩大工具结果（替换为 '[tool output omitted]' 占位），永不裁 system。返回裁剪后的 messages 并保证总 est 不超 budget；无法满足时抛错。

```js
function trimContext(messages, budget, est) {
  const last4 = messages.slice(-4);
  const rest = messages.slice(0, -4).filter(m => m.role !== 'system');
  const system = messages.filter(m => m.role === 'system');
  const total = arr => arr.reduce((s, m) => s + est(m), 0);

  // 第一刀：丢弃最老的 history 直到放得下（含必保部分）
  let keep = [...rest];
  while (total([...system, ...keep, ...last4]) > budget && keep.length) {
    keep = keep.slice(1);                                  // 从最老开始丢
  }
  // 第二刀：还不够就压缩大工具结果
  if (total([...system, ...keep, ...last4]) > budget) {
    keep = keep.map(m => m.role === 'tool' && est(m) > 200
      ? { ...m, content: '[tool output omitted]' } : m);
  }
  const out = [...system, ...keep, ...last4];
  if (total(out) > budget) throw new Error('context overflow: even system+last4 too big');
  return out;
}
```

**评分点**：
- 分层正确：system 永不裁、最后 4 条必保，中间才可动
- 两刀顺序：先丢老消息再压缩工具结果（保信息优先于保量）
- 抛错条件清晰：system + 必保也超预算属于配置错误必须显式失败
- 能说出 est 为什么是注入的（不同模型 tokenizer 不同，测试可替换）

