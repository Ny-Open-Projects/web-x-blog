---
title: [RBL-585] 构建器自身的测试体系：AST 快照、产物 golden 测试与最小复现库
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-585：构建器自身的测试体系：AST 快照、产物 golden 测试与最小复现库

**答**：
- 构建器是「把代码变代码」的工具，测试难点在产物断言：直接 diff 压缩后的 JS 字符串极其脆弱（变量名/顺序抖动）——分层策略：1) **AST 层断言**（产物 parse 回 AST 后做规范化比较，忽略标识符命名与格式）；2) **golden 文件测试**（固定输入→固定产物快照，更新走显式 `UPDATE_SNAPSHOTS=1` 审查流程）；3) **行为测试**（产物在 Node/JSDOM 里真实执行，断言运行结果而非文本）。
- 最小复现库（repro fixture corpus）是核心资产：每个 bug 修复都沉淀一个最小 fixture（目录：input + rolldown.config + expected-output + issue 链接），回归测试集随 bug 只增不减——这是打包器质量的基本盘（esbuild/rolldown 都是数千 fixture 起步）。
- 跨工具一致性测试：同一输入跑 rolldown 与 webpack/rollup，对比「模块图结构 + 导出集合」这种语义级产物而非文本——发现分歧即兼容性 bug。
- fuzzing：随机生成/变异合法 JS 输入，断言「不崩溃 + 产物可被解析 + 语义保持」（配合 RBL-546 随机语义等价测试）。
- 追问钩子：为什么构建器测试要用「真实大型项目」做基准（benchmark suite）？——合成 fixture 测不出真实依赖树里的 resolve 竞争、循环依赖组合等集成问题；esbuild 维护 three.js/d3 等 OSS 项目作为构建基准正是此理。

```javascript
// 分层测试骨架
// 1) fixture 驱动的回归测试
describe('fixtures', () => {
  for (const dir of collectFixtures('tests/fixture/')) {
    it(dir.name, async () => {
      const out = await build({ input: dir.input, config: dir.config });
      const actual = normalize(out);            // AST 规范化：忽略命名/空白
      if (process.env.UPDATE_SNAPSHOTS) return writeGolden(dir, actual);
      expect(actual).toEqual(loadGolden(dir));  // golden 比对
    });
  }
});

// 2) 语义等价断言（不比文本，比执行结果）
function expectSemanticEq(code1, code2, exports) {
  const r1 = runInSandbox(code1, exports), r2 = runInSandbox(code2, exports);
  expect(r1).toEqual(r2);                       // 行为一致
}

// 3) 最小复现库沉淀流程（bug 生命周期）
// issue 报告 -> 提取最小 repro（< 5 文件）-> 修复 PR 必须包含 fixture
// fixture 目录约定：
//   tests/fixture/issue-1234/{ input.js, config.json, expected.js, README.md(含 issue 链接) }

// 4) fuzz 断言不变量
for (const mutated of mutations(validInput)) {
  const out = tryBuild(mutated);                // 不抛未捕获异常
  if (out.ok) parse(out.code);                  // 产物可解析
}
```
