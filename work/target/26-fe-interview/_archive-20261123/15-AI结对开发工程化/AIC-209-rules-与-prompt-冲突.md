---
title: [AIC-209] 用户 prompt、rules、系统提示三者冲突时怎么办？举一个实际排障案例的思路。
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-209：用户 prompt、rules、系统提示三者冲突时怎么办？举一个实际排障案例的思路。
**答**：
- 一般优先级：系统提示 > rules > 用户即时指令，但各家实现有差异，实测为准。
- 排障方法：把三方内容分别单独注入做对照实验，定位是哪一层导致的行为。
- 常见坑：rules 里写「永远使用函数组件」，用户临时要求 class 组件做兼容——规则应写成默认值而非绝对禁令。
- 规则措辞建议用「默认/除非」，保留逃生通道。

```javascript
// 对照实验定位冲突层
async function probe(task: string) {
  const variants = [
    { label: 'user-only', sys: null, rules: [] },
    { label: 'sys-only', sys: SYSTEM_PROMPT, rules: [] },
    { label: 'rules-only', sys: null, rules: ['base'] },
    { label: 'all', sys: SYSTEM_PROMPT, rules: ['base'] },
  ];
  for (const v of variants) {
    const out = await runAgent(task, v);
    console.log(v.label, await checkBehavior(out)); // 找出行为翻转的层
  }
}
r
```
