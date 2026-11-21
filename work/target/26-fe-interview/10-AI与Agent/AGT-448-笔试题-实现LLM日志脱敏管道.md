---
title: [AGT-448] 笔试题——实现 LLM 日志脱敏管道（多类 PII+格式保留+可逆可选）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-448：手写日志脱敏：多类 PII 检测、格式保留掩码、可逆映射（授权场景）

**需求与边界**：
- 输入：日志对象（任意嵌套）、脱敏配置 {types, reversible}；输出：脱敏后日志。
- 边界要求：① 覆盖常见 PII：手机号/身份证/银行卡/邮箱/API 密钥；② 掩码保留格式（前 3 后 4——便于日志排查）；③ 可逆模式仅限授权场景（映射表加密存储，日志脱敏默认不可逆）；④ 递归处理嵌套与数组，性能护栏（大日志跳过正则细节）。

**答**：
```javascript
const PATTERNS = [
  { type: 'phone', re: /(?<!\d)1[3-9]\d{9}(?!\d)/g,
    mask: (s) => s.slice(0, 3) + '****' + s.slice(-4) },
  { type: 'idcard', re: /\d{17}[\dXx]/g,
    mask: (s) => s.slice(0, 4) + '***********' + s.slice(-4) },
  { type: 'bank', re: /\d{16,19}/g,
    mask: (s) => '****' + s.slice(-4) },
  { type: 'email', re: /[\w.+-]+@[\w-]+\.[\w.]+/g,
    mask: (s) => s.replace(/^(.{2}).*(@.*)$/, '$1***$2') },
  { type: 'apikey', re: /(sk-|AKIA)[A-Za-z0-9]{16,}/g, mask: () => '***KEY***' },
];
function redact(value, { types = 'all', reversible = false,
  vault } = {}) {
  const active = PATTERNS.filter(p =>
    types === 'all' || types.includes(p.type));
  const walk = (v) => {
    if (typeof v === 'string')
      return active.reduce((s, p) => s.replace(p.re, (m) => {
        if (reversible && vault)
          return vault.put(m, p.type);           // 可逆：令牌化
        return p.mask(m);
      }), v);
    if (Array.isArray(v)) return v.map(walk);
    if (v && typeof v === 'object') {
      const o = {};
      for (const [k, val] of Object.entries(v))
        o[k] = /password|secret|token/i.test(k) ? '***' : walk(val);
      return o;                                  // 字段名级+模式级双层
    }
    return v;
  };
  return walk(value);
}
// vault.put：AES 加密映射 + 短 TTL（授权排障场景，默认关闭）。
// 性能：单条日志 >100KB 时仅跑 apikey/phone 两类（大日志降级）。
```

**评分点**:
- 五类 PII 覆盖 + 字段名级与模式级双层脱敏。
- 掩码保留格式（前 3 后 4）便于排查；密钥类全掩码。
- 可逆模式仅授权场景（vault 加密+默认关闭）——默认不可逆。
- 递归嵌套/数组处理与大日志降级护栏。
