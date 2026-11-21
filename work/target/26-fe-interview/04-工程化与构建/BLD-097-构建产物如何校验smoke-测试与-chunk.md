---
title: [BLD-097] 构建产物如何校验？smoke 测试与 chunk 大小 diff 报告怎么做？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-097：构建产物如何校验？smoke 测试与 chunk 大小 diff 报告怎么做？
**答**：
- 静态校验：产物存在性与引用完整性（manifest 与 html 一致、无 404 资源）、文件名规范、无 sourcemap 泄露、无明文密钥（grep 密钥模式）。
- 大小校验：与基线 stats.json diff，输出每 chunk 增减报表，超阈值失败（见 BLD-060）；重点盯首屏 entry 与 vendors。
- 冒烟测试：产物起本地静态服务后跑真实浏览器检查——首页能渲染、路由可跳转、无 console error；可用 Playwright headless 实现。
- 运行时校验兜底：灰度发布 + 前端监控资源加载失败率告警，构建期测不到的 CDN/跨域问题在这里暴露。

```javascript
// scripts/smoke.js：Playwright 冒烟校验（可运行）
import { chromium } from 'playwright';
import { createServer } from 'node:http';
import { readFileSync, existsSync } from 'node:fs';
import { extname, join } from 'node:path';

const MIME = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css' };
const server = createServer((req, res) => {
  const file = join('dist', req.url === '/' ? 'index.html' : req.url.split('?')[0]);
  if (!existsSync(file)) { res.writeHead(404); return res.end(); }
  res.setHeader('content-type', MIME[extname(file)] || 'application/octet-stream');
  res.end(readFileSync(file));
});
await new Promise((r) => server.listen(4173, r));

const browser = await chromium.launch();
const page = await browser.newPage();
const errors = [];
page.on('console', (m) => m.type() === 'error' && errors.push(m.text()));
page.on('requestfailed', (r) => errors.push(`资源失败 ${r.url()}`));

await page.goto('http://localhost:4173/');
await page.waitForLoadState('networkidle');
if (!(await page.locator('#root > *').count())) errors.push('首页未渲染');
await page.click('text=详情').catch(() => errors.push('路由点击失败'));

console.log(errors.length ? `SMOKE FAIL:\n${errors.join('\n')}` : 'SMOKE PASS');
process.exit(errors.length ? 1 : 0);
```
