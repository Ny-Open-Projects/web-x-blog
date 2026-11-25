---
title: [AIC-056] AI 生成的代码有许可证/抄袭风险吗？团队该怎么评估和处理？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-056：AI 生成的代码有许可证/抄袭风险吗？团队该怎么评估和处理？
**答**：
- 风险来源：模型可能在补全中复现训练数据里的开源代码（长且罕见的函数尤甚），若原代码是 GPL 等强传染协议就构成合规风险。
- 评估手段：相似度检测——把 AI 产出与公开代码库（如 GitHub Search）比对，超长片段（如连续 15 行以上）命中需人工评估来源。
- 处理策略：政策上明确「AI 产出的核心算法代码必须走增强 review」；工具上开启供应商的引用过滤（Copilot 的 duplicate suggestion blocker）。
- 法律边界要诚实：当前对「模型输出是否构成衍生作品」尚无定论，团队合规的重点是**留痕与举证**（记录生成工具、时间、审查人），而不是假装零风险。
- 追问钩子：这条与 AIC-010 隐私合规是一体两面——出向是数据泄漏风险，入向是引入许可风险，都要有清单和流程。

```javascript
// 简化的长片段相似度抽查（n-gram 指纹思路）
function fingerprint(code, n = 8) {
  const tokens = code.replace(/\s+/g, ' ').split(' ');
  return new Set(tokens.slice(0, tokens.length - n + 1)
    .map((_, i) => tokens.slice(i, i + n).join(' ')));
}
function riskySegments(genCode, knownIndex, threshold = 0.2) {
  const fp = fingerprint(genCode);
  let hit = 0;
  for (const gram of fp) if (knownIndex.has(gram)) hit++;
  return hit / fp.size > threshold ? 'NEED_SOURCE_REVIEW' : 'OK';
}
```
