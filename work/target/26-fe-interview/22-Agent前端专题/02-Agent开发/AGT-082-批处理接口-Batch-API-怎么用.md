---
title: [AGT-082] 批处理接口（Batch API）怎么用？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-082：批处理接口（Batch API）怎么用？
**答**：
- 离线任务（历史数据打标、评测集跑批、知识库预摘要）对延迟不敏感：Batch API 通常半价，是成本优化的第一刀。
- 流程：请求写成 JSONL（每行一个 request，带 custom_id）→ 上传文件 → 创建 batch → 轮询状态 → 下载结果文件。
- 注意时效与配额：batch 一般 24h 内完成，有文件大小与条数上限；单条失败在结果文件里标 error，要逐条补偿。
- 工程封装：实时接口与批量接口封装成同一函数，按延迟敏感度选通道，业务无感。

```typescript
import { z } from 'zod';

// Batch API 全流程：JSONL 构建 → 提交 → 轮询 → 取结果
async function createBatchJob(tasks: { id: string; messages: ChatMessage[] }[]) {
  const lines = tasks.map((t) => JSON.stringify({
    custom_id: t.id,
    method: 'POST',
    url: '/v1/chat/completions',
    body: { model: 'gpt-4o-mini', messages: t.messages, max_tokens: 512 },
  }));
  const file = await uploadFile(Buffer.from(lines.join('\n')), 'batch_input.jsonl'); // 上传到 /v1/files
  return api<{ id: string }>('POST', '/v1/batches', {
    input_file_id: file.id, endpoint: '/v1/chat/completions', completion_window: '24h',
  });
}

export async function runBatch(tasks: Parameters<typeof createBatchJob>[0]) {
  const batch = await createBatchJob(tasks);
  let status = '';
  while (!['completed', 'failed', 'expired'].includes(status)) {
    await sleep(60_000);                                       // 分钟级轮询足够
    status = (await api<{ status: string }>('GET', `/v1/batches/${batch.id}`)).status;
  }
  const outputText = await downloadFile((await api<{ output_file_id: string }>('GET', `/v1/batches/${batch.id}`)).output_file_id);
  // 结果按 custom_id 关联回业务；error 行单独补偿处理
  return outputText.trim().split('\n').map((l) => {
    const r = JSON.parse(l);
    return {
      id: r.custom_id,
      ok: !!r.response,
      content: r.response?.body?.choices?.[0]?.message?.content ?? r.error?.message ?? '',
    };
  });
}
```
