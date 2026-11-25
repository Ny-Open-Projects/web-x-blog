---
title: [SCN-1288] 手写一个 VAT 含税价拆分器
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## SCN-1288：手写一个 VAT 含税价拆分器

**答**：
- 需求：implement VatSplitter(country)。split(grossAmount) 从含税价拆出净价与 VAT：net = gross / (1 + rate)，vat = gross - net；reverse(net) 反向合成含税价；rounding 按 OIML 四舍五入到分。
- 边界：rate 缺失查 VAT_RATE 表，未知国家抛错；gross 为 0 返回全零；保留 2 位精度一致性（net+vat === gross 校验）。
- 评分点：含税拆分；差额法；reverse；未知国家

```javascript
class VatSplitter {
  constructor(country) {
    this.rate = { DE: 0.19, FR: 0.20, JP: 0.10 }[country];
    if (this.rate == null) throw new Error('未知税率: ' + country);
  }
  split(gross) {
    const net = Math.round(gross / (1 + this.rate) * 100) / 100;
    const vat = +(gross - net).toFixed(2);             // 差额法保证 net+vat === gross
    return { gross, net, vat: +vat.toFixed(2), rate: this.rate };
  }
  reverse(net) {
    return Math.round(net * (1 + this.rate) * 100) / 100;
  }
}
```
