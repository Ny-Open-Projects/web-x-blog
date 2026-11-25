---
title: [AIC-917] 笔试：实现「Agent 写集冲突预检器」（文件/符号级冲突检测，含 glob 与所有权）
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-917：笔试：实现「Agent 写集冲突预检器」（文件/符号级冲突检测，含 glob 与所有权）
**答**：
- 核心需求：实现 `precheckWriteSets(agents)`。`agents: { id, writes:string[], symbols?:string[] }[]`，路径可含 glob（如 `src/**/*.ts`）。返回 `{ ok, fileConflicts, symbolConflicts }`。
- glob 匹配用简单通配：`**` 匹配任意层级，`*` 匹配单层；两个 glob 互为「可匹配到同一路径」时视为文件冲突（保守判断：互相能匹配对方示例路径即冲突）。
- symbolConflicts 检测不同 agent 声明了相同 symbol（如都改 `computePrice`），同样视为冲突。
- 边界：同一 agent 内部重复写不报冲突；空输入返回 ok=true；未声明 writes 的 agent 跳过；glob 匹配大小写敏感。
- 语义：这是「预防性预检」，在 Agent 动手前发现潜在重叠——预检通过不代表运行时无冲突（动态生成路径无法预知）。
- 追问钩子：能指出「glob 的保守匹配会误报，需在准确率与漏报间权衡；动态路径仍是盲区」的候选人理解静态预检的边界。

```typescript
function globToReg(g) {
  return new RegExp('^' + g.replace(/[.+^${}()|[\]\\]/g,'\\$&')
    .replace(/\*\*/g,'__DEEP__').replace(/\*/g,'[^/]*').replace(/__DEEP__/g,'.*') + '$');
}
function matches(a, b) { // a 的示例路径能否被 b 匹配
  const demo = a.replace(/\*\*/g,'x/y').replace(/\*/g,'x');
  return globToReg(b).test(demo);
}
function precheckWriteSets(agents = []) {
  const fileConflicts = [], symbolConflicts = [], symOwner = new Map();
  for (let i = 0; i < agents.length; i++) for (let j = i + 1; j < agents.length; j++) {
    const [a, b] = [agents[i], agents[j]];
    for (const pa of a.writes || []) for (const pb of b.writes || [])
      if (matches(pa, pb) || matches(pb, pa))
        fileConflicts.push({ a:a.id, b:b.id, paths:[pa, pb] });
  }
  for (const ag of agents) for (const s of ag.symbols || []) {
    if (symOwner.has(s)) symbolConflicts.push({ symbol:s, agents:[symOwner.get(s), ag.id] });
    else symOwner.set(s, ag.id);
  }
  return { ok: !fileConflicts.length && !symbolConflicts.length, fileConflicts, symbolConflicts };
}
console.log(precheckWriteSets([{id:'ui',writes:['src/**/*.tsx']},{id:'api',writes:['src/api/*.ts']}]).ok);
```
**评分点**：
- glob 转正则正确处理 **（跨层级）与 *（单层）及特殊字符转义。
- 双向匹配检测两个 glob 是否可能命中同一路径，fileConflicts 成对输出。
- symbolConflicts 用 Map 检测跨 agent 重复符号，同 agent 内不误报。
- 空输入、未声明 writes、边界情况处理正确。
- 能说明保守匹配的误报与动态路径盲区（加分项）。
