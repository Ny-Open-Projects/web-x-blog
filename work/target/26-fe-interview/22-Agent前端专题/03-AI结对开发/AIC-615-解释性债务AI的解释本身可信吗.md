---
title: [AIC-615] 让 AI 解释它生成的代码，这份解释本身可信吗？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-615：让 AI 解释它生成的代码，这份解释本身可信吗？

**答**：
- 结论先行：**AI 的解释是「事后合理化」（post-hoc rationalization），不是生成决策的真实复盘，因此只能当线索不能当证据**。它擅长编出一段听起来合理但与代码实际行为不符的说明——这叫「解释性债务」：你以为懂了，其实欠着一份未经核实的认知。
- 为什么不可信：1) LLM 生成解释时看的是代码 token，而非它生成代码时的「动机」（它也没有真实动机）；2) 解释会迎合提问方式——你问「这段为什么用 useMemo」，它就说性能优化，哪怕真实原因是误用；3) 解释与代码可能同时错，形成「双重幻觉」。
- 如何验证解释：1) **对照法**：让 AI 解释后，人工对照代码逐条核实（变量来源、分支条件、副作用）；2) **追问法**：针对解释里的关键断言追问「如果输入 X 会怎样」，看解释是否自洽（AIC-538 意图漂移）；3) **执行法**：写一个小测试验证解释声称的行为，跑一遍看结果。
- 正确使用姿势：把 AI 解释当作「快速浏览地图」，帮你定位代码在干什么，但「地图不等于地形」——关键逻辑、安全边界、性能路径必须人眼确认。
- 追问钩子：为什么「让人写注释」比「让 AI 写注释」更能减少解释性债务？——因为人写注释时需要真正理解代码（认知加工），这个过程本身消除了债务；而读 AI 解释是被动接受，容易产生「理解错觉」（illusion of understanding）。

```typescript
// 解释可信度检查：对 AI 解释中的关键断言生成验证用例
type Claim = { assertion: string; input: any; expected: any };

function verifyExplanation(
  fn: (x: any) => any,
  claims: Claim[],
): { claim: string; verified: boolean }[] {
  return claims.map(c => {
    let actual;
    try { actual = fn(c.input); } catch (e) { actual = 'THREW'; }
    // 用 JSON 字符串比较，覆盖对象/基本类型
    return {
      claim: c.assertion,
      verified: JSON.stringify(actual) === JSON.stringify(c.expected),
    };
  });
}

// AI 解释声称：parseQty('1,000') 返回 1000
const parseQty = (s: string) => Number(s.replace(/,/g, ''));
const results = verifyExplanation(parseQty, [
  { assertion: '千分位字符串转数字', input: '1,000', expected: 1000 },
  { assertion: '空字符串返回0', input: '', expected: 0 }, // 实际返回 0 ✓
]);
console.log(results.every(r => r.verified)); // true —— 解释与行为一致才可信
```
