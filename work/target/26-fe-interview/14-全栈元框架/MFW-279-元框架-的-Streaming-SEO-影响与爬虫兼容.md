---
title: [MFW-279] 流式渲染的 SEO 影响与爬虫兼容
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 笔试题
---

## MFW-279：流式 × SEO

**答**:
- 现代爬虫（Google）可执行 JS 且接受流式 HTML——但保守策略仍推荐：关键 SEO 内容（title/description/h1/正文）在首段同步输出（Shell 内），互动区才流式——不赌爬虫的流式解析完整度
- meta 标签时机：metadata 必须在首段（流式后补的 meta 部分爬虫忽略）——generateMetadata 的数据不能放慢 Suspense 段
- 结构化数据（JSON-LD）：随首段脚本输出；分段列表页的分页 canonical/relnext 与流式配合要显式验证（抓取模拟器跑一遍）
- 验证工具链：抓取模拟（Google 友好测试本地版）+ Search Console 覆盖率监控——「以为爬到」要用数据证实

```text
纪律：SEO 关键内容 ∈ 首段 Shell（同步）
meta 不可流式后补；JSON-LD 随首段
验证：本地抓取模拟 + GSC 覆盖率双保险
```
