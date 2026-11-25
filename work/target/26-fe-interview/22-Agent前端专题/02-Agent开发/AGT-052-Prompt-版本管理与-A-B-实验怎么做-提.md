---
title: [AGT-052] Prompt 版本管理与 A/B 实验怎么做（提示词即代码）？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-052：Prompt 版本管理与 A/B 实验怎么做（提示词即代码）？
**答**：
- 提示词是核心资产，要像代码一样管理：入库评审、版本号、变更记录，禁止散落在业务代码字符串里。
- 运行时经注册表取提示：name + version 解析模板并渲染变量；每次请求记录实际使用的版本，线上问题可回溯到具体版本。
- A/B 分流：按 userId 稳定哈希把小比例流量导到实验版本，对比线上指标（采纳率/负反馈率），显著优于对照才全量。
- 与回归评测打通：改提示必须跑评测集出报告，形成「改 prompt = 改代码」的工程心智。

```typescript
// 提示词注册表：版本化 + 分流 + 使用记录
interface PromptVersion { version: string; template: string; }
const registry = new Map<string, PromptVersion[]>([
  ['summary', [
    { version: 'v1', template: '请总结以下内容：\n{{content}}' },
    { version: 'v2', template: '请用不超过 3 个要点总结以下内容，每个要点一行：\n{{content}}' },
  ]],
]);

function render(tpl: string, vars: Record<string, string>) {
  return tpl.replace(/\{\{(\w+)\}\}/g, (_, k) => vars[k] ?? '');
}

export function pickPrompt(name: string, userId: string): PromptVersion {
  const versions = registry.get(name)!;
  const stable = versions[0];          // 对照组
  const candidate = versions.at(-1)!;  // 实验组：最新版本
  // 按 userId 稳定哈希，10% 灰度进实验组
  const bucket = [...userId].reduce((h, c) => (h * 31 + c.charCodeAt(0)) >>> 0, 0) % 100;
  return bucket < 10 ? candidate : stable;
}

export async function summarize(content: string, userId: string) {
  const p = pickPrompt('summary', userId);
  const text = await chatOnce([{ role: 'user', content: render(p.template, { content }) }]);
  log.info({ event: 'prompt_used', name: 'summary', version: p.version, userId }); // 指标按版本聚合对比
  return text;
}
```
