---
title: [ALG-422] 手写 KMP 完整匹配：模板串扫描
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-422：手写 KMP 完整匹配：模板串扫描

**答**：
- 题目：模板校验——文档流中检测模板串「{{name}}」占位是否全部按序出现（子序列级）。KMP 变体：匹配成功后不重置 j（继续子序列匹配）。
- 思路：标准 KMP 主循环去掉「命中后收集」，改为 j 走完即标记 matched；子序列语义：主串不回退天然满足。
- 评分点：命中后 j 处理的三种语义（重叠/非重叠/子序列）；线性复杂度证明（i 单调前进）。

```javascript
function subsequenceMatch(text, p) {                       // p 是 text 的子序列？
  const next = buildNext(p);
  let j = 0;
  for (let i = 0; i < text.length && j < p.length; i++) {
    while (j > 0 && text[i] !== p[j]) j = next[j - 1];     // 尽量延续匹配前缀
    if (text[i] === p[j]) j++;
  }
  return j === p.length;                                   // 全部匹配完即子序列成立
}
// 场景：模板占位符按序校验、事件流规则匹配
// 复杂度：O(n + m)——主串指针只前进，无回溯
```
