---
title: [SCN-1243] AI 产品的安全红队测试（越狱防护前端配合）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1243：AI 产品的安全红队测试（越狱防护前端配合）

**答**：
- 红队：越狱测试集（角色扮演绕过/编码绕过）定期测试，漏洞修复回归。
- 前端：多轮攻击模式检测（连续绕过尝试风控），限流/封禁。
- 报告：红队报告（漏洞类型/修复状态）归档。

```javascript
// 越狱防护
const JAILBREAK_PATTERNS = [/扮演.*无限制/, /忽略.*以上/, /DAN/];
function jailbreakGuard(history) {
  const attempts = history.filter(m =>
    JAILBREAK_PATTERNS.some(p => p.test(m.content)));
  if (attempts.length >= 3)
    return { action: 'rate-limit', note: '多次异常尝试，临时限流' };
  return { action: 'monitor' };
}
```
