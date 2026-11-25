---
title: [TST-084] matchMedia 与响应式行为在测试里怎么模拟？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-084：matchMedia 与响应式行为在测试里怎么模拟？
**答**：
- 根因：jsdom 没有 window.matchMedia（antd/MUI 等组件库挂载直接报错），且测试需要「切换断点」驱动响应式分支。
- mock 设计：`createMatchMedia(matches)` 工厂——返回函数，按 query 命中规则给 matches；带 listeners 数组支持 addEventListener，测试手动派发 change 事件模拟断点切换。
- 断言面：初始断点下渲染 PC/移动布局；派发 change 后组件跟随（useSyncExternalStore 消费场景）。
- 放置：setup 全局兜底默认 false，个别用例覆盖为 true 或可切换版。

```typescript
// 工厂：可控 matchMedia
function createMatchMedia(matchesMap: Record<string, boolean>) {
  return (query: string) => {
    const listeners = new Set<() => void>();
    return {
      matches: matchesMap[query] ?? false,
      media: query,
      onchange: null,
      addEventListener: (_: string, cb: () => void) => listeners.add(cb),
      removeEventListener: (_: string, cb: () => void) => listeners.delete(cb),
      addListener: (cb: () => void) => listeners.add(cb),
      removeListener: (cb: () => void) => listeners.delete(cb),
      dispatchChange: (matches: boolean) => {          // 测试手动切断点
        (this as any).matches = matches;
        listeners.forEach((cb) => cb());
      },
      dispose: () => {},
    };
  };
}

// 用法
test('移动端隐藏侧栏', () => {
  const mql = createMatchMedia({ '(max-width: 768px)': true });
  vi.stubGlobal('matchMedia', mql);
  render(<Layout />);
  expect(screen.queryByTestId('sidebar')).toBeNull();
});
```
