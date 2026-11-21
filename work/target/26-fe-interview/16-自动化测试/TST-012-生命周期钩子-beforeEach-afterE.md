---
title: [TST-012] Vitest 生命周期钩子的执行顺序和作用域是怎样的？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-012：Vitest 生命周期钩子的执行顺序和作用域是怎样的？
**答**：
- 作用域：describe 内注册的钩子只对该 describe 下的用例生效；外层钩子对内层也生效（形成洋葱包裹）。
- 顺序：beforeAll → 每个 it 前 beforeAll(外→内)/beforeEach(外→内) → it → afterEach(内→外)/afterAll。after 系列与 before 系列嵌套顺序相反。
- 常见用法：beforeEach 里重置 mock、重建夹具；afterEach 里 `cleanup()`（RTL 自动调用）、restoreAllMocks、清 storage。
- 陷阱：钩子是异步感知的，返回 Promise 会被等待；在 beforeAll 里初始化的共享变量若被用例修改，会造成用例顺序依赖——每条用例应拿到全新实例。
- 追问钩子：`beforeEach(fn, timeout)` 第二参设超时；钩子里的失败记到对应用例上。

```javascript
import { describe, it, beforeEach, afterEach, beforeAll, afterAll } from 'vitest';

describe('外层', () => {
  beforeAll(() => console.log('1 beforeAll'));
  beforeEach(() => console.log('2 beforeEach 外'));
  afterEach(() => console.log('5 afterEach 外'));

  describe('内层', () => {
    beforeEach(() => console.log('3 beforeEach 内'));
    afterEach(() => console.log('4 afterEach 内'));

    it('用例', () => console.log('用例执行'));
    // 输出：1 beforeAll → 2 外 → 3 内 → 用例 → 4 内 → 5 外
  });
});
```
