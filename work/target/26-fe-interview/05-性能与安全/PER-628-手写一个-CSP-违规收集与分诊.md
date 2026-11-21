---
title: [PER-628] 手写一个 CSP 违规收集与分诊服务端：接收 report-uri 上报，自动分类并生成策略调整建议
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-628：手写一个 CSP 违规收集与分诊服务端：接收 report-uri 上报，自动分类并生成策略调整建议

**答**：
- 上报体字段：`document-uri/violated-directive/blocked-uri/source-file/line`；分诊规则：blocked-uri 为空（内联/eval 违规）-> 策略需加 nonce 或改写；第三方域 -> 接入方式改造；同域未知路径 -> 可疑，优先排查（可能是注入行为本身）。
- 要点：同指纹聚合（directive + blocked-uri + source-file）防止报告洪水；每类输出建议动作"；攻击样特征（document-uri 带奇怪 query、source-file 为空）单列安全事件通道。
- 边界：浏览器扩展会产生噪音（chrome-extension: 域过滤）；样本要限流；分诊结果回写到策略评审清单形成闭环。
- 评分点：攻击特征单列与扩展噪音过滤。

```javascript

// Node/Express 分诊服务
app.post('/csp-report', express.json({ type: 'application/csp-report' }), (req, res) => {
  const r = req.body['csp-report'] ?? req.body;
  const { 'document-uri': doc, 'violated-directive': dir, 'blocked-uri': blocked,
          'source-file': src } = r;
  if (/^chrome-extension:|^moz-extension:/.test(blocked ?? '')) return res.end(); // 扩展噪音
  const fp = hash([dir, blocked, src].join('|'));
  const triage =
    !blocked || blocked === 'inline'
      ? { cls: 'inline-or-eval', advice: '加 nonce 或改造为外链脚本' }
      : !blocked.startsWith(location.origin)
        ? { cls: 'third-party', advice: '第三方接入改造或策略加白' }
        : /\?[^\s]{40,}/.test(doc ?? '')
          ? { cls: 'attack-suspect', advice: '同域未知违规，安全事件通道排查' }
          : { cls: 'first-party', advice: '业务路径补白名单' };
  aggregate(fp, { doc, dir, blocked, src, ...triage });    // 聚合防洪水
  res.end();
});
function hash(s) { let h = 0; for (const c of s) h = (h * 31 + c.charCodeAt(0)) | 0; return h; }
// 输出：每周策略评审清单 { 聚合指纹数, 分类分布, 建议动作 }
```
