---
title: [PER-646] 安全用例如何进自动化回归？把 XSS/CSRF/越权测试固化进 e2e 的实践
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-646：安全用例如何进自动化回归？把 XSS/CSRF/越权测试固化进 e2e 的实践

**答**：
- 思路：把渗透测试的人肉发现沉淀成回归用例"——每修一个漏洞就固化一条 e2e 用例，安全回归套件随 CI 跑，防止同型漏洞复发。
- 用例类型：**XSS 注入用例**（payload 库对每个输入点注入，断言净化后无脚本执行痕迹）、**CSRF 用例**（跨站页面发起请求，断言被 token 拦截）、**越权用例**（低权账号直接调高权接口，断言 403）、**开放重定向用例**（returnTo 恶意值断言回退）。
- 实施要点：用例要轻（安全回归 5 分钟内跑完，只测关键入口）；payload 库版本化（新漏洞类型补充）；测试数据隔离（越权测试用专用账号池）。
- 度量：安全回归拦截过多少次回归（真实价值）；用例覆盖率 = 已固化用例覆盖的入口数 / 攻击面地图入口数。

```javascript

// e2e 安全回归示例（Playwright 风格）
const XSS_PAYLOADS = ['<script>alert(1)</script>', '<img src=x onerror=alert(1)>',
  '"><svg onload=alert(1)>', 'javascript:alert(1)', '<svg><style><img src=x onerror=alert(1)>'];
test('评论输入点 XSS 回归', async ({ page }) => {
  for (const p of XSS_PAYLOADS) {
    await page.goto('/article/1');
    await page.fill('#comment-input', p);
    await page.click('#submit');
    const executed = await page.evaluate(() =>
      document.querySelector('[data-xss-executed]') !== null); // 探针：payload 里带执行标记
    const escaped = await page.evaluate(() =>
      document.querySelector('#comment-list')?.innerHTML.includes('&lt;script'));
    expect({ executed, escaped }).toEqual({ executed: false, escaped: true });
  }
});
test('低权账号越权回归', async ({ request }) => {
  const res = await request.delete('/api/admin/user/1',
    { headers: { Authorization: `Bearer ${LOW_TOKEN}` } });
  expect(res.status()).toBe(403);                             // 断言拒绝而非 200
```
