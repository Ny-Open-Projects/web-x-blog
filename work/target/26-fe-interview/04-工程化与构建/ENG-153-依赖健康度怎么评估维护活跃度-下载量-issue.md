---
title: [ENG-153] 依赖健康度怎么评估？维护活跃度 下载量 issue 响应怎么量化？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-153：依赖健康度怎么评估？维护活跃度 下载量 issue 响应怎么量化？
**答**：
- 引入新依赖前做健康度评估：最近发布时间、版本迭代频率、issue 平均响应、贡献者集中度（bus factor）。
- 自动化评分卡：npm registry 拉发布元数据，GitHub API 拉仓库状态，输出统一报告供准入流程引用。
- 分档决策：健康直接依赖；观察锁死版本并写 adapter 隔离层；高风险评估自研或 fork 成本再定。
- 评估是准入动作的一部分：新依赖走内部准入清单时必须附评分卡，事后抽查对照。

```javascript
// scripts/dep-health-check.mjs —— 依赖健康度评分卡
const dep = process.argv[2]
const headers = { Authorization: `Bearer ${process.env.GITHUB_TOKEN}` }

const npmInfo = await (await fetch(`https://registry.npmmirror.com/${dep}`)).json()
const gh = npmInfo.repository?.url?.match(/github\.com\/([^/]+\/[^/.]+)/)?.[1]
const repo = await (await fetch(`https://api.github.com/repos/${gh}`, { headers })).json()

const lastPublish = new Date(npmInfo.time.modified)
const days = Math.floor((Date.now() - lastPublish) / 864e5)

const score = {
  依赖: dep,
  距上次发布天数: days,
  版本迭代次数: Object.keys(npmInfo.versions ?? {}).length,
  star: repo.stargazers_count,
  openIssue数: repo.open_issues_count,
  评级: days < 180 ? '健康' : days < 365 ? '观察 锁版本并加 adapter' : '高风险 评估自研或 fork',
}
console.log(JSON.stringify(score, null, 2))
// 用法 node scripts/dep-health-check.mjs dayjs
```

## 第三十章 微前端工程化（ENG-154 ~ ENG-158）
