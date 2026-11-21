---
title: [TST-064] React 测试里的 act 警告根因是什么？怎么排查？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-064：React 测试里的 act 警告根因是什么？怎么排查？
**答**：
- 根因：React 期望「可能触发更新的操作」都包在 act() 中执行（同步 flush 更新）；当用例外有未 await 的 Promise（被测组件自己发的请求）在断言后才 setState，就触发「update not wrapped in act」警告——本质是「测试在 React 更新尚未落地时继续跑」。
- 常见触发源：① render 后没等异步请求就断言；② 全局定时器（组件里 setTimeout/轮询）在用例结束后触发；③ 事件监听器（window resize 等模拟）未包 act。
- 排查方法：看警告栈定位是哪个 setState；把「事件与断言之间的等待」改为 findBy/waitFor（它们内部包 act）；组件卸载前清理定时器（effect cleanup）。
- 误区：不是「包一层 act 压警告」就完了——先问这个更新是否是测试应等待的行为；用 await act(async () => { ... }) 处理确实需要手动 flush 的场景（如直接触发回调）。
- 追问钩子：RTL 的 render/userEvent/waitFor 都已内置 act，警告几乎总来自「测试外」的异步（全局监听、未清理 effect）。

```jsx
// 典型警告场景与修复
import { render, screen, act } from '@testing-library/react';

// ❌ 警告版本：render 时组件发起请求，用例同步结束
// render(<Profile />);
// expect(screen.getByText('张三')).toBeInTheDocument(); // 更新还在路上

// ✅ 修复：等待异步结果（内部已 act）
// render(<Profile />);
// expect(await screen.findByText('张三')).toBeInTheDocument();

// ✅ 手动 flush：模拟 window 回调触发更新
test('resize 后重新计算布局', () => {
  render(<Layout />);
  act(() => {                       // 同步事件 → act 同步包裹
    window.dispatchEvent(new Event('resize'));
  });
  expect(screen.getByTestId('layout')).toHaveAttribute('data-cols', '1');
});

// ✅ 组件卸载清理定时器（未清理是 act 警告的另一大头）
// useEffect(() => { const t = setInterval(poll, 1000); return () => clearInterval(t); }, []);
```
