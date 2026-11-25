---
title: [AIC-062] 让 AI 系统性补齐错误处理和加载态的 prompt 怎么写？怎么避免它「到处 try-catch」？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-062：让 AI 系统性补齐错误处理和加载态的 prompt 怎么写？怎么避免它「到处 try-catch」？
**答**：
- 先定错误处理约定再让 AI 动手：分层策略（网络层统一拦截错误码、业务层只处理可恢复场景、UI 层渲染错误边界 + 用户反馈），约定本身就是规则文件。
- prompt 要给出「错误处理的决策树」：可重试的（网络超时→自动重试+loading）、用户可行动的（表单校验→行内提示）、致命的（渲染错误→ErrorBoundary 兜底页）。
- 防到处 try-catch：明确「禁止吞错的 catch（只 console.log）」「禁止 catch 后返回 undefined 假装成功」；每个 catch 必须选择：重试/上抛/降级 UI 三选一。
- 加载态同理：约定「骨架屏 vs spinner vs 局部 loading」的使用场景，AI 按场景套用而不是每个按钮都加。
- 追问钩子：这类任务适合用「场景清单驱动」——列出全部数据获取点，逐个检查三态（loading/error/empty）覆盖，比全局撒网有效。

```javascript
// 三态覆盖检查清单（AI 逐点自查）
const threeStateChecklist = (fetchPoints) => fetchPoints.map(p => `
- ${p}：loading？error（区分网络错/业务错）？empty（空态文案与行动引导）？
  catch 行为：重试 | 上抛 | 降级 UI（三选一，禁止吞错）`).join('\n');
```
