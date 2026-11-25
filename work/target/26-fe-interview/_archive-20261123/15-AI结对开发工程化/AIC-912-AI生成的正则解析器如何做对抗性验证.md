---
title: [AIC-912] 让 AI 生成的商品 SKU 解析正则/解析器，如何做「对抗性验证」防止它只过正常样例？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-912：让 AI 生成的商品 SKU 解析正则/解析器，如何做「对抗性验证」防止它只过正常样例？
**答**：
- 对抗性验证 = 主动构造「刁难输入」：超长字符串、空串、特殊字符、 Unicode、近似合法但非法的 SKU，看解析器是否崩溃/误判/灾难性回溯。
- 正则类 AI 产出要特别防「ReDoS」：用包含大量重复字符的输入测试执行时间，指数级回溯会让接口被拖垮。
- 建立「合法/非法」双向用例集：不仅验证合法 SKU 能被解析，也要验证非法 SKU 被拒绝——AI 常写出「什么都匹配」的宽松正则。
- 追问钩子：能提到「用 fuzzing 自动生成对抗输入 + 设置超时熔断」的候选人，把验证从静态用例升级为主动攻击。

```typescript
// 对抗性验证：刁难输入 + 超时熔断防 ReDoS
const adversarial = ['', 'A'.repeat(10000), 'SKU-中文-🎉', 'SKU--001', null, 'sku-001\n<script>'];
function adversarialCheck(parser, timeout = 100) {
  return adversarial.map(input => {
    const t = Date.now();
    try {
      const r = parser(input);
      const cost = Date.now() - t;
      return { input:String(input).slice(0,20), ok:cost < timeout, cost, r };
    } catch (e) { return { input:String(input).slice(0,20), ok:false, err:e.message }; }
  });
}
const parser = s => /^SKU-\d{3}$/.test(s ?? '') ? s : null;
console.log(adversarialCheck(parser)); // 宽松正则会在 'A'*10000 类输入暴露缺陷
```
