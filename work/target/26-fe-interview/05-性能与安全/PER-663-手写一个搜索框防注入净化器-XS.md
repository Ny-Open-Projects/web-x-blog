---
title: [PER-663] 手写一个搜索框防注入净化器：XSS 特征剥离 + LIKE 通配符转义 + 长度控制（输入侧纵深）
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-663：手写一个搜索框防注入净化器：XSS 特征剥离 + LIKE 通配符转义 + 长度控制（输入侧纵深）

**答**：
- 搜索框是高频注入入口，前端侧做输入净化（纵深一层，服务端仍是主防线）：XSS 特征剥离（防 v-html 渲染搜索历史）、LIKE 通配符转义（%/_ 转义，防全表扫描拖库）、SQL 注释特征提示、长度与频控。
- 要点：转义在拼查询串处做而不是展示处做——两处语义不同（展示转义是 HTML 实体，查询转义是通配符）；历史记录存 localStorage 前也过净化。
- 边界：用户合法搜索含 %（如"75% off"）要保留语义——转义规则与服务端约定（\% -> 字面 %），不能粗暴删除；emoji/全角字符正常放行。
- 评分点：通配符语义转义与服务端约定一致。

```javascript

function sanitizeSearch(raw, { maxLen = 60 } = {}) {
  let q = String(raw).slice(0, maxLen).trim();
  if (!q) return q;
  // 1) XSS 特征剥离（防搜索历史被 v-html 渲染时执行）
  q = q.replace(/<[^>]*>?/g, '')                                // 任意标签剥除
       .replace(/on\w+\s*=/gi, '')                             // 事件属性
       .replace(/javascript:/gi, '');
  // 2) LIKE 通配符按约定转义（保留用户语义，服务端用 ESCAPE '\' 解析）
  q = q.replace(/([%_\\])/g, '\\$1');
  // 3) 注释特征提示（服务端参数化查询为主，此处仅记录可疑）
  if (/(--|\/\*|\*\/)/.test(raw)) report('search-sqli-suspect', { q: raw.slice(0, 40) });
  return q;
}
sanitizeSearch('75% off<script>alert(1)</script>');   // => '75\\% off'
```
