---
title: [TST-568] 笔试：笔试：AI 生成用例质量评分
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-568：笔试：笔试：AI 生成用例质量评分

**题目**：实现 qualityScore(c, coverageDelta)。c={ code, assertions:[{type, hasMatcher}], deterministic:boolean, readsSpec:boolean, lines }。coverageDelta 为该用例新增覆盖行占比(0~1)。要求计算综合分(0~100)：① 断言质量(40分)：每个断言有 matcher 得满分，否则折半，按断言数归一化；② 确定性(20分)：deterministic 为真满分否则 0；③ 规范对齐(15分)：readsSpec 为真满分；④ 覆盖贡献(25分)：coverageDelta*25；⑤ 边界：code 为空或断言数组为空返回 0 分并标记 invalid；输出 {score, valid, breakdown}。

**答**：
- 结论：加权评分 = 断言质量×40 + 确定性×20 + 规范×15 + 覆盖×25，断言按 matcher 完整度折算。
- 实现要点：断言得分 = Σ(hasMatcher?1:0.5)/count；各维度 clamp；无 code/无断言返回 invalid、score=0；breakdown 给出各维度分便于解释。
- 追问钩子：分数低就一定不用吗？——不一定，需结合场景；评分用于「排序优先审」与发现系统性问题（如 AI 普遍缺 matcher），而非一票否决。

```javascript
function qualityScore(c = {}, coverageDelta = 0) {
  if (!c.code || !Array.isArray(c.assertions) || !c.assertions.length)
    return { score: 0, valid: false, breakdown: {} };
  const assertionRatio = c.assertions.filter(a => a.hasMatcher).length / c.assertions.length
    + c.assertions.filter(a => !a.hasMatcher).length * 0.5 / c.assertions.length;
  const breakdown = {
    assertion: +(assertionRatio * 40).toFixed(1),
    deterministic: c.deterministic ? 20 : 0,
    spec: c.readsSpec ? 15 : 0,
    coverage: +(Math.min(1, coverageDelta) * 25).toFixed(1),
  };
  const score = +Object.values(breakdown).reduce((a, b) => a + b, 0).toFixed(1);
  return { score, valid: true, breakdown };
}
```

**评分点**：
- 四维度权重正确（40/20/15/25），断言按 matcher 折算。
- coverageDelta clamp 到 0~1，确定性/规范布尔计分正确。
- 无 code 或无断言返回 score=0 且 valid=false。
- breakdown 分维度输出，分数可解释可断言。
