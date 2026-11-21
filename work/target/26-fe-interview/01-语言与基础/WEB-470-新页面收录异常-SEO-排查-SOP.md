---
title: [WEB-470] 新页面收录异常的 SEO 排查 SOP
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 排查SOP]
type: 面试题
---

## WEB-470：新页面收录异常的 SEO 排查 SOP

**答**：
- 先确认可达性链路：robots.txt 是否屏蔽 → 页面是否 noindex → sitemap 是否提交且状态码 200 → 内链是否可爬到
- 再看渲染问题：SPA 页面爬虫拿到空 HTML？检查 Google Search Console 的「网址检查」实际渲染结果；关键内容必须服务端可渲染或用预渲染/SSR
- 重定向与 canonical：链式 302、canonical 指向别页、多语言 hreflang 缺失都会稀释收录
- 权重与索引预算：新站或大量低质页会挤占索引配额，优先提交核心页并做内链支撑
- 工具链：Search Console 的覆盖率报告 + 日志分析（爬虫实际抓了什么、返回什么码），比 SEO 插件可信

```bash
# 模拟爬虫视角
curl -sA "Googlebot" https://example.com/page | head -20   # 是否输出正文
curl -s https://example.com/robots.txt | grep -A5 Disallow
```
