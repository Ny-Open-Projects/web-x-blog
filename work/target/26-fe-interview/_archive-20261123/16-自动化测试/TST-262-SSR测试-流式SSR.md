---
title: [TST-262] 流式 SSR（Suspense streaming）的测试设计？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-262：流式 SSR（Suspense streaming）的测试设计？
**答**：
- 分段到达测试：mock 数据源延迟，断言壳先到、内容块后到（HTML 分段接收）。
- fallback 与替换：流式块到达前显示 fallback，到达后正确替换。
- 错误流：某块服务端抛错时的降级内容（error boundary 段）正确输出且不影响其他块。
- 客户端水合时机：流未结束时的用户交互（渐进水合）行为断言。

```javascript
test('流式分段到达', async () => {
  const res = await fetch('/slow-page');             // mock：shell 立即，goods 延迟 500ms
  const reader = res.body!.getReader();
  const first = await readChunk(reader, 100);        // 前 100ms
  expect(first).toContain('skeleton');
  const later = await readChunk(reader, 1500);
  expect(later).toContain('goods-card');             // 内容块后到
});
r
```
