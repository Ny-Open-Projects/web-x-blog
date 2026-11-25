---
title: [NODE-548] Node 服务的敏感词过滤（DFA/热更新/旁路）如何实现？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面题, 20]
type: 面试题
---

## NODE-548：敏感词过滤实现
**答**:
- 匹配引擎：DFA/Trie（词库匹配 O(n)——ARC-ALG Trie 敏感词延伸）、变体对抗（谐音/拆字/插符——归一化预处理（去零宽/全半角/拼音映射）+ 正则组合对抗）、分级词库（禁止词（直接拒）/替换词（打码）/审核词（进人审）——分级处理）。
- 热更新：词库热更新（词库版本化发布——运行时重建 Trie 原子切换 NODE-490 热更边界；多实例同步失效广播 NODE-507）。
- 应用位与性能：发布链路同步过滤（毫秒级预算——Trie 内存常驻）、存量内容扫描（批量扫描任务——词库更新后全量复扫 NODE-437 编排）、上下文过滤（UGC 评论/昵称/签名各自策略）。
- 旁路与对抗：过滤绕过检测（变体命中模式统计——对抗升级数据）、误杀反馈（用户申诉 → 词库调整流程——误杀率治理）。
- 合规：词库来源合规（监管词库 + 平台自维护——分级管理审计 NODE-442）、过滤日志（命中记录——审核追溯）。
```javascript
// Trie 过滤 + 归一化
const trie = new AhoCorasick(loadWords());
function filter(text) {
  const norm = normalize(text);                                  // 全角/零宽/拆字归一
  const hits = trie.match(norm);
  if (hits.some(h => h.level === 'block')) throw new ContentBlocked(hits);
  return replaceMasked(text, hits.filter(h => h.level === 'mask'));
}
// 热更：bus.on('dict.updated', v => trieSwap(new AhoCorasick(load(v))))  // 原子切换
```
