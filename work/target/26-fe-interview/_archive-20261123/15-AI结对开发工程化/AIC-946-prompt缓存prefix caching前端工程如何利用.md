---
title: [AIC-946] 听说模型支持 prefix caching（提示词缓存），前端工程里怎么利用它来降本提速？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-946：听说模型支持 prefix caching（提示词缓存），前端工程里怎么利用它来降本提速？
**答**：
- 原理：对「相同前缀」的多次请求，模型复用前缀的 KV 缓存，只计算增量部分——结论：把稳定的、重复的内容放在 prompt 最前面，变动内容放后面。
- 前端可缓存的稳定前缀包括：系统提示、团队 rules、项目结构说明、公共工具函数签名——这些几乎每次都相同，非常适合做前缀。
- 注意「前缀必须逐字相同」：哪怕一个标点变化都会导致缓存失效；因此要避免把时间戳、随机 ID、会话 ID 放进前缀区，把它们放增量区。
- 追问钩子：能说出「缓存命中率要靠日志观测；不同模型缓存策略不同、有些按 token 边界缓存」的候选人，知道落地要看实际收益。

```typescript
// 构造对 prefix caching 友好的 prompt：稳定前缀 + 变动后缀
function buildPrompt({ rules, projectMap, task, sessionId }) {
  const stablePrefix = [
    '你是资深前端工程师，遵守以下规则：',
    ...rules,                    // 团队 rules，稳定
    '项目结构：' + projectMap,    // 稳定
  ].join('\n');
  const dynamicSuffix = `\n\n会话:${sessionId}\n任务:${task}`; // 变动放后面
  return { prefix:stablePrefix, suffix:dynamicSuffix };
}
// 稳定前缀多次请求可命中缓存；sessionId/task 变化不影响前缀命中
console.log(buildPrompt({ rules:['用TS'], projectMap:'src/*', task:'改价格', sessionId:'s1' }).prefix.length);
```
