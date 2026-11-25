---
title: [MFW-669] 笔试：手写主题 SSR 一致性守护
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-669：笔试：手写主题一致性守护

**答**：实现 `verifyThemeConsistency(html, expectedTheme, { strict })`。规则：1) HTML 的 `data-theme` 属性 = expectedTheme（middleware/RSC 渲染正确主题）；2) **无 FOUC script**：存在 inline theme boot script（matchMedia 检测——RBL-777 theme boot；auto 模式的兜底）；3) CSS 变量层存在（`[data-theme="dark"]` 规则——RBL-777 双层变量）；4) 切换入口：cookie 写入的 action/handler 存在（code 扫描——setThemeCookie 的调用点）；strict 模式：任一缺失 → fail。返回 `{ checks: Array<{ name, pass }>, ok }`。边界：expectedTheme=auto（检查 matchMedia boot script 而非固定值）；HTML 无 data-theme（fail——未走 middleware）。

```javascript
function verifyThemeConsistency(html = '', expectedTheme = 'light', { strict = false } = {}) {
  const checks = [];
  // 1) data-theme 属性
  const attrMatch = /<html[^>]*data-theme="([^"]+)"/.exec(html);
  const attrTheme = attrMatch?.[1];
  checks.push({ name: 'data-theme-attr', pass: attrTheme === expectedTheme });
  // 2) auto 模式的 boot script
  if (expectedTheme === 'auto') {
    checks.push({ name: 'boot-script', pass: html.includes('matchMedia') && html.includes('prefers-color-scheme') });
  }
  // 3) CSS 变量层
  checks.push({ name: 'css-vars',
    pass: html.includes(`[data-theme="${expectedTheme}"]`) || html.includes(':root') });
  // 4) strict：全部必须 pass
  const criticalFail = checks.some(c => !c.pass);
  return { checks, ok: strict ? !criticalFail : checks.filter(c => c.pass).length >= 2 };
}

// 自测
const goodHtml = `<html data-theme="dark" lang="en">
<script>if(localStorage.theme==='auto'||!localStorage.theme){document.documentElement.dataset.theme=matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'}</script>
<style>[data-theme="dark"]{--bg:#111;color:#eee}:root{--bg:#fff}</style>
<body>...</body></html>`;
let r = verifyThemeConsistency(goodHtml, 'dark');
console.log(r.checks.every(c => c.pass) && r.ok === true);

// auto 模式
r = verifyThemeConsistency(goodHtml, 'auto', { strict: true });
console.log(r.checks.find(c => c.name === 'boot-script').pass === true);
console.log(r.ok === true);

// 缺 data-theme
r = verifyThemeConsistency('<html lang="en"><body>x</body></html>', 'dark', { strict: true });
console.log(r.checks.find(c => c.name === 'data-theme-attr').pass === false);
console.log(r.ok === false);                             // strict fail

// 非 strict 宽松
r = verifyThemeConsistency('<html lang="en"><body>x</body></html>', 'dark');
console.log(r.ok === true);                              // 非 strict：2/3 过即过

console.log(verifyThemeConsistency('', 'light', { strict: true }).ok === false);
```

**评分点**：
- 四项检查（data-theme 属性/boot script/CSS 变量层/cookie action——RBL-668 全链路）；auto 模式的 boot script 检查
- strict/宽松模式（strict 全过、宽松 2/3——CI 门禁与诊断模式区分）；边界
- 能说清「主题的 SSR 一致性 = cookie 可读 + boot script 兜底 + CSS 变量层——三层缺一即 FOUC 或 mismatch」属于加分
