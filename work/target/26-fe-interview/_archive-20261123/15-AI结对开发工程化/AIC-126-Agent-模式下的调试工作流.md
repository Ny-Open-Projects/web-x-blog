---
title: [AIC-126] Agent 模式下调试工作流怎么变化？「把调试变成可复现任务」指什么？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-126：Agent 模式下调试工作流怎么变化？「把调试变成可复现任务」指什么？
**答**:
- 传统调试是人与断点的交互；agent 模式下调试信息必须「文本化供给」——报错栈、console 输出、网络面板摘录、复现步骤，agent 只能消费文本证据。
- 可复现任务的意思：给 agent 的不是「这个 bug 修一下」，而是「最小复现路径 + 确定性输入 + 失败断言」——能被反复执行到红的复现脚本，是 agent 修复循环（AIC-083）的燃料。
- 调试供给清单：错误完整栈（首错优先）、相关请求的 request/response 摘录、数据快照（store 状态）、期望 vs 实际的对照描述。
- 人的新职责：把「含混的现场」整理成「可复现的证据包」——这是 agent 时代调试中人力投入最大也最值钱的环节。
- 追问钩子：无法文本化的调试问题（视觉 bug）要走截图供给（多模态），但验证仍然依赖人对像素的确认——「最后一公里永远是人」。

```javascript
// bug 证据包模板（agent 可消费的调试任务）
const evidencePack = `
## 复现：npm run dev → /goods/list → 点击第3页 → 列表闪烁
## 证据：
- Console: "TypeError: Cannot read properties of undefined (reading 'map') at GoodsList.tsx:42"
- 状态快照：page=3, loading=false, list=undefined
## 期望：page=3 时正常渲染；失败断言：vitest run goods-pagination --grep "page3"（当前红）
## 约束：修复后该测试必须绿，且不得改动 API 层`;
```
