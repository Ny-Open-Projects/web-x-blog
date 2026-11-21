---
title: [TST-008] vi.mock 与 vi.spyOn 的区别是什么？各自适合什么场景？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-008：vi.mock 与 vi.spyOn 的区别是什么？各自适合什么场景？
**答**：
- 作用层级：vi.mock 拦截「整个模块」，该模块的所有消费方都被替换；vi.spyOn 替换「对象上的一个方法」，不影响模块本身，也不影响其他属性。
- 默认行为：vi.mock 不给工厂时自动 auto-mock（所有导出变 undefined/空函数）；spyOn 默认保留原实现（可 spy 后再 mockImplementation 覆盖），适合「只观察不改变」。
- 生命周期：vi.mock 是文件级提升、模块加载期生效；spyOn 必须在对象存在后调用，且要配 `mockRestore()` 恢复原方法，否则污染同文件其他用例。
- 选型：换掉网络/存储等外部依赖用 vi.mock；验证「内部某个方法确实被调/调参」而不想改行为用 spyOn。
- 追问钩子：`vi.spyOn(console, 'error').mockImplementation(() => {})` 是压掉测试噪音的经典用法。

```javascript
// spyOn：保留原对象，只观察或临时替换方法
import { describe, it, expect, vi, afterEach } from 'vitest';
import * as utils from './utils';   // { formatMoney }

afterEach(() => vi.restoreAllMocks());

describe('pay', () => {
  it('观察内部调用，不改行为', () => {
    const spy = vi.spyOn(utils, 'formatMoney');  // 原实现仍生效
    expect(utils.formatMoney(1)).toBe('¥1.00');  // 行为不变
    expect(spy).toHaveBeenCalledWith(1);
  });

  it('临时改行为', () => {
    vi.spyOn(utils, 'formatMoney').mockReturnValue('FREE');
    expect(utils.formatMoney(1)).toBe('FREE');   // 行为被替换
    // afterEach 已 restore，不影响下一用例
  });
});
// 对比：vi.mock('./utils') 则整个模块对所有 import 方都变成 mock。
```
