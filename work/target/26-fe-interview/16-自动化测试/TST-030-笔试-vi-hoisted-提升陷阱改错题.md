---
title: [TST-030] 笔试：修复一段因 vi.mock 提升导致的报错代码
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-030：笔试：修复一段因 vi.mock 提升导致的报错代码
**答**：
- 题面：下方代码运行报「Cannot access 'mockData' before initialization」，请修复并说明原因。
- 根因：`vi.mock` 工厂被提升到文件最顶部执行，而 `const mockData` 在其后才初始化——工厂执行时处于 TDZ。
- 正确做法：把依赖放进 `vi.hoisted(() => ...)`（它同样被提升，但保证先于 mock 工厂运行）；或在工厂内部自包含数据；测试中途动态改返回值则用 `mocked.mockReturnValue` 而不是共享外部变量。

```javascript
// ❌ 原始错误代码
// const mockData = [{ id: 1 }];
// vi.mock('./api', () => ({ list: () => mockData }));  // 提升后 TDZ 报错

// ✅ 修复方案一：vi.hoisted
const { mockData } = vi.hoisted(() => [{ id: 1, name: '键盘' }]);
vi.mock('./api', () => ({ list: () => mockData }));
import { list } from './api';

// ✅ 修复方案二：工厂内自包含 + 用例里通过 mock 机制改行为
// vi.mock('./api', () => ({ list: vi.fn() }));
// import { list } from './api';
// import { vi } from 'vitest';
// vi.mocked(list).mockReturnValue([{ id: 2 }]);

import { describe, it, expect } from 'vitest';
describe('list', () => {
  it('使用提升后的 mock 数据', () => {
    expect(list()).toEqual([{ id: 1, name: '键盘' }]);
  });
});
```
**评分点**：
- 准确说出「vi.mock 工厂被提升到 import 之前执行」这一根因（而不是笼统说顺序问题）。
- 给出 vi.hoisted 修复且保证 hoisted 先于工厂。
- 备选方案：工厂自包含或 mockReturnValue 动态注入，说明「测试内改行为别靠共享变量」。
