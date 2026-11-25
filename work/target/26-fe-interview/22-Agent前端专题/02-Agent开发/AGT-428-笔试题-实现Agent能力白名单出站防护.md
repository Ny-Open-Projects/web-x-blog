---
title: [AGT-428] 笔试题——实现出站数据防护（白名单+敏感扫描+审计）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-428：手写 DLP 出站防护：域名白名单、敏感模式扫描、分级拦截

**需求与边界**：
- 输入：外发请求 {target, payload}；输出：放行/拦截/脱敏后放行。
- 边界要求：① 域名白名单精确匹配（子域防绕过：evil.com 假扮 api.x.com.evil.com 必须拦截）；② 敏感模式扫描（密钥/身份证/内网 IP）；③ 分级处置（公开放行/内部脱敏放行/高敏拦截）；④ 全部请求审计含拦截。

**答**：
```javascript
const WHITELIST = ['api.partner-a.com', 'hooks.slack.com'];
const SENSITIVE = [
  { re: /(sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16})/, level: 'secret' },
  { re: /\d{17}[\dXx]/, level: 'pii' },                    // 身份证
  { re: /10\.\d+\.\d+\.\d+|192\.168\.\d+\.\d+/, level: 'internal' },
];
function isSubdomainOf(host, domain) {
  return host === domain || host.endsWith('.' + domain);
}
function outboundGuard({ target, payload }) {
  const url = new URL(target);
  const allowed = WHITELIST.some(d => isSubdomainOf(url.hostname, d));
  if (!allowed) return audit({ action: 'block',
    reason: 'domain_not_whitelisted', target });
  let level = 'public'; const hits = [];
  const scan = (v) => typeof v === 'string' ? SENSITIVE
    .filter(s => s.re.test(v)) : Array.isArray(v) ? v.flatMap(scan)
    : v && typeof v === 'object' ? Object.values(v).flatMap(scan) : [];
  hits.push(...scan(payload));
  level = hits.some(h => h.level === 'secret') ? 'secret'
    : hits.some(h => h.level === 'pii' || h.level === 'internal')
      ? 'internal' : 'public';
  if (level === 'secret')
    return audit({ action: 'block', reason: 'secret_detected', hits });
  if (level === 'internal') {
    let clean = payload;
    for (const h of hits) clean = redactPattern(clean, h.re);
    return audit({ action: 'allow_redacted', payload: clean, hits });
  }
  return audit({ action: 'allow', payload });
}
function audit(r) { log({ ts: Date.now(), ...r }); return r; }
// 递归扫描深嵌套 payload；secret 级直接拦截不脱敏。
```

**评分点**:
- 白名单子域校验方向正确（endsWith 防前缀拼接绕过 evil-api.com）。
- 敏感扫描递归覆盖嵌套对象/数组，三级分级处置（放行/脱敏放行/拦截）。
- secret 级直接拦截（密钥不可脱敏放行——宁可拒绝）。
- 全部请求（含拦截）审计留痕。
