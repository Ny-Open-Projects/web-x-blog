---
title: [ENG-137] 版本策略全景怎么设计？semver 预发布版本与 dist-tag 怎么配合？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-137：版本策略全景怎么设计？semver 预发布版本与 dist-tag 怎么配合？
**答**：
- semver 只回答"怎么编号"，版本策略要回答"什么时候发什么版本 用户怎么选风险等级"。
- 预发布版本让激进变更先在 opt-in 用户中验证：1.3.0-beta.2 不会污染默认 npm install 的用户。
- dist-tag 是频道机制：latest next beta lts 并行，用户用 pkg@beta 自选，tag 被大量使用后就不要移动语义。
- 每个 tag 的含义写进维护文档，废弃频道用 dist-tag rm 收回并公告替代版本。

```bash
# 版本策略全景：预发布 + dist-tag 实操
npm version prerelease --preid=beta       # 1.2.0 -> 1.2.1-beta.0
npm publish --tag next                     # 发到 next 频道 不影响 latest 用户

npm dist-tag add my-pkg@1.2.0 lts          # 旧稳定版标记为 lts 长期维护线
npm dist-tag ls my-pkg                     # latest 1.3.0 / next 1.2.1-beta.0 / lts 1.2.0

# 预发布验证充分后转正
npm dist-tag add my-pkg@1.3.0 latest
```
