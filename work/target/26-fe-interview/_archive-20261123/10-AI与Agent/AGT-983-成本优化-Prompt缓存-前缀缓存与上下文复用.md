---
title: [983] Prompt 缓存的原理和工程用法
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 成本延迟, 缓存]
type: 面试题
---

## 983：Prompt 缓存的原理和工程用法

**答**：
- 原理：模型侧对相同前缀的 KV cache 复用——system prompt、工具定义、长文档前缀放最前面且保持逐字节一致，命中后这部分输入不再重新计算，成本与首 token 延迟双降。
- 工程要点：前缀稳定性（任何字节差异都失效，包括时间戳、随机 ID 混在前缀里）、把易变内容放尾部、多轮对话把历史按原样续在尾部。
- 收益量化：前缀占 prompt 60% 以上的场景（长 system + 工具集），缓存命中可省 50%+ 输入成本。
- 追问钩子：为什么 prefix 顺序重要？——KV cache 是按位置对齐的，中间插一句话后面全部失效，所以「稳定前缀 + 追加尾部」是铁律。

```ts
function buildPrompt(ctx) {
  return [
    SYSTEM_PROMPT,           // 稳定前缀：绝不插入动态内容
    toolDefs,                // 工具定义第二段：同样稳定
    ctx.history,             // 会话历史：多轮按原样追加
    ctx.userInput,           // 易变内容永远放最后
  ].join('\n');
}
// 反例：把 Date.now() 放 system 里 -> 每次请求前缀都不同，缓存全失效
```

