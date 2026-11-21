---
title: [TST-141] 笔试：为 AbortController 请求取消写测试（卸载取消 + 切换取消）
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-141：笔试：为 AbortController 请求取消写测试（卸载取消 + 切换取消）
**答**：
- 场景：详情页快速切换 tab 时，上一个未完成的请求要被 abort（省流量 + 防过期渲染）；组件卸载时也要 abort。测试核心是断言 `abort` 真被调用且组件对 AbortError 静默（不把取消当错误弹 toast）。
- 手段：mock 掉 fetch（或 MSW 里读 `request.signal`），用 spy 观察 `AbortController.prototype.abort`；MSW 延迟中 abort 会在服务端收到 signal.aborted。
- 两个易错点：① 只断言 UI 不变是不够的，要断言请求层真的取消；② AbortError 应被组件识别为「预期中断」而非错误——用例要断言无错误 toast。

```jsx
import { render, screen, unmount } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { http, HttpResponse, delay } from 'msw';
import { server } from '@/mocks/server';
import Detail from './Detail';

test('切换 tab 时上一个请求被 abort', async () => {
  const abortedSignals = [];
  server.use(
    http.get('/api/detail/:tab', async ({ request, params }) => {
      // 监听取消：signal.aborted 变化时记录
      request.signal.addEventListener('abort', () => abortedSignals.push(params.tab));
      await delay(500);
      return HttpResponse.json({ name: `内容-${params.tab}` });
    }),
  );

  render(<Detail />);
  const user = userEvent.setup();

  await user.click(screen.getByRole('tab', { name: '评价' }));   // 发起请求 A
  await user.click(screen.getByRole('tab', { name: '参数' }));   // 发起请求 B（A 应被取消）

  await screen.findByText('内容-参数');
  expect(abortedSignals).toContain('评价');                       // A 真被 abort
  expect(screen.queryByText(/加载失败/)).toBeNull();              // AbortError 不当错误提示
});

test('组件卸载时取消在途请求', async () => {
  const signals = [];
  server.use(http.get('/api/detail/:tab', async ({ request }) => {
    request.signal.addEventListener('abort', () => signals.push('aborted'));
    await delay(500);
    return HttpResponse.json({ name: 'x' });
  }));

  const { unmount } = render(<Detail />);
  unmount();                                                      // 立即卸载
  await vi.waitFor(() => expect(signals).toContain('aborted'));   // 卸载触发 abort
});
```

**评分点**：
1. 断言「请求层取消」而非只看 UI（signal abort 事件监听）。
2. AbortError 与真实错误区分——取消不弹错误提示。
3. 覆盖卸载取消与切换取消两个时机。
4. 使用 request.signal 而非全局 mock abort（贴近真实语义）。
