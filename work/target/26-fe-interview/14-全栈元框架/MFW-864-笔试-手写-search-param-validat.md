---
title: [MFW-864] 笔试：手写 search param validator 链归一化器
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-864：笔试：手写 search param validator 链归一化器

**答**：
- 结论：逐字段按 validator 解析，非法值与缺失值降级到 default 并记录 errors；单个字段非法不中断整次导航。
- 关键：运行时校验是必须的——URL 可被用户篡改，编译期类型无法覆盖。
- 追问钩子：归一化 vs 抛错重定向怎么选？——展示型参数归一化，身份/权限相关参数应拒绝并重定向。

```javascript
function normalizeSearch(params, validators) {
  const value = {}, errors = [];
  for (const [key, def] of Object.entries(validators)) {
    const raw = params[key];
    if (raw == null) { value[key] = def.default; continue; }
    try { value[key] = def.parse(raw); }
    catch (e) { errors.push(key); value[key] = def.default; }
  }
  return { value, errors };
}

// 自测
const V = {
  page: {
    parse: s => { const n = +s; if (!Number.isInteger(n) || n < 1) throw Error(); return n; },
    default: 1
  },
  tab: {
    parse: s => { if (!['info', 'comments'].includes(s)) throw Error(); return s; },
    default: 'info'
  }
};
const r = normalizeSearch({ page: '3', tab: 'bad' }, V);
console.log(JSON.stringify(r)); // { value:{page:3,tab:'info'}, errors:['tab'] }
```

**评分点**：
- 逐字段解析，非法值降级到 default 并记录 errors
- 缺失字段用 default；单个非法字段不中断整次导航
- 返回 value + errors 供上层决定提示或重定向
- 能说明运行时校验必要性（URL 可篡改）与归一化/拒绝的取舍（加分）
