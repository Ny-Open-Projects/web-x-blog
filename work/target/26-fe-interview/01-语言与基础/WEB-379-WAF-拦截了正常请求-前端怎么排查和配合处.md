---
title: [WEB-379] WAF 拦截了正常请求，前端怎么排查和配合处理？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 安全]
type: 面试题
---

## WEB-379：WAF 拦截了正常请求，前端怎么排查和配合处理？
**答**：
- 特征识别：被拦常表现为 403/412 或返回 HTML 拦截页（JSON 解析报错）、特定参数（含 sql/js 关键词）触发。
- 排查：复现最小请求、二分参数定位触发字段、对照 WAF 拦截日志（规则 ID）、检查是否被误伤（业务名含敏感词如 select）。
- 配合：加白规则或改参数编码；前端对该接口做友好降级提示与上报，不能让用户面对裸报错。

```javascript
const res = await fetch('/api/query', { body: { name: 'select-user-plan' } });
if (res.status === 403 && await res.text().then(t => t.includes('waf'))) {
  report({ level: 'warn', msg: 'WAF 误伤', field: 'name' });
  return toast('请求被安全策略拦截，请联系管理员');
}
console.log('误伤常见于参数值含关键词 → 编码或改字段名');
```
