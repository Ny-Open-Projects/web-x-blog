---
title: [AIC-588] AI 生成代码的可读性评估
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-588：AI 代码可读性评估

**答**:
- AI 代码的可读性问题：1) **过度简洁**（AI 压缩代码：一行链式调用完成 10 步逻辑——"简洁但不可读"（人需要花时间理解——AI 写给自己看不是给人看）；2) **命名不直观**（AI 用抽象名——`processData`、`handleThing`（不表达具体业务含义——"data"是什么数据？"thing"是什么东西？）；3) **魔法值**（AI 用硬编码常量——`if (status === 3)`（3 是什么？——应该用枚举 `OrderStatus.SHIPPED`）；4) **嵌套过深**（AI 生成的回调嵌套——3 层以上的 if/for 嵌套（认知复杂度 RBL-583）。
- 可读性的评估维度：1) **命名质量**：变量/函数名是否描述业务意图（`getUserOrders` > `getData`）；2) **注释覆盖**：复杂逻辑是否有解释（RBL-514 注释即 Prompt 的可读性维度）；3) **复杂度匹配**（认知复杂度与业务复杂度匹配 RBL-583）；4) **魔法值**：硬编码常量的存在（应提取为常量/枚举）。
- 追问钩子：为什么「AI 代码的可读性」比「人写代码的可读性」更需要主动评估？——人写代码的可读性在写的过程中自然形成（人命名时思考业务含义——逐步改进）；AI 一次性生成（没有"逐步改进可读性"的过程——生成即最终——可读性问题需要事后检测）；「AI 的可读性盲区」：AI 不知道自己生成的代码对人来说是否可读（AI 的"理解"与人的"理解"不同——AI 能理解自己的输出但人可能不能）。

```typescript
// 可读性评估
function assessReadability(code: string) {
  const issues: string[] = [];
  // 1) 魔法值
  const magicNumbers = [...code.matchAll(/[^\w]([2-9]\d+)[^\w]/g)]
    .filter(m => !/version|port|timeout/i.test(code.slice(0, m.index ?? 0)));
  if (magicNumbers.length > 2) issues.push('magic-numbers');
  // 2) 抽象命名
  const abstractNames = [...code.matchAll(/(?:function|const)\s+(process|handle|manage|do|run)\w*/gi)];
  if (abstractNames.length > 2) issues.push('abstract-naming');
  // 3) 链式过长
  const longChains = code.match(/\.\w+\(\)\.\w+\(\)\.\w+\(\)\.\w+\(/g);
  if (longChains?.length) issues.push('long-chain');
  // 4) 嵌套深度
  const maxIndent = Math.max(...code.split('\n').map(l =>
    (l.match(/^\s*/)?.[0].length ?? 0) / 2));
  if (maxIndent > 5) issues.push('deep-nesting');
  // 5) 注释缺失
  const fnCount = (code.match(/function\s+\w+|=>\s*{/g) ?? []).length;
  const commentCount = (code.match(/\/\/|\/\*/g) ?? []).length;
  if (fnCount > 3 && commentCount === 0) issues.push('no-comments');
  return { issues, readable: issues.length <= 1 };
}
```
