---
title: [ALG-252] 价格区间与数字范围的本地化格式化：Intl.NumberFormat 的 RangeFormat 与自定义区间？
date: 2026-11-19
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---
## ALG-252：价格区间与数字范围的本地化格式化：Intl.NumberFormat 的 RangeFormat 与自定义区间？
**答**：筛选面板显示价格区间："¥100 - ¥200"（中文）vs "$100 - $200"（英文）vs "100~200 元"——Intl 支持 range format（Intl.NumberFormat.formatRange），不同 locale 的连接符/符号位置自动正确。

**思路**：formatRange（同币种区间）；步长对齐（区间端点按档位取整：99.9 → 100）；开放区间（200 以上 → ¥200 起/¥200+）。

```javascript
const fmt = new Intl.NumberFormat('zh-CN', { style: 'currency', currency: 'CNY', maximumFractionDigits: 0 });
fmt.formatRange(100, 200);            // "¥100 - 200"（locale 自动：货币符号只出现一次）
const fmtEn = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' });
fmtEn.formatRange(100, 200);          // "$100.00 – $200.00"
function priceBand(min, max, { fmt, unit } = {}) {
  if (min == null && max == null) return '全部';
  if (min == null) return `${fmt.format(max)} 以下`;
  if (max == null) return `${fmt.format(min)} 起`;                  // 开放区间
  if (min === max) return fmt.format(min);
  return fmt.formatRange(min, max);
}
// 档位端点取整：99.9 → 100（priceBand(99.9, 200.5) → round 到 ¥100 - ¥200，展示友好）
// 兼容性：formatRange 需要 ES2023 Intl（Chrome 95+/Safari 15.4+）—— 降级手动拼 `${fmt.format(min)} - ${fmt.format(max)}`
```

**评分点**：
- formatRange 的 locale 自动语义（符号只出现一次、连接符随 locale）。
- 开放区间/单值/全部的分支语义。
- 档位端点取整的展示友好性。
- 兼容性降级方案（旧环境手动拼接）。
