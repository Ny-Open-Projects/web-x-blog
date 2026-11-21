---
title: [ALG-272] 混合多语言列表排序：中英日混合按各自 locale 分组内排序再组间固定序（分组桶排序）？
date: 2026-11-19
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

**场景**：通讯录混合中英日名：整体 Collator 排序会把日文混在中间（日语用户预期"あ行在最后"或独立分组）——分组桶排序：按脚本检测分组（拉丁/中文/日文假名），组内 locale 排序，组间固定序（可配置：中文优先/拼音序）。

**思路**：脚本检测（字符 Unicode 区段）→ 分桶 → 各桶 Intl.Collator 对应 locale 排序 → 按配置顺序拼接。

```javascript
function detectScript(ch) {
  const code = ch.codePointAt(0);
  if (code >= 0x3040 && code <= 0x30ff) return 'ja';       // 假名
  if (code >= 0x4e00 && code <= 0x9fff) return 'zh';       // CJK 统一表意
  if (code >= 0xac00 && code <= 0xd7af) return 'ko';       // 谚文
  return 'latin';                                          // 默认拉丁
}
function groupedSort(items, nameKey, groupOrder = ['latin', 'zh', 'ko', 'ja']) {
  const collators = { zh: new Intl.Collator('zh'), ja: new Intl.Collator('ja'),
                      ko: new Intl.Collator('ko'), latin: new Intl.Collator('en') };
  const buckets = new Map(groupOrder.map((g) => [g, []]));
  for (const item of items) {
    const script = detectScript(item[nameKey][0] ?? 'a');  // 首字符定组
    (buckets.get(script) ?? buckets.get('latin')).push(item);
  }
  const out = [];
  for (const group of groupOrder) {
    const list = buckets.get(group);
    if (list?.length) out.push(...list.sort((a, b) => collators[group].compare(a[nameKey], b[nameKey])));
  }
  return out;
}
// 分组序可配置（产品语义：中文用户期望 zh 组在前）
// 对比单 Collator 整排：Intl.Collator('zh') 对日文行为依实现——分组排序确定性明确
// 分组标题（通讯录索引条）：latin=A-Z、zh=拼音字母、ja=五十音 —— 分组排序天然支持索引
```

**评分点**：
- 脚本检测（Unicode 区段）+ 分组桶排序——本题核心。
- 组间序可配置的产品语义。
- 单 Collator 混排的不确定性对照。
- 与通讯录索引条（分组标题）的天然衔接。
