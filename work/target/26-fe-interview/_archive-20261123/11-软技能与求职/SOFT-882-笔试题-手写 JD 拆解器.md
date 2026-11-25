---
title: [SOFT-882] 手写 jdParser：JD 的三层拆解（关键词/痛点/隐含要求）与简历装配清单输出？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-882：手写 jdParser：JD 的三层拆解（关键词/痛点/隐含要求）与简历装配清单输出

**需求与边界**：
- 实现 jdParser(jdText)。
- 边界要求：① 关键词层：技术名词与硬要求提取（机筛命中——SOFT-864）；② 痛点层：JD 中“解决/优化/治理”类动词指向的团队痛点（用人经理的愁事）；③ 隐含层：JD 没写但暗示的要求（“快节奏环境”=加班与迭代速度；“从 0 到 1”=基建能力）；④ 输出装配清单：每层对应的简历动作（关键词自然覆盖/痛点案例前置/隐含层准备话术 SOFT-867）。

**答**：
```javascript
function jdParser(jdText) {
  const TECH = /React|Vue|TypeScript|Node|性能|工程化|可视化|跨端|低代码/gi;
  const PAIN = /(解决|优化|治理|提升|重构|稳定性|降本)[^，。；]*/g;
  const HINT = [/快节奏|迭代/, /从\s*0\s*到\s*1/, /复杂|高并发/, /跨团队|协作/];
  const HINTMAP = ['快节奏=加班与迭代速度——准备节奏适应的信号',
    '从0到1=基建能力——备0→1案例',
    '复杂/高并发=难度场景——备架构取舍案例',
    '跨团队=协作软实力——备外交与冲突案例（SOFT-728）'];
  const keywords = [...new Set((jdText.match(TECH) ?? []).map(t => t))];
  const pains = [...new Set((jdText.match(PAIN) ?? []).map(p => p.trim()))];
  const implied = HINT.map((re, i) =>
    re.test(jdText) ? HINTMAP[i] : null).filter(Boolean);
  return {
    keywords,
    pains, painAction: pains.length
      ? `痛点案例前置：${pains[0]}对应的你的案例放第一屏（SOFT-863）`
      : null,
    implied,
    assembly: [
      `关键词自然覆盖：${keywords.join('/')}（不堆砌）`,
      pains.length ? `痛点案例：${pains.map(p => p.slice(0, 15)).join(';')}——前置` : null,
      implied.length ? `隐含层话术准备：${implied.length}条（SOFT-867话术库）` : null,
    ].filter(Boolean) };
}
```

**评分点**:
- 三层拆解（关键词机筛/痛点人筛/隐含暗示——SOFT-864 落地）。
- 痛点动词的提取（解决/优化/治理=用人经理的愁事）。
- 装配清单直接可执行（每层对应简历动作与话术准备）。

