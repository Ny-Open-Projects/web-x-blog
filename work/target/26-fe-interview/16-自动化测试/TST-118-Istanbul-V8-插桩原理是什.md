---
title: [TST-118] 覆盖率是怎么统计出来的？V8 与 Istanbul 插桩原理
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-118：覆盖率是怎么统计出来的？V8 与 Istanbul 插桩原理
**答**：
- 两条技术路线。Istanbul（babel 插桩）：编译期把源码改写——每个语句/分支包进计数器（`cov_xxx.s[0]++`、分支记录走 true/false 哪条），运行时执行计数，最后从计数器生成报告。优点：分支/语句位置精确、可统计「部分覆盖」的行；缺点：改写代码，执行慢、和某些语法/调试器可能冲突。
- V8 coverage（原生）：不改代码，直接读 V8 引擎的**代码块覆盖率**（JS 层按 function/block 粒度，`NODE_V8_COVERAGE` 或 inspector API 拿到），换算成行/分支。优点：零插桩、速度快；缺点：单行内多个分支无法拆分（一行里 `a && b || c` 的部分覆盖不知道），粒度粗。
- Vitest 里怎么选：默认 v8（快）；需要精确分支统计（门禁卡 branches）时上 istanbul，或 v8 + `all: true`（把没被任何测试 import 的文件也纳入统计——不然「从未 require 的文件」不在报告里，覆盖率虚高）。
- 原理追问点：为什么 v8 要 `all: true`？为什么 istanbul 的行覆盖能标出 `0x/2x`？为什么 monorepo 里要看 `remap`（sourcemap 映射回 TS 源码）？
- 追问钩子：怎么统计「这段代码是哪个用例覆盖的」？——istanbul 的 hook 模式按 test snapshot，或 per-test coverage（v8 逐用例拿 coverage 再 diff 合并），用于「改动影响了哪些用例」的反向查询。

```javascript
// Istanbul 插桩示意（源码 → 改写后）
// 源码：
//   const f = (a) => a > 0 ? 'p' : 'n';
// 插桩后（简化）：
const cov_1 = { s: [0, 0], b: [[0, 0]] };
const f = (a) => (cov_1.s[0]++,
  a > 0 ? (cov_1.b[0][0]++, 'p')
        : (cov_1.b[0][1]++, 'n'));

// vitest.config.ts
export default defineConfig({
  test: {
    coverage: {
      provider: 'v8',
      all: true,          // 未被 import 的文件也计入分母
      reportOnFailure: true, // 失败也出报告
    },
  },
});
```
