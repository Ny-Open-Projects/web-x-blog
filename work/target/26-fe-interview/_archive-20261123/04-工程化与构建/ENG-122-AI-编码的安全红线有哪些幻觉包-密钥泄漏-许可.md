---
title: [ENG-122] AI 编码的安全红线有哪些？幻觉包、密钥泄漏、许可证污染怎么防？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-122：AI 编码的安全红线有哪些？幻觉包、密钥泄漏、许可证污染怎么防？
**答**：
- 幻觉包：AI 推荐的包可能不存在或是相近名字的恶意包，装包前必须到 registry 核实且查维护状态。
- 密钥泄漏：对话与生成代码两侧都要防——输入侧禁止粘贴凭证，输出侧用 gitleaks 等扫描兜底。
- 许可证污染：AI 生成代码可能复述 GPL 类受协议保护的片段，重要场景要求标注来源并过 license 审查。
- 三道自动化红线接入 pre-push/CI：registry 核验、secret 扫描、license 白名单检查（见 ENG-060）。

```bash
# 红线一：幻觉包核验，包不存在或发布时间极近都视为可疑
npm view left-pad-express version time --json || echo "疑似幻觉包，禁止安装"

# 红线二：密钥泄漏扫描，扫全量提交历史
gitleaks detect --source . --report-path leaks.json --redact

# 红线三：许可证白名单，GPL 类进商业项目即拦截
npx license-checker --production --onlyAllow "MIT;ISC;Apache-2.0;BSD-3-Clause;0BSD"
```
