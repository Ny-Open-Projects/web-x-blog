---
title: [AIC-661] AI 生成的测试有「测试味道」，怎么识别？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-661：AI 生成的测试有「测试味道」，怎么识别？

**答**：
- 结论先行：**「测试味道」= 测试能通过但没真正验证行为的代码气味**。AI 生成的测试常见三种味道：冗余（测了实现细节）、脆弱（一点重构就失败）、缓慢（大量 sleep/真实等待）——它们让测试「看起来有」但实际是负担。
- 冗余味：断言 `expect(fn.toString()).toContain('map')` 这种测实现而非行为的断言；或对 mock 的调用次数过度断言（`toHaveBeenCalledTimes(5)`）——实现一重构就失败，却不保护任何行为。
- 脆弱味：依赖固定时间（`new Date()`）、固定顺序、真实网络/定时器；用 `setTimeout(500)` 等异步而非 `waitFor`——不稳定且慢。
- 缓慢味：每个用例都 `jest.resetModules()` + 全量 mock 重建；或测试里 sleep 很久。
- 治理：1) **静态扫描**：扫弱断言（AIC-413）、sleep、实现细节断言；2) **变异分数兜底**：测试味道重的用例杀不死变异体（AIC-644）；3) **review 清单**：「这个测试失败时能告诉我什么 bug？」——答不上来就是冗余测试，删掉。
- 追问钩子：为什么「测实现细节」的测试比「没测试」更有害？——因为它会在正确的重构时误报失败（增加维护成本），却在真正出 bug 时可能照样通过（没保护行为）——既添乱又不干活，还给人「有测试保护」的错觉，比没有更危险。

```typescript
type TestSmell = { re: RegExp; type: string; why: string };

const SMELLS: TestSmell[] = [
  { re: /setTimeout\s*\(\s*\d{3,}/, type: 'slow-sleep', why: '用固定sleep等异步，改用waitFor' },
  { re: /toHaveBeenCalledTimes/, type: 'implementation-detail', why: '断言调用次数，重构易碎' },
  { re: /toString\(\).*toContain/, type: 'implementation-detail', why: '测实现而非行为' },
  { re: /expect\([^)]*\)\.toBeDefined\(\)/, type: 'weak-assertion', why: '弱断言，杀不死变异体' },
];

function detectTestSmells(testCode: string): string[] {
  return SMELLS.filter(s => s.re.test(testCode)).map(s => `${s.type}: ${s.why}`);
}

const test = `
await new Promise(r => setTimeout(r, 500));
expect(fn).toHaveBeenCalledTimes(3);
expect(result).toBeDefined();
`;
console.log(detectTestSmells(test).length === 3);
```
