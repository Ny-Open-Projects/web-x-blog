---
title: [TST-172] 用 AI 生成测试代码，怎么把好质量关？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-172：用 AI 生成测试代码，怎么把好质量关？
**答**：
- AI 的强项：样板生成（给已实现的代码补 happy path 用例、fixture 工厂、mock 模板）、把人写的一两条用例扩展成参数化矩阵、为老代码生成特征测试（characterization test）打底。弱项：不知道业务意图（会照着实现写测试，「测实现」）、遗漏边界、生成看似合理实际永真的断言。
- 把关三条线：① 断言有效性——变异测试抽查（AI 生成的测试 mutation score 低 = 假测试高发）；② 反实现耦合——review 时检查是否断言内部 state/mock 调用细节；③ 边界覆盖——人工补 AI 漏掉的异常分支（AI 的 happy path 偏好是结构性的）。
- 工程化做法：把团队的测试规范写成提示词上下文（AGENTS.md / lint 规则：禁 sleep、role 定位、断言行为），AI 输出先过 lint + 必须能变异存活；生成用例的 PR 单独标注便于重点 review。
- 数据佐证话术：AI 可以把「写测试」的成本降一半，但「设计测试」的思考不可外包——分支分析、场景设计还是要人（这也是面试官想听到的判断）。
- 追问钩子：AI 会不会让测试变多但变差？——会，所以指标要转向质量指标（mutation score、抓 bug 数）而不是数量/覆盖率。

```javascript
// AI 生成测试的质量门禁流水线
const aiTestGate = [
  'lint: eslint-plugin-jest（禁 sleep / no-focused-tests / 期望实现）',
  'run: 全部通过（基础）',
  'mutation: 对被测模块抽样变异，score < 50 打回',   // 假测试检测
  'review: 检查断言行为而非实现 + 补漏的异常分支',
];
// 示例：AI 常见的假断言
// expect(result).toBeDefined()        ← AI 生成率高，mutation 存活
// expect(calculate(2, 3)).toBe(5)     ← 有效，变异 >→>= 会被杀死
```
