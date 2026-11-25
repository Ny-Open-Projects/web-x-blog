---
title: [TST-146] 笔试：为前端监控上报 SDK 写测试（sendBeacon mock + 采样与去重）
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-146：笔试：为前端监控上报 SDK 写测试（sendBeacon mock + 采样与去重）
**答**：
- 场景：错误上报 SDK——`report.error(err, context)` 上报到 `/api/collect`；策略：错误去重（同一指纹 1 分钟内只报一次）、采样率（10% 用户全量）、`navigator.sendBeacon` 失败降级 fetch keepalive。
- 测试难点：sendBeacon 在 jsdom 不存在且「fire-and-forget」无法 await——spy 它并让返回值可控（true/false）来验证降级链路；采样用注入可控随机源（`random: () => 0.01`）替代 Math.random。
- 可控随机是本题灵魂：依赖真实 Math.random 的测试无法稳定覆盖「采样命中/不命中」两条路径。

```jsx
import { vi } from 'vitest';
import { Reporter } from './reporter';

function setup({ beaconResult = true, random = () => 0 } = {}) {
  const beacon = vi.fn().mockReturnValue(beaconResult);
  const fetchSpy = vi.fn().mockResolvedValue(new Response('{}'));
  vi.stubGlobal('navigator', {
    ...navigator,
    sendBeacon: beacon,
  });
  vi.spyOn(Math, 'random').mockImplementation(random);
  const reporter = new Reporter({ sampleRate: 1, endpoint: '/api/collect' });
  return { beacon, fetchSpy, reporter };
}
afterEach(() => vi.unstubAllGlobals());

test('sendBeacon 成功时优先使用，不调 fetch', () => {
  const { beacon, fetchSpy, reporter } = setup();
  reporter.error(new TypeError('x is not a function'), { page: '/a' });
  expect(beacon).toHaveBeenCalledTimes(1);
  const [url, blob] = beacon.mock.calls[0];
  expect(url).toBe('/api/collect');
  expect(JSON.parse(blob)).toMatchObject({ type: 'error', page: '/a' });
  expect(fetchSpy).not.toHaveBeenCalled();
});

test('sendBeacon 返回 false 降级 fetch keepalive', async () => {
  const { beacon, fetchSpy, reporter } = setup({ beaconResult: false });
  reporter.error(new Error('boom'), {});
  expect(fetchSpy).toHaveBeenCalledWith('/api/collect',
    expect.objectContaining({ keepalive: true, method: 'POST' }));
});

test('同一错误指纹 1 分钟内去重', () => {
  const { beacon, reporter } = setup();
  const err = new Error('same');
  reporter.error(err, {});
  reporter.error(err, {});
  reporter.error(err, {});
  expect(beacon).toHaveBeenCalledTimes(1);           // 指纹去重

  vi.advanceTimersByTime?.(60_000);                  // 或注入 fake clock
  reporter.error(err, {});
  expect(beacon).toHaveBeenCalledTimes(2);           // 过期后再报
});

test('采样率不命中时不上报', () => {
  const { beacon, reporter } = setup({ random: () => 0.5 });  // 恒不命中
  const r = new Reporter({ sampleRate: 0.1, endpoint: '/x' });
  r.track('click', {});
  expect(beacon).not.toHaveBeenCalled();
});
```

**评分点**：
1. sendBeacon spy 化且返回值可控，验证优先级与降级链路。
2. 采样用注入随机源替代 Math.random（可控性思维）。
3. 去重基于错误指纹而非引用相等（两次 throw 同文案不同实例）。
4. keepalive 降级参数断言（页面卸载时上报不丢）。
