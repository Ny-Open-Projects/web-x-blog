---
title: [AIC-948] 如何让 AI「按需取上下文」而不是一开始就把所有资料打包塞给它？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-948：如何让 AI「按需取上下文」而不是一开始就把所有资料打包塞给它？
**答**：
- 思路是给 AI「工具」而非「资料堆」：把代码库检索、文件读取、符号查找封装成 AI 可调用的函数（function calling / tool use），AI 判断需要什么就主动调什么。
- 设计一个小而精的工具集：如 `searchSymbol(name)`、`readFile(path, range)`、`grep(pattern)`——结论：工具接口就是 AI 观察代码的「眼睛」，设计好接口比堆上下文更重要。
- 要防「工具滥用」：限制调用次数/范围、记录每次调用日志（可追溯）、对返回结果做二次裁剪，避免 AI 用一个宽泛 grep 又把海量内容拉回来。
- 追问钩子：能提出「按需取上下文本质是把上下文管理权部分交给 AI，但要通过工具设计和预算约束防止它失控」的候选人理解 Agentic 检索的核心。

```typescript
// 给 AI 的工具集：按需检索，返回结果再裁剪
const tools = {
  searchSymbol(name) { return files.filter(f=>f.content.includes(name)).map(f=>f.path); },
  readFile(path, range) { const f=files.find(x=>x.path===path); return sliceLines(f?.content, range); },
};
function sliceLines(content, range){ return (content||'').split('\n').slice(range?.[0]??0, range?.[1]).join('\n'); }
const files=[{path:'price.ts',content:'function computePrice(){}\n// logic'}];
// AI 决策：先搜符号 → 再按需读文件片段（而非全量塞入）
const paths = tools.searchSymbol('computePrice');
const snippet = paths.length ? tools.readFile(paths[0], [0, 1]) : '';
console.log(paths, snippet);
// 工具调用记日志 → 可追溯
```
