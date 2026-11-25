---
title: [AIC-659] AI 代码安全左移：怎么在 prompt 阶段就注入安全约束？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-659：AI 代码安全左移，怎么在 prompt 阶段就注入安全约束？

**答**：
- 结论先行：**安全左移 =「不让 AI 写出不安全代码」优于「写完再扫描」**。在 prompt/rules 里预置前端安全约束（XSS/注入/敏感数据），比事后 SAST 扫描成本低得多——修复成本随阶段指数上升。
- 注入什么（前端高频）：1) **XSS**：禁止 `dangerouslySetInnerHTML` 渲染用户输入，必须走转义/白名单；2) **命令/URL 注入**：禁止拼接用户输入的 URL 或 `eval`；3) **敏感数据**：token/PII 不进 localStorage、不打日志（AIC-596）；4) **权限**：接口调用带 tenant/user 过滤（AIC-431）。
- 怎么注入：1) **rules 固化**：把上述写成 Cursor rules 的「永远遵守」条款，每个请求自动带上；2) **安全 prompt 模板**：涉及用户输入/鉴权/数据流的任务，用专门的安全强化模板；3) **few-shot 反例**：给 AI 看「不安全写法 → 安全写法」的对照示例；4) **生成后扫描兜底**：prompt 约束是概率的，仍需 SAST + 敏感扫描作为最后防线（AIC-488）——左移不等于取消右移。
- 认知：AI 是「安全知识丰富但不会主动应用」——它知道 XSS 但写 demo 时图省事就 `innerHTML` 了；所以约束要显式、自动化，不靠它「自觉」。
- 追问钩子：为什么「rules 自动注入」比「每次 prompt 手打安全要求」更可靠？——因为人写 prompt 时会忘记（尤其赶进度时），而 rules 随每次请求自动附加，不依赖人的记忆——把「靠人记得提」变成「系统自动带」，这是左移能落地的机制保障。

```typescript
const SECURITY_RULES = `
安全约束（必须遵守）：
1. 禁止 dangerouslySetInnerHTML 渲染用户输入，用 DOMPurify 或转义
2. 禁止 eval / new Function / 拼接用户输入的 URL
3. token/PII 不得写入 localStorage 或 console.log
4. 所有数据查询必须带 tenantId 过滤
`;

function buildSecurePrompt(task: string, involvesUserInput: boolean): string {
  // 涉及用户输入的任务强制带安全约束，不依赖人记得写
  return involvesUserInput
    ? `${SECURITY_RULES}

任务：${task}`
    : task;
}

const prompt = buildSecurePrompt('渲染商品评论列表', true);
console.log(prompt.includes('DOMPurify') && prompt.includes('tenantId'));
```
