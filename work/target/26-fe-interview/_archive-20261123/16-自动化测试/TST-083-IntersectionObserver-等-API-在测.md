---
title: [TST-083] IntersectionObserver / ResizeObserver 在测试里怎么 mock？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-083：IntersectionObserver / ResizeObserver 在测试里怎么 mock？
**答**：
- 根因：jsdom 不实现这两类 observer，组件挂载即报 `IntersectionObserver is not defined`；测试目标是控制「回调何时触发、带什么数据」，不是实现 observer 语义。
- mock 模板：构造带 observe/unobserve/disconnect 的类，把回调存在实例上；测试中手动调用 `instances[0].callback(entries)` 模拟交叉/尺寸变化。
- 触发数据：IntersectionObserverEntry 用普通对象（isIntersecting/boundingClientRect）即可，无需真实构造。
- 放置位置：setup 文件全局兜底（所有用例可用）+ 用例内按需覆盖实例行为。

```typescript
// vitest.setup.ts —— 全局 mock IntersectionObserver
class MockIntersectionObserver {
  static instances: MockIntersectionObserver[] = [];
  constructor(public cb: IntersectionObserverCallback) { MockIntersectionObserver.instances.push(this); }
  observe = vi.fn();
  unobserve = vi.fn();
  disconnect = vi.fn();
}
vi.stubGlobal('IntersectionObserver', MockIntersectionObserver);

// ResizeObserver 同理
vi.stubGlobal('ResizeObserver', class { observe = vi.fn(); unobserve = vi.fn(); disconnect = vi.fn(); });

// 测试：手动触发交叉
test('列表滚动到底触发加载更多', () => {
  render(<InfiniteList />);
  const io = MockIntersectionObserver.instances.at(-1)!;
  io.cb([{ isIntersecting: true } as IntersectionObserverEntry], io as any);
  expect(onLoadMore).toHaveBeenCalled();
});
```
