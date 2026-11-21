---
title: [TST-045] 笔试：手写 console 沙箱（捕获输出 + 压噪 + 还原）
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-045：笔试：手写 console 沙箱（捕获输出 + 压噪 + 还原）
**答**：
- 需求：测试期间拦截 console.error/warn：① 不污染报告输出；② 捕获内容供断言（「代码确实打了错误日志」）；③ 结束后完整还原，防全局污染。
- 核心：临时替换 console 上的方法为新函数，内部 push 到数组；restore 时把原引用挂回；spyOn 语义——默认保留原输出可叠加。
- 边界：只替换目标方法而非整个 console 对象；多次嵌套捕获要按栈还原；捕获数组每条带方法名与参数（参数可能是对象，浅拷贝引用即可）。

```javascript
function sandboxConsole(methods = ['error', 'warn']) {
  const captured = [];
  const originals = new Map();

  function install() {
    for (const m of methods) {
      originals.set(m, console[m]);            // 先存原引用
      console[m] = (...args) => {
        captured.push({ method: m, args });    // 记录（不吐出，压噪）
      };
    }
  }
  function restore() {
    for (const [m, orig] of originals) console[m] = orig;
    originals.clear();
  }
  return { captured, install, restore };
}

// ---- 用法：测试错误分支时压噪 + 断言日志 ----
import { describe, it, expect, afterEach } from 'vitest';
describe('pay 失败分支', () => {
  const box = sandboxConsole(['error', 'warn']);
  afterEach(() => box.restore());           // 无论成败都还原

  it('失败时打了 error 日志且不向控制台喷红', () => {
    box.install();
    pay({ amount: -1 });                    // 被测代码内部 console.error(...)
    expect(box.captured.some((c) => c.method === 'error')).toBe(true);
    expect(box.captured[0].args[0]).toMatch(/invalid amount/);
  });
});
```
**评分点**：
- 只替换指定方法、保存原引用并在 restore 归还（整个 console 换对象是常见扣分写法）。
- captured 带 method 与 args，可断言「打过日志」。
- afterEach/finally 保证还原（异常路径也要还原）。
- 对应 vi.spyOn(console, 'error').mockImplementation(() => {}) 的原生用法。
