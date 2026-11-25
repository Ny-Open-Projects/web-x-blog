---
title: [RBL-827] 场景题：合规 Cookie 交互层与构建的配合——同意门控的产物注入
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-827：场景题：合规 Cookie 交互层与构建的配合——同意门控的产物注入

**答**:
- GDPR/个保法下的 Cookie 同意门控：追踪类脚本（埋点/广告 SDK）必须在用户同意后加载——构建器的配合：1) **脚本分级**（essential（必需，直接加载）/tracking（同意后）/unknown（默认按 tracking 处理——保守默认））；2) 同意门控注入（产物中的 tracking 脚本改为「consent gate 包裹」——同意事件触发才加载）；3) manifest 的 consent 角色标注（RBL-618 的角色扩展）。
- 门控的实现模式：动态 import 包裹（`consentGranted('analytics').then(() => import('./analytics'))`）——构建器把「直接 import tracking 模块」转换为门控形态（AST 转换）或要求显式 API（门控 API 更可审计——转换魔法 vs 显式契约）。
- 合规审计：产物扫描「未门控的追踪脚本」（第三方 SDK 的 URL 模式/已知埋点包名）→ blocker；同意前的 cookie 写入检测（document.cookie 在同意前执行）→ 诊断。
- 同意状态与缓存的交互：同意后注入的脚本无预加载（等用户点同意——LCP 无影响但要保证加载快：同意后立即动态 import，prefetch 提示不适用「同意前不能预取」的法律约束）。
- 追问钩子：为什么「unknown 默认按 tracking 处理」而不是「默认 essential」？——合规的过错方是数据控制者：漏放一个追踪脚本 = 违规；多包一个必需脚本 = 功能延迟（可通过审计清单修正）——保守默认把风险从「合规违规」移到「性能损耗」，性能损耗可观测可修复，违规不可逆。

```javascript
// 构建期脚本分级与门控注入
const SCRIPT_ROLES = {
  essential: ['app.js', 'consent-cmp.js'],
  tracking: ['analytics.js', 'ads-sdk.js'],
  // unknown: 其余默认 tracking（保守）
};
function gateTracking(manifest) {
  for (const f of manifest.files) {
    const role = SCRIPT_ROLES.essential.includes(f.name) ? 'essential'
      : 'tracking';                                      // unknown 保守归 tracking
    f.consent = role === 'tracking' ? 'required' : 'none';
  }
  // entry 的 tracking import 改为门控
  rewriteEntry(manifest, (code) =>
    code.replace(/import\s+'\.\/analytics'/,
      `consentGranted('analytics').then(() => import('./analytics'))`));
}
// 合规审计
function auditConsent(products, { knownTrackers }) {
  const findings = [];
  for (const f of products)
    for (const t of knownTrackers)
      if (f.code.includes(t) && !f.code.includes('consentGranted'))
        findings.push({ file: f.name, tracker: t, detail: '追踪脚本未门控——GDPR blocker' });
  return findings;
}
```
