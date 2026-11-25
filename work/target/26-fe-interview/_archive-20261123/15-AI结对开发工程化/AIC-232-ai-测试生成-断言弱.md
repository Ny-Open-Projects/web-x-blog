---
title: [AIC-232] AI 生成的单测大量使用 `expect(x).toBeDefined()` 这类弱断言，如何系统性治理？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-232：AI 生成的单测大量使用 `expect(x).toBeDefined()` 这类弱断言，如何系统性治理？
**答**：
- 提示词给「断言强度标准」：每个测试必须断言业务结果（值/调用参数/状态变化），禁止 only-defined 类断言。
- 静态扫描弱断言模式进 CI 门禁，AI 产出不过门禁就打回重生成。
- 给黄金示例：一对「弱断言改写前后」的样例，比规则描述有效。
- 变异测试兜底：弱断言测试杀不死变异体，用存活变异体定位弱测试。

```javascript
// 弱断言扫描器（CI 门禁）
const weak = [/toBeDefined\(\)/, /not\.toThrow\(\)$/, /toBeTruthy\(\)(?![\s\S]{0,40}expect)/];
function scanWeakAssertions(code: string) {
  return code.split('\n').map((line, i) => ({ line: i + 1, text: line }))
    .filter(l => weak.some(r => r.test(l.text)));
}
r
```
