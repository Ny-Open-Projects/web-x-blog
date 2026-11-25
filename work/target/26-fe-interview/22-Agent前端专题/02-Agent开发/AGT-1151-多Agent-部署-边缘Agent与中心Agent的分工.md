---
title: [1151] 哪些 Agent 能力可以下沉到边缘/端侧
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 部署]
type: 面试题
---

## 1151：哪些 Agent 能力可以下沉到边缘/端侧

**答**：
- 下沉判据：低延迟需求 + 小模型可胜任 + 数据敏感（不出设备）三者满足才下沉；典型端侧能力：意图识别、格式化、敏感数据预处理、简单 RAG（本地文档索引）。
- 中心保留：多步推理、大上下文任务、跨设备状态——端侧小模型「预处理 + 路由」，复杂任务上中心。
- 分工的接口：端侧产出的结构化结果（意图/脱敏后文本）上送，中心返回结果；网络断开时端侧降级运行（只提供本地能力并明确提示）。
- 追问钩子：端侧模型的更新怎么管理？——OTA 版本化 + 行为基线校验（同中心侧的模型锁定纪律），端侧模型漂移比云端更难发现，必须有端侧探针。

```ts
// 端侧预处理 + 中心推理的分工
const local = { intent: localModel.classify, sanitize: localDlp };
async function onDevice(input) {
  const intent = local.intent(input);
  if (intent.local_able) return local.answer(input);      // 端侧可答
  const safe = local.sanitize(input);                      // 出界前脱敏
  const r = await cloud.infer(safe, { hint: intent });     // 中心推理
  if (!r) return localOffline(intent);                     // 断网降级
  return r;
}
```
