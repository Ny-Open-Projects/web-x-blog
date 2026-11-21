---
title: [ARC-083] SDK 的测试策略如何设计（单测/集成/真机）？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-083：SDK 的测试策略如何设计（单测/集成/真机）？
**答**：
- 三层：单测覆盖纯逻辑（队列、采样、协议序列化）；集成测试在 jsdom/Playwright 里验证"采集→上报"全链路（mock 网络，断言 payload 结构）；真机测试验证 bridge/性能/兼容。
- 关键工具：mock 网络层（拦截 fetch/XHR 断言上报内容）、时间控制（fake timers 测批量/重试）、契约测试（上报 schema 与服务端共享 schema 双向校验）。
- 兼容性矩阵是验收标准：目标浏览器列表 + WebView 版本跑冒烟。

```typescript
// 集成测试：断言"异常发生 → 批量上报 payload"全链路
import { setupServer } from 'msw/node';

const server = setupServer(
  rest.post('*/collect', async (req, res, ctx) => {
    reported.push(await req.json());
    return res(ctx.json({ ok: true }));
  }),
);

it('捕获错误并批量上报，payload 符合契约', async () => {
  vi.useFakeTimers();
  const sdk = initMonitor({ dsn: '/collect', sampleRate: 1 });
  window.dispatchEvent(new ErrorEvent('error', { message: 'boom' }));
  vi.advanceTimersByTime(5000);                       // 触发批量 flush
  await vi.runAllTimersAsync();
  const [batch] = reported;
  expect(batch[0]).toMatchSchema(MonitorEventSchema); // 与服务端共享同一份 JSON Schema（契约测试）
  expect(batch[0].stack).toContain('boom');
  vi.useRealTimers();
});
// 真机层：browserstack 跑 iOS/Android WebView 冒烟 —— bridge.invoke/超时/重试
```
