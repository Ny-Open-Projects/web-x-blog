---
title: [TST-666] 笔试：实现日志脱敏管道（PII 识别 + 可逆映射 + 审计）
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-666：笔试：实现日志脱敏管道（PII 识别 + 可逆映射 + 审计）

**题目**：实现 Redactor：redact(text) 识别手机号/邮箱并替换为 <type_N>，保存占位符→原值的可逆映射与审计记录；restore(text) 还原。映射不对外输出。

**答**：
- PII 用正则识别（手机号/邮箱/身份证），替换为占位符。
- 可逆映射用 Map 保存占位符→原值，密钥由调用方持有；映射不随 prompt 输出。
- 记录审计条目：命中次数、字段类型，便于追溯。

```javascript
class Redactor {
  constructor() { this.map = new Map(); this.audit = []; }
  redact(text) {
    const rules = [
      { re: /1[3-9]\d{9}/g, type: 'phone' },
      { re: /[\w.]+@[\w.]+\.\w+/g, type: 'email' },
    ];
    let out = String(text);
    rules.forEach(r => {
      out = out.replace(r.re, m => {
        const token = `<${r.type}_${this.map.size}>`;
        this.map.set(token, m);
        this.audit.push({ type: r.type, token });
        return token;
      });
    });
    return out;
  }
  restore(text) {
    return [...this.map].reduce((s, [k, v]) => s.split(k).join(v), text);
  }
}
```

**评分点**：
- PII 正则识别准确
- 可逆映射与还原正确
- 审计记录完整
- 脱敏后不泄露原值
