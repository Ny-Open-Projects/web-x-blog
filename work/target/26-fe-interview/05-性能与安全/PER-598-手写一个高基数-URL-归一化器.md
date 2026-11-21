---
title: [PER-598] 手写一个高基数 URL 归一化器：把原始 URL 归并成路由模板作为监控维度，保留明细原文
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-598：手写一个高基数 URL 归一化器：把原始 URL 归并成路由模板作为监控维度，保留明细原文

**答**：
- 监控维度的第一 sanity：`/order/88231` 和 `/order/88232` 必须归并成 `/order/:id`，否则 series 爆炸；归一化分层——静态路由表优先、动态段正则、未知路径兜底为 `other`。
- 要点：规则可配置（数字段/uuid/长 hash 的通用模式）；保留原文但只进明细不上聚合；未匹配路由先归 `other` 并单独上报未匹配样本供补充规则。
- 边界：query 参数全部剥离（分页/追踪参数是纯噪声）；大小写统一；尾斜杠统一。
- 评分点：规则优先级与 other 兜底上报。

```javascript

const ROUTES = [ '/home', '/list', '/detail/:id', '/order/:id/items/:itemId', '/user/:uuid' ];
const PATTERNS = [
  [/^\/[0-9a-f]{8}-[0-9a-f]{4}(-[0-9a-f]{4}){3}/i, ':uuid'],  // uuid 段
  [/^\d+$/, ':id'],                                            // 纯数字段
  [/^[a-f0-9]{16,}$/i, ':hash'],                                // 长 hash
];
function normalizeUrl(rawUrl) {
  const u = new URL(rawUrl, location.origin);
  let path = u.pathname.toLowerCase().replace(/\/+$/, '') || '/';
  const segs = path.split('/').map(seg => {
    for (const [re, name] of PATTERNS) if (re.test(seg)) return name;
    return seg;
  });
  const candidate = '/' + segs.slice(1).join('/');
  const hit = ROUTES.find(r => {
    const rp = r.split('/'); const cp = candidate.split('/');
    return rp.length === cp.length &&
      rp.every((s, i) => s.startsWith(':') || s === cp[i]);
  });
  const dim = hit ?? 'other';
  if (!hit) reportUnmatched(candidate);                     // 未匹配样本上报补规则
  return { dim, raw: u.pathname + (u.search ? '' : ''),    // query 全剥离
    detail: u.pathname + u.search };                        // 原文只进明细
}
normalizeUrl('/Order/88231/?from=push');  // -> { dim: '/order/:id', detail: '/Order/88231/' }
```
