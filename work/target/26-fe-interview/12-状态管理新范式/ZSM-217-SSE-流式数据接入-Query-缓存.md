---
title: [ZSM-217] SSE 或流式接口的增量数据怎么接进 Query 缓存
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-217：SSE 或流式接口的增量数据怎么接进 Query 缓存

**答**：
- 流式响应不适合让 queryFn 一次性 resolve：queryFn 读到 ReadableStream 后边读边 `setQueryData` 追加 chunk，最终 resolve 完整数据
- 缓存 key 按流会话定义，追加更新用 updater 函数保证并发安全；断流要 abort + 清理，避免半截数据被当作完整数据
- 与轮询方案的取舍：SSE 实时性好但连接管理复杂；轮询简单但延迟高，流式场景（AI 生成、行情）必须 SSE
- 注意 React 批渲染：高频 chunk 要做帧级合帧（requestAnimationFrame 节流）再 setQueryData

```javascript
useQuery({
  queryKey: ['ai-answer', qid],
  queryFn: async ({ queryKey }) => {
    const res = await fetch(`/api/answer?qid=${qid}`)
    let acc = ''
    const reader = res.body.getReader()
    const dec = new TextDecoder()
    for (;;) {
      const { done, value } = await reader.read()
      if (done) break
      acc += dec.decode(value, { stream: true })
      // rAF 合帧：高频 chunk 不每帧触发渲染
      schedule(() => queryClient.setQueryData(queryKey, acc))
    }
    return acc
  },
})
```
