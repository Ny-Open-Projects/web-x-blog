---
title: [WCN-805] 技术委员会评审一个 WC 组件提案，应该从哪几个维度打分？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-805：技术委员会评审一个 WC 组件提案，应该从哪几个维度打分？

**答**：
- 结论先行：评审不是「看代码写得好不好」，而是「看这个组件进平台后会不会变成负担」——统一用一张加权评分卡，低于阈值直接打回，避免人情评审。
- API 契约（权重最高）：property/事件/slot 命名是否符合规范、是否过度暴露内部实现、是否好演进（向后兼容空间）。
- 复用价值：是否真有多个业务方需要（避免一次性组件污染平台）、与现有组件的边界是否清晰、能否组合而非新增。
- 工程质量：a11y 达标、token 化无裸值、跨框架一致性测试、体积预算、SSR/DSD 支持。
- 可维护性：文档完整度、是否有 owner、是否有弃用与迁移方案、依赖是否最小化。
- 追问钩子：面试官常问「两个维度冲突怎么裁决」——答：复用价值与契约是一票否决项，其余按加权分排序；并强调评审结论要落 ADR 留痕。

```javascript
// 评审打分卡：契约与复用是一票否决，其余加权
const DIM = {
  apiContract: { weight: 3, veto: true },
  reuse:        { weight: 3, veto: true },
  a11y:         { weight: 2, veto: false },
  tokenized:    { weight: 1, veto: false },
  docs:         { weight: 1, veto: false },
};
function review(score) {
  for (const [k, cfg] of Object.entries(DIM)) {
    if (cfg.veto && score[k] < 3) return `打回：一票否决项 ${k} 得分过低`;
  }
  let total = 0, max = 0;
  for (const [k, cfg] of Object.entries(DIM)) { total += score[k] * cfg.weight; max += 5 * cfg.weight; }
  const pct = Math.round((total / max) * 100);
  return pct >= 75 ? `通过（${pct}分）` : `退回修改（${pct}分）`;
}
console.log(review({ apiContract: 4, reuse: 4, a11y: 5, tokenized: 5, docs: 3 }));
console.log(review({ apiContract: 2, reuse: 5, a11y: 5, tokenized: 5, docs: 5 }));
```
