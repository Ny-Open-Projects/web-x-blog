---
title: [SCN-1230] AI 对话的响应流异常恢复（断流续传）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1230：AI 对话的响应流异常恢复（断流续传）

**答**：
- 异常：网络抖动断流（半截回复）——重连续传（服务端支持 offset）或标记中断并提供续写按钮。
- 检测：流超时（5s 无新 token）判定断流。
- 一致：断流内容标记（不完整），重试不重复计费（服务端幂等）。

```javascript
// 断流恢复
async function resilientStream(payload, onDelta) {
  let offset = 0, acc = '';
  for (let i = 0; i < 3; i++) {
    try {
      const stream = await openStream({ ...payload, offset });
      await readStream(stream, d => { acc += d; offset += d.length; onDelta(acc); });
      return { complete: true, text: acc };
    } catch (e) {
      if (i === 2) return { complete: false, text: acc,
        action: '续写按钮' };                          // 断流标记
      await sleep(1000);
    }
  }
}
```
